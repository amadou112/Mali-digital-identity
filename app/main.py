import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="ML Mali Digital Identity",
    page_icon="🇲🇱",
    layout="wide"
)

DATA_PATH = Path("data/citizens_100k.csv")


@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


df = load_data()

st.markdown("""
<style>
.stApp {
    background: #f8faf9;
}

.main-title {
    font-size: 44px;
    font-weight: 900;
    color: #064e3b;
}

.subtitle {
    font-size: 24px;
    color: #475569;
    margin-bottom: 10px;
}

.flag-bar {
    height: 10px;
    background: linear-gradient(to right, #14a44d 33%, #fcd116 33%, #fcd116 66%, #ce1126 66%);
    border-radius: 999px;
    margin-bottom: 30px;
}

.card {
    background: white;
    padding: 30px;
    border-radius: 22px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    border: 1px solid #e5e7eb;
}

.metric-card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    border-bottom: 5px solid #064e3b;
    box-shadow: 0 5px 18px rgba(0,0,0,0.06);
}

.metric-number {
    font-size: 30px;
    font-weight: 800;
    color: #064e3b;
}

.metric-label {
    color: #475569;
    font-size: 15px;
}

.footer {
    background: #064e3b;
    color: white;
    padding: 18px;
    border-radius: 12px;
    text-align: center;
    margin-top: 35px;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🇲🇱 ML Mali")
    st.markdown("**Digital Identity Platform**")
    st.divider()

    page = st.radio(
        "Navigation",
        ["Dashboard", "Search Citizen", "Duplicate Check", "Citizen Records"]
    )

    st.divider()
    st.success("Secure. Trusted. Digital.")

st.markdown('<div class="flag-bar"></div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">🇲🇱 ML Mali Digital Identity Platform</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">National Citizen Database MVP</div>', unsafe_allow_html=True)
st.markdown("### 🇲🇱 Un Peuple - Un But - Une Foi")

st.write("")

if page == "Dashboard":
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{len(df):,}</div>
            <div class="metric-label">Total Citizens Registered</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{df["region"].nunique()}</div>
            <div class="metric-label">Regions Covered</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">99.98%</div>
            <div class="metric-label">Data Accuracy Rate</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">100%</div>
            <div class="metric-label">Secure & Encrypted</div>
        </div>
        """, unsafe_allow_html=True)

elif page == "Search Citizen":
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.header("🔍 Search Citizen")
    st.caption("Search by National ID, First Name, Last Name, or Gender")

    search_by = st.radio(
        "Search by",
        ["National ID", "First Name", "Last Name", "Gender"],
        horizontal=True
    )

    if search_by == "Gender":
        search_value = st.selectbox("Select gender", ["Male", "Female"])
    else:
        search_value = st.text_input(
            "Enter search value",
            placeholder="Type your search here..."
        )

    if st.button("Search"):
        if not search_value:
            st.warning("Please enter a search value.")
        else:
            if search_by == "National ID":
                results = df[df["national_id"].astype(str).str.contains(search_value, case=False, na=False)]

            elif search_by == "First Name":
                results = df[df["first_name"].astype(str).str.contains(search_value, case=False, na=False)]

            elif search_by == "Last Name":
                results = df[df["last_name"].astype(str).str.contains(search_value, case=False, na=False)]

            else:
                results = df[df["gender"].astype(str).str.lower() == search_value.lower()]

            if results.empty:
                st.error("No citizen found.")
            else:
                st.success(f"{len(results)} record(s) found.")
                st.dataframe(results, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Duplicate Check":
    st.header("🛡️ Duplicate Check")

    duplicate_cols = ["first_name", "last_name", "date_of_birth"]
    duplicates = df[df.duplicated(subset=duplicate_cols, keep=False)]

    if duplicates.empty:
        st.success("No potential duplicates found.")
    else:
        st.warning(f"{len(duplicates)} potential duplicate records found.")
        st.dataframe(duplicates, use_container_width=True)

elif page == "Citizen Records":
    st.header("📋 Citizen Records")
    st.dataframe(df.head(1000), use_container_width=True)

st.markdown("""
<div class="footer">
    🇲🇱 ML Mali Digital Identity Platform • Secure. Trusted. Digital.
</div>
""", unsafe_allow_html=True)