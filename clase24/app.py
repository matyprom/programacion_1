import streamlit as st

st.title("mi terrible app")
st.header("subtitulo")
st.write("hola desde streamlit  oo   du")

nombre = st.text_input("nombre")
descripcion = st.text_area("descripcion")
unidades = st.number_input("unidades", 1)
color = st.selectbox("color", ["rojo", "azul"])
urgente = st.checkbox("es urgente")
st.write(nombre)

nombre = st.text_input("nombre", value="luz")

if st.button("saludar"):
    st.write("hi")