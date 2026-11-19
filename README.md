<!-- Animated Corporate Header Banner -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0A192F,50:1E293B,100:E01E2E&height=220&section=header&text=TELKOM%20GROUP%202025&fontSize=52&fontColor=FFFFFF&fontAlignY=38&desc=Strategic%20Executive%20Dashboard%20%26%20What-If%20Simulator&descAlignY=60&descSize=18&animation=fadeIn" width="100%" alt="Telkom Group Header"/>
</p>

<!-- Animated Typing Effect with Custom Font -->
<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Montserrat&weight=700&size=20&duration=3000&pause=1000&color=E01E2E&center=true&vCenter=true&width=750&lines=Subsidiary+Performance+%26+Clean+Sheet+Restructuring;AR+Aging+%26+Credit+Risk+Provisioning+Modeler;Customer+Churn+%26+FMC+ARPU+Optimization;Competitive+Intelligence+%26+Market+Repair;CapEx+Allocation+%26+Depreciation+Lifecycle;Digital+Investment+Portfolio+%26+GoTo+Sensitivity" alt="Typing SVG" />
  </a>
</p>

<!-- Tech Stack Badges -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-0A192F?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Streamlit-1.36%2B-E01E2E?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/Plotly-Interactive-1E293B?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly"/>
  <img src="https://img.shields.io/badge/Pandas_%26_SciPy-Analytics-0A192F?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
</p>

---

<p align="center">
  <a href="#ringkasan-eksekutif">Ringkasan Eksekutif</a> &nbsp;&bull;&nbsp;
  <a href="#arsitektur-modul-interaktif">Arsitektur Modul</a> &nbsp;&bull;&nbsp;
  <a href="#struktur-direktori">Struktur Direktori</a> &nbsp;&bull;&nbsp;
  <a href="#panduan-instalasi">Panduan Instalasi</a>
</p>

---

## Ringkasan Eksekutif

**Telkom Group Strategic Executive Dashboard 2025** adalah aplikasi analitik multi-halaman berbasis Python dan Streamlit yang dirancang untuk memantau, menganalisis, dan mensimulasikan solusi atas **6 pilar isu strategis** yang teridentifikasi dalam Laporan Tahunan PT Telkom Indonesia (Persero) Tbk Tahun 2025.

Dibangun dengan standar antarmuka korporat Telkom (**Telkom Red** `#E01E2E` dan **Deep Navy** `#0A192F`), dashboard ini menggabungkan visualisasi data interaktif Plotly dengan *What-If Simulator* untuk mendukung pengambilan keputusan tingkat eksekutif.

---

## Arsitektur Modul Interaktif

Klik setiap bagian di bawah ini untuk melihat rincian metrik dan simulator yang tersedia pada masing-masing halaman:

<details>
<summary><b>1. Pengawasan Kinerja Anak Perusahaan (Subsidiary Performance)</b></summary>
<br/>

* **Fokus Masalah:** Tekanan pendapatan konsolidasian (-2,2% YoY menjadi Rp146.742 Miliar), penurunan laba bersih (-20,5% YoY), serta pembengkakan rugi pada Telkomsigma (-Rp363,6B) dan Telkomsat (-Rp249,5B).
* **Visualisasi:** P&L Contributor Bar Chart (Untung vs Rugi) dan perbandingan pendapatan segmen B2B Infra.
* **What-If Simulator:** *Clean Sheet Restructuring Impact* — mengatur persentase efisiensi Opex dan pertumbuhan pendapatan untuk memproyeksikan titik impas (*Break-Even Point*).

</details>

<details>
<summary><b>2. Manajemen Piutang & Risiko Provisi Kredit (AR Aging & Credit Risk)</b></summary>
<br/>

* **Fokus Masalah:** Lonjakan beban penyisihan kerugian kredit ekspektasian (+62,1% YoY menjadi Rp561 Miliar) dan tingginya piutang berumur >6 bulan (Rp6.763 Miliar dengan tingkat provisi 86,1%).
* **Visualisasi:** Donut Chart matriks umur piutang dan Stacked Bar segmentasi Pihak Berelasi (BUMN) vs Pihak Ketiga.
* **What-If Simulator:** *Cash Flow Recovery Modeler* — mensimulasikan *collection rate* piutang >6 bulan untuk menghitung tambahan arus kas masuk operasi dan pemulihan provisi.

</details>

<details>
<summary><b>3. Retensi Pelanggan & Optimalisasi ARPU (Customer Churn & FMC)</b></summary>
<br/>

* **Fokus Masalah:** Penurunan pelanggan seluler Telkomsel (159,4 Juta menjadi 156,1 Juta) serta pergeseran konsumsi IndiHome B2C dari paket Triple-Play (3P) ke Single-Play (1P / EZnet).
* **Visualisasi:** Tren Churn Rate Bulanan Regional dan Heatmap klaster wilayah berisiko tinggi.
* **What-If Simulator:** *FMC Conversion Simulator* — menghitung potensi kenaikan ARPU dan total pendapatan tahunan dari konversi pelanggan 1P/EZnet ke Telkomsel One.

</details>

<details>
<summary><b>4. Intelijen Persaingan & Pangsa Pasar (Competitive Intelligence)</b></summary>
<br/>

* **Fokus Masalah:** Erosi pangsa pasar IndiHome (65,2% menjadi 63,0%) dan dinamika pasar seluler pascamerger XLSmart (Telkomsel 48,4% vs Kompetitor 51,6%).
* **Visualisasi:** Grouped Bar Chart tren pangsa pasar 3 tahun (2023-2025) dan Scatter Plot *Pricing Benchmark Matrix*.
* **What-If Simulator:** *Market Repair Scenario Modeler* — menguji elastisitas permintaan terhadap penyesuaian harga paket data (+2% s/d +10%).

</details>

<details>
<summary><b>5. Simulator Depresiasi Aset & Belanja Modal (CapEx & Depreciation)</b></summary>
<br/>

* **Fokus Masalah:** Lonjakan beban penyusutan & amortisasi (+10,1% YoY menjadi Rp37.649 Miliar) akibat reklasifikasi aset *drop cable* dengan masa manfaat 5 tahun.
* **Visualisasi:** CapEx Allocation Treemap (Rp24.577 Miliar) dan proyeksi beban depresiasi 5 tahun.
* **What-If Simulator:** *Asset Lifecycle & NeutraDC Modeler* — simulasi perubahan masa manfaat *drop cable* serta potensi pendapatan dari peningkatan utilisasi Data Center NeutraDC (baseline 89%).

</details>

<details>
<summary><b>6. Valuasi Portofolio Investasi Digital (Investment Portfolio)</b></summary>
<br/>

* **Fokus Masalah:** Kerugian belum direalisasi atas perubahan nilai wajar investasi (-Rp242 Miliar) akibat fluktuasi harga saham GoTo (Rp64/saham di 2025 vs Rp70/saham di 2024).
* **Visualisasi:** Grafik sensitivitas harga saham GoTo terhadap Laba Rugi dan matriks kinerja portofolio MDI Ventures (19 akumulatif *exit*).
* **What-If Simulator:** *Mark-to-Market Valuation Slider* — simulasi dampak pergerakan harga saham GoTo (Rp50 s/d Rp120) terhadap laporan keuangan Telkom.

</details>

---

## Struktur Direktori

```text
telkom-strategic-dashboard-2025/
├── app.py                              # Main entry point, st.navigation, & tema korporat
├── data_loader.py                      # Generator dataset konsolidasi & mock Telkom 2025
├── requirements.txt                    # Daftar dependensi Python
├── README.md                           # Dokumentasi interaktif proyek
└── pages/
    ├── 1_Subsidiary_Performance.py     # Modul 1: Kinerja Anak Perusahaan
    ├── 2_AR_Aging_and_Credit_Risk.py   # Modul 2: Piutang & Risiko Kredit
    ├── 3_Customer_Churn_and_ARPU.py    # Modul 3: Retensi & FMC
    ├── 4_Competitive_Intelligence.py   # Modul 4: Persaingan & Pangsa Pasar
    ├── 5_CapEx_and_Depreciation.py     # Modul 5: Belanja Modal & Depresiasi
    └── 6_Investment_Portfolio.py       # Modul 6: Portofolio Investasi Digital
