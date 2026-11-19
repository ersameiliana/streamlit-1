import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from data_loader import load_data

data = load_data()
ms_df = data["market_share"].copy()
pb_df = data["pricing_benchmark"].copy()

st.markdown("""
<div class="telkom-banner">
    <h2>Intelijen Persaingan & Pangsa Pasar (Competitive Intelligence)</h2>
    <p>Pelacakan erosi pangsa pasar IndiHome, dinamika pascamerger XLSmart, serta simulasi strategi Market Repair.</p>
</div>
""", unsafe_allow_html=True)

# KPI Metric Cards
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Market Share IndiHome (2025)", "63.0%", "-2.2% vs 2024 (65.2%)", delta_color="inverse")
with c2:
    st.metric("Market Share Seluler Telkomsel", "48.4%", "vs Kompetitor 51.6% (XLSmart + IOH)")
with c3:
    st.metric("Market Share Telkomsigma (SI)", "9.4%", "Segmen System Integration")
with c4:
    st.metric("Yield Harga Telkomsel", "Rp 3.450 / GB", "+25% Premium vs IOH")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Tren Pangsa Pasar Fixed Broadband 3 Tahun (2023-2025)")
    fig_ms = px.bar(
        ms_df,
        x="Year",
        y="Fixed_BB_Share_Pct",
        color="Operator",
        barmode="group",
        color_discrete_map={
            "IndiHome (Telkom)": "#E01E2E",
            "IconNet (PLN)": "#0A192F",
            "Link Net / XL": "#3B82F6",
            "MyRepublic & MNC Play": "#94A3B8"
        },
        labels={"Fixed_BB_Share_Pct": "Market Share (%)", "Year": "Tahun"}
    )
    fig_ms.update_layout(template="plotly_white", height=420, xaxis=dict(dtick=1))
    st.plotly_chart(fig_ms, use_container_width=True)

with col2:
    st.subheader("Pricing Benchmark Matrix: Yield vs Market Share")
    fig_scatter = px.scatter(
        pb_df,
        x="Yield_IDR_per_GB_or_Mbps",
        y="Market_Share_2025_Pct",
        color="Category",
        size="Market_Share_2025_Pct",
        text="Operator",
        color_discrete_sequence=["#E01E2E", "#0A192F"],
        labels={"Yield_IDR_per_GB_or_Mbps": "Yield Harga (Rp per GB / Mbps)", "Market_Share_2025_Pct": "Pangsa Pasar 2025 (%)"}
    )
    fig_scatter.update_traces(textposition="top center")
    fig_scatter.update_layout(template="plotly_white", height=420)
    st.plotly_chart(fig_scatter, use_container_width=True)

# Market Repair Scenario Modeler
st.markdown("---")
st.subheader("Market Repair Scenario Modeler (Penyesuaian Harga Paket Data)")
st.caption("Simulasikan penyesuaian harga paket data (+2% s/d +10%) untuk melihat dampak elastisitas terhadap pangsa pasar dan pendapatan.")

mc1, mc2 = st.columns([1, 2])
with mc1:
    price_adj = st.slider("Kenaikan Harga Paket Data (%)", min_value=2.0, max_value=10.0, value=5.0, step=0.5)
    elasticity = st.slider("Asumsi Elastisitas Permintaan", min_value=-0.8, max_value=-0.1, value=-0.35, step=0.05)

vol_impact_pct = price_adj * elasticity
net_rev_impact_pct = ((1 + price_adj / 100.0) * (1 + vol_impact_pct / 100.0) - 1) * 100.0
rev_impact_idr_b = 109307.0 * (net_rev_impact_pct / 100.0)
new_ms = 48.4 + (vol_impact_pct * 0.4)

with mc2:
    r1, r2, r3 = st.columns(3)
    r1.metric("Dampak Volume / Market Share", f"{new_ms:.2f}%", f"{vol_impact_pct * 0.4:.2f}% Share")
    r2.metric("Net Revenue Impact (%)", f"{net_rev_impact_pct:+.2f}%")
    r3.metric("Tambahan Pendapatan Telkomsel", f"Rp {rev_impact_idr_b:+,.1f} B")
