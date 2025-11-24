# Milestone-4

## Overview

Milestone 4 extends the internal API of BeautifulSoup by making the
`BeautifulSoup` object **fully iterable**. This milestone teaches the following
core concepts from the Programming Styles course:

### 1. **Extending an Existing Library**
You enhance the behavior of a large third-party package (BeautifulSoup) without
rewriting it or breaking its public API.  
This simulates real-world work, where engineers must extend or adapt existing
frameworks safely.

### 2. **Iterator Pattern**
You implement an iterator so that the soup object can be used in:

```python
for node in soup:
    ...

python -m beautifulsoup.apps.m4.task8

def __iter__(self):
    for node in self.descendants:
        yield node
