import pandas as pd  # 데이터 처리를 위한 라이브러리
import numpy as np  # 고성능 수치 연산 및 배열 처리를 위한 라이브러리
import seaborn as sns  # 데이터 시각화를 위한 라이브러리
import matplotlib.pyplot as plt  # 플롯(그래프) 시각화를 위한 라이브러리
from shapely.geometry import Point, LineString, Polygon  # 지리 데이터를 처리하기 위한 라이브러리
import geopandas as gpd  # 공간 데이터를 처리하고 시각화하기 위한 라이브러리
import json  # JSON 파일 처리를 위한 기본 라이브러리
import streamlit as st  # Streamlit 앱 작성용 라이브러리

# --- 1️⃣ GeoJSON 데이터 불러오기 및 처리 ---
st.markdown("### 1. GeoJSON 데이터 불러오기 및 처리")
# GeoJSON 파일을 GeoDataFrame 형태로 불러오기
gdf = gpd.read_file("C:/Users/김새난/data/BND_SIGUNGU_PG.json")
st.write("GeoDataFrame (gdf)의 상위 5개 데이터:")
st.dataframe(gdf.head())

# GeoJSON 파일로 저장하기
gdf.to_file("C:/Users/김새난/data/BND_SIGUNGU_PG.json", driver="GeoJSON")
st.markdown("#### 저장된 GeoJSON 파일 확인")
st.write("저장된 GeoJSON 파일을 다시 불러옵니다.")

# 저장된 GeoJSON 파일 불러오기
with open("C:/Users/김새난/data/BND_SIGUNGU_PG.json", encoding='UTF-8') as f:
    geojson_data = json.load(f)

# GeoJSON 데이터의 내용 일부 출력 (800자까지 제한)
st.markdown("#### GeoJSON 데이터 (일부 출력)")
st.code(json.dumps(geojson_data, indent=4, ensure_ascii=False)[0:800])

# GeoDataFrame의 좌표계 확인
st.markdown("#### GeoDataFrame 좌표계 (CRS)")
st.write(gdf.crs)

# --- 2️⃣ 출생률 데이터 불러오기 및 컬럼 정리 ---
st.markdown("### 2. 출생률 데이터 불러오기 및 컬럼 정리")
# CSV 파일을 DataFrame으로 불러오기
df = pd.read_csv(
    "C:/Users/김새난/Downloads/연령별_출산율_및_합계출산율_행정구역별__20241119164143.csv",
    encoding='cp949',
    low_memory=False,
    header=1
)
# 컬럼명 정리
df.columns = ["시군구별", "합계출산율"]
st.write("출생률 데이터 (상위 5개):")
st.dataframe(df.head())

# --- 3️⃣ GeoJSON 이름과 출생률 데이터 이름 비교 ---
st.markdown("### 3. GeoJSON 이름과 출생률 데이터 이름 비교")
# GeoJSON 데이터의 이름과 출생률 데이터의 이름 추출
geo_names = set(gdf['SIGUNGU_NM'])
birth_names = set(df['시군구별'])

# 일치하지 않는 이름 확인
geo_unmatched = geo_names - birth_names  # GeoJSON에만 있는 이름
birth_unmatched = birth_names - geo_names  # 출생률 데이터에만 있는 이름

st.markdown("#### 이름 비교 결과")
st.write("GeoJSON에만 있는 이름:")
st.write(geo_unmatched)

st.write("출생률 데이터에만 있는 이름:")
st.write(birth_unmatched)

