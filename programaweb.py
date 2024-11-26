import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Función para el ejercicio 1
def f(x):
    return x**2 - 4*x + 5

# Función para el ejercicio 2
def g(x):
    return np.abs(x)

# Función para el ejercicio 3
def h(x):
    return np.sin(x)

# Función para el ejercicio 4
def f_2d(x, y):
    return x**2 + y**2

# Streamlit App
st.title("Resolución de Ejercicios de Minimización")

# Ejercicio 1
st.header("1. Verificar minimizadores de f(x) = x² - 4x + 5")
st.subheader("a) ¿x=2 y x=0 son minimizadores globales o locales?")
x_values = [2, 0]

st.latex(r"f(x) = x^2 - 4x + 5")
st.latex(r"f'(x) = 2x - 4")
st.latex(r"2x - 4 = 0 \implies x = 2")
st.latex(r"f(2) = (2)^2 - 4(2) + 5 = 1")
st.latex(r"f(0) = (0)^2 - 4(0) + 5 = 5")
st.latex(r"\text{Conclusión: } x=2 \text{ es el mínimo global. } x=0 \text{ no es un mínimo local ni global.}")

# Mostrar gráfico de f(x)
x_vals = np.linspace(-1, 5, 500)
y_vals = f(x_vals)
plt.figure(figsize=(8, 4))
plt.plot(x_vals, y_vals, label=r"f(x) = x^2 - 4x + 5")
plt.axvline(0, color="blue", linestyle="--", label=r"x=0")
plt.scatter([2], [f(2)], color="red", label=r"Mínimo global en x=2")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.legend()
st.pyplot(plt)

# Ejercicio 2
st.header("2. Dibujar f(x) = |x| y verificar mínimo en x=0")
st.latex(r"f(x) = |x|")
st.latex(r"f(0) = |0| = 0")
st.latex(r"\text{Conclusión: } x=0 \text{ es el mínimo global de } f(x) = |x|.")

# Mostrar gráfico de f(x) = |x|
x_vals_g = np.linspace(-5, 5, 500)
y_vals_g = g(x_vals_g)
plt.figure(figsize=(8, 4))
plt.plot(x_vals_g, y_vals_g, label=r"f(x) = |x|")
plt.scatter([0], [g(0)], color="red", label=r"Mínimo global en x=0")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.legend()
st.pyplot(plt)

# Ejercicio 3
st.header("3. f(x) = sin(x) en [0, π] y el Teorema de Weierstrass")
st.latex(r"f(x) = \sin(x)")
st.latex(r"f(0) = \sin(0) = 0, \, f(\pi) = \sin(\pi) = 0, \, f(\pi/2) = \sin(\pi/2) = 1")
st.latex(r"\text{Conclusión: El mínimo global es } f(x) = 0 \text{ en } x=0 \text{ y } x=\pi.")

# Mostrar gráfico de f(x) = sin(x)
x_vals_h = np.linspace(0, np.pi, 500)
y_vals_h = h(x_vals_h)
plt.figure(figsize=(8, 4))
plt.plot(x_vals_h, y_vals_h, label=r"f(x) = \sin(x)")
plt.scatter([0, np.pi], [h(0), h(np.pi)], color="red", label=r"Mínimos globales")
plt.scatter([np.pi / 2], [h(np.pi / 2)], color="blue", label=r"Máximo global")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.legend()
st.pyplot(plt)

# Ejercicio 4
st.header("4. f(x, y) = x² + y² en x² + y² ≤ 1")
st.latex(r"f(x, y) = x^2 + y^2")
st.latex(r"f(0, 0) = 0")
st.latex(r"\text{Conclusión: El mínimo global ocurre en } (0, 0).")

# Mostrar gráfico de f(x) = x² + y² para y=0
x_vals_4 = np.linspace(-1, 1, 500)
y_vals_4 = f_2d(x_vals_4, 0)
plt.figure(figsize=(8, 4))
plt.plot(x_vals_4, y_vals_4, label=r"f(x, 0) = x^2")
plt.scatter([0], [f_2d(0, 0)], color="red", label=r"Mínimo global en (0, 0)")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.legend()
st.pyplot(plt)

# Ejercicio 5
st.header("5. Ejemplo con múltiples mínimos globales")
st.latex(r"f(x) = \cos(x)")
st.latex(r"\text{Mínimos globales: } x=\pi, \, f(\pi) = -1.")
st.latex(r"\text{Conclusión: Múltiples mínimos globales en el dominio.}")

# Mostrar gráfico de f(x) = cos(x)
x_vals_multi = np.linspace(0, 2 * np.pi, 500)
y_vals_multi = np.cos(x_vals_multi)
plt.figure(figsize=(8, 4))
plt.plot(x_vals_multi, y_vals_multi, label=r"f(x) = \cos(x)")
plt.scatter([np.pi], [-1], color="red", label=r"Mínimo global en x=\pi")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.legend()
st.pyplot(plt)
