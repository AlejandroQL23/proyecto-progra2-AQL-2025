import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

class Visualizador:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def filtrar(self, equipo: str = None, pos: str = None) -> pd.DataFrame:
        df_filtrado = self.df.copy()

        if equipo:
            df_filtrado = df_filtrado[df_filtrado["Team"].str.lower() == equipo.lower()]
            if df_filtrado.empty:
                print(f"No se encontraron jugadores del equipo '{equipo}'")
                return df_filtrado

        if pos:
            df_filtrado = df_filtrado[df_filtrado["Position"].str.lower() == pos.lower()]
            if df_filtrado.empty:
                print(f"No se encontraron jugadores en la posición '{pos}' para el equipo '{equipo or 'Todos'}'")
                return df_filtrado

        return df_filtrado

    def goles_vs_asistencias(self, equipo: str = None, pos: str = None):
        df = self.filtrar(equipo, pos)
        fig = px.scatter(
            df,
            x="Goals",
            y="Assists",
            color="Player",
            size="Minutes",
            hover_name="Player",
            title=f"Goles vs Asistencias — {equipo or 'Todos'} ({pos or 'Todas las posiciones'})"
        )
        fig.show()

    def minutos_vs_goles(self, equipo: str = None, pos: str = None):
        df = self.filtrar(equipo, pos)
        fig = px.scatter(
            df,
            x="Minutes",
            y="Goals",
            color="Player",
            hover_name="Player",
            title=f"Minutos jugados vs Goles — {equipo or 'Todos'} ({pos or 'Todas las posiciones'})"
        )
        fig.show()

    def precision_pases(self, equipo: str = None, pos: str = None):
        df = self.filtrar(equipo, pos)
        fig = px.scatter(
            df,
            x="Passes Attempted",
            y="Passes Completed",
            size="Pass Completion %",
            color="Player",
            hover_name="Player",
            title=f"Precisión y volumen de pases — {equipo or 'Todos'} ({pos or 'Todas las posiciones'})"
        )
        fig.show()

    def disciplina(self, equipo: str = None, pos: str = None):
        df = self.filtrar(equipo, pos)
        df_disciplinado = df.groupby("Player")[["Yellow Cards", "Red Cards"]].sum().reset_index()
        fig = go.Figure()
        fig.add_trace(go.Bar(x=df_disciplinado["Player"], y=df_disciplinado["Yellow Cards"], name="Yellow Cards", marker_color="gold"))
        fig.add_trace(go.Bar(x=df_disciplinado["Player"], y=df_disciplinado["Red Cards"], name="Red Cards", marker_color="red"))
        fig.update_layout(
            title=f"Disciplina — {equipo or 'Todos'} ({pos or 'Todas las posiciones'})",
            barmode="stack",
            xaxis_title="Jugador",
            yaxis_title="Cantidad de tarjetas"
        )
        fig.show()

    def xg_vs_goles(self, equipo: str = None, pos: str = None):
        df = self.filtrar(equipo, pos)
        fig = px.scatter(
            df,
            x="Expected Goals (xG)",
            y="Goals",
            color="Player",
            trendline="ols",
            title=f"Expected Goals (xG) vs Goles reales — {equipo or 'Todos'} ({pos or 'Todas las posiciones'})"
        )
        fig.show()

    def xag_vs_asistencias(self, equipo: str = None, pos: str = None):
        df = self.filtrar(equipo, pos)
        fig = px.scatter(
            df,
            x="Expected Assists (xAG)",
            y="Assists",
            color="Player",
            trendline="ols",
            title=f"xpected Assists (xAG) vs Asistencias — {equipo or 'Todos'} ({pos or 'Todas las posiciones'})"
        )
        fig.show()

    def acciones_creativas(self, equipo: str = None, pos: str = None):
        df = self.filtrar(equipo, pos)
        fig = px.bar(
            df,
            x="Player",
            y=["Shot-Creating Actions", "Goal-Creating Actions"],
            title=f"Acciones creativas — {equipo or 'Todos'} ({pos or 'Todas las posiciones'})"
        )
        fig.show()

    def goles_por_pais(self, pais: str = None):
        df = self.df.copy()

        if pais:
            df = df[df["Nation"].str.lower() == pais.lower()]
            if df.empty:
                print(f"No se encontraron jugadores de la nación '{pais}'.")
                return

        df_goles = df.groupby(["Nation", "Player"])["Goals"].sum().reset_index()

        fig = px.bar(
            df_goles,
            x="Player",
            y="Goals",
            color="Nation",
            title=f"Goles por jugador — {pais if pais else 'Todos los países'}",
            text="Goals"
        )
        fig.update_traces(textposition="outside")
        fig.update_layout(
            xaxis_title="Jugador",
            yaxis_title="Total de Goles",
            xaxis={'categoryorder':'total descending'}
        )
        fig.show()

    def defensiva_jugadores(self, equipo: str = None, pos: str = None):
        df = self.filtrar(equipo, pos)

        df_def = df.groupby("Player")[["Blocks", "Tackles"]].sum().reset_index()

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df_def["Player"],
            y=df_def["Tackles"],
            name="Tackles",
            marker_color="steelblue"
        ))
        fig.add_trace(go.Bar(
            x=df_def["Player"],
            y=df_def["Blocks"],
            name="Blocks",
            marker_color="orange"
        ))

        fig.update_layout(
            title=f"Rendimiento Defensivo — {equipo or 'Todos'} ({pos or 'Todas las posiciones'})",
            xaxis_title="Jugador",
            yaxis_title="Cantidad",
            barmode="group",
            xaxis={'categoryorder': 'total descending'}
        )

        fig.show()


