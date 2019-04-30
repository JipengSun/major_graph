import re
import jieba
import math

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
                    self.root.add_content(para)
                    success = True

        begin = False
        #print(self.root.get_contents())
        return success

    def build_nodes(self, current_node, slide):
        threshold = 0.9
        result = []
        possible_node = current_node
        for shape in slide:
            if slide.index(shape) == 0:
                nodename = SlideTree.get_node_name(shape)
                match = SlideTree.parent_match(possible_node,nodename)
                result.append([match, possible_node])
                while match < threshold and possible_node.parent is not None:
                    possible_node = possible_node.parent
                    match = SlideTree.parent_match(possible_node,nodename)
                    result.append([match, possible_node])
                if match >= threshold:
                    if len(possible_node.get_children()) != 0:

                        l = []
                        for child in possible_node.get_children():
                            print('Child: ',child.get_name())
                            s = SlideTree.cal_similarity(child.get_name(),nodename)
                            t = [child,s]
                            l.append(t)
                        l.sort(key=lambda x: x[1], reverse=True)
                        new_node = l[0][0]
                    else:
                        new_node = SlideNode(parentnode= possible_node, nodename= nodename)
                        possible_node.add_child(new_node)
                    #print(new_node.get_contents())
                    continue
                    #current_node = new_node
                elif possible_node.parent is None:
                    match = SlideTree.parent_match(possible_node, nodename)
                    result.append([match, possible_node])

                result.sort(key=lambda x:x[0], reverse=True)
                new_node = SlideNode(parentnode=result[0][1],nodename = nodename, contentlist=[])
                result[0][1].add_child(new_node)
                #current_node = new_node
                #print(new_node.get_contents())
            else:
                for para in shape:
                    new_node.add_content(para)
                    #print(para)
                    #print(new_node.get_contents())
        #print(new_node.get_name())
        #print(new_node.get_contents())
        return new_node

    @staticmethod
    def get_node_name(shape):
        raw_name = shape[0][0]
        return raw_name

    @staticmethod
    def parent_match(node, title):
        if not node.get_contents():
            return 0
        else:
            all = []
            #print(node.get_contents())
            for para in node.get_contents():
                if para[1] == 0:
                    s = SlideTree.cal_similarity(para[0], title)
                    l = [para, s]
                    all.append(l)
            all.sort(key=lambda x:x[1], reverse= True)
            #print(title)
            #print(all)
            return all[0][1]

    @staticmethod
    def cal_similarity(content, title):
        content = str(content)
        title = str(title)
        if title in content or content in title:
            return 1
        elif content == '':
            return 0
        else:
            c_cut = [i for i in jieba.cut(content) if i != '']
            t_cut = [i for i in jieba.cut(title) if i != '']
            word_set = set(c_cut).union(set(t_cut))
            word_dict = dict()
            i = 0
            for word in word_set:
                word_dict[word] = i
                i += 1
            #c_cut_code = [word_dict[word] for word in c_cut]
            c_cut_code = [0]*len(word_dict)
            for word in c_cut:
                c_cut_code[word_dict[word]] += 1

            t_cut_code = [0]*len(word_dict)
            for word in t_cut:
                t_cut_code[word_dict[word]] += 1
            sum = 0
            sq1 = 0
            sq2 = 0
            for i in range(0,len(c_cut_code)):
                sum += c_cut_code[i] * t_cut_code[i]
                sq1 += pow(c_cut_code[i],2)
                sq2 += pow(t_cut_code[i],2)
            try:
                result = round(float(sum)/(math.sqrt(sq1)*math.sqrt(sq2)), 2)
            except ZeroDivisionError:
                result = 0.0
            return result



'''
    def add_child(self, parent, child):
        parent.append(child)
        child.setParent = parent
        
    def get_children(self):
        pass;
'''


class SlideNode:

    def __init__(self,parentnode=None, childrenlist = [], contentlist=[], nodename = None):
        self.parent = parentnode
        self.children = childrenlist
        self.contents = contentlist
        self.name = nodename

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def add_content(self, content):
        self.contents.append(content)

    def get_contents(self):
        return self.contents

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name