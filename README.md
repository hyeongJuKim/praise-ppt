# PPT 슬라이드 자동 생성 프로그램
PPT 슬라이드에 텍스트를 반복해서 입력하여 PPT를 생성한다.

## 사용 가이드
config.ini 파일에 설정을 한다.

## 요구사항
### 필요 한 것
- PPT slide template 파일
- 입력할 텍스트 파일

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
  - [ ] config.ini 파일의 값들 유효성 검사 및 exception 처리

### 문제
- [ ] 크롭된 상태의 이미지를 복사하기
- [x] 줄바꿈 적용시 자동 단락이 추가됨
  
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