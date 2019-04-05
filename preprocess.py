from ppt_extract import extract_ppt
import operator

# Delete duplicates and nulls, sort the shapes

path = '/Users/mac/major_graph/课件/'
file_name = '01引言_软件学院.pptx'
chapter = extract_ppt(path,file_name)
statistic = dict()
rd = set()
placeword = ['灯片编号占位符', '页脚占位符']

for slide in chapter:
    for shape in slide:
        for paragraph in shape:
            #print(paragraph[2])
            #print(paragraph)
            if paragraph[0] == '':
                shape.remove(paragraph)
                #print(paragraph)
            else:
                for word in placeword:
                    #print(word)
                    #print(paragraph[2])
                    if word in paragraph[2]:
                        shape.remove(paragraph)
                        #print(paragraph)

for slide in chapter:
    while [] in slide:
        slide.remove([])


#print(chapter)



'''
for slide in chapter:
    if slide not in rd:
        rd.add(slide)
    else:
        chapter.remove(slide)
'''
#print(statistic)

print(chapter)
print('页脚占位符 5'.find('页脚占位符'))



def is_contents(slide):
    contents_word = ['主要内容']
    for shape in slide:
        for paragraph in shape:
            for word in contents_word:
                if word in paragraph[0]:
                    return True

