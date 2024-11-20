import json
import os

# 폴더 생성 함수
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError as e:
        print(f'Error: Creating directory {directory} - {e}')

# GeoJSON 분할 함수
def splitgeoJson(Jsonfilename):
    # json 파일 읽기
    with open(Jsonfilename, 'r', encoding='UTF-8') as rf:
        geojson = json.loads(rf)

    # 저장 폴더 생성
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'geojson')
    createFolder(path)

    # features 배열 반복
    for item in geojson['features']:
        code = item['properties']['SIG_CD']  # 행정구역 코드
        eng_name = item['properties'].get('SIG_ENG_NM', 'Unknown')  # 행정구역명 영어
        kor_name = item['properties'].get('SIG_KOR_NM', '알 수 없음')  # 행정구역명 한국

        # json 파일 저장 경로
        file_name = f"{code}_{kor_name}.json"
        file_path = os.path.join(path, file_name)
        print(f"Saving: {file_path}")

        # json 객체 생성
        geo = {
            'type': 'FeatureCollection',
            'features': [item]  # 배열에 단일 Feature 추가
        }

        # json 파일 저장
        with open(file_path, 'w', encoding='UTF-8') as wf:
            json.dump(geo, wf, ensure_ascii=False, indent=4)  # 들여쓰기 추가로 가독성 향상

# 메인 실행부
if __name__ == '__main__':
    splitgeoJson('TL_SCCO_SIG.json')
