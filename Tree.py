class SlideTree:

    def __init__(self):
        self.root = None

    def set_root(self, node):
        self.root = node

'''
    def add_child(self, parent, child):
        parent.append(child)
        child.setParent = parent
        
    def get_children(self):
        pass;
'''


class SlideNode:

    def __init__(self):
        self.parent = None
        self.children = []
        self.contents = None
        self.name = None

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def set_contents(self, content):
        self.contents = content

    def get_contents(self):
        return self.contents

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name