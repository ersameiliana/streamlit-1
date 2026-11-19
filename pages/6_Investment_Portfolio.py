import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from data_loader import load_data

data = load_data()
mdi_df = data["mdi_portfolio"].copy()

st.markdown("""
<div class="telkom-banner">
    <h2>Valuasi Portofolio Investasi Digital (Investment Portfolio)</h2>
    <p>Pemantauan dampak fluktuasi nilai wajar saham GoTo terhadap laba rugi serta matriks kinerja portofolio MDI Ventures.</p>
</div>
""", unsafe_allow_html=True)

# KPI Metric Cards
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Kerugian Belum Direalisasi (2025)", "-Rp 242 B", "vs Untung Rp 188B (2024)", delta_color="inverse")
with c2:
    st.metric("Harga Saham GoTo (Penutupan)", "Rp 64 / saham", "-8.6% vs 2024 (Rp 70)", delta_color="inverse")
with c3:
    st.metric("MDI Ventures Cumulative Exits", "19 Startup", "Akumulatif")
with c4:
    total_carrying = mdi_df["Carrying_Value_IDR_B"].sum()
    st.metric("Total Nilai Tercatat Portofolio", f"Rp {total_carrying:,.0f} B", "10 Aset Utama")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Sensitivitas Saham GoTo terhadap Laba Rugi Telkom")
    goto_prices = np.arange(50, 125, 5)
    # Asumsi kepemilikan ~26.25 Miliar saham (Rp 64 -> Rp 1.680B; penurunan Rp 6 -> -Rp 242B)
    shares_billion = 26.25
    pnl_impact = (goto_prices - 64.0) * shares_billion
    
    fig_sens = go.Figure(go.Scatter(
        x=goto_prices,
        y=pnl_impact,
        mode="lines+markers",
        line=dict(color="#E01E2E", width=3),
        marker=dict(size=7, color="#0A192F")
    ))
    fig_sens.add_hline(y=0, line_dash="dash", line_color="#64748B")
    fig_sens.add_vline(x=64, line_dash="dot", line_color="#E01E2E", annotation_text="Harga 2025 (Rp 64)")
    fig_sens.update_layout(
        template="plotly_white",
        xaxis_title="Harga Saham GoTo (Rp / Lembar)",
        yaxis_title="Dampak Laba/Rugi Belum Direalisasi (Rp Miliar)",
        height=420
    )
    st.plotly_chart(fig_sens, use_container_width=True)

with col2:
    st.subheader("Matriks Kinerja Portofolio MDI Ventures")
    fig_mdi = px.bar(
        mdi_df,
        x="Startup_Name",
        y="Unrealized_Gain_Loss_IDR_B",
        color="Stage",
        color_discrete_sequence=["#E01E2E", "#0A192F", "#3B82F6", "#10B981"],
        labels={"Unrealized_Gain_Loss_IDR_B": "Unrealized Gain/Loss (Rp B)", "Startup_Name": "Startup"}
    )
    fig_mdi.update_layout(template="plotly_white", height=420)
    st.plotly_chart(fig_mdi, use_container_width=True)

# Simulator Harga Saham GoTo
st.markdown("---")
st.subheader("Simulator Valuasi Saham GoTo")
sim_goto = st.slider("Simulasi Harga Saham GoTo (Rp / Lembar)", min_value=50, max_value=120, value=75, step=1)
sim_impact = (sim_goto - 64) * 26.25
st.metric(
    "Proyeksi Dampak Laba/Rugi (Mark-to-Market)",
    f"Rp {sim_impact:+,.1f} Miliar",
    f"Pada harga Rp {sim_goto}/saham"
)
