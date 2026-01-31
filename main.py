import requests
import ctypes
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants
API_KEY = os.getenv("NASA_API_KEY")
API_URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
IMAGE_FILE = "wallpaper.jpg"
STORY_FILE = "story.txt"

def main():
    if not API_KEY:
        print("Error: NASA_API_KEY not found in .env file.")
        return

    print("Fetching data from NASA APOD...")
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return

    media_type = data.get("media_type")
    title = data.get("title")
    explanation = data.get("explanation")
    
    print(f"Title: {title}")
    
    if media_type != "image":
        print(f"Today's APOD is a {media_type}, not an image. Skipping wallpaper update.")
        # Still save the story/explanation
        save_story(title, explanation)
        return

    hdurl = data.get("hdurl")
    if not hdurl:
        print("No HD URL found.")
        return

    print(f"Downloading image from {hdurl}...")
    if download_image(hdurl, IMAGE_FILE):
        print("Image downloaded successfully.")
        
        save_story(title, explanation)
        print(f"Explanation saved to {STORY_FILE}.")
        
        print("Setting wallpaper...")
        set_wallpaper(os.path.abspath(IMAGE_FILE))
        print("Wallpaper set successfully!")
    else:
        print("Failed to download image.")

def download_image(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, "wb") as f:
            f.write(response.content)
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
        return False

def save_story(title, explanation):
    try:
        with open(STORY_FILE, "w", encoding="utf-8") as f:
            f.write(f"Title: {title}\n\n")
            f.write(explanation)
    except IOError as e:
        print(f"Error saving story: {e}")

def set_wallpaper(image_path):
    # SPI_SETDESKWALLPAPER = 20
    # SPIF_UPDATEINIFILE = 0x01
    # SPIF_SENDCHANGE = 0x02
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

if __name__ == "__main__":
    main()
