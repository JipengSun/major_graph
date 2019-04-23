from ppt_extract import extract_ppt



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

def is_contents(slide):
    contents_word = ['主要内容']
    for word in contents_word:
        if word in slide[0][0]:
            return True
        else:
            return False

# Check for the slides which have high similarity
def check_duplicate():

    pass
