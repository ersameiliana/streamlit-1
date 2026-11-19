import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from data_loader import load_data

data = load_data()
capex_df = data["capex_alloc"].copy()

st.markdown("""
<div class="telkom-banner">
    <h2>Simulator Depresiasi Aset & Belanja Modal (CapEx & Asset Lifecycle)</h2>
    <p>Analisis lonjakan beban penyusutan akibat reklasifikasi drop cable, alokasi CapEx, dan optimalisasi utilisasi NeutraDC.</p>
</div>
""", unsafe_allow_html=True)

# KPI Metric Cards
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Beban Penyusutan & Amortisasi", "Rp 37.649 B", "+10.1% YoY", delta_color="inverse")
with c2:
    st.metric("Realisasi CapEx 2025", "Rp 24.577 B", "16.7% dari Pendapatan")
with c3:
    st.metric("Infrastruktur BTS & Menara", "293.136 BTS", "4.913 BTS 5G | 44.702 Menara")
with c4:
    st.metric("Utilisasi Data Center (NeutraDC)", "89.0%", "Batam & Cikarang")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Alokasi Belanja Modal (CapEx) 2025")
    fig_tree = px.treemap(
        capex_df,
        path=["Category"],
        values="Allocation_IDR_B",
        color="Allocation_IDR_B",
        color_continuous_scale=["#0A192F", "#E01E2E"],
        hover_data=["Share_Pct", "Useful_Life_Years"]
    )
    fig_tree.update_layout(height=420, margin=dict(t=30, b=20))
    st.plotly_chart(fig_tree, use_container_width=True)

with col2:
    st.subheader("Proyeksi Beban Depresiasi 5 Tahun (Masa Manfaat Drop Cable)")
    useful_life = st.slider("Simulasi Masa Manfaat Aset Drop Cable (Tahun)", min_value=3, max_value=10, value=5, step=1)
    years = [2025, 2026, 2027, 2028, 2029]
    base_dep = 37649.0
    drop_cable_pool = 12500.0
    
    # Perbandingan baseline 5 tahun vs simulasi
    dep_baseline = [base_dep + (i * 850) for i in range(5)]
    dep_sim = [base_dep - (drop_cable_pool / 5.0) + (drop_cable_pool / useful_life) + (i * 850) for i in range(5)]
    
    proj_df = pd.DataFrame({
        "Tahun": years,
        "Baseline (5 Tahun)": dep_baseline,
        f"Simulasi ({useful_life} Tahun)": dep_sim
    })
    fig_proj = px.line(
        proj_df,
        x="Tahun",
        y=["Baseline (5 Tahun)", f"Simulasi ({useful_life} Tahun)"],
        markers=True,
        color_discrete_sequence=["#94A3B8", "#E01E2E"],
        labels={"value": "Beban Depresiasi (Rp Miliar)", "variable": "Skenario"}
    )
    fig_proj.update_layout(template="plotly_white", height=350, xaxis=dict(dtick=1))
    st.plotly_chart(fig_proj, use_container_width=True)

# ROI & Utilization Modeler
st.markdown("---")
st.subheader("ROI & Utilization Modeler: NeutraDC")
u1, u2 = st.columns([1, 2])
with u1:
    target_util = st.slider("Target Utilisasi NeutraDC (%)", min_value=80.0, max_value=98.0, value=93.0, step=1.0)
with u2:
    incremental_rev = (target_util - 89.0) * 65.0 # Estimasi Rp 65B per 1% utilisasi
    st.metric(
        "Potensi Tambahan Pendapatan Data Center",
        f"Rp {incremental_rev:+,.1f} B / Tahun",
        f"Dari 89.0% ke {target_util:.1f}% Utilisasi"
    )
