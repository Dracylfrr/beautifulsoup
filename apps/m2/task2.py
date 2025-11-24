# task2.py
from bs4 import BeautifulSoup, SoupStrainer

def main():
    filename = "beautifulsoup/apps/m2/html53.html"


    # Only parse <a> tags to save memory
    strainer = SoupStrainer("a")

    with open(filename, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser", parse_only=strainer)

        # Print every <a> tag and its href
        for link in soup.find_all("a", href=True):
            print(link["href"])

if __name__ == "__main__":
    main()
