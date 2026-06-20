
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props == None:
            return ""
        key_list = list(self.props.keys())
        props_string = ''
        for key in key_list:
            props_string += f' {key}="{self.props[key]}"'
        return props_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
        self.props = props or {}

    def to_html(self):
        if self.value == None:
            raise ValueError("All leafnodes must have a value!")
        elif not self.tag:
            return self.value
        else:
            if self.tag == "a":
                return f"<a{self.props_to_html()}>{self.value}</a>"
            elif self.tag == "img":
                return f"<img{self.props_to_html()} >"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
        self.props = props or {}
    
    def to_html(self):
        if not self.tag:
            raise ValueError("No tag is not permitted!")
        if not self.children:
            raise ValueError("All parent nodes must have a child!")
        return f"<{self.tag}>{self.recursive_on_children()}</{self.tag}>"
    
    def recursive_on_children(self):
        return "".join(child.to_html() for child in self.children)

