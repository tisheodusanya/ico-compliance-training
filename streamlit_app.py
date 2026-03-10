import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="UK Data Compliance Training", layout="wide")

st.title("UK Data Legislation & ICO Compliance Training")

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Computer Misuse Act",
        "Data Protection Act",
        "Freedom of Information Act",
        "UK GDPR",
        "PECR",
        "ICO Oversight",
        "Case Study",
        "Assessment",
        "Analytics Dashboard",
    ],
)

if "results" not in st.session_state:
    st.session_state.results = []

# -------------------------
# HOME
# -------------------------

if page == "Home":
    st.header("Welcome to Compliance Training")

    st.write(
        """
This interactive system helps staff understand UK data legislation and the role of the ICO.

Modules include:

• Computer Misuse Act 1990  
• Data Protection Act 2018  
• Freedom of Information Act 2000  
• UK GDPR  
• Privacy and Electronic Communications Regulations (PECR)

The system records quiz results and generates analytics to identify compliance risk areas.
"""
    )

# -------------------------
# LAW MODULES
# -------------------------

if page == "Computer Misuse Act":
    st.header("Computer Misuse Act 1990")

    st.write(
        """
This law makes it illegal to:

• Access computer systems without permission  
• Hack into accounts or databases  
• Spread malware  
"""
    )

    q = st.radio(
        "Which activity breaks the Computer Misuse Act?",
        [
            "Accessing a file with permission",
            "Guessing a password to access a colleague's account",
            "Logging out of a shared computer",
        ],
    )

    if st.button("Submit Answer - CMA"):
        score = 1 if q == "Guessing a password to access a colleague's account" else 0
        st.session_state.results.append({"law": "CMA", "score": score})
        st.success("Answer recorded")


if page == "Data Protection Act":
    st.header("Data Protection Act 2018")

    st.write(
        """
The Data Protection Act controls how personal data is used.

Key principles include:

• Lawful processing  
• Data minimisation  
• Accuracy  
• Security of personal data
"""
    )

    q = st.radio(
        "Which is a principle of the Data Protection Act?",
        [
            "Collect unlimited personal data",
            "Store data securely",
            "Sell personal data without permission",
        ],
    )

    if st.button("Submit Answer - DPA"):
        score = 1 if q == "Store data securely" else 0
        st.session_state.results.append({"law": "DPA", "score": score})
        st.success("Answer recorded")


if page == "Freedom of Information Act":
    st.header("Freedom of Information Act 2000")

    st.write(
        """
FOIA allows the public to request information from public authorities.

It promotes:

• Transparency
• Accountability
"""
    )

    q = st.radio(
        "Who can request information under FOIA?",
        [
            "Only journalists",
            "Any member of the public",
            "Only government officials",
        ],
    )

    if st.button("Submit Answer - FOIA"):
        score = 1 if q == "Any member of the public" else 0
        st.session_state.results.append({"law": "FOIA", "score": score})
        st.success("Answer recorded")


if page == "UK GDPR":
    st.header("UK GDPR")

    st.write(
        """
UK GDPR regulates how organisations process personal data.

It gives individuals rights including:

• Right to access data  
• Right to erasure  
• Right to correct inaccurate data
"""
    )

    q = st.radio(
        "Which right exists under UK GDPR?",
        [
            "Right to be forgotten",
            "Right to unlimited data storage",
            "Right to bypass security",
        ],
    )

    if st.button("Submit Answer - GDPR"):
        score = 1 if q == "Right to be forgotten" else 0
        st.session_state.results.append({"law": "GDPR", "score": score})
        st.success("Answer recorded")


if page == "PECR":
    st.header("Privacy and Electronic Communications Regulations (PECR)")

    st.write(
        """
PECR controls electronic marketing communications such as:

• Email marketing  
• Cookies  
• SMS advertising
"""
    )

    q = st.radio(
        "Which action breaks PECR?",
        [
            "Sending marketing emails without consent",
            "Asking for permission before emails",
            "Allowing users to unsubscribe",
        ],
    )

    if st.button("Submit Answer - PECR"):
        score = 1 if q == "Sending marketing emails without consent" else 0
        st.session_state.results.append({"law": "PECR", "score": score})
        st.success("Answer recorded")


# -------------------------
# ICO SECTION
# -------------------------

if page == "ICO Oversight":
    st.header("Information Commissioner's Office")

    st.write(
        """
The ICO is the UK's independent authority for data protection.

Responsibilities include:

• Enforcing UK GDPR and DPA 2018  
• Investigating data breaches  
• Issuing fines and enforcement notices  
• Providing guidance to organisations  
• Promoting transparency
"""
    )

    q = st.radio(
        "What can the ICO do?",
        [
            "Issue fines for data breaches",
            "Arrest employees",
            "Control internet access",
        ],
    )

    if st.button("Submit Answer - ICO"):
        score = 1 if q == "Issue fines for data breaches" else 0
        st.session_state.results.append({"law": "ICO", "score": score})
        st.success("Answer recorded")

# -------------------------
# CASE STUDY
# -------------------------

if page == "Case Study":
    st.header("Real ICO Enforcement Case")

    st.write(
        """
Case: British Airways Data Breach

Hackers accessed customer data including payment details.

ICO investigation found poor security controls.
"""
    )

    q = st.radio(
        "Which law was breached?",
        [
            "UK GDPR",
            "Freedom of Information Act",
            "Computer Misuse Act only",
        ],
    )

    if st.button("Submit Answer - Case"):
        score = 1 if q == "UK GDPR" else 0
        st.session_state.results.append({"law": "Case Study", "score": score})
        st.success("Answer recorded")

    st.write(
        """
Outcome:

• ICO fined British Airways £20 million  
• Required security improvements  
• Highlighted importance of protecting personal data
"""
    )

# -------------------------
# ASSESSMENT
# -------------------------

if page == "Assessment":
    st.header("Final Compliance Assessment")

    q1 = st.radio(
        "Which law protects personal data?",
        ["Data Protection Act", "Freedom of Information Act", "Computer Misuse Act"],
    )

    q2 = st.radio(
        "Who enforces data protection laws?",
        ["ICO", "Police", "HMRC"],
    )

    if st.button("Submit Assessment"):
        score = 0
        if q1 == "Data Protection Act":
            score += 1
        if q2 == "ICO":
            score += 1

        st.session_state.results.append({"law": "Assessment", "score": score})

        st.success(f"Assessment Score: {score}/2")

# -------------------------
# ANALYTICS DASHBOARD
# -------------------------

if page == "Analytics Dashboard":
    st.header("Learning Analytics Dashboard")

    if len(st.session_state.results) == 0:
        st.warning("No data yet. Complete modules first.")
    else:
        df = pd.DataFrame(st.session_state.results)

        law_scores = df.groupby("law").mean().reset_index()

        fig = px.bar(
            law_scores,
            x="law",
            y="score",
            title="Average Understanding by Law",
        )

        st.plotly_chart(fig)

        avg_score = df["score"].mean()

        st.metric("Overall Compliance Readiness", f"{round(avg_score*100)}%")

        weak = law_scores.sort_values("score").iloc[0]["law"]

        st.write(f"⚠ Weakest knowledge area: **{weak}**")
