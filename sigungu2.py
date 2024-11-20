import json
import os

# 폴더 생성 함수
def createFolder(directory):
    """폴더가 없으면 생성하는 함수"""
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError as e:
        print(f'Error: Creating directory {directory} - {e}')

# GeoJSON 분할 함수
def splitgeoJson(json_filename):
    """GeoJSON 파일을 읽어 각 Feature별로 파일 분리"""
    # JSON 파일 경로 확인
    if not os.path.exists(json_filename):
        raise FileNotFoundError(f"GeoJSON 파일을 찾을 수 없습니다: {json_filename}")

    # JSON 파일 읽기
    with open(json_filename, 'r', encoding='UTF-8') as rf:
        try:
            geojson = json.load(rf)  # GeoJSON 파일 로드
        except json.JSONDecodeError as e:
            raise ValueError(f"GeoJSON 파일이 올바르지 않습니다: {e}")

    # 저장 폴더 생성
    base_path = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(base_path, 'geojson')
    createFolder(save_path)

    # Features를 순회하며 분할 저장
    for item in geojson['features']:
        code = item['properties'].get('SIG_CD', 'Unknown')  # 행정구역 코드
        kor_name = item['properties'].get('SIG_KOR_NM', '알 수 없음')  # 한글 이름
        eng_name = item['properties'].get('SIG_ENG_NM', 'Unknown')  # 영어 이름

        # 파일명 생성
        file_name = f"{code}_{kor_name}.json"
        file_path = os.path.join(save_path, file_name)

        print(f"Saving: {file_path}")

        # 새로운 GeoJSON 객체 생성
        geo = {
            'type': 'FeatureCollection',
            'features': [item]  # 단일 Feature 추가
        }

        # JSON 파일로 저장
        with open(file_path, 'w', encoding='UTF-8') as wf:
            json.dump(geo, wf, ensure_ascii=False, indent=4)  # 들여쓰기 추가

# 메인 실행부
if __name__ == '__main__':
    # GeoJSON 파일 경로 지정
    geojson_file = 'sigungu.geojson'  # 같은 디렉토리에 GeoJSON 파일이 있다고 가정
    try:
        splitgeoJson(geojson_file)
    except Exception as e:
        print(f"오류 발생: {e}")
