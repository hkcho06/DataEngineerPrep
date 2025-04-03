# Data Engineer Preparation
3개월 동안 주니어 데이터 엔지니어 준비를 위해 진행한 프로젝트 모음입니다.  
하루 2시간씩 투자하며 Python, Spark를 학습하고 ETL 파이프라인을 구축했습니다.

## Project 1: Python ETL
- **목표**: Titanic 데이터를 활용한 ETL 파이프라인 구현.
- **기술**: Python, pandas, SQLite.
- **작업**:
  1. `titanic.csv`에서 데이터 읽기.
  2. 나이 결측치를 평균값으로 채움.
  3. SQLite에 저장 후 등급별 생존율 쿼리.
- **결과**: [Python_ETL/titanic_etl.py](Python_ETL/titanic_etl.py)  
  [결과 스크린샷](Python_ETL/result_screenshot.png).

## Project 2: Spark Analysis
- **목표**: Spark로 대규모 데이터 처리 및 분석.
- **기술**: PySpark, Databricks.
- **작업**:
  1. Databricks 샘플 데이터 로드.
  2. 제품별 판매량 합계 계산.
  3. 결과를 CSV로 저장.
- **결과**: [Spark/spark_analysis.ipynb](Spark/spark_analysis.ipynb)  
  [결과 파일](Spark/result.csv) | [스크린샷](Spark/result_screenshot.png).

## 사용 방법
- Python 프로젝트: `python titanic_etl.py` 실행 (titanic.csv 필요).
- Spark 프로젝트: Databricks에서 `.ipynb` 실행.

## 배운 점
- Python으로 ETL 기본 흐름 익힘.
- Spark로 분산 데이터 처리 경험.
- GitHub로 작업 정리 및 포트폴리오화.
