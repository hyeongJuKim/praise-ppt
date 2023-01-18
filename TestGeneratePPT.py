import unittest

from generatePPT import input_keyboard, generate_ppt


class TestGeneratePPT(unittest.TestCase):

    """
    파일명을 키보드로 입력받는다.
    입력한 파일이 현재 디렉토리에 존재하는지 확인한다.
    """
    def testInputKeyboard(self):
        self.assertIsNotNone(input_keyboard())

    """
    텍스트파일의 문자열을 읽는다.
    """
    def testGetText(self):
        generate_ppt("word-sample.txt")
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
