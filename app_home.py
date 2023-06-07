import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def run_app_home():
    df = pd.read_csv('RB_THIRTY_YEARS_ABOVE_RSTRNT_INFO_20211231.csv')
    df1 = df.drop(['CTPRVN_CD','SIGNGU_CD','FCLTY_LO','FCLTY_LA','BASE_DE'],axis=1)
    df1.rename(columns={'FCLTY_NM':'식당이름','RDNMADR_NM':'도로명주소','AREA_NM':'지역','REPRSNT_MENU_NM':'대표메뉴','MENU_PRC':'가격'},inplace=True)
    df4 = df.drop(['CTPRVN_CD','SIGNGU_CD','FCLTY_LO','FCLTY_LA','BASE_DE'],axis=1)
    df4.rename(columns={'FCLTY_NM':'식당이름','RDNMADR_NM':'도로명주소','AREA_NM':'지역','REPRSNT_MENU_NM':'대표메뉴','MENU_PRC':'가격'},inplace=True)
    df2 = df1.dropna(axis=0)
    df1.loc[df1['대표메뉴'] == '자장면','대표메뉴'] = '짜장면'
    df3 = df1
    li4 = [ '함흥회냉면', '함흥냉면', '양구이', '한우 추어탕(통)', '미락정 정식',
       '물막국수', '순메밀막국수', '잡어매운탕', '생 갈비 1인분(2대)', '한방백숙', '참복매운탕', '옻닭',
       '추어탕', '전통평양냉면', '평양냉면', '설렁탕', '토종닭볶음탕','닭발 소', '매운탕', '복국', '수구레국밥', '한정식',
       '소갈비 270g', '민물장어구이 (1인분)', '특수부위 100g', '찰보리밥 정식', '돼지갈비찜',
       '버섯(낙불삼) 철판볶음(매운맛선택)', '특 모듬 한정식', '산채한정식', '한우갈비살', '쫄면', '바다메기 매운탕(물메기 미역치)', '한우수육小', '곰탕',
       '냉면', '낙지전골(1인)', '대동할매국수 보통', '석쇠 돼지 불고기', '참깨콩국수', '찜갈비', '냉동삼겹살', '유황 오리 불고기(700g)',
       '갯장어소금구이  양념구이  통구이 대', '완당', '밀면(물 / 비빔)', '토종 흑염소 숯불구이', '동래파전',
       '곱창전골', '아구찜', '낙곱새', '산낙지불고기(1인분)', '숯불족발', '막국수', '보리밥', '한식',
       '명동칼국수', '평안냉면 (물 / 비빔)', '돼지갈비(1인)', '물 막국수', '설농탕', '순대국', '해장국',
       '목살쌈밥', '낙지 연포탕', '보글보글섞어찌개', '복매운탕', '노가리 1마리당', '특미(110g)', '정식',
       '기본선지국', '생등심(국내산한우150g)', '민물장어 1kg (2인분)', '꽃등심', '오리코스요리',
       '제육밥상', '왕갈비 300g', '해태정식(1인)',
       '광양 불고기 국내산(180g)', '장어구이(소금/양념) 1인분', '흑산도홍어삼합', '마늘통닭',
       '서대회 1인분', '한우 생고기 비빔밥', '녹두삼계탕', '반지회덮밥', '메기매운탕', '백합죽',
       '무진장한우암소특선모듬 (500g)', '(특)육회 비빈밥', '늘채움정식', '참게장 정식', '큰댁정식', '갈비찜 1인분', '생복찜', '영양굴밥', '돼지갈비(200g)', '진주불고기',
       '게국지', '올갱이 해장국', '금강 정식', '해제비', '가자미 양념구이', '능이백숙', '붕어 찜(대)','해장국(특)','돼지갈비 (600g)', '장어구이','육개장', '미니족발', '선지해장국', '전통 꿩요리 B코스(2인이상)', '곰탕,수육', '전통개장국',
       '전통비빔밥', '떡갈비', '진주비빔밥', '짚불곰장어', '불고기', '추탕', '꼬리토막', '불고기, 냉면',
       '갈낙탕', '소갈비', '소머리국밥', '쌈밥정식', '콩나물국밥', '진주물냉면', '따로국밥', '돼지국밥',
       '묵밥', '꼬리곰탕', '국밥', '소갈비구이', '낙지백반', '물냉면', '고래수육', '영양탕', '꼬막정식',
       '육회비빔밥', '가리국밥', '백반', '한정식, 전주비빔밥', '돼지갈비', '비빔밥', '광양불고기', '순대국밥', '콩국수', '민물장어구이', '빈대떡', '어죽', '생선회', '감자국',
       '회비빔밥', '추어숙회', '곱돌비빕밥', '삼계탕', '짚불구이', '바싹불고기', '육회', '곱창 전골',
       '붕어찜(대)','칼국수', '우족탕', '닭한만리', '반찬전문점','생선탕', '순대 (1인분)', '오징어순대','충무김밥','순대','목살1인분(200g']

    df3.loc[df3['대표메뉴'].isin(li4),'대표메뉴'] = '한식종류'
    df3 = df3.replace('한식종류','한식')

    li3 = [ '짜장면', '간짜장', '삼선짜장면','옛날 짜장면','해물짬뽕','짜장']
    df3.loc[df3['대표메뉴'].isin(li3),'대표메뉴'] = '중식종류'
    df3 = df3.replace('중식종류','중식')

    li5 = ['온소바', '문어 나가사키 짬뽕 나베','복사시미', '우동','왕새우까스', '소바']
    df3.loc[df3['대표메뉴'].isin(li5),'대표메뉴'] = '일식종류'
    df3 = df3.replace('일식종류','일식')

    df3.loc[df3['대표메뉴'].str.contains('후라이드치킨'),'대표메뉴'] = '양식종류'
    df3 = df3.replace('양식종류','양식')
    df3.loc[df3['대표메뉴'].str.contains('크림치즈아인슈페너'),'대표메뉴'] = '음료종류'
    df3 = df3.replace('음료종류','음료')
    st.divider()
    st.subheader('🍽️전국의 30년 이상된 식당 현황')
    st.dataframe(df4)
    link='데이터 출처 [link](https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=af65689c-5a0f-4dd1-a91f-254d70053816)'
    st.markdown(link,unsafe_allow_html=True)
    st.divider()
    if st.button('🍴대표메뉴 가격이 가장 비싼 식당') :
        st.dataframe(df4.loc[df4['가격']==df4['가격'].max(),])
    
    if st.button('🍴대표메뉴 가격이 가장 싼 식당') :
        st.dataframe(df4.loc[df4['가격']==df4['가격'].min(),])
    st.divider()
    if st.button('👉지역별 식당 수'):
        fig = plt.figure()
        sns.set(font="Malgun Gothic",font_scale=0.8, 
        rc={"axes.unicode_minus":False},
        style='darkgrid')
        ax2 = sns.countplot(x='지역', data=df1)
        for p in ax2.patches:
            height = p.get_height()
            ax2.text(p.get_x() + p.get_width() / 2., height + 1, int(height), ha = 'center', size = 7)
            ax2.set_ylim(0, 55)
        st.pyplot(fig)


    if st.button('👉음식별 식당 수'):
        fig = plt.figure()
        sns.set(font="Malgun Gothic",font_scale=0.8, 
        rc={"axes.unicode_minus":False},
        style='darkgrid')
        ax = sns.countplot(x='대표메뉴', data=df3)
        for p in ax.patches:
            height = p.get_height()
            ax.text(p.get_x() + p.get_width() / 2., height + 5, int(height), ha = 'center', size = 8)
            ax.set_ylim(0, 250)
        st.pyplot(fig)
    
    if st.button('👉가격별 식당 수'):
        fig2 = plt.figure()
        ax1 = df2['가격'].hist()
        for p in ax1.patches:
            height = p.get_height()
            ax1.text(p.get_x() + p.get_width() / 2., height + 5, int(height), ha = 'center', size = 8)
            ax1.set_ylim(0, 100)

        st.pyplot(fig2)