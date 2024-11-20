import pandas as pd
import os

# 파일 경로와 필요한 컬럼
input_file_path = '건물에너지DB_좌표매칭_최종(19-22)(대전)_test.csv'
output_file_path = '건물에너지DB_좌표매칭_최종(19-22)(대전)(lotno_addr)_test.csv'
columns_to_read = ['LOTNO_ADDR', 'LOTNO_MNO', 'LOTNO_SNO']

try:
    # 입력 파일이 존재하는지 확인
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"파일을 찾을 수 없습니다: {input_file_path}")

    # CSV 파일 읽기 및 필요한 열 선택
    data = pd.read_csv(input_file_path, usecols=columns_to_read, encoding='utf-8')

    # 데이터 개수 확인
    row_count = len(data)
    print(f"추출된 데이터 개수: {row_count}개")

    # 결과를 새로운 CSV 파일로 저장
    data.to_csv(output_file_path, index=False, encoding='utf-8-sig')
    print(f"필요한 컬럼만 저장된 파일이 생성되었습니다: {output_file_path}")

except FileNotFoundError as fnf_error:
    print(fnf_error)
except ValueError as ve:
    print(f"지정된 컬럼이 CSV 파일에 존재하지 않습니다: {ve}")
except Exception as e:
    print(f"오류 발생: {e}")
