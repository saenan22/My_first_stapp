import streamlit as st
st.write('# 1. steamlit')
#Streamlit의 장점
'''
- 간단하게 파이썬 코드로 앱을 빌드할 수 있음
- 인터랙티브한 기능 제공(백엔드 개발이나 HTTP 요청 구현할 필요 없음)
- 다양한 예시 제공
- 커뮤니티에서 개발한 Component도 존재
- Streamlit에서 배포할 수 있는 Cloud 제공
- 화면을 녹화할 수 있는 Record 기능도 제공
- app을 빌드한 후, 오른쪽 ☰ 버튼을 클릭하면 Record a screencast를 확인할 수 있음
'''

 # 텍스트
st.header('🤖텍스트 출력')

st.write('') # 빈 줄 삽입
st.write('# 마크다운 H1 : st.write()')
st.write('마크다운 H3 : st.write()')
st.write('')
st.title('제목 : st.title()')
st.header('헤더 : st.header()')
st.subheader('서브헤더 : st.subheader()')
st.text('본문 텍스트 : st.text()')
st.write('')
st.markdown('마크다운 : st.markdown()')
st.markdown('''
            1. ordered item
 1. ordered item
    - unordered item
    - unordered item
 2. ordered item
 3. ordered item
 ''')
st.divider() # 구분선


# 마크다운
'''# Magic에 마크다운을 조합
 1. ordered item- 강조: **unordered item- 기울임: *unordered item
 2. ordered item
 3. ordered item
 '''
 # 데이터프레임
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df # 데이터프레임 출력

# 차트
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
fig # 차트출력


# 사이드바
# st.header('⬅⬅⬅⬅ 사이드바')
st.sidebar.write('사이드바 텍스트')
st.sidebar.checkbox('체크박스 1')
st.sidebar.checkbox('체크박스 2')
st.sidebar.radio('라디오 버튼', ['radio 1', 'radio 2', 'radio 3'])
st.sidebar.selectbox('셀렉트박스', ['select 1', 'select 2', 'select 3'])

# 레이아웃: 컬럼
st.header('컬럼 레이아웃')
col_1, col_2, col_3 = st.columns([1,2,1]) # 컬럼 인스턴스 생성. 1:2:1 비율로 컬럼을 나눔
with col_1:
  st.write(' 1번 컬럼')
  st.checkbox('이것은 1번 컬럼에 속한 체크박스 1')
  st.checkbox('이것은 1번 컬럼에 속한 체크박스 2')
 
with col_2:
 st.write(' 2번 컬럼')
 col_3.write(' 3번 컬럼')

 st.radio('2번 컬럼의 라디오 버튼', ['radio 1', 'radio 2', 'radio 3']) # 동일한 라디오 버튼을 생성할 수 없음
# 사이드바에 이미 라디오 버튼이 생성되어 있기 때문에, 여기서는 라디오 버튼의 내용을 변경해야 오류가 발생하지
col_3.selectbox('3번 컬럼의 셀렉트박스', ['select 1', 'select 2', 'select 3'])
 # 사이드바에 이미 셀렉트박스가 생성되어 있기 때문에, 여기서는 셀렉트박스의 내용을 변경해야 오류가 발생하지 않음

# 레이아웃: 탭
st.header('탭 레이아웃')
 # 탭 인스턴스 생성. 3개의 탭을 생성
tab_1, tab_2, tab_3 = st.tabs(['탭AAAAA', '탭BBBBB', '탭CCCCC']) 
with tab_1:
   st.write('탭AAAAA')
   st.write('이것은 탭A의 내용입니다.')
with tab_2:
   st.write('탭BBBBB')
   st.write('이것은 탭B의 내용입니다.')
tab_3.write('탭CCCCC')
tab_3.write('이것은 탭C의 내용입니다.')