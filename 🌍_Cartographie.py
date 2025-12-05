import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Cartographie des Flux", page_icon="🌍", layout="wide")

st.title("Cartographie des Flux")
st.markdown("### Vue satellite des points d'affluence majeurs")

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