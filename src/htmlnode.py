from enum import Enum

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag                  # string
        self.value = value              # string
        self.children = children        # list
        self.props = props              # dictionary
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html = ""
        if self.props == None:
            return html
        else:
            for p, i in self.props.items():
                html += f" {p}=\"{i}\""
            return html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Missing 'tag' property....")
        if self.children == None:
            raise ValueError("Missing 'children' property...")
        return f"<{self.tag}{self.props_to_html()}>{', '.join(map(str, list(self.children)))}</{self.tag}>"
        
        