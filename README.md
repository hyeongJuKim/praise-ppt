# PPT 슬라이드 자동 생성 프로그램
PPT 슬라이드에 텍스트를 반복해서 입력하여 PPT를 생성한다.

### 빌드
- `pyinstaller generatePPT.py` 명령어를 통해 빌드
- `dist/generatePPT/` 디렉토리안에 config.ini 파일 복사
- `dist/generatePPT/` 디렉토리를 복사하여 사용한다.

### 사용 방법
- `template/` 디렉토리 안에 PPT 양식파일과, 가사 txt 파일을 위치 시킨다. 
- `config.ini` 필요한 설정을 변경한다.
  - templatePptDir : PPT 파일 양식 파일이 존재하는 디렉토리명을 입력한다. (실행 파일 기준) 
  - resultPptDir : 가사 PPT 파일이 생성될 디렉토리명을 입력한다. (실행 파일 기준)

### 기능 요구사항
- 텍스트 파일을 읽어서 template 슬라이드에 입력 후 PPT 파일을 생성한다.
  - [x] 텍스트의 파일명을 입력한다.
    - [x] 존재하지 않는 파일이면 다시 입력 받는다.
  - [x] 텍스트 파일을 읽는다
  - [ ] 한 페이지에 입력할 구분자를 받아, 각 페이지별로 출력한다.
  - [x] PPT를 생성한다.
  - [x] template PPT의 슬라이드를 복사한다.
  - [x] 곡 제목을 입력한다.
  - [x] 가사를 입력한다.
- [x] template 디렉토리의 모든 txt 파일을 읽어서 out 디렉토리에 가사를 생성한다.
  - [x] 파일의 이름은 `txt 파일명-날짜-시간` 으로 생성한다.
  - [x] config.ini 파일의 값 유효성 검사 및 exception 처리
- [ ] exe,dmg 파일로 생성한다
  - [ ] 배포 스크립트를 생성한다.
    - pyinstaller -> copy config.ini

---

파이썬 피피티 샘플
https://gist.github.com/vinovator/9874b791bfc98111690f#file-pptplay-py-L4


파이썬 네이밍
https://dowtech.tistory.com/38


파일 읽고 쓰기
https://wikidocs.net/26


PPT 다루기1,2
https://coding-kindergarten.tistory.com/221
https://coding-kindergarten.tistory.com/222


파이썬 TDD
https://dentuniverse.tistory.com/entry/TDDPython-unittest-예제로-익혀보기


커밋 컨벤션
https://velog.io/@shin6403/Git-git-커밋-컨벤션-설정하기