import streamlit as st
import plotly.graph_objects as go
import numpy as np
from datetime import datetime

st.set_page_config(page_title="Supervision Temps Réel", page_icon="🚇", layout="wide")

st.title("Supervision Temps Réel")
st.markdown(f"### {datetime.now().strftime('%d/%m/%Y - %H:%M')}")

st.sidebar.markdown("### Paramètres Live")
st.sidebar.info("Actualisation automatique simulée.")

with st.expander("Légende Opérationnelle (Seuils de charge)", expanded=True):
    st.markdown("""
    **Niveaux de service :**
    - **Régime Nominal (<50%)** : Fluidité optimale.
    - **Densification (50-80%)** : Charge soutenue.
    - **Saturation Critique (>80%)** : Seuil d'alerte.
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
