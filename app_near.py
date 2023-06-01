import pandas as pd
import streamlit as st
from geopy.geocoders import Nominatim

def run_app_near():
    df = pd.read_csv('RB_THIRTY_YEARS_ABOVE_RSTRNT_INFO_20211231.csv')
    df1 = df.drop(['CTPRVN_CD','SIGNGU_CD','FCLTY_LO','FCLTY_LA','BASE_DE'],axis=1)
    df1.rename(columns={'FCLTY_NM':'식당이름','RDNMADR_NM':'도로명주소','AREA_NM':'지역','REPRSNT_MENU_NM':'대표메뉴','MENU_PRC':'가격'},inplace=True)
    st.subheader('가까운 식당을 검색합니다')
    my_address = st.text_input('현재 위치를 입력하세요(시/군/구, 동까지)')
    

    # 위도, 경도 반환하는 함수
    def geocoding(address):
        li = []
        geolocator = Nominatim(user_agent='chiricuto')
        location = geolocator.geocode(address)

        latitude = location.latitude
        longitude = location.longitude
        li.append(longitude)
        li.append(latitude)
        return li
        
    address = geocoding(my_address)
    def findNearNum(exList, values):
        answer = 0 # answer 리스트 0으로 초기화

        minValue = min(exList, key=lambda x:abs(x-values))
        answer = minValue
    
        return answer
    
    st.dataframe(df.loc[df['FCLTY_LO']==findNearNum(df['FCLTY_LO'],address[0]), ])
    
    
        
    
