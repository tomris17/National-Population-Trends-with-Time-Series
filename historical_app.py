import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="National Population Trends App", layout="centered")

st.title("Historical National Population Trends App")
st.write(
    "Bu uygulama, uzun vadeli ulusal nüfus verilerini analiz ederek on yıllar içindeki demografik büyüme trendlerini görselleştirir."
)

@st.cache_data
def load_data():
    df = pd.read_csv("POPH.csv", low_memory=False)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").reset_index(drop=True)
    df["Population_Growth_Rate"] = df["value"].pct_change() * 100
    return df

try:
    df = load_data()
    
    st.subheader("Nüfus Veri Seti Önizlemesi")
    st.dataframe(df.head())

    st.subheader("Nüfus Büyüme Grafikleri")
    
    chart_type = st.selectbox("Grafik Türü Seçin", ["Toplam Nüfus Trendi", "Yıllık Büyüme Oranı (%)"])
    
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(10, 5))
    
    if chart_type == "Toplam Nüfus Trendi":
        ax.plot(df["date"], df["value"], label="National Population", color="purple", linewidth=2.5)
        ax.set_title("Historical National Population Growth Over Time", fontsize=14, fontweight="bold")
        ax.set_ylabel("Population (Persons)", fontsize=12)
    else:
        ax.plot(df["date"], df["Population_Growth_Rate"], label="Annual Growth Rate (%)", color="teal")
        ax.set_title("Annual National Population Growth Rate", fontsize=14, fontweight="bold")
        ax.set_ylabel("Growth Rate (%)", fontsize=12)
        
    ax.set_xlabel("Year", fontsize=12)
    ax.legend()
    st.pyplot(fig)

except Exception as e:
    st.error(f"Veri yüklenirken veya işlenirken bir hata oluştu: {e}")