from pptx import Presentation
'''
from pptx import Presentation

prs = Presentation()
title_slide_layout = prs.slide_layouts[0]
slide = prs.slides.add_slide(title_slide_layout)
title = slide.shapes.title
subtitle = slide.placeholders[1]

title.text = "Hello, World!"
subtitle.text = "python-pptx was here!"

prs.save('test.pptx')
'''
def extract_ppt (path,file_name):

    prs = Presentation(path+file_name)

    chapter = []
    for slide in prs.slides:
        page = []
#        print(len(slide.placeholders))
        for shape in slide.shapes:
            shape_contents = []
            #            print(len(prs.slide_master.slide_layouts))
            if not shape.has_text_frame:
                continue
            for paragraph in shape.text_frame.paragraphs:
                paragraph_contents = []
                paragraph_contents.append(paragraph.text)
                paragraph_contents.append(paragraph.level)
#                paragraph_contents.append(paragraph.font.size)
                if shape.is_placeholder:
                    paragraph_contents.append(shape.name)
                else:
                    paragraph_contents.append('')
                paragraph_contents.append(shape.top)
                shape_contents.append(paragraph_contents)
            page.append(shape_contents)
        chapter.append(page)

    '''The structure of the chapter is the chapter[page_num][shape_num][paragraph_num], for example, 
    chapter[1][1][0] returns ['数据库系统概念----引言', 0, '页脚占位符 5']'''
    print(chapter)
    return chapter
