import streamlit as st

# Konfigurasi Halaman Utama
st.set_page_config(
    page_title="Telkom Group Strategic Executive Dashboard 2025",
    page_icon=":material/analytics:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk Tema Korporat Telkom (#E01E2E, #0A192F, #F8F9FA, #1E293B)
st.markdown("""
    <style>
        /* Latar belakang utama */
        .stApp {
            background-color: #F8F9FA;
            color: #1E293B;
        }
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #0A192F;
            color: #FFFFFF;
        }
        [data-testid="stSidebar"] * {
            color: #F8F9FA !important;
        }
        /* Metric Card Styling */
        [data-testid="stMetric"] {
            background-color: #FFFFFF;
            border-left: 5px solid #E01E2E;
            padding: 15px 20px;
            border-radius: 8px;
            box-shadow: 0 2px 6px rgba(10, 25, 47, 0.08);
        }
        [data-testid="stMetricLabel"] {
            font-weight: 600;
            color: #475569;
            font-size: 0.9rem;
        }
        [data-testid="stMetricValue"] {
            font-weight: 700;
            color: #0A192F;
        }
        /* Header & Title */
        h1, h2, h3 {
            color: #0A192F;
            font-weight: 700;
        }
        .telkom-banner {
            background: linear-gradient(90deg, #0A192F 0%, #1E293B 70%, #E01E2E 100%);
            padding: 18px 24px;
            border-radius: 10px;
            color: #FFFFFF;
            margin-bottom: 20px;
        }
        .telkom-banner h2 {
            color: #FFFFFF !important;
            margin: 0;
            font-size: 1.5rem;
        }
        .telkom-banner p {
            color: #E2E8F0;
            margin: 4px 0 0 0;
            font-size: 0.95rem;
        }
    </style>
""", unsafe_allow_html=True)

# Definisi Halaman Navigasi Modern (st.Page dengan Material Icons)
pages = [
    st.Page("pages/1_Subsidiary_Performance.py", title="Subsidiary Performance", icon=":material/apartment:"),
    st.Page("pages/2_AR_Aging_and_Credit_Risk.py", title="AR Aging & Credit Risk", icon=":material/credit_card:"),
    st.Page("pages/3_Customer_Churn_and_ARPU.py", title="Customer Churn & ARPU", icon=":material/group:"),
    st.Page("pages/4_Competitive_Intelligence.py", title="Competitive Intelligence", icon=":material/bar_chart:"),
    st.Page("pages/5_CapEx_and_Depreciation.py", title="CapEx & Depreciation", icon=":material/domain:"),
    st.Page("pages/6_Investment_Portfolio.py", title="Investment Portfolio", icon=":material/show_chart:")
]

pg = st.navigation(pages)

with st.sidebar:
    st.markdown("### TELKOM INDONESIA")
    st.caption("Strategic Executive Dashboard 2025")
    st.divider()
    st.markdown("**Konteks Laporan Tahunan 2025**")
    st.caption("Pemantauan 6 Pilar Isu Strategis, Risiko Kredit, FMC, Persaingan, CapEx, dan Portofolio Digital.")

pg.run()
