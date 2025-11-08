import sys
from pathlib import Path
# agregar el directorio src al path para imports
sys.path.append(str(Path(__file__).parent / 'src'))
from cargaDatos.cargador_datos import CargadorDatos
from clases import jugador, equipo



def main():
    try:
        # instancia del cargador
        cargador = CargadorDatos(ruta_base="data/raw")

        df = cargador.cargar_csv("premier.csv")

        #print(df)

    except FileNotFoundError as e:
        print(f"\n ERROR: {e}")
        print("\n💡 Sugerencias:")
        print("  1. Verifica que el archivo exista")
        print("  2. Ajusta la ruta en: cargador = CargadorDatos(ruta_base='TU_RUTA')")
        print("  3. Revisa la estructura de carpetas")
        print()

    except Exception as e:
        print(f"\n ERROR INESPERADO: {e}")
        print(f"Tipo de error: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        print()


if __name__ == "__main__":
    main()