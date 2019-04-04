from ppt_extract import extract_ppt

# Delete duplicates and nulls, sort the shapes

path = '/Users/mac/major_graph/课件/'
file_name = '01引言_软件学院.pptx'
chapter = extract_ppt(path,file_name)
statistic = dict()
for slide in chapter:
    for shape in slide:
        for paragraph in shape:
            if paragraph[2] not in statistic.keys():
                statistic[paragraph[2]] = 1
            else:
                statistic[paragraph[2]] +=1
            print(paragraph)
        print('shape')
    print('slide')

print(statistic)
#print(chapter)

def is_contents(slide):
    contents_word = ['主要内容']
    for shape in slide:
        for paragraph in shape:
            for word in contents_word:
                if word in paragraph[0]:
                    return True

