# task6.py
from bs4 import BeautifulSoup
from bs4 import SoupReplacer   # <-- this is the new class you added inside BeautifulSoup

def main():
    # input and output file paths
    input_file = "html53.html"
    output_file = "output_task6.html"

    # Create the replacer: convert all <b> tags to <blockquote>
    replacer = SoupReplacer("b", "blockquote")

    # Read the HTML file
    with open(input_file, "r", encoding="utf-8") as f:
        html = f.read()

    # Parse using your new replacer
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    # Write the modified HTML tree to a file
    with open(output_file, "w", encoding="utf-8") as out:
        out.write(soup.prettify())

    print(f"Converted all <b> tags to <blockquote> and wrote result to {output_file}")

if __name__ == "__main__":
    main()
