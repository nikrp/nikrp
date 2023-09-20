# Import Required Libs
from github import Github
import requests
import os
import dotenv

# Load the .env file
dotenv.load_dotenv()

# Login to Git
GH_ACCESS_TOKEN = os.getenv("GH_ACCESS_TOKEN")
git = Github("nikrp", GH_ACCESS_TOKEN)

# Get the README from the repository
repository = git.get_user().get_repo("nikrp")
file = repository.get_contents("README.md")
readme = file.decoded_content.decode("utf-8")

# Collect the url
url = requests.get("http://192.168.1.51:3000/api/random-meme?g=coding").content.decode("utf-8")

# Find the img tag for the meme and replace it with a new tag that has a new url
img_tag_start = readme.find("<img src=")
img_tag = readme[img_tag_start:].strip()

new_img_tag = f'<img src="{url}" alt="random meme" style="height: 400px;"/>'

readme = readme.replace(img_tag, new_img_tag)

# Update the README
repository.update_file("README.md", "changed readme", readme, file.sha)