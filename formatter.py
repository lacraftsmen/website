import os
from bs4 import BeautifulSoup

source_dir = "./docs"

html_files = []

for subdir, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(subdir, file))
    
for file in html_files:
    with open(file, "r") as f:
        original_html = f.read()
        soup = BeautifulSoup(original_html, "html.parser")
        formatted_html = soup.prettify()

    with open(file, "w") as f:
        f.write(formatted_html)
        print(f"Formatted - {file}")

print("Formatting Complete")