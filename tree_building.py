from ppt_extract import extract_ppt
import Tree
import queue
from py2neo import Graph, Node, Relationship
import csv

path = '/Users/mac/major_graph/课件/'
file_name = '01引言_软件学院.pptx'
#file_name = '001C  程序设计 -1.pptx'
graph = Graph('http://localhost:7474',username = 'neo4j', password='lukasbill')
(chapter, addition) = extract_ppt(path, file_name)
tree = Tree.SlideTree()
title = False
contents = False
with open('/Users/mac/major_graph/neo4j-community/import/test.csv', 'w', newline='',encoding='utf-8') as f:
    for i in range(0,len(chapter.keys())):
    #for i in range(0, 7):

        if not title:
            title = tree.build_title(chapter[str(i)])
            current_node = tree.root
            exact_node = tree.root
            #print(i)
        elif not contents:
            contents = tree.build_content(chapter[str(i)])
            #print(i)
            '''
            if contents:
                seg = tree.corpus(i+1,chapter)
                print(seg)
            '''
        elif chapter[str(i)]:
            #print(current_node.get_contents())
            new_node,exact_node = tree.build_nodes(current_node,exact_node,chapter[str(i)])
            print('before node is ',current_node.get_name())
            print('current node is',new_node.get_name())
            #print(new_node.get_contents())
            print('parent is ',new_node.get_parent().get_name())


            data = [new_node.get_parent().get_name(),new_node.get_name()]
            writer = csv.writer(f)
            writer.writerow(data)

            '''
            parentnode = Node(label='Test',name = str(new_node.get_parent().get_name()).replace('_',''))
            childnode = Node(label='Test', name= str(new_node.get_name()).replace('_',''))
            INCLUDE = Relationship.type('contains')
            graph.merge(INCLUDE(parentnode,childnode),'Test','name')
            '''
            '''
            MATCH (n { label: 'Test' })
            DETACH DELETE n
            '''
            current_node = new_node
f.close()
list = tree.get_root().get_children()
for child in list:
    print(child.get_name())
#print(list)


'''
q = queue.Queue()
q.put(tree.get_root())
level = 0
while not q.empty():
    length = q.qsize()
    while length != 0:
        print(length)
        node = q.get()
        print('Level',level,node.get_name())
        children = node.get_children()
        for child in children:
            q.put(child)
        length = length - 1
    level += 1
    print('####')
'''