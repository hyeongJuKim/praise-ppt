import copy
import os
from pptx import Presentation

TEMPLATE_PPT = "template/lyrics-template2.pptx"
TARGET_PPT = "result.pptx"


def main():
    text_file_name = input_keyboard()
    generate_ppt(TEMPLATE_PPT, text_file_name)


def input_keyboard():
    while True:
        file_name = input("가사가 포함된 파일명을 입력하세요.\n")
        if os.path.isfile("./" + file_name):
            break
        else:
            print("파일이 존재하지 않습니다.")

    return file_name


def generate_ppt(text_file_name):
    template_prs = Presentation(TEMPLATE_PPT)

    with open(text_file_name, 'r') as f:
        reads = f.read()
        lyrics = reads.split('\n\n')
        title = lyrics.pop(0)

        for entry in lyrics:
            duplicate_slide(template_prs, 0, title, entry)

    delete_slide(template_prs, 0)
    template_prs.save(TARGET_PPT)


def duplicate_slide(pres, index, title, entry):
    source = pres.slides[index]
    try:
        blank_slide_layout = pres.slide_layouts[6]
    except:
        blank_slide_layout = pres.slide_layouts[len(pres.slide_layouts) - 1]

    new_slide = pres.slides.add_slide(blank_slide_layout)
    img_dict = {}

    for shp in source.shapes:
        if shp.shape_type == 13:
            # copy pictures
            with open(shp.name + '.jpg', 'wb') as f:
                f.write(shp.image.blob)
            img_dict[shp.name + '.jpg'] = [shp.left, shp.top, shp.width, shp.height]

            # add pictures
            for k, v in img_dict.items():
                new_slide.shapes.add_picture(k, v[0], v[1], v[2], v[3])
                os.remove(k)
        else:
            count = 0
            el = shp.element
            for paragraph in shp.text_frame.paragraphs:
                for run in paragraph.runs:
                    if shp.name == '제목 1':  # 동적으로 변경
                        run.text = title
                    elif shp.name == '부제목 2':
                        count += 1
                        if count == 1:
                            run.text = entry

            newel = copy.deepcopy(el)
            new_slide.shapes._spTree.insert_element_before(newel, 'p:extLst')


def delete_slide(prs, index):
    xml_slides = prs.slides._sldIdLst
    slides = list(xml_slides)
    xml_slides.remove(slides[index])


if __name__ == "__main__":
    main()
