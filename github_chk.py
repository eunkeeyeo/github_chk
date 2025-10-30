import requests

# 깃헙에 있는 파이썬 파일의 'Raw' 주소 (예: https://raw.githubusercontent.com/...)
github_file_url = "여기에 깃헙 Raw 파일 주소를 입력하세요. (예: https://raw.githubusercontent.com/user/repo/branch/module.py)"

try:
    # 1. 파일 내용 다운로드
    response = requests.get(github_file_url)
    response.raise_for_status()  # HTTP 오류가 발생하면 예외 발생

    # 2. 다운로드한 내용을 파이썬 모듈로 실행/로드
    # 이 코드를 로드할 딕셔너리를 정의합니다.
    module_namespace = {}

    # exec() 함수로 코드를 실행합니다.
    exec(response.text, module_namespace)

    # 3. 로드된 네임스페이스에서 함수/클래스 접근
    # 'module_namespace'에서 원하는 함수나 클래스를 가져옵니다.
    # 만약 깃헙 파일에 'hello_world'라는 함수가 있었다면:
    if 'hello_world' in module_namespace:
        hello_function = module_namespace['hello_world']
        hello_function()
    else:
        print("원하는 함수를 찾을 수 없습니다.")

except requests.exceptions.RequestException as e:
    print(f"다운로드 중 오류가 발생했습니다: {e}")

# exec() 사용 시 주의사항:
# ❗ exec()는 다운로드한 코드를 실행하므로, 신뢰할 수 없는 출처의 코드를 실행하면 보안상 심각한 위험이 있을 수 있습니다.