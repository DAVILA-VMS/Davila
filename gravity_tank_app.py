import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Calculadora Gravity Tank Cedervall", layout="centered")

# Mostrar los logos
col1, col2 = st.columns([1, 1])
with col1:
    st.image("logo_vms.png", width=150)
with col2:
    st.image("logo_cedervall.png", width=150)

st.title("🛠️ Calculadora de Altura del Gravity Tank Cedervall")
st.markdown("Modelo: Cedervall Sterntube Seals")

# Mostrar plano técnico
st.subheader("📐 Plano técnico de referencia")
st.image("plano_gravity_tank.png", caption="Plano del sistema de tanque de gravedad", use_column_width=True)

# Entrada de datos
st.subheader("🔢 Datos de entrada")
Dmax = st.number_input("Profundidad máxima (Dmax) [m]", min_value=0.0, format="%.2f")
x = st.number_input("Distancia vertical al eje (x) [m]", min_value=0.0, format="%.2f")
qo = st.number_input("Densidad del aceite (qo) [kg/m³] (opcional)", min_value=0.0, format="%.2f")

# Cálculo
if Dmax> 0 and x>= 0:
    Hw = Dmax - x
    if qo> 0:
        Ho = (Hw * 1025) / (qo * 9.81 * 10000)
        metodo = "Usando densidad proporcionada"
    else:
        Ho = 1.14 * Hw + 1.2
        metodo = "Usando densidad estándar (900 kg/m³)"

    st.subheader("📊 Resultados")
    st.write(f"**Hw (profundidad al eje):** {Hw:.2f} m")
    st.write(f"**Ho (altura del tanque):** {Ho:.2f} m")
    st.write(f"**Método usado:** {metodo}")

    # Gráfico
    fig, ax = plt.subplots()
    ax.plot([0, Ho], [0, Hw], marker='o')
    ax.set_xlabel("Ho (altura del tanque)")
    ax.set_ylabel("Hw (profundidad al eje)")
    ax.set_title("Relación entre Ho y Hw")
    st.pyplot(fig)
else:

    st.warning("Por favor ingresa valores válidos para Dmax y x.")

