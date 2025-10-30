import os
import sys
import tempfile
import shutil
import subprocess

repo_url = 'https://github.com/eunkeeyeo/github_chk.git'
repo_name = "github_chk"  # 'import' 시 사용할 모듈 이름 (폴더 이름)

# 1. 임시 디렉토리 생성
temp_dir = tempfile.mkdtemp()
clone_path = os.path.join(temp_dir, repo_name)

try:
    # 2. Git을 사용하여 레포지토리 복제
    print(f"[{repo_name}] 깃헙에서 레포지토리 복제 중...")
    subprocess.check_call(['git', 'clone', repo_url, clone_path])

    # 3. 임시 경로를 파이썬 모듈 검색 경로에 추가
    sys.path.append(clone_path)

    # 4. 모듈 불러오기
    # 레포지토리 안에 있는 모듈 이름(예: 'my_module')으로 import 합니다.
    # import my_module
    # my_module.some_function()

    print(f"[{repo_name}] 모듈 임시로 로드 완료. 이제 import하여 사용 가능합니다.")
    import printing_sth

    # 이제 모듈 내의 함수를 호출할 수 있습니다.

    # 1) 함수 호출 예시:
    message = "깃헙 모듈 활용 테스트!"
    printing_sth.print_message(message)
    # 예상 출력: 모듈에서 출력됨: 깃헙 모듈 활용 테스트!

    # 2) 다른 함수 호출 예시:
    result = printing_sth.calculate_sum(5, 7)
    print(f"계산 결과: {result}")
    # 예상 출력: 계산 결과: 12



    # 5. 작업 후 경로 제거 (프로그램 종료 시 자동으로 사라지지만 명시적으로 제거 가능)
    sys.path.remove(clone_path)

finally:
    # 6. 임시 디렉토리 정리
    shutil.rmtree(temp_dir, ignore_errors=True)
    print(f"[{repo_name}] 임시 디렉토리 정리 완료.")