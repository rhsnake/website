from textnode import *

def main():
    print("Hello World")
    text = TextNode("This is a text node",TextType.BOLD, "https://www.boot.dev")
    print(repr(text))


main()