import streamlit as st

mbti_data = {
    "INTJ": {
        "traits": "전략적이고 독립적인 사색가. 큰 그림을 보며 체계적인 계획을 세우는 것을 좋아합니다.",
        "books": [
            "괴테 - 파우스트",
            "조지 오웰 - 1984",
            "플라톤 - 국가"
        ],
        "reason": "INTJ는 깊이 있는 사유와 철학적 내용을 선호하므로, 구조적이고 사상적인 고전을 추천합니다.",
        "travel": "노르웨이 피오르 – 한적하고 장엄한 자연 속에서 사색하며 여유를 즐기기 좋습니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/40/Geirangerfjord_2007_05_23.jpg"
    },
    "INFP": {
        "traits": "이상주의적이며 감성적인 내면 세계를 가진 유형. 의미와 가치를 중요하게 여깁니다.",
        "books": [
            "헤르만 헤세 - 데미안",
            "조지 엘리엇 - 미들마치",
            "톨스토이 - 안나 카레니나"
        ],
        "reason": "INFP는 감정과 철학이 조화를 이루는 작품에서 깊은 울림을 느낄 수 있어 내면 성찰형 고전을 추천합니다.",
        "travel": "체코 프라하 – 예술과 감성이 흐르는 도시에서 영감을 얻기에 안성맞춤입니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/25/Prague_Montage.png"
    },
    "ENTP": {
        "traits": "호기심 많고 에너지 넘치는 토론가. 유쾌하고 재치 있는 스타일을 선호합니다.",
        "books": [
            "세르반테스 - 돈키호테",
            "조너선 스위프트 - 걸리버 여행기",
            "마키아벨리 - 군주론"
        ],
        "reason": "ENTP는 풍자와 실험적 구조, 도전적인 내용에 흥미를 느끼므로 유쾌하고 지적인 고전을 추천합니다.",
        "travel": "도쿄 – 끊임없이 새로운 자극이 있는 도시로, ENTP의 호기심을 만족시켜줍니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/08/Shibuya_Crossing_2019_%28cropped%29.jpg"
    },
    "ISFJ": {
        "traits": "헌신적이고 온화한 수호자. 안정감 있는 관계와 따뜻한 이야기를 선호합니다.",
        "books": [
            "제인 오스틴 - 오만과 편견",
            "루이자 메이 올컷 - 작은 아씨들",
            "찰스 디킨스 - 위대한 유산"
        ],
        "reason": "ISFJ는 정서적으로 따뜻하고 인간 중심적인 이야기를 선호하므로 감성적인 고전을 추천합니다.",
        "travel": "교토 – 고요한 사찰과 전통이 살아 있는 도시에서 마음의 안정을 찾을 수 있습니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/a/aa/Kiyomizu-dera_2010_01.JPG"
    }
}

st.set_page_config(page_title="MBTI 고전 책 & 여름 여행 추천기", page_icon="📚")

st.title("📚 MBTI 고전 책 + 여름 여행 추천기")
st.markdown("당신의 MBTI 유형에 딱 맞는 고전 책 3권과 여름 여행지를 추천해드릴게요!")

selected_mbti = st.selectbox("당신의 MBTI는 무엇인가요?", list(mbti_data.keys()))

if selected_mbti:
    st.balloons()
    mbti_info = mbti_data[selected_mbti]
    
    st.subheader(f"🧠 {selected_mbti}의 성격 특징")
    st.markdown(f"_{mbti_info['traits']}_")
    
    st.subheader("📖 추천 고전 3권")
    for i, book in enumerate(mbti_info["books"], start=1):
        st.markdown(f"**{i}. {book}**")
        
    st.subheader("💡 추천 이유")
    st.info(mbti_info["reason"])
    
    st.subheader("🌴 이번 여름에 어울리는 여행지")
    st.success(mbti_info["travel"])
    
    st.image(mbti_info["image"], caption="추천 여행지 풍경", use_column_width=True)
