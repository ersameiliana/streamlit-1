import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from data_loader import load_data

data = load_data()
df = data["ar_aging"].copy()

st.markdown("""
<div class="telkom-banner">
    <h2>Manajemen Piutang & Risiko Provisi Kredit (AR Aging & Bad Debt)</h2>
    <p>Pemantauan eksposur piutang macet (>6 bulan), lonjakan beban penyisihan kredit ekspektasian, dan simulasi arus kas masuk.</p>
</div>
""", unsafe_allow_html=True)

# KPI Metric Cards
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Provisi Penurunan Nilai Piutang", "Rp 6.955 B", "+14.7% vs 2024 (Rp 6.064B)", delta_color="inverse")
with c2:
    st.metric("Beban Kerugian Kredit Ekspektasian", "Rp 561 B", "+62.1% YoY", delta_color="inverse")
with c3:
    st.metric("Piutang > 6 Bulan (Bruto)", "Rp 6.763 B", "Tingkat Provisi 86.1%", delta_color="inverse")
with c4:
    total_gross_ar = df["Gross_AR_2025"].sum()
    st.metric("Total Piutang Usaha Bruto", f"Rp {total_gross_ar:,.0f} B", "4 Kelompok Umur")

st.markdown("---")

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Komposisi Matriks Umur Piutang Bruto")
    fig_donut = go.Figure(data=[go.Pie(
        labels=df["Aging_Bucket"],
        values=df["Gross_AR_2025"],
        hole=0.5,
        marker=dict(colors=["#0A192F", "#3B82F6", "#F59E0B", "#E01E2E"])
    )])
    fig_donut.update_layout(template="plotly_white", height=400, margin=dict(t=30, b=20))
    st.plotly_chart(fig_donut, use_container_width=True)

with col_right:
    st.subheader("Segmentasi: Pihak Berelasi (BUMN) vs Pihak Ketiga")
    fig_stack = go.Figure()
    fig_stack.add_trace(go.Bar(
        name="Pihak Berelasi (BUMN)",
        x=df["Aging_Bucket"],
        y=df["Related_Party_BUMN"],
        marker_color="#0A192F"
    ))
    fig_stack.add_trace(go.Bar(
        name="Pihak Ketiga (Korporasi & Retail)",
        x=df["Aging_Bucket"],
        y=df["Third_Party_Corporate_Retail"],
        marker_color="#E01E2E"
    ))
    fig_stack.update_layout(
        barmode="stack",
        template="plotly_white",
        yaxis_title="Nilai Piutang (Rp Miliar)",
        height=400,
        margin=dict(t=30, b=20)
    )
    st.plotly_chart(fig_stack, use_container_width=True)

# Cash Flow Modeler
st.markdown("---")
st.subheader("Credit Risk Early Warning & Cash Flow Recovery Modeler")
st.caption("Simulasikan tingkat penagihan (collection rate) pada piutang berisiko tinggi (>6 bulan senilai Rp 6.763 Miliar) untuk melihat tambahan arus kas operasi.")

s1, s2 = st.columns([1, 2])
with s1:
    collection_rate = st.slider("Target Collection Rate Piutang > 6 Bulan (%)", min_value=5.0, max_value=60.0, value=20.0, step=2.5)
    bumn_priority = st.checkbox("Prioritaskan Penagihan BUMN (Rp 3.120 B)", value=True)

ar_over_6m = 6763.0
cash_inflow = ar_over_6m * (collection_rate / 100.0)
provision_reversal = cash_inflow * 0.861

with s2:
    k1, k2 = st.columns(2)
    k1.metric("Tambahan Arus Kas Operasi", f"Rp {cash_inflow:,.1f} B", f"+{collection_rate:.1f}% Tertagih")
    k2.metric("Potensi Pemulihan Provisi (Reversal)", f"Rp {provision_reversal:,.1f} B", "Dampak Positif Laba")
    if bumn_priority:
        st.success(f"Fokus pada klaster BUMN menghasilkan likuiditas cepat hingga Rp {3120 * (collection_rate/100.0):,.1f} Miliar.")
