from bs4 import BeautifulSoup, SoupReplacer

html_doc = """
<html><body>
<b>Hello</b>
<p class="note">keep me</p>
</body></html>
"""

# Example 1 — rename <b> to <blockquote>
replacer1 = SoupReplacer("b", "blockquote")
print(BeautifulSoup(html_doc, "html.parser", replacer=replacer1).prettify())

# Example 2 — remove all 'class' attributes
def remove_class(tag):
    if "class" in tag.attrs:
        del tag.attrs["class"]

replacer2 = SoupReplacer(xformer=remove_class)
print(BeautifulSoup(html_doc, "html.parser", replacer=replacer2).prettify())
