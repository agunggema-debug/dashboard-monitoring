# 📊 Delivery Channel Monitoring Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://share.streamlit.io/) 
![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Dashboard pemantauan sistem perbankan real-time yang dirancang untuk memantau kesehatan operasional saluran pengiriman (*Delivery Channels*) seperti Mobile Banking, Internet Banking, ATM, dan Integrasi API.
<img width="1875" height="1004" alt="dashboard-monitoring" src="https://github.com/user-attachments/assets/0da9980a-df25-4a64-b32f-c6a84c9335c6" />


## 🚀 Fitur Utama
* **Real-time Metrics:** Pantau Uptime, Latency, dan Volume Transaksi secara instan.
* **System Status Tracking:** Label status otomatis (Normal, Warning, Critical) berdasarkan ambang batas performa.
* **Interactive Visualizations:** Grafik interaktif menggunakan Plotly untuk analisis tren transaksi dan respons sistem.
* **Automated Alerting:** Integrasi notifikasi email otomatis (SMTP) ketika sistem mendeteksi kegagalan (status *Critical*).
* **Maintenance Logs:** Pencatatan riwayat pemeliharaan sistem oleh tim engineer.

## 🛠️ Teknologi yang Digunakan
* **Python**: Bahasa pemrograman utama.
* **Streamlit**: Framework untuk membangun UI dashboard yang elegan.
* **Pandas & NumPy**: Pengolahan dan manipulasi data.
* **Plotly**: Library untuk visualisasi data interaktif.
* **SMTPLib**: Protokol pengiriman email peringatan.

## 📋 Struktur Proyek
```text
.
├── app.py                # Aplikasi utama Streamlit
├── requirements.txt      # Daftar dependensi library
└── README.md             # Dokumentasi proyek
