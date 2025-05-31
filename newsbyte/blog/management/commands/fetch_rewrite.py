import os
import requests
from django.core.management.base import BaseCommand
from blog.models import Article
from openai import OpenAI
from django.contrib.auth import get_user_model

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

class Command(BaseCommand):
    help = "Fetch and rewrite news articles"

    def handle(self, *args, **options):
        # Create or get a default author (superuser or placeholder)
        User = get_user_model()
        author = User.objects.filter(is_superuser=True).first()

        if not author:
            self.stdout.write(self.style.ERROR("No superuser found to assign as author."))
            return

        url = f"https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey={NEWS_API_KEY}"


        response = requests.get(url)
        data = response.json()

        articles = data.get("articles", [])[:5]  # Limit for demo purposes

        for article in articles:
            original_title = article["title"]
            original_content = article["description"] or article["content"] or ""

            if not original_content:
                continue

            # Avoid duplicates
            if Article.objects.filter(title__icontains=original_title[:50]).exists():
                continue

            # Use OpenAI to rewrite and expand the article
            prompt = f"""
            Rewrite and significantly expand the following news summary into a detailed article suitable for a blog. Use a professional tone and elaborate with more context:

            "{original_title}"

            {original_content}
            """

            try:
                completion = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a professional journalist."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=800,
                    temperature=0.7,
                )
                rewritten_content = completion.choices[0].message.content.strip()
            except Exception as e:
                self.stderr.write(self.style.ERROR(f"OpenAI error: {e}"))
                continue

            # Save article to the database
            new_article = Article(
                title=original_title,
                content=rewritten_content,
                author=author
            )
            new_article.save()
            self.stdout.write(self.style.SUCCESS(f"Saved: {original_title}"))
