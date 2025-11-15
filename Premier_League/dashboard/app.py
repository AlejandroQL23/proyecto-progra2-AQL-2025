import streamlit as st
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.cargaDatos.cargador_datos import CargadorDatos
from src.visualizacion.visualizador import Visualizador

cargador = CargadorDatos(ruta_base="Premier_League/src/data/processed")
df = cargador.cargar_csv("premier_clean.csv")
viz = Visualizador(df)


st.set_page_config(
    page_title="PRS",
    page_icon="⚽",
    layout="wide"
)

st.title("Player Recruitment System")

st.markdown("""
Explora el rendimiento de los jugadores de la Premier League.  
Utiliza los filtros de **equipo**, **posición** y **país**.
""")


equipos = sorted(df["Team"].dropna().unique())
posiciones = sorted(df["Position"].dropna().unique())


col1, col2 = st.columns(2)

with col1:
    equipo_sel = st.selectbox("Selecciona un equipo:", ["Todos"] + equipos)
with col2:
    pos_sel = st.selectbox("Selecciona una posición:", ["Todas"] + posiciones)


equipo = None if equipo_sel == "Todos" else equipo_sel
pos = None if pos_sel == "Todas" else pos_sel


tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Goleadores por País",
    "Disciplina",
    "Información General",
    "Rendimiento Ofensivo",
    "Rendimiento Defensivo"
])


with tab1:
    pais = sorted(df["Nation"].dropna().unique())
    pa_sel = st.selectbox("Selecciona un país:", ["Todas"] + pais)
    pais = None if pa_sel == "Todas" else pa_sel

    st.markdown("### Goleadores por País")
    fig = viz.goles_por_pais(pais)
    st.plotly_chart(fig, use_container_width=True)


with tab2:
    st.markdown("### Tarjetas Amarillas y Rojas")
    fig = viz.disciplina(equipo, pos)
    st.plotly_chart(fig, use_container_width=True)


with tab3:
    colA, colB = st.columns(2)
    colC, colD = st.columns(2)

    with colA:
        st.markdown("### Pases completos a lo largo de la temporada")
        fig = viz.grafico_pases_completados_tiempo(equipo)
        st.plotly_chart(fig, use_container_width=True)


    with colB:
        st.markdown("### Pases completados y pases progresivos")
        fig = viz.grafico_pases_completados_vs_progresivos(equipo)
        st.plotly_chart(fig, use_container_width=True)

    with colC:
        st.markdown("### Relación entre carries y progressive carries")
        fig = viz.grafico_carries_vs_progresivos(equipo)
        st.plotly_chart(fig, use_container_width=True)


    with colD:
        st.markdown("### Acciones creativas")
        fig = viz.acciones_creativas(equipo)
        st.plotly_chart(fig, use_container_width=True)


with tab4:
    colE, colF = st.columns(2)

    with colE:
        st.markdown("### Goles vs Asistencias")
        fig = viz.goles_vs_asistencias(equipo)
        st.plotly_chart(fig, use_container_width=True)

    with colF:
        st.markdown("### Goles esperados vs Goles")
        fig = viz.xg_vs_goles(equipo)
        st.plotly_chart(fig, use_container_width=True)

with tab5:
    colG, colH = st.columns(2)

    with colG:
        st.markdown("### Precisión y volumen de pases (promedio por jugador)")
        fig = viz.precision_pases(equipo, pos)
        st.plotly_chart(fig, use_container_width=True)

    with colH:
        st.markdown("### Rendimiento Defensivo")
        fig = viz.defensiva_jugadores(equipo, pos)
        st.plotly_chart(fig, use_container_width=True)


st.markdown("---")
st.caption("Desarrollado por **Alejandro Quesada Leiva** — Proyecto Premier League Insights (2025)")
