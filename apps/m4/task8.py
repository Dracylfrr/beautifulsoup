"""
Milestone 4 – Task 8
Demonstration of iterable BeautifulSoup.

This script loads some HTML and iterates over all nodes in the soup
to prove that BeautifulSoup is now iterable after the M4 update.
"""

from bs4 import BeautifulSoup, NavigableString, Comment

HTML_DOC = """
<html>
  <body>
    <h1>Milestone 4</h1>
    <p>Hello <b>world</b>!</p>
    <!-- comment node here -->
    <div>
       <span>Nested</span> content
    </div>
  </body>
</html>
"""


def main():
    # Create soup object (must use bs4 from your project folder)
    soup = BeautifulSoup(HTML_DOC, "html.parser")

    print("=== Iterating over soup nodes (depth-first) ===")
    for node in soup:
        # Show details about the node
        if hasattr(node, "name") and node.name is not None:
            print(f"[TAG] <{node.name}>")
        elif isinstance(node, Comment):
            print(f"[COMMENT] {node}")
        elif isinstance(node, NavigableString):
            text = str(node).strip()
            if text:
                print(f"[TEXT] {text}")
        else:
            print(f"[NODE] {node}")

    print("\nIteration complete. BeautifulSoup is iterable!")


if __name__ == "__main__":
    main()
