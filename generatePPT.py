import copy
import itertools
import os
from pptx import Presentation

TEMPLATE_PPT = "template/lyrics-template.pptx"
TARGET_PPT = "result.pptx"


def main():
    text_file_name = input_keyboard()
    generate_ppt(TEMPLATE_PPT, text_file_name)


def input_keyboard():
    while True:
        file_name = input("입력할 가사 파일명을 입력하세요.\n")
        if os.path.isfile("./" + file_name):
            break
        else:
            print("입력한 파일이 존재하지 않습니다.")

    return file_name


def generate_ppt(text_file_name):
    template_prs = Presentation(TEMPLATE_PPT)
    txt = open(text_file_name, 'r')
    title = txt.readlines()[0].rstrip('\n')
    with open(text_file_name, 'r') as f:
        reads = f.read()
        for entry in reads.split('\n\n'):
            duplicate_slide(template_prs, 0, title, entry)

    template_prs.save(TARGET_PPT)
    txt.close()


def duplicate_slide(pres, index, title, entry):
    source = pres.slides[index]
    try:
        blank_slide_layout = pres.slide_layouts[6]
    except:
        blank_slide_layout = pres.slide_layouts[len(pres.slide_layouts) - 1]

    dest = pres.slides.add_slide(blank_slide_layout)
    img_dict = {}

    for shp in source.shapes:
        if shp.shape_type == 13:
            # copy pictures
            with open(shp.name + '.jpg', 'wb') as f:
                f.write(shp.image.blob)
            img_dict[shp.name + '.jpg'] = [shp.left, shp.top, shp.width, shp.height]

            # add pictures
            for k, v in img_dict.items():
                dest.shapes.add_picture(k, v[0], v[1], v[2], v[3])
                os.remove(k)  # 이미지를 한 번 생성하도록 리팩토링
        else:
            el = shp.element
            for paragraph in shp.text_frame.paragraphs:
                for run in paragraph.runs:
                    if shp.name == '제목 1':  # 동적으로 변경
                        run.text = title
                    elif shp.name == '부제목 2':
                        # print(run)
                        # print(run.font.bold)
                        # paragraph.font.bold = run.font.bold
                        # paragraph.font.size = run.font.size
                        # paragraph.font.name = run.font.name
                        # paragraph.text = entry
                        run.text = entry
                        # print(entry)
                        # print('----')

            newel = copy.deepcopy(el)
            dest.shapes._spTree.insert_element_before(newel, 'p:extLst')


if __name__ == "__main__":
    main()
