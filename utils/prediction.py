import joblib
import pandas as pd
import sklearn
import streamlit as st

from utils.preprocessing import (
    create_seniority_tier,
    encode_features,
    create_candidate_dataframe,
    create_skill_features
)

model = joblib.load("models/gradient_boosting_model.pkl")

scaler = joblib.load("models/scaler.pkl")

encoders = joblib.load("models/label_encoders.pkl")

feature_order = joblib.load("models/feature_order.pkl")

skill_columns = joblib.load("models/skill_columns.pkl")


def predict_candidate(
    education_level,
    years_experience,
    num_relevant_skills,
    internal_referral,
    interview_score,
    technical_test_score,
    soft_skill_score,
    selected_skills
):
    """
    Predict hiring eligibility for one candidate.
    """

    # =====================================
    # Feature Engineering
    # =====================================
    exp_level, seniority_tier = create_seniority_tier(
        years_experience,
        education_level
    )

    # =====================================
    # Encode categorical features
    # =====================================
    (
        education_encoded,
        referral_encoded,
        tier_encoded
    ) = encode_features(
        education_level,
        internal_referral,
        seniority_tier,
        encoders
    )

    # =====================================
    # Create candidate dataframe
    # =====================================
    candidate_df = create_candidate_dataframe(
        education_encoded,
        years_experience,
        num_relevant_skills,
        referral_encoded,
        interview_score,
        technical_test_score,
        soft_skill_score,
        tier_encoded
    )

    # =====================================
    # Create skill dummy variables
    # =====================================
    skill_df = create_skill_features(
        selected_skills,
        skill_columns
    )

    # =====================================
    # Combine candidate + skill features
    # =====================================
    candidate_full = pd.concat(
        [candidate_df, skill_df],
        axis=1
    )

    # =====================================
    # Match training feature order
    # =====================================
    candidate_full = candidate_full[feature_order]

    # =====================================
    # Scaling
    # =====================================

    candidate_scaled = scaler.transform(candidate_full)

    # =====================================
    # Prediction
    # =====================================
    prediction = model.predict(candidate_scaled)[0]

    probability = model.predict_proba(candidate_scaled)[0]

    # =====================================
    # Convert prediction to label
    # =====================================
    label = (
        "Eligible"
        if prediction == 1
        else "Not Eligible"
    )

    # =====================================
    # Return result
    # =====================================
    return {
        "label": label,
        "prediction": int(prediction),
        "eligible_probability": float(probability[1]),
        "not_eligible_probability": float(probability[0])
    }

if __name__ == "__main__":

    result = predict_candidate(
        education_level="Bachelor",
        years_experience=7,
        num_relevant_skills=2,
        internal_referral="No",
        interview_score=8.5,
        technical_test_score=9,
        soft_skill_score=8,
        selected_skills=["Python", "SQL"]
    )

    print(result)

