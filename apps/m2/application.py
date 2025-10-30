# application.py
import sys
import argparse
from bs4 import BeautifulSoup, SoupStrainer

def parse_args():
    p = argparse.ArgumentParser(
        description="Print tag names from a large HTML/XML file using SoupStrainer."
    )
    p.add_argument("file", help="Path to HTML/XML file (use '-' for stdin)")
    p.add_argument(
        "--parser",
        default="html.parser",
        choices=["html.parser", "lxml", "lxml-xml", "xml"],
        help="Underlying parser to use (default: html.parser)"
    )
    p.add_argument(
        "--all",
        action="store_true",
        help="Print every tag occurrence in document order (instead of unique names)"
    )
    p.add_argument(
        "--sorted",
        dest="sort_output",
        action="store_true",
        help="Sort unique tag names before printing (ignored with --all)"
    )
    return p.parse_args()

def main():
    args = parse_args()

    # Strain to only parse tags (skip text, comments, etc.) for speed/memory savings.
    only_tags = SoupStrainer(True)  # True == allow all tag names

    fh = sys.stdin if args.file == "-" else open(args.file, "r", encoding="utf-8", errors="ignore")
    with fh:
        soup = BeautifulSoup(fh, args.parser, parse_only=only_tags)

    if args.all:
        # Print every tag occurrence in document order
        for tag in soup.find_all(True):
            print(tag.name)
    else:
        # Print unique tag names
        names = {tag.name for tag in soup.find_all(True)}
        if args.sort_output:
            for name in sorted(names):
                print(name)
        else:
            for name in names:
                print(name)

if __name__ == "__main__":
    main()
