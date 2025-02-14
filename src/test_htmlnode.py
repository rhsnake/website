import unittest

from htmlnode import HTMLNode

class TESTHTMLNode(unittest.TestCase):
    def test_props(self):
        prop = {"href": "www.botdev.com",
                "target": "_blank"}
        node = HTMLNode(None,None,None,prop)
        print(node.props_to_html)
    
    def test_repr(self):
        prop = {"href": "www.botdev.com",
                "target": "_blank"}
        node = HTMLNode("p","Hello World",None,prop)
        print(repr(node))
        
    def test_None(self):
        node = HTMLNode()
        print(repr(node))