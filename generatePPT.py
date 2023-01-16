import os


def main():
    fine_name = input_keyboard()
    get_text(fine_name)


def input_keyboard():
    while True:
        file_name = input("입력할 가사 파일명을 입력하세요.\n")
        if os.path.isfile("./" + file_name):
            break
        else:
            print("입력한 파일이 존재하지 않습니다.")

    return file_name


def get_text(fine_name):
    txt = open(fine_name, 'r')
    for i in txt:
        print(i)

    txt.close()


if __name__ == "__main__":
    main()
