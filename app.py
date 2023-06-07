import streamlit as st
import pandas as pd
from app_region import run_app_region
from app_home import run_app_home
from app_food import run_app_food
from app_price import run_app_price
from app_near import run_app_near

def main() :
    st.title(':orange[특]별한 :orange[식]당을 찾는 :orange[당]신을 위해')
    menu = ['Home','지역별 검색','음식별 검색','가격별 검색','가까운 식당']
    st.subheader('전국에 있는 :red[30년] 이상된 :blue[식당]을 알려드립니다')
    st.sidebar.image('https://cdn-icons-png.flaticon.com/512/7591/7591647.png')
    st.sidebar.title('특식당')
    choice = st.sidebar.selectbox('메뉴',menu)

    if choice == menu[0]:
        run_app_home()
    elif choice == menu[1]:
        run_app_region()
    elif choice == menu[2]:
        run_app_food()
    elif choice == menu[3]:
        run_app_price()
    else:
        run_app_near()


if __name__ == '__main__':
    main()