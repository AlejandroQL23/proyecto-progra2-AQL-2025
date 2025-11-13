import pandas as pd
import numpy as np
from typing import Optional, List
from pathlib import Path
from Premier_League.src.helpers.utilidades import Utilidades


class ProcesadorEDA(Utilidades):
    def __init__(self):
        self._dataframe: Optional[pd.DataFrame] = None


    @property
    def dataframe(self) -> Optional[pd.DataFrame]:
        return self._dataframe


    def resumen_descriptivo(
            self,
            df: pd.DataFrame,
            columnas: Optional[List[str]] = None
    ) -> pd.DataFrame:

        super().validar_dataframe(df)

        print("TIPOS DE DATOS POR COLUMNA")
        print("=" * 80)

        # Obtener información de tipos
        tipos_info = []
        for col in df.columns:
            tipo = str(df[col].dtype)

            tipos_info.append({
                'Columna': col,
                'Tipo': tipo
            })

        # DF con info
        df_tipos = pd.DataFrame(tipos_info)
        print(df_tipos)

        # una columna numérica? (como minimo)
        # df.select_dtypes filtro por tipo de dato
        # np.number = numpy
        columnas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()

        if len(columnas_numericas) == 0:
            print("El DataFrame no contiene columnas numéricas")
            raise ValueError("El DataFrame debe tener al menos una columna numérica")

        # validar columnas seleccionadas
        if columnas is not None:
            # las columnas existen?
            # para cada columna col dentro de la lista columnas, incluir en la nueva lista solo si NO esta presente en df.columns
            columnas_faltantes = [col for col in columnas if col not in df.columns]
            if columnas_faltantes:
                print(f"Columnas no encontradas: {columnas_faltantes}")
                raise ValueError(f"Las siguientes columnas no existen: {columnas_faltantes}")

            # si selecciona columnas no #s, filtramos
            columnas_a_analizar = [col for col in columnas if col in columnas_numericas]

            if len(columnas_a_analizar) == 0:
                print("Ninguna de las columnas especificadas es numérica")
                raise ValueError("Debe especificar al menos una columna numérica")

            columnas_no_numericas = [col for col in columnas if col not in columnas_numericas]
            if columnas_no_numericas:
                print(f"Columnas no numéricas ignoradas: {columnas_no_numericas}")
        else:
            columnas_a_analizar = columnas_numericas

        # resumen
        print(f"Generando resumen descriptivo para {len(columnas_a_analizar)} columnas")

        # Crear DataFrame con estadísticas personalizadas
        resumen = pd.DataFrame({
            'count': df[columnas_a_analizar].count(),
            'mean': df[columnas_a_analizar].mean(),
            'std': df[columnas_a_analizar].std(),
            'min': df[columnas_a_analizar].min(),
            'q1_25%': df[columnas_a_analizar].quantile(0.25),
            'median_50%': df[columnas_a_analizar].median(),
            'q3_75%': df[columnas_a_analizar].quantile(0.75),
            'max': df[columnas_a_analizar].max()
        }).T

        # redondeo a 2 para que no salgan tantos decimales
        resumen = resumen.round(2)

        """
        print("=" * 80)
        print("RESUMEN DESCRIPTIVO")
        print("=" * 80)
        print(f"Columnas analizadas: {len(columnas_a_analizar)}")
        print(f"Filas totales: {len(df)}")
        print("-" * 80)
        """

        print("\n Resumen Estadístico (primeras 5 columnas):\n")
        print(resumen.iloc[:, :5].to_string())

        if len(resumen.columns) > 5:
            print(f"\n... y {len(resumen.columns) - 5} columnas más")

            print("=" * 80)

        return resumen

    def matriz_correlacion(
            self,
            df: pd.DataFrame,
            columnas: Optional[List[str]] = None,
            metodo: str = 'pearson',
    ) -> pd.DataFrame:

        super().validar_dataframe(df)

        # metodo seleccionado es valido?
        metodos_validos = ['pearson', 'kendall', 'spearman']
        if metodo not in metodos_validos:
            print(f"Método '{metodo}' no válido")
            raise ValueError(f"Método debe ser uno de: {metodos_validos}")

        # columnas numéricas
        columnas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()

        # hay al menos dos columnas #s?
        if len(columnas_numericas) < 2:
            print("Se necesitan al menos 2 columnas numéricas para calcular correlación")
            raise ValueError("El DataFrame debe tener al menos 2 columnas numéricas")

        # validar columnas seleccionadas
        if columnas is not None:
            # existen?
            columnas_faltantes = [col for col in columnas if col not in df.columns]
            if columnas_faltantes:
                print(f"Columnas no encontradas: {columnas_faltantes}")
                raise ValueError(f"Las siguientes columnas no existen: {columnas_faltantes}")

            # si selecciona columnas no #s, filtramos
            columnas_a_analizar = [col for col in columnas if col in columnas_numericas]

            if len(columnas_a_analizar) < 2:
                print("Se necesitan al menos 2 columnas numéricas")
                raise ValueError("Debe especificar al menos 2 columnas numéricas")

            columnas_no_numericas = [col for col in columnas if col not in columnas_numericas]
            if columnas_no_numericas:
                print(f"Columnas no numéricas ignoradas: {columnas_no_numericas}")
        else:
            columnas_a_analizar = columnas_numericas


        # matriz de correlacion
        print(f"Calculando matriz de correlación ({metodo}) para {len(columnas_a_analizar)} columnas...")

        try:
            matriz_corr = df[columnas_a_analizar].corr(method=metodo)

            # redondeamos a 3
            matriz_corr = matriz_corr.round(3)


            """
            print("=" * 80)
            print("MATRIZ DE CORRELACIÓN")
            print("=" * 80)
            print(f"Método: {metodo.capitalize()}")
            print(f"Columnas analizadas: {len(columnas_a_analizar)}")
            print(f"Filas con datos: {df[columnas_a_analizar].dropna().shape[0]}")
            """


            print("-" * 80)

            print(f"\n Matriz de correlación ({matriz_corr.shape[0]}x{matriz_corr.shape[1]}):")
            print(matriz_corr.iloc[:5, :5].to_string())

            if matriz_corr.shape[0] > 5:
                print(f"\n... matriz completa de {matriz_corr.shape[0]} variables")

            print("=" * 80)

            return matriz_corr

        except Exception as e:
            print(f"Error al calcular matriz de correlación: {str(e)}")
            raise

# ----------*----------------------*---------------------------*-------------------*-----------------------------*--------------------------*-

    def limpieza_datos(
            self,
            df: pd.DataFrame,
            ruta_salida: str = 'src/data/processed/premier_clean.csv'
    ) -> pd.DataFrame:

        super().validar_dataframe(df)

        print("=" * 80)
        print("LIMPIEZA DE DATOS")
        print("=" * 80)

        # valores sin borrar
        filas_inicial = len(df)
        columnas_inicial = len(df.columns)
        nulos_inicial = df.isnull().sum().sum()
        porcentaje_nulos_inicial = (nulos_inicial / df.size) * 100

        print(f"\nEstado inicial:")
        print(f"  Filas: {filas_inicial:,}")
        print(f"  Columnas: {columnas_inicial}")
        print(f"  Valores nulos: {nulos_inicial:,} ({porcentaje_nulos_inicial:.2f}%)")

        # columnas con nulos
        columnas_con_nulos = df.isnull().sum()
        columnas_con_nulos = columnas_con_nulos[columnas_con_nulos > 0].sort_values(ascending=False)

        if len(columnas_con_nulos) > 0:
            print(f"\n Columnas con valores nulos:")
            for col, count in columnas_con_nulos.items():
                porcentaje = (count / filas_inicial) * 100
                print(f"  • {col}: {count} nulos ({porcentaje:.2f}%)")

        # eliminar nulos
        print(f"\nEliminando filas con valores nulos...")
        df_limpio = df.dropna()

        # valores despues de borrar nulos
        filas_final = len(df_limpio)
        filas_eliminadas = filas_inicial - filas_final
        porcentaje_perdidas = (filas_eliminadas / filas_inicial) * 100

        print(f"\nEstado final:")
        print(f"  Filas: {filas_final:,}")
        print(f"  Filas eliminadas: {filas_eliminadas:,} ({porcentaje_perdidas:.2f}%)")

        # limpiar POSITION (se deja solo la principal)

        if 'Position' in df_limpio.columns:

            # cuantas tienen multi posiciones?
            multi_pos = df_limpio['Position'].str.contains(',', na=False).sum()

            if multi_pos > 0:
                print(f" Registros con múltiples posiciones: {multi_pos}")

                # dejamos solo la primera pos
                df_limpio['Position'] = df_limpio['Position'].str.split(',').str[0].str.strip()

                # ver poss unicas
                #posiciones_unicas = sorted(df_limpio['Position'].dropna().unique())
                #print(f"  • Posiciones únicas: {len(posiciones_unicas)}")
                #print(f"    {posiciones_unicas}")

        # COLUMNA AGE (dejar solo primera parte de xx-xxx)
        if 'Age' in df_limpio.columns:

            df_limpio['Age'] = df_limpio['Age'].astype(str).str.split('-').str[0]

            # seteamos tipo int
            df_limpio['Age'] = pd.to_numeric(df_limpio['Age'], errors='coerce')

        # limpiar PASS COMPLETION % de Object a Float
        if 'Pass Completion %' in df_limpio.columns:

            # comas por puntos
            df_limpio['Pass Completion %'] = df_limpio['Pass Completion %'].astype(str).str.replace(',', '.')

            # pasa a float
            df_limpio['Pass Completion %'] = pd.to_numeric(df_limpio['Pass Completion %'], errors='coerce')

        # limpiar DATE de Object a date
        if 'Date' in df_limpio.columns:

            # pasa a datetime
            df_limpio['Date'] = pd.to_datetime(df_limpio['Date'], errors='coerce')

        # Se quitan columnas que NO van a ser utilizadas

        eliminar = [
            '#',
            'Penalty Shoot on Goal',
            'Penalty Shoot',
            'Non-Penalty xG (npxG)',
            'Dribbles',
            'Dribble Attempts',
            'Successful Dribbles'
        ]

        # existen en el DF?
        columnas_a_eliminar = [col for col in eliminar if col in df_limpio.columns]

        if columnas_a_eliminar:
            df_limpio = df_limpio.drop(columns=columnas_a_eliminar)


        # guardar
        self.guardar_csv_limpio(df_limpio, ruta_salida)

        print("=" * 80)

        return df_limpio

    def guardar_csv_limpio(self, df: pd.DataFrame, ruta_salida: str):
        try:
            ruta = Path(ruta_salida)

            # guardar csv limpio
            df.to_csv(ruta, index=False, encoding='utf-8')

            print(f"\nArchivo guardado:")

        except Exception as e:
            print(f"\nError al guardar: {str(e)}")
            raise


