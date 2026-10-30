import streamlit as st

st.write("### 🧠 간단 MBTI 성격 유형 테스트")
st.text("질문별로 솔직하게 답해주세요!")

# 1. E vs I (외향?내향?)
st.write("#### [1] 외향?내향? (E vs I)")
q1 = st.radio("1. 주말에 에너지를 충전하는 방법은?", ["사람들을 만나며 활력을 얻는다 (E)", "집에서 혼자만의 시간을 가지며 쉰다 (I)"], key="q1")
q2 = st.radio("2. 새로운 모임이나 파티에 갔을 때 나는?", ["먼저 사람들에게 다가가 말을 건다 (E)", "아는 사람이 올 때까지 조용히 기다린다 (I)"], key="q2")
q3 = st.radio("3. 평소 대화를 할 때 나의 스타일은?", ["생각을 말로 바로 내뱉으며 정리한다 (E)", "속으로 충분히 생각한 뒤에 이야기한다 (I)"], key="q3")

st.markdown("---")

# 2. S vs N (인식 기능)
st.write("#### [2] 인식 기능 (S vs N)")
q4 = st.radio("4. 영화나 소설을 볼 때 나는?", ["실제 있었던 사건이나 현실적인 스토리에 몰입한다 (S)", "상상력을 자극하는 판타지나 미래지향적 세계관이 좋다 (N)"], key="q4")
q5 = st.radio("5. 길을 찾거나 새로운 것을 배울 때?", ["구체적인 매뉴얼과 경험, 사실을 중시한다 (S)", "직관적인 느낌과 전체적인 흐름을 먼저 파악한다 (N)"], key="q5")
q6 = st.radio("6. 아이디어를 낼 때 나는?", ["현실적으로 실현 가능한 방안을 먼저 생각한다 (S)", "새롭고 독창적인 가능성을 열어두고 구상한다 (N)"], key="q6")

st.markdown("---")

# 3. T vs F (판단 기능)
st.write("#### [3] 판단 기능 (T vs F)")
q7 = st.radio("7. 친구가 고민을 털어놓을 때 나의 반응은?", ["객관적인 원인 분석과 해결책을 제시해 준다 (T)", "먼저 감정에 공감하고 위로를 건넨다 (F)"], key="q7")
q8 = st.radio("8. 중요한 결정을 내릴 때 가장 중요한 것은?", ["논리적인 타당성과 효율성 (T)", "주변 사람들에게 미칠 영향과 조화 (F)"], key="q8")
q9 = st.radio("9. 피드백을 주고받을 때 나는?", ["감정보다는 사실과 성과 위주의 직설적 피드백이 좋다 (T)", "부드럽고 배려 있는 어조의 피드백이 좋다 (F)"], key="q9")

st.markdown("---")

# 4. J vs P (생활 양식)
st.write("#### [4] 생활 양식 (J vs P)")
q10 = st.radio("10. 여행을 갈 때 나는?", ["일자별, 시간별로 꼼꼼하게 계획을 세운다 (J)", "큰 틀만 정하고 즉흥적으로 움직인다 (P)"], key="q10")
q11 = st.radio("11. 과제나 업무를 처리할 때?", ["마감일보다 훨씬 여유 있게 미리 끝낸다 (J)", "마감 직전에 집중해서 한 번에 끝낸다 (P)"], key="q11")
q12 = st.radio("12. 내 방이나 책상의 상태는?", ["물건의 제자리가 정해져 있고 깔끔하다 (J)", "조금 어지러워 보여도 내 기준에선 편하다 (P)"], key="q12")

st.markdown("---")

# 결과 확인 버튼
if st.button("결과 확인하기"):
    # 지표별 점수 산출
    e_count = sum([1 for q in [q1, q2, q3] if "(E)" in q])
    i_count = 3 - e_count
    
    s_count = sum([1 for q in [q4, q5, q6] if "(S)" in q])
    n_count = 3 - s_count
    
    t_count = sum([1 for q in [q7, q8, q9] if "(T)" in q])
    f_count = 3 - t_count
    
    j_count = sum([1 for q in [q10, q11, q12] if "(J)" in q])
    p_count = 3 - j_count

    # MBTI 조합
    mbti = ""
    mbti += "E" if e_count >= i_count else "I"
    mbti += "S" if s_count >= n_count else "N"
    mbti += "T" if t_count >= f_count else "F"
    mbti += "J" if j_count >= p_count else "P"

    # 결과 출력
    st.success(f"🎉 당신의 MBTI 유형은 **{mbti}** 입니다!")
    st.info(f"📊 세부 점수 - E/I: {e_count}:{i_count} | S/N: {s_count}:{n_count} | T/F: {t_count}:{f_count} | J/P: {j_count}:{p_count}")