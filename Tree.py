import re


class SlideTree:

    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def set_root(self, node):
        self.root = node

    def build_title(self, slide):
        node = SlideNode()
        success = False
        begin = False
        for shape in slide:
            for para in shape:
                a = re.match(r'.*第..章|.*第.章', para[0])
                if a is not None:
                    # print(para[0])
                    if a.end() != len(para[0]):
                        name = para[0][a.end():len(para[0])]
                        name = name.strip()
                        node.set_name(name)
                        success = True
                        begin = False
                    else:
                        begin = True
                elif begin:
                    name = para[0].strip()
                    node.set_name(name)
                    # print(name)
                    success = True
                    begin = False
        #print(node.get_name())

        if success:
            self.root = node

        return success

    def build_content(self,slide):
        begin = False
        success = False
        for shape in slide:
            for para in shape:
                if not begin:
                    a = re.match(r'.*目录|.*内容',para[0])
                    if a is not None:
                        begin = True
                else:

                    node = SlideNode(parentnode = self.root,nodename=para[0].strip())
                    self.root.add_child(node)
                    success = True

        begin = False
        return success

    def build_nodes(self, current_node, slide):
        for shape in slide:
            for para in shape:
                
        pass


'''
    def add_child(self, parent, child):
        parent.append(child)
        child.setParent = parent
        
    def get_children(self):
        pass;
'''


class SlideNode:

    def __init__(self,parentnode=None, childrenlist = [], contents=None, nodename = None):
        self.parent = parentnode
        self.children = childrenlist
        self.contents = contents
        self.name = nodename

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