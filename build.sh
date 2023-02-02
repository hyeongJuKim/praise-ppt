function build() {
  echo "pyinstaller 빌드를 수행합니다."
  pyinstaller generatePPT.py
}

function cp_file() {
  echo "필수 파일을 복사합니다."
  cp config.ini ./dist/generatePPT/config.ini
}

function mk_dir() {
  echo "필수 디렉토리를 생성합니다."
  mkdir ./dist/generatePPT/template/
}

echo "generatePPT 빌드를 시작합니다."

build
cp_file
mk_dir

echo "generatePPT 빌드를 종료합니다."