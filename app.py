import base64

import streamlit as st
import pandas as pd

from utils.prediction import predict_candidate

st.set_page_config(
    page_title="TalentMatch AI",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>

/* ============ Apple-inspired design system ============ */

@import url('https://fonts.cdnfonts.com/css/sf-pro-display');

html, body, [class*="css"] {
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display",
                 "SF Pro Text", "Helvetica Neue", Arial, sans-serif;
}

.stApp{
    background:#F5F5F7;
}

/* Kill Streamlit's default top padding for a tighter, Apple-like hero */
.block-container{
    padding-top:2.5rem;
    max-width:1100px;
}

.main-header{
    background:#FFFFFF;
    padding:56px 48px;
    border-radius:28px;
    margin-bottom:36px;
    border:1px solid #F0F0F2;
    box-shadow:0 1px 2px rgba(0,0,0,.02), 0 12px 32px rgba(0,0,0,.04);
}

.main-title{
    font-size:44px;
    font-weight:700;
    letter-spacing:-0.02em;
    color:#1D1D1F;
}

.main-subtitle{
    font-size:19px;
    color:#86868B;
    font-weight:400;
}

.eyebrow{
    display:inline-block;
    font-size:13px;
    font-weight:600;
    letter-spacing:.02em;
    color:#0071E3;
    background:#EAF2FE;
    padding:5px 14px;
    border-radius:999px;
    margin-bottom:14px;
}

/* Section labels */
.section-label{
    font-size:13px;
    font-weight:600;
    letter-spacing:.03em;
    text-transform:uppercase;
    color:#86868B;
    margin:8px 0 18px 0;
}

/* Cards */
.upload-card{
    background:#FFFFFF;
    padding:28px;
    border-radius:20px;
    border:1px solid #F0F0F2;
    margin-bottom:25px;
    box-shadow:0 1px 2px rgba(0,0,0,.02), 0 8px 24px rgba(0,0,0,.03);
}

.result-card{
    background:#FFFFFF;
    border-radius:24px;
    padding:44px 32px;
    text-align:center;
    margin-top:24px;
    border:1px solid #F0F0F2;
    box-shadow:0 1px 2px rgba(0,0,0,.02), 0 16px 40px rgba(0,0,0,.05);
}

.success-card{
    border-top:4px solid #30D158;
}

.error-card{
    border-top:4px solid #FF3B30;
}

.result-card h2{
    color:#1D1D1F;
    font-weight:600;
    letter-spacing:-0.01em;
}

.big-probability{
    font-size:52px;
    font-weight:700;
    letter-spacing:-0.02em;
    color:#1D1D1F;
    margin:8px 0;
}

.small-text{
    color:#86868B;
    font-size:14px;
}

/* Streamlit native widget polish */
div[data-testid="stMetricValue"]{
    color:#1D1D1F;
    font-weight:700;
}

.stButton > button{
    background:#0071E3;
    color:#FFFFFF;
    border:none;
    border-radius:980px;
    font-weight:600;
    font-size:16px;
    padding:12px 28px;
    transition:background .2s ease, transform .1s ease;
    box-shadow:none;
}

.stButton > button:hover{
    background:#0077ED;
    transform:translateY(-1px);
}

.stButton > button:active{
    transform:translateY(0px);
}

/* Tabs */
.stTabs [data-baseweb="tab-list"]{
    gap:8px;
    background:#F5F5F7;
    padding:6px;
    border-radius:14px;
}

.stTabs [data-baseweb="tab"]{
    border-radius:10px;
    padding:10px 20px;
    font-weight:500;
    color:#6E6E73;
}

.stTabs [aria-selected="true"]{
    background:#FFFFFF;
    color:#1D1D1F;
    box-shadow:0 1px 3px rgba(0,0,0,.08);
}

/* Sliders — Apple blue thumb/track */
div[data-baseweb="slider"] div[role="slider"]{
    background-color:#0071E3 !important;
    border-color:#0071E3 !important;
}

div[data-testid="stTickBar"]{
    display:none;
}

/* Section cards (Candidate Information / Assessment Scores) */
div[data-testid="stVerticalBlockBorderWrapper"]{
    background:#FFFFFF;
    border-radius:20px !important;
    border:1px solid #E8E8ED !important;
    box-shadow:0 1px 2px rgba(0,0,0,.02), 0 8px 24px rgba(0,0,0,.04);
    padding:8px 6px 20px 6px;
}

/* Field labels */
.stSelectbox label, .stNumberInput label, .stSlider label{
    font-size:14px !important;
    font-weight:500 !important;
    color:#1D1D1F !important;
}

/* Selectbox */
div[data-baseweb="select"] > div{
    background:#F5F5F7 !important;
    border:1px solid #E8E8ED !important;
    border-radius:12px !important;
    box-shadow:none !important;
}

/* Number input */
.stNumberInput input{
    background:#F5F5F7 !important;
    border:1px solid #E8E8ED !important;
    border-radius:12px !important;
    color:#1D1D1F !important;
}

.stNumberInput button{
    background:#F5F5F7 !important;
    border:1px solid #E8E8ED !important;
}

/* Checkboxes */
.stCheckbox label p{
    color:#1D1D1F !important;
    font-size:15px !important;
}

/* Expander */
.streamlit-expanderHeader{
    background:#FFFFFF;
    border-radius:14px;
    font-weight:500;
    color:#1D1D1F;
}

/* DataFrame / table corners */
[data-testid="stDataFrame"]{
    border-radius:16px;
    overflow:hidden;
    border:1px solid #F0F0F2;
}

hr{
    border:none;
    border-top:1px solid #E8E8ED;
    margin:24px 0;
}

</style>
""", unsafe_allow_html=True)

with open("assets/logo.png", "rb") as logo_file:
    logo_base64 = base64.b64encode(logo_file.read()).decode()

st.markdown(
    f"""
    <div class="main-header" style="display:flex; align-items:center; gap:28px;">
        <img src="data:image/png;base64,{logo_base64}"
             width="90"
             style="border-radius:18px; flex-shrink:0;" />
        <div>
            <span class="eyebrow">DECISION SUPPORT SYSTEM</span>
            <h1 class="main-title" style="margin:6px 0 4px 0;">
                TalentMatch AI
            </h1>
            <p class="main-subtitle" style="margin:0;">
                AI-powered hiring recommendation platform for post-assessment decisions.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =====================================================
# Tabs
# =====================================================

tab1, tab2 = st.tabs([
    "🔍 Individual Prediction",
    "📂 Batch Prediction"
])

with tab1:

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.markdown(
                "<h4 style='padding:10px 12px 4px 12px; color:#1D1D1F;'>Candidate Information</h4>",
                unsafe_allow_html=True
            )

            inner1, inner2 = st.columns([0.06, 0.94])

            with inner2:

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

        with st.container(border=True):

            st.markdown(
                "<h4 style='padding:10px 12px 4px 12px; color:#1D1D1F;'>Assessment Scores</h4>",
                unsafe_allow_html=True
            )

            inner1, inner2 = st.columns([0.06, 0.94])

            with inner2:

                interview_score = st.slider(
                    "Interview Score",
                    0.0,
                    10.0,
                    8.0,
                    0.1
                )

                technical_test_score = st.slider(
                    "Technical Test Score",
                    0.0,
                    10.0,
                    8.0,
                    0.1
                )

                soft_skill_score = st.slider(
                    "Soft Skill Score",
                    0.0,
                    10.0,
                    8.0,
                    0.1
                )

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    with st.container(border=True):

        st.markdown(
            "<h4 style='padding:10px 12px 4px 12px; color:#1D1D1F;'>💻 Technical Skills</h4>",
            unsafe_allow_html=True
        )

        skill_pad, skill_body = st.columns([0.03, 0.97])

        with skill_body:

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

    st.markdown("<br>", unsafe_allow_html=True)

    predict = st.button(
        "🚀 Predict Candidate",
        use_container_width=True,
        type="primary"
    )

    if predict:

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

        # ===========================
        # Prediction Card
        # ===========================

        if result["prediction"] == 1:

            st.markdown(f"""
            <div class="result-card success-card">
                <h2>✅ Candidate is Eligible</h2>
                <div class="big-probability">
                    {result['eligible_probability']:.1%}
                </div>
                <div class="small-text">
                    Hiring Recommendation Confidence
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.balloons()

        else:

            st.markdown(f"""
            <div class="result-card error-card">
                <h2>❌ Candidate is Not Eligible</h2>
                <div class="big-probability">
                    {result['not_eligible_probability']:.1%}
                </div>
                <div class="small-text">
                    Hiring Recommendation Confidence
                </div>
            </div>
            """, unsafe_allow_html=True)

        # ===========================
        # Confidence
        # ===========================

        st.subheader("📊 Prediction Confidence")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Eligible",
                f"{result['eligible_probability']:.1%}"
            )

            st.progress(
                float(result["eligible_probability"])
            )

        with col2:

            st.metric(
                "Not Eligible",
                f"{result['not_eligible_probability']:.1%}"
            )

            st.progress(
                float(result["not_eligible_probability"])
            )

        # ===========================
        # Candidate Summary
        # ===========================

        with st.expander("📄 Candidate Summary", expanded=False):

            summary = pd.DataFrame({

                "Field": [
                    "Education",
                    "Experience",
                    "Relevant Skills",
                    "Referral",
                    "Interview",
                    "Technical Test",
                    "Soft Skill"
                ],

                "Value": [
                    education_level,
                    f"{years_experience} Years",
                    num_relevant_skills,
                    internal_referral,
                    interview_score,
                    technical_test_score,
                    soft_skill_score
                ]

            })

            st.table(summary)

            st.write("### 💻 Technical Skills")

            if selected_skills:
                st.success(", ".join(selected_skills))
            else:
                st.info("No skills selected.")

with tab2:

    st.markdown("## 📂 Batch Prediction")

    st.write(
        """
Upload a CSV file containing multiple candidates to predict
their hiring eligibility simultaneously.
"""
    )

    uploaded_file = st.file_uploader(
        "Upload Candidate CSV",
        type=["csv"],
        key="batch_upload"
    )

    with open("assets/candidate_quality_improved.csv", "rb") as sample_file:
        st.download_button(
            "⬇ Download Sample CSV",
            data=sample_file,
            file_name="sample_candidate.csv",
            mime="text/csv"
        )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.success(
            f"✅ {len(df)} candidates successfully loaded."
        )

        st.dataframe(df)

        if st.button("🚀 Predict All Candidates"):

            with st.spinner("Analyzing all candidates..."):

                predictions = []
                eligible_probs = []
                not_eligible_probs = []

                for _, row in df.iterrows():

                    row_skills = [
                        skill.strip()
                        for skill in str(row.get("selected_skills", "")).split(",")
                        if skill.strip()
                    ]

                    result = predict_candidate(
                        education_level=row.get("education_level"),
                        years_experience=row.get("years_experience"),
                        num_relevant_skills=row.get("num_relevant_skills"),
                        internal_referral=row.get("internal_referral"),
                        interview_score=row.get("interview_score"),
                        technical_test_score=row.get("technical_test_score"),
                        soft_skill_score=row.get("soft_skill_score"),
                        selected_skills=row_skills
                    )

                    predictions.append(
                        "Eligible" if result["prediction"] == 1 else "Not Eligible"
                    )
                    eligible_probs.append(result["eligible_probability"])
                    not_eligible_probs.append(result["not_eligible_probability"])

                df["Prediction"] = predictions
                df["Eligible Probability"] = eligible_probs
                df["Not Eligible Probability"] = not_eligible_probs

            st.success("✅ Batch prediction completed.")

            st.dataframe(df)

            st.download_button(
                "⬇ Download Prediction Results",
                data=df.to_csv(index=False).encode("utf-8"),
                file_name="prediction_results.csv",
                mime="text/csv"
            )