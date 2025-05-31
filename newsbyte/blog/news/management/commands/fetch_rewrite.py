import os
import requests
import openai
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.utils.dateparse import parse_datetime
from django.utils import timezone
from django.contrib.auth import get_user_model

from news.models import Article, Category

User = get_user_model()

class Command(BaseCommand):
    help = "Fetch news from NewsAPI, rewrite with OpenAI, save as Article with author and slug"

    def handle(self, *args, **options):
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        NEWS_API_KEY = os.getenv("NEWS_API_KEY")

        if not OPENAI_API_KEY or not NEWS_API_KEY:
            self.stdout.write(self.style.ERROR("Please set OPENAI_API_KEY and NEWS_API_KEY environment variables"))
            return

        openai.api_key = OPENAI_API_KEY

        # Find or create an author for these articles (you can customize username)
        author_username = "newsbot"
        author, created = User.objects.get_or_create(
            username=author_username,
            defaults={"email": "newsbot@example.com", "is_staff": False, "is_superuser": False},
        )
        if created:
            self.stdout.write(f"Created author user '{author_username}'")

        # Find or create a default category for imported articles
        category_name = "Automated"
        category, _ = Category.objects.get_or_create(name=category_name)

        self.stdout.write("Fetching news articles from NewsAPI...")
        url = "https://newsapi.org/v2/top-headlines"
        params = {
            "language": "en",
            "pageSize": 5,
            "apiKey": NEWS_API_KEY,
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error fetching news: {e}"))
            return

        articles = data.get("articles", [])
        self.stdout.write(f"Fetched {len(articles)} articles.")

        for art in articles:
            title = art.get("title") or "No Title"
            description = art.get("description") or ""
            content = art.get("content") or description or ""
            published_at = art.get("publishedAt")
            source = art.get("source", {}).get("name") or ""

            if not content.strip():
                self.stdout.write(f"Skipping article (no content): {title}")
                continue

            # Check if article with this title already exists
            if Article.objects.filter(title=title).exists():
                self.stdout.write(f"Article already exists, skipping: {title}")
                continue

            self.stdout.write(f"Rewriting article: {title}")

            try:
                prompt = (
                    "Rewrite this news article to be original, "
                    "engaging, and SEO-friendly, preserving facts:\n\n" + content
                )
                completion = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                )
                rewritten_content = completion.choices[0].message["content"].strip()
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"OpenAI API error: {e}"))
                continue

            pub_date = parse_datetime(published_at) if published_at else timezone.now()

            slug = slugify(title)

            article = Article(
                title=title,
                slug=slug,
                content=rewritten_content,
                published_at=pub_date,
                source=source,
                author=author,
                category=category,
                status=Article.PUBLISHED,  # Use the status constant for published
            )
            article.save()
            self.stdout.write(self.style.SUCCESS(f"Saved article: {title}"))

        self.stdout.write(self.style.SUCCESS("Done fetching and rewriting articles."))
