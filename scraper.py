<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup
import json

# URL for Yoga Poses list
CATEGORY_URL = "https://www.yogajournal.com/poses"

# Send request to the website
response = requests.get(CATEGORY_URL)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully fetched the page")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the yoga pose links (can change the tag and class based on website structure)
pose_links = []
for a_tag in soup.find_all('a', class_='c-hero__link'):
    href = a_tag.get('href')
    if href and href.startswith('/poses/'):
        full_url = f"https://www.yogajournal.com{href}"
        pose_links.append(full_url)

# Function to scrape individual yoga pose data
def scrape_yoga_pose(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract Yoga pose data
    try:
        name = soup.find('h1', class_='article__headline').text.strip()
    except AttributeError:
        name = "N/A"
    
    try:
        sanskrit_name = soup.find('span', class_='sanskrit-name').text.strip()
    except AttributeError:
        sanskrit_name = "N/A"
    
    try:
        benefits = [benefit.text.strip() for benefit in soup.find_all('li', class_='benefit-item')]
    except AttributeError:
        benefits = []
    
    try:
        instructions = [step.text.strip() for step in soup.find_all('li', class_='instruction')]
    except AttributeError:
        instructions = []
    
    try:
        precautions = [precaution.text.strip() for precaution in soup.find_all('li', class_='precaution')]
    except AttributeError:
        precautions = []

    # Difficulty Level and Target Area
    difficulty_level = soup.find('span', class_='difficulty-level')
    target_area = soup.find('span', class_='target-area')

    data = {
        "yoga_pose_name": name,
        "sanskrit_name": sanskrit_name,
        "benefits": benefits,
        "instructions": instructions,
        "precautions": precautions,
        "difficulty_level": difficulty_level.text.strip() if difficulty_level else "N/A",
        "target_area": target_area.text.strip() if target_area else "N/A"
    }
    
    return data

# Main script to scrape poses from Yoga Journal
all_yoga_data = []
for link in pose_links[:10]:  # Limit to first 10 poses for testing
    print(f"Scraping yoga pose: {link}")
    data = scrape_yoga_pose(link)
    all_yoga_data.append(data)

# Save the scraped data into a JSON file
with open("yoga_journal_poses.json", "w") as f:
    json.dump(all_yoga_data, f, indent=2)

print("✅ Yoga poses scraping complete. Data saved to 'yoga_journal_poses.json'")
=======
import requests
from bs4 import BeautifulSoup
import json

# URL for Yoga Poses list
CATEGORY_URL = "https://www.yogajournal.com/poses"

# Send request to the website
response = requests.get(CATEGORY_URL)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully fetched the page")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the yoga pose links (can change the tag and class based on website structure)
pose_links = []
for a_tag in soup.find_all('a', class_='c-hero__link'):
    href = a_tag.get('href')
    if href and href.startswith('/poses/'):
        full_url = f"https://www.yogajournal.com{href}"
        pose_links.append(full_url)

# Function to scrape individual yoga pose data
def scrape_yoga_pose(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract Yoga pose data
    try:
        name = soup.find('h1', class_='article__headline').text.strip()
    except AttributeError:
        name = "N/A"
    
    try:
        sanskrit_name = soup.find('span', class_='sanskrit-name').text.strip()
    except AttributeError:
        sanskrit_name = "N/A"
    
    try:
        benefits = [benefit.text.strip() for benefit in soup.find_all('li', class_='benefit-item')]
    except AttributeError:
        benefits = []
    
    try:
        instructions = [step.text.strip() for step in soup.find_all('li', class_='instruction')]
    except AttributeError:
        instructions = []
    
    try:
        precautions = [precaution.text.strip() for precaution in soup.find_all('li', class_='precaution')]
    except AttributeError:
        precautions = []

    # Difficulty Level and Target Area
    difficulty_level = soup.find('span', class_='difficulty-level')
    target_area = soup.find('span', class_='target-area')

    data = {
        "yoga_pose_name": name,
        "sanskrit_name": sanskrit_name,
        "benefits": benefits,
        "instructions": instructions,
        "precautions": precautions,
        "difficulty_level": difficulty_level.text.strip() if difficulty_level else "N/A",
        "target_area": target_area.text.strip() if target_area else "N/A"
    }
    
    return data

# Main script to scrape poses from Yoga Journal
all_yoga_data = []
for link in pose_links[:10]:  # Limit to first 10 poses for testing
    print(f"Scraping yoga pose: {link}")
    data = scrape_yoga_pose(link)
    all_yoga_data.append(data)

# Save the scraped data into a JSON file
with open("yoga_journal_poses.json", "w") as f:
    json.dump(all_yoga_data, f, indent=2)

print("✅ Yoga poses scraping complete. Data saved to 'yoga_journal_poses.json'")
>>>>>>> 8ecbcdbfe3636b835577a4dbad54f1b21810e350
