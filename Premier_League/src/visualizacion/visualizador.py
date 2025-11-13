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

    def goles_vs_asistencias(self, equipo: str = None):
        df = self.filtrar(equipo)
        df_grouped = df.groupby("Player", as_index=False).agg({
            "Goals": "sum",
            "Assists": "sum",
            "Minutes": "sum"
        })

        fig = px.bar(
            df_grouped,
            x="Player",
            y=["Goals", "Assists"],
            barmode="group",
            title=f"Goles y Asistencias — {equipo or 'Todos'}",
            labels={"value": "Cantidad", "variable": "Estadística"},
        )

        fig.update_layout(xaxis={'categoryorder': 'total descending'})
        fig.show()

    def precision_pases(self, equipo: str = None, pos: str = None):
        df = self.filtrar(equipo, pos)

        df_grouped = df.groupby("Player", as_index=False).agg({
            "Passes Attempted": "mean",
            "Passes Completed": "mean",
            "Pass Completion %": "mean",
            "Minutes": "sum",
            "Team": "first"
        })

        fig = px.scatter(
            df_grouped,
            x="Passes Attempted",
            y="Passes Completed",
            size="Pass Completion %",
            color="Player",
            hover_name="Player",
            title=f"Precisión y volumen de pases (promedio por jugador) — {equipo or 'Todos'} ({pos or 'Todas las posiciones'})"
        )
        fig.update_layout(
            xaxis_title="Pases intentados (promedio)",
            yaxis_title="Pases completados (promedio)",
            legend_title="Jugador",
            template="plotly_white"
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

    def xg_vs_goles(self, equipo: str = None):
        df = self.filtrar(equipo)

        df_grouped = df.groupby("Player", as_index=False).agg({
            "Expected Goals (xG)": "mean",
            "Goals": "sum",
            "Team": "first"
        })

        df_melted = df_grouped.melt(
            id_vars=["Player", "Team"],
            value_vars=["Expected Goals (xG)", "Goals"],
            var_name="Métrica",
            value_name="Valor"
        )

        fig = px.bar(
            df_melted,
            x="Player",
            y="Valor",
            color="Métrica",
            barmode="group",
            title=f"Expected Goals (xG) vs Goles reales — {equipo or 'Todos'}"
        )

        fig.update_layout(
            xaxis_title="Jugador",
            yaxis_title="Valor",
            legend_title="Métrica",
            template="plotly_white",
            xaxis={'categoryorder': 'total descending'}
        )

        fig.show()

    def acciones_creativas(self, equipo: str = None, pos: str = None):
        df = self.filtrar(equipo, pos)

        df_grouped = df.groupby("Player", as_index=False).agg({
            "Shot-Creating Actions": "sum",
            "Goal-Creating Actions": "sum",
            "Team": "first"
        })

        fig = px.bar(
            df_grouped,
            x="Player",
            y=["Shot-Creating Actions", "Goal-Creating Actions"],
            title=f"Acciones creativas — {equipo or 'Todos'} ({pos or 'Todas las posiciones'})",
            barmode="group"
        )
        fig.update_layout(
            xaxis_title="Jugador",
            yaxis_title="Cantidad total de acciones",
            legend_title="Tipo de acción",
            template="plotly_white",
            xaxis={'categoryorder': 'total descending'}
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

    def grafico_pases_completados_tiempo(self, equipo: str = None):
        df = self.filtrar(equipo)
        fig = px.line(
            df,
            x="Date",
            y="Pass Completion %",
            color="Player",
            title="Evolución del porcentaje de pases completados a lo largo del tiempo",
            markers=True
        )
        fig.update_layout(
            xaxis_title="Fecha",
            yaxis_title="Porcentaje de pases completados (%)",
            legend_title="Jugador",
            template="plotly_white"
        )
        return fig


    def grafico_pases_completados_vs_progresivos(self, equipo: str = None):
        df = self.filtrar(equipo)
        df_grouped = df.groupby("Player", as_index=False).agg({
            "Passes Completed": "mean",
            "Progressive Passes": "mean",
            "Minutes": "sum",
            "Team": "first"
        })

        fig = px.scatter(
            df_grouped,
            x="Passes Completed",
            y="Progressive Passes",
            color="Team",
            size="Minutes",
            hover_name="Player",
            title="Comparativa entre pases completados y pases progresivos (promedio por jugador)"
        )
        fig.update_layout(
            xaxis_title="Pases completados (promedio)",
            yaxis_title="Pases progresivos (promedio)",
            legend_title="Equipo",
            template="plotly_white"
        )
        return fig


    def grafico_carries_vs_progresivos(self, equipo: str = None):
        df = self.filtrar(equipo)
        df_grouped = df.groupby("Player", as_index=False).agg({
            "Carries": "mean",
            "Progressive Carries": "mean",
            "Minutes": "sum",
            "Team": "first"
        })

        fig = px.scatter(
            df_grouped,
            x="Carries",
            y="Progressive Carries",
            color="Team",
            size="Minutes",
            hover_name="Player",
            title="Relación entre carries y progressive carries (promedio por jugador)"
        )
        fig.update_layout(
            xaxis_title="Carries (promedio)",
            yaxis_title="Progressive Carries (promedio)",
            legend_title="Equipo",
            template="plotly_white"
        )
        return fig



