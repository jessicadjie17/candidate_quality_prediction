"""
Preprocessing functions for TalentMatchAI
"""

import pandas as pd


def create_seniority_tier(years_experience, education_level):
    """
    Membuat exp_level dan seniority_tier
    sesuai pipeline training.
    """

    exp_level = pd.cut(
        [years_experience],
        bins=[-1, 2, 5, 10, 19],
        labels=["Entry", "Junior", "Mid", "Senior"]
    )[0]

    seniority_tier = f"{exp_level}_{education_level}"

    return exp_level, seniority_tier



def encode_features(
    education_level,
    internal_referral,
    seniority_tier,
    encoders
):

    education_encoded = encoders["education_level"].transform(
        [education_level]
    )[0]

    referral_encoded = encoders["internal_referral"].transform(
        [internal_referral]
    )[0]

    tier_encoded = encoders["seniority_tier"].transform(
        [seniority_tier]
    )[0]

    return (
        education_encoded,
        referral_encoded,
        tier_encoded
    )



def create_candidate_dataframe(
    education_encoded,
    years_experience,
    num_relevant_skills,
    referral_encoded,
    interview_score,
    technical_test_score,
    soft_skill_score,
    tier_encoded
):
    """
    Membuat DataFrame kandidat
    sebelum digabung dengan skill features.
    """

    candidate_df = pd.DataFrame({
        "education_level": [education_encoded],
        "years_experience": [years_experience],
        "num_relevant_skills": [num_relevant_skills],
        "internal_referral": [referral_encoded],
        "interview_score": [interview_score],
        "technical_test_score": [technical_test_score],
        "soft_skill_score": [soft_skill_score],
        "seniority_tier": [tier_encoded]
    })

    return candidate_df

def create_skill_features(selected_skills, skill_columns):
    """
    Membuat dummy variables untuk skill
    sesuai urutan saat training.
    """

    skill_dict = {}

    for skill in skill_columns:
        skill_dict[skill] = 1 if skill in selected_skills else 0

    skill_df = pd.DataFrame([skill_dict])

    return skill_df