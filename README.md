# Premier League Insights

Sistema de análisis exploratorio de datos (EDA) de la **Premier League 2024/2025** desarrollado con Python y Programación Orientada a Objetos (POO). Permite limpieza, análisis estadístico y visualización interactiva de datos de jugadores.

---

## Tabla de Contenidos

- [Características](#-características)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Requisitos](#-requisitos)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Módulos](#-módulos)

---

## Características

### Funcionalidades Principales

- **Limpieza de Datos**: Manejo de valores nulos y normalización de tipos de datos
- **Análisis EDA**: Resúmenes estadísticos descriptivos y matrices de correlación
- **Visualizaciones Interactivas**: 8 gráficos con Plotly sobre rendimiento en diversos ambitos
- **Modelado POO**: Clases de dominio (Jugador, Equipo, EstadisticasPartido)

### Tecnologías Utilizadas

- **Python 3.11**
- **Pandas** - Manipulación de datos
- **NumPy** - Operaciones numéricas
- **Plotly** - Visualizaciones interactivas
- **Programación Orientada a Objetos (POO)**

---

## Estructura del Proyecto


---

## 🔧 Requisitos

### Requisitos del Sistema

- Python 3.11 
- pip (gestor de paquetes de Python)
- 2 GB de RAM mínimo
- 1 GB de espacio en disco

### Dependencias Python

```txt
pandas
numpy
plotly
```

---

## Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/AlejandroQL23/proyecto-progra2-AQL-2025.git
cd premier-league-insights
```


## Uso

### Uso Básico

```python

# 1. Cargar datos
cargador = CargadorDatos(ruta_base="src/data/raw")
df = cargador.cargar_csv("premier.csv")

# 2. Limpiar datos
procesador = ProcesadorEDA()
df_limpio = procesador.limpieza_datos(df)

# 3. Análisis estadístico
resumen = procesador.resumen_descriptivo(df_limpio)
matriz_corr = procesador.matriz_correlacion(df_limpio)

# 4. Visualizaciones
visualizador = Visualizador()
```


## Módulos

### 1. CargadorDatos

**Funcionalidad**:
- Carga archivos CSV con validación
- Registra métricas de calidad (filas, columnas, nulos)
- Genera reportes de carga automáticos

### 2. ProcesadorEDA

**Funcionalidad**:
- **Limpieza de datos**: Elimina nulos, normaliza tipos, limpia columnas
- **Resumen descriptivo**: Calcula count, mean, std, min, q1, median, q3, max
- **Matriz de correlación**: Correlaciones de Pearson, Kendall o Spearman

**Transformaciones aplicadas**:
- Position: Solo posición principal (elimina múltiples posiciones)
- Age: Convierte "29-343" → 29 (solo años)
- Pass Completion %: "71,7" → 71.7 (float)
- Date: String → datetime
- Elimina columnas: `#`, `Penalty Shoot on Goal`, `Penalty Shoot`, `Dribbles`, `Non-Penalty xG (npxG)`, `Dribble Attempts`, `Successful Dribbles`

---

### 3. Visualizador

**Funcionalidad**: Crea visualizaciones interactivas con Plotly

#### Visualizaciones Disponibles

| # | Visualización |
|:-:|:--------------|
| 1 | **Goles y Asistencias** |
| 2 | **Precisión y Volumen de Pases** |
| 3 | **Cantidad de Tarjetas** |
| 4 | **Expected Goals (xG) vs Goles Reales** |
| 5 | **Acciones Creativas** |
| 6 | **Total de Goles** |
| 7 | **Rendimiento Defensivo** |
| 8 | **Porcentaje de Pases Completados** |
| 9 | **Comparativa Pases Completados vs Progresivos** |
| 10 | **Relación Carries vs Progressive Carries** |

---

### 4. Utilidades

**Funcionalidad**: Funciones auxiliares reutilizables


<div align="center">

** Desarrollado con pasión por el fútbol y Python 🐍**

</div>
