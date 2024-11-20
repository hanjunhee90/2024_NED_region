import pandas as pd

# 파일 경로와 필요한 컬럼
file_path = '건물에너지DB_좌표매칭_최종(15-18).csv'
columns_to_read = ['STNDD_YR', 'USE_MM', 'ELRW_GRGS_DSAMT', 'CTY_GAS_GRGS_DSAMT', 'SUM_GRGS_DSAMT', 'ROAD_NM_ADDR']

# CSV 파일 읽기 및 필요한 열 선택
data = pd.read_csv(file_path, usecols=columns_to_read)

# '대전광역시'가 포함된 데이터 필터링
filtered_data = data[data['ROAD_NM_ADDR'].str.contains('대전광역시', na=False)]

# 필터링된 데이터 확인
print(filtered_data)

# 결과를 새로운 CSV 파일로 저장
filtered_data.to_csv('filtered_data.csv', index=False, encoding='utf-8-sig')