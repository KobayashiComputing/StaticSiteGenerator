from textnode import *

def main():
    n1 = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    n2 = TextNode("This is an image of Allen", "image", "allen.png")
    print(n1.__repr__())
    print(n2.__repr__())
    print(f"n1 and n2 are equal! ({n1.__eq__(n2)})")

main()
