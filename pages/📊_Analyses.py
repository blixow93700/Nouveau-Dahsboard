import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime, timedelta
import os

st.set_page_config(page_title="Analyses Historiques", page_icon="📊", layout="wide")

COLOR_PALETTE = px.colors.qualitative.Bold

# --- CHARGEMENT DES DONNÉES (Fonction locale pour cette page) ---
@st.cache_data
def load_data_extended():
    # Remplacez par le chemin réel si besoin, ou mettez le fichier dans le dossier principal
    filename = "frequentation-du-pole-de-la-defense-experimentation-lissage-des-heures-de-pointe.csv"
    
    # Gestion du chemin relatif (remonter d'un niveau si le csv est à la racine)
    if not os.path.exists(filename) and os.path.exists(f"../{filename}"):
        filename = f"../{filename}"

    if os.path.exists(filename):
        df_hist = pd.read_csv(filename, sep=";")
        if not pd.api.types.is_datetime64_any_dtype(df_hist['date']):
            df_hist['date'] = pd.to_datetime(df_hist['date'])
        last_date = df_hist['date'].max()
    else:
        last_date = datetime(2021, 12, 31)
        df_hist = pd.DataFrame()

    dates_future = pd.date_range(start=last_date + timedelta(days=1), end="2025-12-31", freq='D')
    data_future = []
    for date in dates_future:
        if date.weekday() >= 5: base = 120000
        else: base = 380000
        growth = 1 + (date.year - 2021) * 0.05
        noise = np.random.normal(0, 40000)
        total = int((base * growth) + noise)
        data_future.append({
            "date": date, 
            "Type_Jour": "SA" if date.weekday()==5 else ("DIJFP" if date.weekday()==6 else "JOHV"), 
            "Total": max(0, total)
        })
        
    df_future = pd.DataFrame(data_future)
    if not df_hist.empty:
        df_final = pd.concat([df_hist, df_future], ignore_index=True)
    else:
        df_final = df_future
    
    # Pre-processing
    df_final['date'] = pd.to_datetime(df_final['date'])
    df_final['Année'] = df_final['date'].dt.year
    mapping = {"JOHV": "Ouvré", "SA": "Samedi", "DIJFP": "Dimanche/Férié", "JOVS": "Vacances"}
    df_final['Type_Label'] = df_final['Type_Jour'].map(mapping).fillna("Autre")
    
    return df_final.sort_values('date')

df = load_data_extended()

st.title("Analyses de Fréquentation")

# Sidebar Filtres
st.sidebar.header("Filtres")
years = sorted(df['Année'].unique(), reverse=True)
sel_years = st.sidebar.multiselect("Années à analyser", years, default=years[:2])
df_filtered = df[df['Année'].isin(sel_years)] if sel_years else df

st.subheader("Évolution du volume voyageurs")
fig_area = px.area(
    df_filtered, x='date', y='Total', color='Type_Label',
    color_discrete_sequence=COLOR_PALETTE,
    labels={'Total': 'Volume Voyageurs', 'date': 'Date', 'Type_Label': 'Typologie Jour'}
)
st.plotly_chart(fig_area, use_container_width=True)

c1, c2 = st.columns(2)
with c1:
    st.subheader("Répartition Hebdomadaire")
    df_bar = df_filtered.groupby('Type_Label')['Total'].mean().reset_index()
    fig_bar = px.bar(df_bar, x='Type_Label', y='Total', color='Type_Label', color_discrete_sequence=COLOR_PALETTE)
    st.plotly_chart(fig_bar, use_container_width=True)
with c2:
    st.subheader("Segmentation des flux")
    fig_pie = px.pie(df_filtered, values='Total', names='Type_Label', color_discrete_sequence=COLOR_PALETTE)
    st.plotly_chart(fig_pie, use_container_width=True)
