# task3.py
from bs4 import BeautifulSoup, SoupStrainer

def main():
    filename = "html53.html"

    # Parse only tags (ignore text/comments)
    strainer = SoupStrainer(True)  # True means allow all tags

    with open(filename, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser", parse_only=strainer)

        # Get all tag names (unique)
        tags = {tag.name for tag in soup.find_all(True)}

    print("All tags found in the document:")
    for tag in sorted(tags):
        print(tag)

if __name__ == "__main__":
    main()
