import streamlit as st
import pandas as pd
import tempfile
import os

from src.carga_datos import cargar_datos


st.set_page_config(
    page_title="Análisis de uso de pantalla",
    page_icon="📱",
    layout="wide"
)

st.title("📱 Análisis de tiempo de uso en pantalla")
st.write("Subí un archivo CSV para analizar el uso de distintas aplicaciones.")


archivo_subido = st.file_uploader(
    "Cargar archivo CSV",
    type=["csv"]
)


if archivo_subido is not None:
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
            tmp.write(archivo_subido.getvalue())
            ruta_temporal = tmp.name

        df = cargar_datos(ruta_temporal)

        os.remove(ruta_temporal)

        st.success("Archivo cargado y validado correctamente.")

        st.subheader("Vista previa de los datos")
        st.dataframe(df)

        st.subheader("Indicadores principales")

        total_registros = len(df)
        total_uso = df["tiempo_uso"].sum()
        promedio_uso = df["tiempo_uso"].mean()
        app_mas_usada = (
            df.groupby("app")["tiempo_uso"]
            .sum()
            .idxmax()
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Cantidad de registros", total_registros)
        col2.metric("Tiempo total de uso", f"{total_uso:.2f} min")
        col3.metric("Promedio de uso", f"{promedio_uso:.2f} min")
        col4.metric("App más usada", app_mas_usada)

        st.subheader("Tiempo total de uso por aplicación")

        uso_por_app = (
            df.groupby("app")["tiempo_uso"]
            .sum()
            .sort_values(ascending=False)
        )

        st.bar_chart(uso_por_app)

        st.subheader("Cantidad de usos por aplicación")

        usos_por_app = (
            df.groupby("app")["cantidad_uso"]
            .sum()
            .sort_values(ascending=False)
        )

        st.bar_chart(usos_por_app)

    except ValueError as e:
        st.error(str(e))

    except FileNotFoundError:
        st.error("No se encontró el archivo.")

    except Exception as e:
        st.error(f"Ocurrió un error inesperado: {e}")

else:
    st.info("Subí un archivo CSV para comenzar.")

