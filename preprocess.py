from ppt_extract import extract_ppt
from py2neo import Graph, Node, Relationship


path = '/Users/mac/major_graph/课件/'
file_name = '01引言_软件学院.pptx'
#file_name = '001C  程序设计 -1.pptx'
(chapter,addition) = extract_ppt(path,file_name)

'''
for slide in chapter:
    if slide not in rd:
        rd.add(slide)
    else:
        chapter.remove(slide)
'''
print(addition)
for i in range(0,len(chapter.keys())):
    print(str(i)+': ')
    print(chapter[str(i)])
'''
graph = Graph('http://localhost:7474',username = 'neo4j', password='lukasbill')
c = Node(label='Test', name= 'Just')
graph.create(c)
graph.run('MATCH (n) RETURN n').to_table()
#print(c)
'''
