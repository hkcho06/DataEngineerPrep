import pandas as pd
import sqlite3

# Extract: CSV 파일 읽기
df = pd.read_csv("titanic.csv")

# Transform: 나이 결측치 평균값으로 채우기
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Load: SQLite에 저장
conn = sqlite3.connect("titanic.db")
df.to_sql("passengers", conn, if_exists="replace", index=False)

# 간단한 쿼리 실행
cursor = conn.cursor()
query = "SELECT Pclass, AVG(Survived) as survival_rate FROM passengers GROUP BY Pclass"
result = cursor.execute(query).fetchall()
print("등급별 생존율:", result)

conn.close()
