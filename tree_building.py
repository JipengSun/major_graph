from ppt_extract import extract_ppt
import Tree

path = '/Users/mac/major_graph/课件/'
file_name = '01引言_软件学院.pptx'
#file_name = '001C  程序设计 -1.pptx'
(chapter, addition) = extract_ppt(path, file_name)
tree = Tree.SlideTree()

title = False
contents = False
for i in range(0,len(chapter.keys())):
    if not title:
        title = tree.build_title(chapter[str(i)])
        print(i)
    if not contents:
        contents = tree.build_content(chapter[str(i)])
        print(i)


list = tree.get_root().get_children()
for child in list:
    print(child.get_name())


