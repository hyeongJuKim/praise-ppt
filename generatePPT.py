import os


def main():
    input_keyboard()


def input_keyboard():
    while True:
        file_name = input("입력할 가사 파일명을 입력하세요.\n")
        if os.path.isfile("./" + file_name):
            break
        else:
            print("입력한 파일이 존재하지 않습니다.")

    return file_name


if __name__ == "__main__":
    main()
