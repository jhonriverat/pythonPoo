import streamlit as st
import pandas as pd
import model.animales as animalesModel
import model.habitat as habitatModel
import model.zoologico as zoologicoModel
import controller.zoologicoController as ZoologicoController

class zoologicoView():
    def __init__(self):
        self._zoologico = zoologicoModel.Zoologico(0)
        self._controlador = ZoologicoController.zoologicoController(self._zoologico, self)

    def menu(self):
        st.title("Bienvenido al RHLMZoo 🐾👹")
        with st.sidebar:
            st.header("Elige una opcion:")

            botonCrearAnimal = st.button("Crear animal", key=1, use_container_width=True)
            botonCrearHabitat = st.button("Crear habitat", key=2, use_container_width=True)

            if botonCrearAnimal:
                st.session_state["opcion"] = 1
            elif botonCrearHabitat:
                st.session_state["opcion"] = 2

            if "opcion" in st.session_state:
                self._controlador.ejecutarOpciones(st.session_state["opcion"])

    def menu_creacion_animal(self, idAnimal, zoologico):
        st.divider()

        with st.container():
            st.subheader("Datos para agregar animal al RHLMZoo")
            nombre = st.text_input("Nombre del animal: ")
            especie = st.text_input("Especie del animal: ")
            habitat = st.selectbox("Habitat del animal: ", zoologico.tiposHabitats)
            claseDeAlimentacion = st.selectbox("Clase de alimentacion del animal: ", zoologico.tiposAlimentacion)
            edad = st.slider("Edad del animal: ", min_value=0, max_value=10, step=1)
            horasMinimasDormir = st.slider("Horas minimas que debe dormir el animal: ", min_value=0, max_value=24, step=1)
            temperatura = st.slider("Temperatura adaptativa para el animal: ", min_value=-15, max_value=35, step=1)
            botonCrear = st.button("Crear animal")

            if botonCrear:
                nuevoAnimal = animalesModel.animales(idAnimal,nombre,edad,especie,habitat,claseDeAlimentacion,horasMinimasDormir)
                st.success("Se creo el animal con exito")
                st.success("RECORDAR: ingresarlo en un habitat")
