import streamlit as st
import pandas as pd

def run_app_region():
    df = pd.read_csv('RB_THIRTY_YEARS_ABOVE_RSTRNT_INFO_20211231.csv')
    df1 = df.drop(['CTPRVN_CD','SIGNGU_CD','FCLTY_LO','FCLTY_LA','BASE_DE'],axis=1)
    df1.rename(columns={'FCLTY_NM':'식당이름','RDNMADR_NM':'도로명주소','AREA_NM':'지역','REPRSNT_MENU_NM':'대표메뉴','MENU_PRC':'가격'},inplace=True)
    st.subheader('지역별 검색을 합니다')
    li = df1['지역'].unique()
    column_list = st.multiselect('지역을 선택하세요',li)
    if len(column_list) >= 1:
        st.dataframe(df1[df1['지역'].isin(column_list)])
    #st.dataframe(df1.loc([column_list])