import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from data_loader import load_data

data = load_data()
df = data["churn"].copy()

st.markdown("""
<div class="telkom-banner">
    <h2>Retensi Pelanggan & Optimalisasi ARPU (Customer Churn & FMC)</h2>
    <p>Analisis penurunan pelanggan seluler, pertumbuhan IndiHome B2C, pergeseran ke paket Single-Play (EZnet), dan simulasi konversi FMC.</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.subheader("Filter Wilayah Regional")
    selected_regions = st.multiselect(
        "Pilih Regional",
        options=df["Region"].unique(),
        default=df["Region"].unique()
    )

filtered_df = df[df["Region"].isin(selected_regions)]

# KPI Metric Cards
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Pelanggan Seluler Telkomsel", "156,1 Juta", "-3.3 Juta vs 2024 (159,4 Juta)", delta_color="inverse")
with c2:
    st.metric("Pelanggan IndiHome B2C", "10,3 Juta", "+7.4% YoY")
with c3:
    avg_mobile_churn = filtered_df["Mobile_Churn_Pct"].mean()
    st.metric("Rata-rata Churn Seluler", f"{avg_mobile_churn:.2f}%", "Bulanan Regional")
with c4:
    avg_indihome_arpu = filtered_df["IndiHome_ARPU_IDR"].mean()
    st.metric("Rata-rata ARPU IndiHome", f"Rp {avg_indihome_arpu:,.0f}", "Tekanan Paket 1P/EZnet", delta_color="inverse")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Tren Churn Rate Bulanan Regional (Seluler)")
    fig_line = px.line(
        filtered_df,
        x="Month",
        y="Mobile_Churn_Pct",
        color="Region",
        markers=True,
        labels={"Mobile_Churn_Pct": "Churn Rate (%)", "Month": "Bulan"}
    )
    fig_line.update_layout(template="plotly_white", height=400)
    st.plotly_chart(fig_line, use_container_width=True)

with col2:
    st.subheader("Heatmap Risiko Churn Regional per Bulan")
    pivot_df = filtered_df.pivot(index="Region", columns="Month", values="Mobile_Churn_Pct")
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    pivot_df = pivot_df[month_order]
    fig_heat = px.imshow(
        pivot_df,
        color_continuous_scale=["#0A192F", "#F59E0B", "#E01E2E"],
        aspect="auto",
        labels=dict(color="Churn (%)")
    )
    fig_heat.update_layout(height=400)
    st.plotly_chart(fig_heat, use_container_width=True)

# What-If FMC Simulator
st.markdown("---")
st.subheader("What-If FMC Simulator: Konversi 1P/EZnet ke Telkomsel One")
st.caption("Hitung potensi kenaikan ARPU dan Total Revenue B2C dari konversi pelanggan Single-Play (1P/EZnet) menjadi pelanggan Fixed-Mobile Convergence (FMC).")

sc1, sc2 = st.columns([1, 2])
with sc1:
    conv_rate = st.slider("Target Konversi Pelanggan 1P ke FMC (%)", min_value=1.0, max_value=35.0, value=12.0, step=1.0)
    arpu_uplift = st.slider("Kenaikan ARPU per Pelanggan Terkonversi (Rp)", min_value=25000, max_value=100000, value=55000, step=5000)

base_1p_subs = 3200000 # Estimasi 3.2 Juta pelanggan 1P/EZnet
converted_subs = base_1p_subs * (conv_rate / 100.0)
monthly_rev_uplift_b = (converted_subs * arpu_uplift) / 1e9
annual_rev_uplift_b = monthly_rev_uplift_b * 12

with sc2:
    m1, m2, m3 = st.columns(3)
    m1.metric("Pelanggan Terkonversi", f"{converted_subs:,.0f} Subs")
    m2.metric("Tambahan Revenue / Bulan", f"Rp {monthly_rev_uplift_b:,.1f} B")
    m3.metric("Potensi Tambahan Revenue / Tahun", f"Rp {annual_rev_uplift_b:,.1f} B", "Dampak Positif B2C")
