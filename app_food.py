import pandas as pd
import streamlit as st


def run_app_food():
    df = pd.read_csv('RB_THIRTY_YEARS_ABOVE_RSTRNT_INFO_20211231.csv')
    df1 = df.drop(['CTPRVN_CD','SIGNGU_CD','FCLTY_LO','FCLTY_LA','BASE_DE'],axis=1)
    df1.rename(columns={'FCLTY_NM':'식당이름','RDNMADR_NM':'도로명주소','AREA_NM':'지역','REPRSNT_MENU_NM':'대표메뉴','MENU_PRC':'가격'},inplace=True)
    df1.loc[df1['대표메뉴'] == '자장면','대표메뉴'] = '짜장면'
    
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
       '붕어찜(대)','칼국수', '우족탕', '닭한만리', '반찬전문점','생선탕', '순대 (1인분)', '오징어순대','충무김밥','순대']
    
    test1 = '|'.join(li4)
    korea = df1[df1['대표메뉴'].str.contains(test1)]

    li3 = [ '짜장면', '간짜장', '삼선짜장면','옛날 짜장면','해물짬뽕','짜장']

    test = '|'.join(li3)
    china = df1[df1['대표메뉴'].str.contains(test)]

    li5 = ['온소바', '문어 나가사키 짬뽕 나베','복사시미', '우동','왕새우까스', '소바']

    test2 = '|'.join(li5)
    japan = df1[df1['대표메뉴'].str.contains(test2)]
    usa = df1[df1['대표메뉴'].str.contains('후라이드치킨')]
    cafe = df1[df1['대표메뉴'].str.contains('크림치즈아인슈페너')]

    li6 = ['한우 추어탕(통)','잡어매운탕','참복매운탕', '추어탕','설렁탕','매운탕', '복국', '수구레국밥','바다메기 매운탕(물메기 미역치)','곰탕','설농탕', '순대국', '해장국','낙지 연포탕','복매운탕','기본선지국',
	'녹두삼계탕','메기매운탕','올갱이 해장국','해장국(특)','육개장','선지해장국','전통개장국','추탕','갈낙탕','소머리국밥','콩나물국밥','따로국밥', '돼지국밥','가리국밥','순대국밥','감자국', '삼계탕','생선탕']

    test3 = '|'.join(li6)
    tang = df1[df1['대표메뉴'].str.contains(test3)]

    li7 = [ '후라이드치킨', '양구이','생 갈비 1인분(2대)','소갈비 270g','특수부위 100g','돼지갈비찜','한우갈비살','한우수육小', '석쇠 돼지 불고기','찜갈비', '냉동삼겹살', '유황 오리 불고기(700g)',
	'토종 흑염소 숯불구이','숯불족발','돼지갈비(1인)','생등심(국내산한우150g)','꽃등심', '오리코스요리', '왕갈비 300g','광양 불고기 국내산(180g)','마늘통닭','무진장한우암소특선모듬 (500g)'
	'갈비찜 1인분','돼지갈비(200g)', '진주불고기','돼지갈비 (600g)', '미니족발','떡갈비','불고기','소갈비','돼지갈비', '광양불고기','바싹불고기']

    test4 = '|'.join(li7)
    meat = df1[df1['대표메뉴'].str.contains(test4)]

    li8 = [ '짜장면', '함흥회냉면', '함흥냉면', '물막국수', '순메밀막국수','전통평양냉면', '평양냉면','간짜장', '삼선짜장면','냉면','대동할매국수 보통','온소바',
	'쫄면','문어 나가사키 짬뽕 나베', '옛날 짜장면', '참깨콩국수', '밀면(물 / 비빔)','막국수','명동칼국수', '평안냉면 (물 / 비빔)','물 막국수','해물짬뽕', '짜장','우동', '칼국수','소바'
	,'진주물냉면','콩국수']

    test5 = '|'.join(li8)
    noodle = df1[df1['대표메뉴'].str.contains(test5)]


    st.subheader('음식별 검색을 합니다')
    food = ['한식','중식','일식','양식','음료']
    selected_food= st.selectbox('음식 종류를 선택하세요',food)
    if selected_food == '한식':
        st.dataframe(korea)
    elif selected_food == '중식':
        st.dataframe(china)
    elif selected_food == '일식':
        st.dataframe(japan)
    elif selected_food == '양식':
        st.dataframe(usa)
    elif selected_food == '음료':
        st.dataframe(cafe)

    st.subheader('뭘 먹을까?')
    food1 = ['뜨끈한 국/탕류','든든한 고기류','면러버 면류']
    selected_food1= st.selectbox('먹고싶은 음식 종류를 선택하세요',food1)
    if selected_food1 == '뜨끈한 국/탕류':
        st.markdown("![Alt Text](https://s3.orbi.kr/data/file/united/2109569778_eZanPj5s_2.gif)")
        st.dataframe(tang)
    elif selected_food1 == '든든한 고기류':
        st.image('https://t1.daumcdn.net/news/202304/26/xportsnews/20230426185004651iayp.jpg',width=400)
        st.dataframe(meat)
    elif selected_food1 == '면러버 면류':
        st.markdown("![Alt Text](https://mblogthumb-phinf.pstatic.net/MjAxOTEwMDJfMTc0/MDAxNTY5OTQ0NDY2MDQ1.XauUSNaEiU5w0xmbpBiml9UIKokFLBrw0jXAzNchFgwg.WEhATJjroUiyMBFAx7WOBCSONL-iymr6MjjPnbWemX8g.GIF.pure082/1569944464188.gif?type=w800)")
        st.dataframe(noodle)