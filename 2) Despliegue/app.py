import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Título de la aplicación
st.title("📊 Visualización de Datos con Streamlit")

# Subtítulo
st.subheader("📌 Tabla de Datos de Muestra")

# Crear un DataFrame con datos de muestra
data = {
    "Categoría": ["A", "B", "C", "D", "E"],
    "Valores": [10, 25, 40, 30, 15]
}
df = pd.DataFrame(data)

# Mostrar la tabla
st.dataframe(df)

# Gráfico de líneas con Matplotlib
st.subheader("📈 Gráfico de Líneas")

fig, ax = plt.subplots()
ax.plot(df["Categoría"], df["Valores"], marker="o", linestyle="-", color="b")
ax.set_xlabel("Categoría")
ax.set_ylabel("Valor")
ax.set_title("Tendencia de Valores")

st.pyplot(fig)  # Mostrar gráfico en Streamlit

# Gráfico de barras con Plotly
st.subheader("📊 Gráfico de Barras")

fig_bar = px.bar(df, x="Categoría", y="Valores", text="Valores", color="Categoría", 
                 title="Distribución de Valores")
st.plotly_chart(fig_bar)
