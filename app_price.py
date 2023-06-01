import pandas as pd
import streamlit as st

def run_app_price():
    df = pd.read_csv('RB_THIRTY_YEARS_ABOVE_RSTRNT_INFO_20211231.csv')
    df1 = df.drop(['CTPRVN_CD','SIGNGU_CD','FCLTY_LO','FCLTY_LA','BASE_DE'],axis=1)
    df1.rename(columns={'FCLTY_NM':'식당이름','RDNMADR_NM':'도로명주소','AREA_NM':'지역','REPRSNT_MENU_NM':'대표메뉴','MENU_PRC':'가격'},inplace=True)
    df2 = df1.dropna(axis=0)
    df2['가격구간'] = pd.cut(df2.가격,bins=[0,9999,19999,29999,39999,49999,99999,129999],labels=['만원미만','만원이상2만원미만','2만원이상3만원미만','3만원이상4만원미만','4만원이상5만원미만','5만원이상10만원미만','10만원이상'])
    
    st.subheader('가격별 검색을 합니다')
    price_li = ['만원미만','만원이상 2만원미만','2만원이상 3만원미만','3만원이상 4만원미만','4만원이상 5만원미만','5만원이상 10만원미만','10만원이상']
    price= st.selectbox('원하는 가격대를 선택하세요',price_li) 
   
    if price == '만원미만':
        st.dataframe(df2.loc[df2['가격구간']=='만원미만',][['식당이름','도로명주소','대표메뉴','가격']])
    elif price == '만원이상 2만원미만':
        st.dataframe(df2.loc[df2['가격구간']=='만원이상2만원미만',][['식당이름','도로명주소','대표메뉴','가격']])
    elif price == '2만원이상 3만원미만':
        st.dataframe(df2.loc[df2['가격구간']=='2만원이상3만원미만',][['식당이름','도로명주소','대표메뉴','가격']])
    elif price == '3만원이상 4만원미만':
        st.dataframe(df2.loc[df2['가격구간']=='3만원이상4만원미만',][['식당이름','도로명주소','대표메뉴','가격']])
    elif price == '4만원이상 5만원미만':
        st.dataframe(df2.loc[df2['가격구간']=='4만원이상5만원미만',][['식당이름','도로명주소','대표메뉴','가격']])
    elif price == '5만원이상 10만원미만':
        st.dataframe(df2.loc[df2['가격구간']=='5만원이상10만원미만',][['식당이름','도로명주소','대표메뉴','가격']]) 
    elif price == '10만원이상':
        st.dataframe(df2.loc[df2['가격구간']=='10만원이상',][['식당이름','도로명주소','대표메뉴','가격']])

    num = st.number_input('갖고있는 돈의 액수를 입력하세요',min_value = 1000)

    st.dataframe(df2.loc[df2['가격'] <= num ,][['식당이름','도로명주소','대표메뉴','가격']])
    
        
    