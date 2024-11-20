import cx_Oracle
import pandas as pd

# Oracle DB 연결 설정
oracle_connection = cx_Oracle.connect(
    user="jdbc",         # Oracle 사용자 이름
    password="jdbc",     # 비밀번호
    dsn="localhost:1521/xe"  # Oracle DSN 정보
)

# 커서 생성
cursor = oracle_connection.cursor()

# CSV 파일 경로 및 데이터 로드
file_path = 'filtered_data.csv'
data = pd.read_csv(file_path, header=None, encoding='utf-8')

# 컬럼 이름 수동 할당
data.columns = ['ROAD_NM_ADDR', 'STNDD_YR', 'USE_MM', 'ELRW_GRGS_DSAMT', 'CTY_GAS_GRGS_DSAMT', 'SUM_GRGS_DSAMT']

# 2015년 데이터만 필터링 (테스트 용)
data = data[data['STNDD_YR'].astype(str).str.contains('2015')]

# 테이블에 삽입할 SQL 쿼리
insert_query = """
    INSERT INTO grgs_dsamt (ROAD_NM_ADDR, STNDD_YR, USE_MM, ELRW_GRGS_DSAMT, CTY_GAS_GRGS_DSAMT, SUM_GRGS_DSAMT)
    VALUES (:1, :2, :3, :4, :5, :6)
"""

# 데이터프레임 데이터를 테이블에 삽입
try:
    for index, row in data.iterrows():
        cursor.execute(insert_query, (
            row['ROAD_NM_ADDR'],
            row['STNDD_YR'],
            row['USE_MM'],
            row['ELRW_GRGS_DSAMT'],
            row['CTY_GAS_GRGS_DSAMT'],
            row['SUM_GRGS_DSAMT']
        ))
    # 커밋
    oracle_connection.commit()
    print(f"{len(data)}개의 행이 성공적으로 삽입되었습니다.")
except Exception as e:
    print(f"오류 발생: {e}")
    oracle_connection.rollback()
finally:
    # 커서 및 연결 종료
    cursor.close()
    oracle_connection.close()