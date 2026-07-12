import streamlit as st

from utils.prediction import predict_candidate

st.set_page_config(
    page_title="TalentMatch AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 TalentMatch AI")
st.subheader("Post Assessment Decision Support System")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    st.header("📋 Candidate Information")

    education_level = st.selectbox(
        "Education Level",
        ["Bachelor", "Master", "PhD"]
    )

    years_experience = st.number_input(
        "Years of Experience",
        min_value=0,
        max_value=20,
        value=5
    )

    num_relevant_skills = st.number_input(
        "Number of Relevant Skills",
        min_value=0,
        max_value=20,
        value=3
    )

    internal_referral = st.selectbox(
        "Internal Referral",
        ["No", "Yes"]
    )


with col2:

    st.header("📝 Assessment Scores")

    interview_score = st.slider(
        "Interview Score",
        0.0,
        10.0,
        8.0,
        0.5
    )

    technical_test_score = st.slider(
        "Technical Test Score",
        0.0,
        10.0,
        8.0,
        0.5
    )

    soft_skill_score = st.slider(
        "Soft Skill Score",
        0.0,
        10.0,
        8.0,
        0.5
    )

st.header("💻 Technical Skills")

skill1, skill2, skill3, skill4 = st.columns(4)

selected_skills = []

with skill1:
    if st.checkbox("Python"):
        selected_skills.append("Python")

    if st.checkbox("SQL"):
        selected_skills.append("SQL")

with skill2:
    if st.checkbox("Excel"):
        selected_skills.append("Excel")

    if st.checkbox("Communication"):
        selected_skills.append("Communication")

with skill3:
    if st.checkbox("Leadership"):
        selected_skills.append("Leadership")

    if st.checkbox("Cloud Computing"):
        selected_skills.append("Cloud Computing")

with skill4:
    if st.checkbox("Machine Learning"):
        selected_skills.append("Machine Learning")

    if st.checkbox("Data Visualization"):
        selected_skills.append("Data Visualization")

if st.button("🔍 Predict Candidate", use_container_width=True):

    with st.spinner("Analyzing candidate..."):

        result = predict_candidate(
            education_level=education_level,
            years_experience=years_experience,
            num_relevant_skills=num_relevant_skills,
            internal_referral=internal_referral,
            interview_score=interview_score,
            technical_test_score=technical_test_score,
            soft_skill_score=soft_skill_score,
            selected_skills=selected_skills
        )

    st.header("📊 Prediction Result")

    if result["prediction"] == 1:
        st.success("✅ Candidate is Eligible")
        st.balloons()
    else:
        st.error("❌ Candidate is Not Eligible")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Eligible Probability",
            f"{result['eligible_probability']:.2%}"
        )

    with col2:
        st.metric(
            "Not Eligible Probability",
            f"{result['not_eligible_probability']:.2%}"
        )

    st.subheader("Prediction Confidence")

    st.write("Eligible")
    st.progress(result["eligible_probability"])

    st.write("Not Eligible")
    st.progress(result["not_eligible_probability"])

    with st.expander("📄 Candidate Summary", expanded=False):

        st.write(f"**Education Level:** {education_level}")
        st.write(f"**Years of Experience:** {years_experience}")
        st.write(f"**Relevant Skills Count:** {num_relevant_skills}")
        st.write(f"**Internal Referral:** {internal_referral}")
        st.write(f"**Interview Score:** {interview_score}")
        st.write(f"**Technical Test Score:** {technical_test_score}")
        st.write(f"**Soft Skill Score:** {soft_skill_score}")

        if selected_skills:
            st.write("**Selected Skills:**")
            st.write(", ".join(selected_skills))
        else:
            st.write("**Selected Skills:** None")