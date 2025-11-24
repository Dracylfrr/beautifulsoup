import unittest
from bs4 import BeautifulSoup, NavigableString, Comment

class TestIterableSoup(unittest.TestCase):

    def test_basic_iteration(self):
        html = "<html><body><p>Hello</p></body></html>"
        soup = BeautifulSoup(html, "html.parser")

        nodes = list(iter(soup))
        tag_names = [node.name for node in nodes if hasattr(node, "name")]

        self.assertIn("html", tag_names)
        self.assertIn("body", tag_names)
        self.assertIn("p", tag_names)

    def test_text_nodes(self):
        html = "<div>abc<span>xyz</span></div>"
        soup = BeautifulSoup(html, "html.parser")

        texts = [str(node) for node in soup if isinstance(node, NavigableString)]
        self.assertIn("abc", texts)
        self.assertIn("xyz", texts)

    def test_depth_first_order(self):
        html = "<a>1<b>2<c>3</c></b></a>"
        soup = BeautifulSoup(html, "html.parser")

        text_nodes = [str(node) for node in soup if isinstance(node, NavigableString)]
        self.assertEqual(text_nodes, ["1", "2", "3"])   # DFS order

    def test_comment_nodes(self):
        html = "<div><!--hey--><p>ok</p></div>"
        soup = BeautifulSoup(html, "html.parser")

        comments = [node for node in soup if isinstance(node, Comment)]
        self.assertEqual(len(comments), 1)
        self.assertEqual(str(comments[0]), "hey")

    def test_multiple_root_tags(self):
        html = "<h1>Title</h1><p>Para</p>"
        soup = BeautifulSoup(html, "html.parser")

        tags = [node.name for node in soup if getattr(node, "name", None)]
        self.assertIn("h1", tags)
        self.assertIn("p", tags)
