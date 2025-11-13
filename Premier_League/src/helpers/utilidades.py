import pandas as pd
from typing import Any


class Utilidades:
    def validar_dataframe(self, df: Any) -> None:
        # es un DF?
        if not isinstance(df, pd.DataFrame):
            print("El parámetro 'df' debe ser un pandas DataFrame")
            raise TypeError(f"Se esperaba pd.DataFrame, se recibió {type(df)}")

        # esta vacío?
        if df.empty:
            print("El DataFrame está vacío")
            raise ValueError("No se puede generar resumen de un DataFrame vacío")