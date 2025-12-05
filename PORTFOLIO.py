import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta
import os
import base64

st.set_page_config(
    page_title="Portfolio - Rayan Rami",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

COLOR_PALETTE = px.colors.qualitative.Bold
COLOR_PRIMARY = "#1f77b4"


def get_base64_of_bin_file(bin_file):
    """Convertit une image locale en base64."""
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return None

def set_background(local_path):
    """
    Injecte le CSS pour le fond d'écran.
    Priorité : Fichier local > URL de secours.
    """
    bin_str = get_base64_of_bin_file(local_path)
    
    
    if bin_str:
        bg_image_css = f"url('data:image/png;base64,{bin_str}')"
    else:
       
        bg_image_css = "url('https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?q=80&w=2000')"

    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.92), rgba(255, 255, 255, 0.97)), {bg_image_css};
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

def local_image(path, width=None, caption=None):
    """Affiche une image locale de manière sécurisée."""
    if os.path.exists(path):
        st.image(path, caption=caption, width=width)


st.sidebar.title("Navigation")
page = st.sidebar.radio("Menu", ["Mon CV", "Projet Transport"], index=0)

st.sidebar.markdown("---")
st.sidebar.success("Statut : En poste (Alternance)")
st.sidebar.markdown("Paris / Île-de-France")
st.sidebar.markdown("[Contacter par Email](mailto:ramirayan.25@icloud.com)")
st.sidebar.markdown("[LinkedIn (Profil)](https://linkedin.com)")
st.sidebar.markdown("---")
st.sidebar.caption("Portfolio - 2025")


if page == "Mon CV":
    
    col_profile, col_intro = st.columns([1, 3])
    with col_intro:
        st.title("Rayan Rami")
        st.markdown("### Expert Data & Business Intelligence")
        st.markdown("""
        > *"Transformer la donnée brute en décision stratégique."*
        
        Étudiant en **BUT Sciences des Données**, je combine expertise technique (Python, SQL, Power BI) et vision business (Audit, Gestion de projet).
        """)
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Expérience", "2 Ans", "Alternance & Stage")
        c2.metric("Projets", "15+", "Académique & Pro")
        c3.metric("Niveau", "Junior Confirmé", "Autonome")

    st.markdown("---")

   
    st.subheader("Compétences")
    tab_tech, tab_soft = st.tabs(["Hard Skills", "Soft Skills"])
    
    with tab_tech:
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            st.markdown("#### Programmation & Data")
            st.progress(0.90, text="Excel (Expert)")
            st.progress(0.85, text="R & RStudio")
            st.progress(0.80, text="Python (Pandas, Streamlit, Plotly)")
            st.progress(0.75, text="SQL (Requêtage complexe)")
        with col_s2:
            st.markdown("#### BI & Outils")
            st.progress(0.70, text="Power BI / Tableau")
            st.progress(0.60, text="SAS")
            st.progress(0.50, text="Access / VBA")
    
    with tab_soft:
        st.markdown("""
        - **Analytique** : Capacité à faire parler les chiffres.
        - **Communication** : Vulgarisation technique pour le management.
        - **Gestion de projet** : Respect des délais et méthode Agile.
        - **Langues** : Anglais (B2 - Pro), Espagnol (B2).
        """)

    st.markdown("---")

    st.subheader("Parcours & Expériences")
    
    with st.container():
        c_date, c_info = st.columns([1, 4])
        c_date.markdown("**Sept 2025 - Présent**")
        c_info.error("**Alternant Auditeur Data IT @ KPMG**")
        c_info.markdown("""
        *Audit financier et Data Analytics.*
        - Automatisation des tests d'audit (SQL/Python).
        - Création de reportings clients automatisés.
        - Collaboration directe avec les équipes Senior Audit.
        """)
    
    with st.container():
        c_date, c_info = st.columns([1, 4])
        c_date.markdown("**Mai 2025 - Août 2025**")
        c_info.warning("**Stage Data Analyst @ Expertise Bureautique**")
        c_info.markdown("""
        *Optimisation des coûts télécoms.*
        - Détection d'anomalies de facturation (-15% de coûts).
        - Mise en place de Dashboards de suivi KPI.
        """)

    with st.container():
        c_date, c_info = st.columns([1, 4])
        c_date.markdown("**Formation**")
        c_info.info("**BUT Sciences des Données @ IUT Paris Rives de Seine**")
        c_info.markdown("Spécialisation Statistique et Informatique Décisionnelle.")

    st.markdown("---")
    st.header("Projets")
    cols_proj = st.columns(3)
    cols_proj[0].success("**JO Paris 2024**\n\nAnalyse d'impact & Prédictions de médailles (R/Python).")
    cols_proj[1].info("**Crypto-Data**\n\nAlgorithme de décryptage et transformation CSV (Python).")
    cols_proj[2].warning("**Market Report**\n\nÉtude de marché complète avec SAS et Excel.")

elif page == "Projet Transport":
    
    bg_path = "image_d34f63.jpg" 
    if not os.path.exists(bg_path):
        bg_path = r"C:\Users\rayan.rami\Downloads\CV\11107786.jpg"
    set_background(bg_path)
    
    @st.cache_data
    def load_data_extended():
        filename = "frequentation-du-pole-de-la-defense-experimentation-lissage-des-heures-de-pointe.csv"
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
        return df_final

    def process_data(df):
        df['date'] = pd.to_datetime(df['date'])
        df['Année'] = df['date'].dt.year
        df['Mois'] = df['date'].dt.month_name()
        df['Jour'] = df['date'].dt.day_name()
        mapping = {"JOHV": "Ouvré", "SA": "Samedi", "DIJFP": "Dimanche/Férié", "JOVS": "Vacances"}
        df['Type_Label'] = df['Type_Jour'].map(mapping).fillna("Autre")
        return df.sort_values('date')

    df_raw = load_data_extended()
    df = process_data(df_raw)

    col_h1, col_h2 = st.columns([3, 1])
    with col_h1:
        st.title("La Défense : Supervision")
        st.markdown("**Supervision des flux voyageurs et analyse prédictive.**")
    with col_h2:
        st.markdown(f"### {datetime.now().strftime('%d/%m/%Y')}")

    st.info("""
    **Objectif du Dashboard :** Cet outil permet aux équipes d'exploitation de visualiser en temps réel la densité des flux piétons sur le parvis de La Défense. 
    Il croise les données historiques de fréquentation avec des modèles prédictifs pour anticiper les saturations et adapter les moyens (sécurité, fréquence des transports).
    """)

 
    st.sidebar.header("Filtres")
    years = sorted(df['Année'].unique(), reverse=True)
    sel_years = st.sidebar.multiselect("Années à analyser", years, default=years[:2])
    df_filtered = df[df['Année'].isin(sel_years)] if sel_years else df

  
    tab_live, tab_analysis, tab_geo = st.tabs(["Temps Réel", "Analyses", "Cartographie"])

    with tab_live:
        st.markdown("### Supervision Temps Réel")
        with st.expander("Légende Opérationnelle (Seuils de charge)", expanded=True):
            st.markdown("""
            **Niveaux de service et densité voyageurs :**
            - **Régime Nominal (<50%)** : Fluidité optimale. Aucun incident de circulation.
            - **Densification (50-80%)** : Charge soutenue. Ralentissements possibles aux accès.
            - **Saturation Critique (>80%)** : Seuil d'alerte. Activation des mesures de régulation de flux.
            """)

        now = datetime.now()
        current_hour = now.hour
        if 8 <= current_hour <= 9 or 17 <= current_hour <= 19: load_factor = 0.95
        elif 10 <= current_hour <= 16: load_factor = 0.60
        else: load_factor = 0.20
        
        live_load = min(100, int(load_factor * 100 + np.random.randint(-5, 5)))
        pax_minute = int(live_load * 45) 
        
        col_live1, col_live2, col_live3 = st.columns(3)
        with col_live1:
            st.markdown("**Taux d'Occupation (Gare)**")
            fig_gauge = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = live_load,
                domain = {'x': [0, 1], 'y': [0, 1]},
                gauge = {
                    'axis': {'range': [None, 100], 'tickwidth': 1},
                    'bar': {'color': "#1f77b4"},
                    'steps': [
                        {'range': [0, 50], 'color': '#e5ecf6'},
                        {'range': [50, 80], 'color': '#ffebd6'},
                        {'range': [80, 100], 'color': '#ffe0e0'}],
                    }))
            fig_gauge.update_layout(height=250, margin=dict(l=10,r=10,t=10,b=10))
            st.plotly_chart(fig_gauge, use_container_width=True)
        with col_live2:
            st.metric("Débit Instantané (Pax/min)", f"{pax_minute}", "Conforme")
            st.metric("Disponibilité Équipements", "100%", "Nominal")
            if st.button("Actualiser Flux"):
                st.rerun()
        with col_live3:
            st.info(f"Dernière synchro : {now.strftime('%H:%M:%S')}")
            st.success("Ligne 1 : Trafic Nominal")
            st.warning("RER A : Forte Densité (Nanterre)")

    with tab_analysis:
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

    with tab_geo:
        st.markdown("### Cartographie des Flux")
        st.markdown("Vue satellite des points d'affluence majeurs.")
        
        map_data = pd.DataFrame([
            {"nom": "Grande Arche", "lat": 48.8925, "lon": 2.2397, "flux": 4500, "type": "Transport"},
            {"nom": "CNIT", "lat": 48.8935, "lon": 2.2405, "flux": 3200, "type": "Commerce/Transport"},
            {"nom": "Esplanade", "lat": 48.8881, "lon": 2.2495, "flux": 1500, "type": "Entrée Piétonne"},
            {"nom": "Westfield 4 Temps", "lat": 48.8905, "lon": 2.2375, "flux": 5000, "type": "Commerce"},
            {"nom": "Coeur Transport", "lat": 48.8915, "lon": 2.2415, "flux": 6000, "type": "Hub Bus"},
        ])
        fig_map = px.scatter_mapbox(
            map_data,
            lat="lat",
            lon="lon",
            color="type",
            size="flux",
            hover_name="nom",
            zoom=14.5,
            center={"lat": 48.8910, "lon": 2.2410},
            color_discrete_sequence=px.colors.qualitative.Bold,
            size_max=50,
            height=600
        )

        fig_map.update_layout(mapbox_style="carto-positron")
        fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        
        st.plotly_chart(fig_map, use_container_width=True)
        
        st.info("La taille des cercles est proportionnelle au volume de passage estimé en temps réel.")




