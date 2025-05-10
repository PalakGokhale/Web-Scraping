import requests
from bs4 import BeautifulSoup
import sys

# Fix for Unicode output
sys.stdout.reconfigure(encoding='utf-8')

# Fetch the page
url = "https://en.wikipedia.org/wiki/Yoga_as_exercise"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Get the page title
print("Page Title:", soup.title.string)

# Extract the introduction (first paragraph before table of contents)
intro_paragraphs = soup.select("div.mw-parser-output > p")
print("\n--- Introduction ---")
for p in intro_paragraphs:
    if p.text.strip():
        print(p.text.strip())
        break

# Extract section headings and their content
print("\n--- Section Details ---")
for header in soup.select("h2"):
    section_title = header.text.strip().replace('[edit]', '')
    print(f"\n## {section_title}")

    content = []
    for tag in header.find_next_siblings():
        if tag.name and tag.name.startswith('h2'):
            break
        if tag.name == 'p':
            content.append(tag.text.strip())

    print('\n'.join(content[:2]))  # Limit to first 2 paragraphs per section


# Container for all pose data
# poses = []

# # Find all pose containers
# pose_sections = soup.find_all(['h2', 'h3'])

# current_pose = None

# for tag in pose_sections:
#     # Collect pose names (usually in h2 or h3 tags)
#     if tag.name in ['h2', 'h3'] and tag.get_text(strip=True):
#         if 'pose' in tag.get_text(strip=True).lower():
#             if current_pose:
#                 poses.append(current_pose)
#             current_pose = {
#                 'name': tag.get_text(strip=True),
#                 'description': ''
#             }
#         elif current_pose:
#             # Add additional titles to description
#             current_pose['description'] += '\n' + tag.get_text(strip=True)
    
#     # Append following paragraph content as description
#     sibling = tag.find_next_sibling()
#     while sibling and sibling.name == 'p':
#         if current_pose:
#             current_pose['description'] += '\n' + sibling.get_text(strip=True)
#         sibling = sibling.find_next_sibling()

# # Add last pose
# if current_pose:
#     poses.append(current_pose)

# # Save to DataFrame
# df = pd.DataFrame(poses)

# # Export to CSV (optional)
# df.to_csv("yoga_poses.csv", index=False)\

# # Print results
# print(df)
