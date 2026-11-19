import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def load_data():
    """
    Menyediakan dataset konsolidasi dan mock realistis PT Telkom Indonesia (Persero) Tbk Tahun 2025.
    Seluruh angka finansial dalam Miliar Rupiah (Rp B) kecuali disebutkan lain.
    """
    
    # 1. Data Kinerja Anak Perusahaan (Subsidiary Performance)
    subsidiaries_df = pd.DataFrame({
        "Subsidiary": ["Telkomsel", "Telin", "Mitratel", "Telkomsigma", "Telkomsat", "Telkom Akses & Lainnya"],
        "Segment": ["Mobile & Consumer", "Wholesale & Intl", "Infrastructure", "B2B IT Services", "Satellite", "Infra & Support"],
        "Revenue_2025": [109307.0, 12169.0, 9534.0, 2613.0, 1844.0, 11275.0],
        "Revenue_2024": [112100.0, 11850.0, 8920.0, 2890.0, 1980.0, 12300.0],
        "Net_Income_2025": [19687.0, 944.0, 2119.0, -363.6, -249.5, -4322.9],
        "Net_Income_2024": [21400.0, 880.0, 2010.0, -145.0, -110.0, -1625.0],
        "EBITDA_Margin_Pct": [56.4, 24.8, 82.1, -4.2, 18.5, 12.0],
        "Opex_2025": [47650.0, 9150.0, 1705.0, 2722.0, 1502.0, 9920.0],
        "Status": ["Profit", "Profit", "Profit", "Loss (Clean Sheet)", "Loss", "Consolidation/Elimination"]
    })
    subsidiaries_df["YoY_Rev_Pct"] = ((subsidiaries_df["Revenue_2025"] - subsidiaries_df["Revenue_2024"]) / subsidiaries_df["Revenue_2024"]) * 100

    # 2. Data Umur Piutang & Risiko Kredit (AR Aging & Credit Risk)
    ar_aging_df = pd.DataFrame({
        "Aging_Bucket": ["Belum Jatuh Tempo", "0 - 3 Bulan", "3 - 6 Bulan", "> 6 Bulan"],
        "Gross_AR_2025": [6687.0, 3155.0, 1573.0, 6763.0],
        "Provision_Rate_Pct": [1.8, 8.5, 24.0, 86.1],
        "Related_Party_BUMN": [2850.0, 1420.0, 780.0, 3120.0],
        "Third_Party_Corporate_Retail": [3837.0, 1735.0, 793.0, 3643.0]
    })
    ar_aging_df["Provision_Amount"] = ar_aging_df["Gross_AR_2025"] * (ar_aging_df["Provision_Rate_Pct"] / 100.0)
    ar_aging_df["Net_AR_2025"] = ar_aging_df["Gross_AR_2025"] - ar_aging_df["Provision_Amount"]

    # 3. Data Pelanggan, Churn & ARPU (Customer Churn & FMC)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    regions = ["Sumatra", "Jabodetabek", "Jawa Barat", "Jawa Tengah", "Jawa Timur & BaliNus", "Kalimantan", "Sulawesi & MalukuPapua"]
    
    np.random.seed(42)
    churn_records = []
    for reg in regions:
        base_churn = np.random.uniform(1.8, 3.2)
        for idx, m in enumerate(months):
            seasonal = 0.25 * np.sin(idx / 2.0)
            churn_records.append({
                "Month": m,
                "Month_Num": idx + 1,
                "Region": reg,
                "Mobile_Churn_Pct": round(max(1.2, base_churn + seasonal + np.random.normal(0, 0.15)), 2),
                "Fixed_BB_Churn_Pct": round(max(0.8, (base_churn * 0.55) + seasonal * 0.5 + np.random.normal(0, 0.1)), 2),
                "Mobile_ARPU_IDR": round(np.random.uniform(41000, 49000), -2),
                "IndiHome_ARPU_IDR": round(np.random.uniform(225000, 265000), -3),
                "Subs_1P_EZnet_K": int(np.random.uniform(180, 450)),
                "Subs_3P_K": int(np.random.uniform(350, 750))
            })
    churn_df = pd.DataFrame(churn_records)

    # 4. Data Intelijen Persaingan (Competitive Intelligence)
    market_share_df = pd.DataFrame({
        "Year": [2023, 2023, 2023, 2023, 2024, 2024, 2024, 2024, 2025, 2025, 2025, 2025],
        "Operator": ["IndiHome (Telkom)", "IconNet (PLN)", "Link Net / XL", "MyRepublic & MNC Play"] * 3,
        "Fixed_BB_Share_Pct": [68.5, 9.2, 11.8, 10.5, 65.2, 11.4, 12.1, 11.3, 63.0, 13.5, 12.0, 11.5]
    })

    pricing_benchmark_df = pd.DataFrame({
        "Operator": ["Telkomsel (Mobile)", "IOH (Indosat)", "XLSmart", "IndiHome (Fixed)", "IconNet (Fixed)", "MyRepublic (Fixed)"],
        "Category": ["Mobile", "Mobile", "Mobile", "Fixed Broadband", "Fixed Broadband", "Fixed Broadband"],
        "Yield_IDR_per_GB_or_Mbps": [3450, 2750, 2890, 4800, 3600, 3950],
        "Market_Share_2025_Pct": [48.4, 27.1, 24.5, 63.0, 13.5, 11.5]
    })

    # 5. Data CapEx & Infrastruktur (CapEx & Depreciation)
    capex_alloc_df = pd.DataFrame({
        "Category": ["Mobile 5G & 4G BTS", "Fiber Optic & FTTH", "Data Center (NeutraDC)", "Submarine Cable & Intl", "IT & Digital Platform"],
        "Allocation_IDR_B": [9830.8, 7618.9, 3440.8, 2211.9, 1474.6],
        "Share_Pct": [40.0, 31.0, 14.0, 9.0, 6.0],
        "Useful_Life_Years": [8, 15, 20, 15, 5]
    })

    # 6. Data Portofolio Investasi Digital (Investment Portfolio)
    mdi_portfolio_df = pd.DataFrame({
        "Startup_Name": ["GoTo (Public)", "FinAccel (Kredivo)", "Alodokter", "Cermati", "Nium", "Payfazz", "Qoala", "Delos", "KoinWorks", "Agraku"],
        "Stage": ["Public", "Growth", "Growth", "Growth", "Exit / Partial", "Growth", "Growth", "Seed", "Growth", "Seed"],
        "Sector": ["Ecosystem", "Fintech", "Healthtech", "Fintech", "Fintech", "Fintech", "Insurtech", "Aquatech", "Fintech", "Agritech"],
        "Carrying_Value_IDR_B": [1680.0, 420.0, 185.0, 210.0, 310.0, 195.0, 160.0, 45.0, 140.0, 38.0],
        "Unrealized_Gain_Loss_IDR_B": [-242.0, 65.0, 18.0, 32.0, 115.0, -14.0, 22.0, 8.0, -9.0, 4.0]
    })

    return {
        "subsidiaries": subsidiaries_df,
        "ar_aging": ar_aging_df,
        "churn": churn_df,
        "market_share": market_share_df,
        "pricing_benchmark": pricing_benchmark_df,
        "capex_alloc": capex_alloc_df,
        "mdi_portfolio": mdi_portfolio_df
    }
