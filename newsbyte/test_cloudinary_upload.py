import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv

# Load your .env variables
load_dotenv()

# Configure Cloudinary with environment variables
cloudinary.config(
    cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),
    api_key=os.environ.get("CLOUDINARY_API_KEY"),
    api_secret=os.environ.get("CLOUDINARY_API_SECRET"),
)

# Upload a sample image (change this to any small static file you have)
upload_result = cloudinary.uploader.upload("media/article_images/metal-robot-dog.png")  # Replace with any small file path
print("Uploaded to:", upload_result["secure_url"])
