from bs4 import BeautifulSoup, SoupReplacer

def test_basic_replacement():
    html = "<b>Hello</b>"
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert soup.find("blockquote") is not None
    assert soup.find("b") is None
    print("test_basic_replacement passed")

def test_nested_replacement():
    html = "<div><b>Inside bold</b><i>italic</i></div>"
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert "<blockquote>" in str(soup)
    print("test_nested_replacement passed")

if __name__ == "__main__":
    test_basic_replacement()
    test_nested_replacement()
