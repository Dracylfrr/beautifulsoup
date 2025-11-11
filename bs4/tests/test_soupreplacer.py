from bs4 import BeautifulSoup, SoupReplacer

# Milestone 2 Tests
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

# Milestone 3 Tests

def test_simple_replace():
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup("<b>text</b>", "html.parser", replacer=replacer)
    assert soup.find("blockquote")

def test_name_xformer():
    replacer = SoupReplacer(name_xformer=lambda t: "i" if t.name == "em" else t.name)
    soup = BeautifulSoup("<em>hi</em>", "html.parser", replacer=replacer)
    assert soup.find("i")

def test_attrs_xformer():
    def add_id(tag):
        tag.attrs["id"] = "demo"
        return tag.attrs
    replacer = SoupReplacer(attrs_xformer=add_id)
    soup = BeautifulSoup("<p>hello</p>", "html.parser", replacer=replacer)
    assert soup.p["id"] == "demo"

def test_xformer_remove_class():
    def remove_class(tag):
        if "class" in tag.attrs:
            del tag.attrs["class"]
    replacer = SoupReplacer(xformer=remove_class)
    soup = BeautifulSoup('<p class="a">hi</p>', "html.parser", replacer=replacer)
    assert "class" not in soup.p.attrs

def test_combined():
    def rename(tag): return "div" if tag.name == "section" else tag.name
    def add_style(tag): tag.attrs["style"] = "color:red;"
    replacer = SoupReplacer(name_xformer=rename, xformer=add_style)
    soup = BeautifulSoup("<section>hi</section>", "html.parser", replacer=replacer)
    div = soup.find("div")
    assert div and div["style"] == "color:red;"

def test_noop():
    replacer = SoupReplacer()
    soup = BeautifulSoup("<p>no change</p>", "html.parser", replacer=replacer)
    assert soup.p.text == "no change"


if __name__ == "__main__":
    #M2
    test_basic_replacement()
    test_nested_replacement()
    #M3
    test_simple_replace()
    test_name_xformer()
    test_attrs_xformer()
    test_xformer_remove_class()
    test_combined()
    test_noop()