import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from data_loader import load_data

data = load_data()
df = data["subsidiaries"].copy()

st.markdown("""
<div class="telkom-banner">
    <h2>Pengawasan Kinerja Anak Perusahaan (Subsidiary Performance)</h2>
    <p>Evaluasi kontribusi P&L konsolidasian, tekanan segmen B2B Infra, serta simulasi restrukturisasi Clean Sheet Strategy.</p>
</div>
""", unsafe_allow_html=True)

# Sidebar Filter
with st.sidebar:
    st.subheader("Filter Kinerja Anak Perusahaan")
    selected_segments = st.multiselect(
        "Pilih Segmen Bisnis",
        options=df["Segment"].unique(),
        default=df["Segment"].unique()
    )

filtered_df = df[df["Segment"].isin(selected_segments)]

# KPI Metric Cards
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Pendapatan Konsolidasian", "Rp 146.742 B", "-2.2% YoY", delta_color="normal")
with col2:
    st.metric("EBITDA Margin Konsolidasian", "49.2%", "-1.1% YoY", delta_color="normal")
with col3:
    st.metric("Laba Bersih Konsolidasian", "Rp 17.814 B", "-20.5% YoY", delta_color="normal")
with col4:
    loss_count = len(df[df["Net_Income_2025"] < 0])
    st.metric("Entitas Merugi (Utama)", f"{loss_count} Entitas", "Telkomsigma & Telkomsat", delta_color="inverse")

st.markdown("---")

# Visualisasi P&L Anak Perusahaan
c1, c2 = st.columns([1.3, 1])

with c1:
    st.subheader("Kontributor Laba/Rugi Bersih Anak Perusahaan (Rp Miliar)")
    colors = ["#E01E2E" if val < 0 else "#0A192F" for val in filtered_df["Net_Income_2025"]]
    fig_bar = go.Figure(go.Bar(
        x=filtered_df["Subsidiary"],
        y=filtered_df["Net_Income_2025"],
        marker_color=colors,
        text=filtered_df["Net_Income_2025"].apply(lambda x: f"Rp {x:,.1f}B"),
        textposition="outside"
    ))
    fig_bar.update_layout(
        template="plotly_white",
        yaxis_title="Laba / Rugi Bersih (Rp Miliar)",
        xaxis_title="Anak Perusahaan",
        height=420,
        margin=dict(t=30, b=30)
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with c2:
    st.subheader("Tekanan Segmen B2B Infra (-36.3% YoY)")
    b2b_df = filtered_df[filtered_df["Subsidiary"].isin(["Telkomsigma", "Telkomsat", "Telin", "Mitratel"])]
    fig_rev = px.bar(
        b2b_df,
        x="Subsidiary",
        y=["Revenue_2024", "Revenue_2025"],
        barmode="group",
        color_discrete_sequence=["#94A3B8", "#E01E2E"],
        labels={"value": "Pendapatan (Rp Miliar)", "variable": "Tahun"}
    )
    fig_rev.update_layout(template="plotly_white", height=420, margin=dict(t=30, b=30))
    st.plotly_chart(fig_rev, use_container_width=True)

# What-If Simulator: Clean Sheet Restructuring Impact
st.markdown("---")
st.subheader("Simulator What-If: Clean Sheet Restructuring Impact")
st.caption("Simulasikan efisiensi biaya operasional (Opex) pada Telkomsigma dan Telkomsat untuk melihat titik impas (Break-Even Point).")

sim_col1, sim_col2 = st.columns([1, 2])
with sim_col1:
    target_entity = st.selectbox("Pilih Entitas Target Restrukturisasi", ["Telkomsigma", "Telkomsat"])
    opex_cut_pct = st.slider("Target Efisiensi Opex (%)", min_value=0.0, max_value=30.0, value=12.0, step=0.5)
    rev_growth_pct = st.slider("Asumsi Pertumbuhan Pendapatan (%)", min_value=-5.0, max_value=25.0, value=5.0, step=1.0)

entity_row = df[df["Subsidiary"] == target_entity].iloc[0]
base_ni = entity_row["Net_Income_2025"]
base_opex = entity_row["Opex_2025"]
base_rev = entity_row["Revenue_2025"]

opex_savings = base_opex * (opex_cut_pct / 100.0)
rev_gain = base_rev * (rev_growth_pct / 100.0)
projected_ni = base_ni + opex_savings + (rev_gain * 0.35) # Asumsi margin kontribusi 35%

with sim_col2:
    m1, m2, m3 = st.columns(3)
    m1.metric("Rugi Bersih Saat Ini (2025)", f"Rp {base_ni:,.1f} B")
    m2.metric("Penghematan Opex", f"Rp {opex_savings:,.1f} B")
    m3.metric(
        "Proyeksi Laba/Rugi Bersih",
        f"Rp {projected_ni:,.1f} B",
        delta="Break-Even Tercapai" if projected_ni >= 0 else "Masih Defisit",
        delta_color="normal" if projected_ni >= 0 else "inverse"
    )
    st.info(
        f"Dengan efisiensi Opex sebesar {opex_cut_pct:.1f}% (Rp {opex_savings:,.1f}B) dan pertumbuhan pendapatan {rev_growth_pct:.1f}%, "
        f"{target_entity} diproyeksikan membukukan kinerja bersih sebesar Rp {projected_ni:,.1f} Miliar."
    )
