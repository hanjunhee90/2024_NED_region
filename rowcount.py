import pandas as pd

# 특정 열만 읽기
file_path = '대전광역시_추출결과2.csv'
data = pd.read_csv(file_path, usecols=[0])  # 첫 번째 열만 읽기

# 행 개수 확인
row_count = len(data)
print(f"CSV 파일의 행 개수: {row_count}개")