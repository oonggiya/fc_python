# Section03
# 파이썬 가상환경 개념, 설정 및 pip 사용법, vscode 연동

# "pip말고 pip3로 설치해보자! (python3기준)
#  python interpreter 경로 설정 다시 직접 bin폴더 python3로 설정해보자!! "

# 외부 설치 패키지 테스트
import simplejson as json

test_dict = {'1': 95, '4': 77, '3': 65, '5': 100, '2': 88}

# simplejson 실행
print(json.dumps(test_dict, sort_keys=True, indent=4 * ' '))


# '''
# python -m venv 가상환경명
# 	Script\activate.bat
# 	Script\deactivate.bat
# 	pip 명령어 : search , install, uninstall, list, freeze, show
# 	pip install search simplejson , simple*
# 	pip install install simplejson
# 	pip install install simplejson==버전
# 	pip install --upgrade simplejson
# 	pip show simplejson
# 	pip show -f simplejson
# 	pip freeze > packages.txt
# 	pip freeze --all > packages.txt
# 	pip install -r packages.txt


# 	python -m venv /path/to/venv : 윈도우, 맥, 리눅스 동일

# 	윈도우 : Script
# 	맥 : bin

# 	윈도우

# 	activate.bat : 가상환경 진입
# 	deactivate.bat : 가상환경 해제

# 	맥
# 	source ./activate : 가상환경 진입
# 	source ./deactivate : 가상환경 해제

# 	command : code 실행
# '''
