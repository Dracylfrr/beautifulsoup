# Milestone-2
Part 2 & Part 3

## Part 2 – Exploring BeautifulSoup Source Code (Version 4.13.0)

This document identifies the **file names and line numbers** for the definitions of all BeautifulSoup API functions used in **Milestone 1** and **Part 1 of Milestone 2**, based on the **original BeautifulSoup 4.13.0 source code** (before any modification).

---

## Version
**File:** `bs4/__init__.py`  
**Line 18:**  
```python __version__ = "4.13.0"```

```
1. BeautifulSoup Class

File: bs4/__init__.py
Definition line: ~245

class BeautifulSoup(Tag):

Description: Main entry point of the library. Represents the parsed HTML or XML document tree and provides methods for searching and navigating it.


2. find_all()

File: bs4/element.py
Definition line: ~1818

def find_all(self, name=None, attrs={}, recursive=True, string=None, limit=None, **kwargs):

Description: Finds all tags that match given criteria (tag name, attributes, string, etc.). Returns a list of matching elements.


3. find()

File: bs4/element.py
Definition line: ~1785

def find(self, name=None, attrs={}, recursive=True, string=None, **kwargs):

Description: Finds the first tag that matches the specified criteria.


4. get_text()

File: bs4/element.py
Definition line: ~1715

def get_text(self, separator="", strip=False, types=(NavigableString,)):

Description: Extracts and concatenates all text content from the tag and its children.


5. prettify()

File: bs4/element.py
Definition line: ~1855

def prettify(self, encoding=None, formatter="minimal"):

Description: Returns a formatted (indented) version of the document for easier reading.


6. SoupStrainer Class

File: bs4/element.py
Definition line: ~121

class SoupStrainer:

Description: Defines filters that restrict parsing to certain portions of the document to improve performance and reduce memory usage.
