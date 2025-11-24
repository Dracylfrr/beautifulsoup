from bs4 import BeautifulSoup, SoupStrainer

def main():
    filename = "beautifulsoup/apps/m2/html53.html"

    # Only parse tags that have an id attribute
    strainer = SoupStrainer(id=True)

    with open(filename, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser", parse_only=strainer)

        # One API call to get all elements with an id
        elements = soup.find_all(True, id=True)

        for elem in elements:
            print(f"<{elem.name}>  id='{elem['id']}'")

if __name__ == "__main__":
    main()
