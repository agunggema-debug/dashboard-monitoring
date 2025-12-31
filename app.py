import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from database_helper import fetch_data_from_sql

def send_alert(channel_name, status):
    # Konfigurasi Pengirim (Gunakan App Password jika menggunakan Gmail)
    sender_email = st.secrets["EMAIL_USER"]
    password = st.secrets["EMAIL_PASS"]

    msg = MIMEText(f"PERINGATAN: Sistem {channel_name} dalam kondisi {status}!")
    msg['Subject'] = f"🚨 Alert: {channel_name} Failure"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        return True
    except Exception as e:
        print(f"Gagal mengirim email: {e}")
        return False

# Logika pengecekan di dalam dashboard
for index, row in df.iterrows():
    if row['Status'] == 'Critical':
        # Kita gunakan st.toast untuk notifikasi di UI
        st.toast(f"Mengirim email peringatan untuk {row['Channel']}...", icon="📧")
        # Panggil fungsi send_alert(row['Channel'], row['Status'])
# Konfigurasi Halaman
st.set_page_config(page_title="Delivery Channel Monitoring", layout="wide")

# --- DATA SIMULATION ---
def get_mock_data():
    channels = ['Mobile Banking', 'Internet Banking', 'ATM', 'API Integration']
    data = {
        'Channel': channels,
        'Uptime': [99.9, 98.5, 95.2, 99.98],
        'Response_Time_ms': [120, 250, 800, 45],
        'Status': ['Normal', 'Warning', 'Critical', 'Normal'],
        'Transactions': [15200, 8400, 3200, 45000]
    }
    return pd.DataFrame(data)

df = get_mock_data()

# --- HEADER SECTION ---
st.title("📊 Delivery Channel Executive Dashboard")
st.markdown(f"**Terakhir diperbarui:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
st.divider()

# --- KPI METRICS ---
col1, col2, col3, col4 = st.columns(4)

metrics = [
    (col1, "Mobile Banking", df.iloc[0]),
    (col2, "Internet Banking", df.iloc[1]),
    (col3, "ATM Network", df.iloc[2]),
    (col4, "API Gateway", df.iloc[3])
]

for col, name, row in metrics:
    with col:
        color = "normal" if row['Status'] == 'Normal' else "inverse"
        st.metric(label=name, value=f"{row['Uptime']}%", delta=row['Status'])
        st.caption(f"Latency: {row['Response_Time_ms']}ms")

st.divider()

# --- VISUALIZATION SECTION ---
left_chart, right_chart = st.columns(2)

with left_chart:
    st.subheader("Volume Transaksi per Channel")
    fig_bar = px.bar(df, x='Channel', y='Transactions', color='Channel', 
                     text_auto='.2s', template="plotly_dark")
    st.plotly_chart(fig_bar, use_container_width=True)

with right_chart:
    st.subheader("Analisis Latency (Response Time)")
    fig_line = px.line(df, x='Channel', y='Response_Time_ms', markers=True, 
                       line_shape="spline", template="plotly_dark")
    fig_line.update_traces(line_color='#00FFCC')
    st.plotly_chart(fig_line, use_container_width=True)

# --- MAINTENANCE LOGS ---
st.subheader("🛠️ System Maintenance Logs")
log_data = {
    "Timestamp": ["2023-10-01 08:00", "2023-10-01 10:30", "2023-10-01 12:00"],
    "System": ["ATM", "Internet Banking", "API"],
    "Action": ["Patch Update", "Database Optimization", "Key Rotation"],
    "Engineer": ["Budi", "Siti", "Andi"]
}
st.table(pd.DataFrame(log_data))

# --- FOOTER ---
st.markdown("---") # Garis pemisah horizontal

# Menggunakan CSS untuk styling footer agar lebih elegan
footer_style = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0E1117;
        color: #FAFAFA;
        text-align: center;
        padding: 10px;
        font-family: 'sans-serif';
        font-size: 14px;
        border-top: 1px solid #4B4B4B;
    }
    </style>
    <div class="footer">
        <p>📊 <b> Delivery Channel Executive Dashboard</b> | Dikembangkan dengan Python & Streamlit | © 2025 Monitoring Delivery Channel </p>
    </div>
"""

# Jika ingin footer yang menempel di bawah (fixed), gunakan ini:
# st.markdown(footer_style, unsafe_allow_html=True)

# Atau jika ingin footer biasa yang mengikuti scroll, cukup gunakan markdown sederhana:
st.markdown(
    """
    <div style="text-align: center; color: grey; padding: 20px;">
        <p>Built with ❤️ by agung_gema | <a href="https://github.com/" target="_blank">View on GitHub</a></p>
        <small>Data simulasi ini dibuat untuk keperluan demonstrasi visualisasi Monitoring Delivery Channel.</small>
    </div>
    """, 
    unsafe_allow_html=True
)