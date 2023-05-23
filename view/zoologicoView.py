import streamlit as st
import pandas as pd
import requests
import time
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
            botonAgregarAnimalHabitat = st.button("Agregar animal a un habitat", key=3, use_container_width=True)

        if botonCrearAnimal:
            st.session_state["opcion"] = 1
        elif botonCrearHabitat:
            st.session_state["opcion"] = 2
        elif botonAgregarAnimalHabitat:
            st.session_state["opcion"] = 3
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

    def menu_creacion_habitat(self,zoologico):
        st.subheader("Datos para agregar un habitat al RHLMZoo")
        nombre = st.text_input("Ingrese el nombre del habitat: ")
        tipoDeHabitat = st.selectbox("Seleccione el tipo de habitat: ", zoologico.tiposHabitats)
        dieta = st.selectbox("Seleccione el tipo de dieta del habitat: ", zoologico.tiposAlimentacion)
        capacidad = st.slider("Elija la capacidad maxima de animales que podra contener el habitat: ", min_value=1, max_value=12, step=1)
        st.divider()
        if tipoDeHabitat == "Desertico":
            escasezDeAgua = st.slider("Cual es el porcentaje de escasez de agua: ", min_value=0,max_value=100,step=1)
            variacionDeTemperatura = st.slider("Cual es el porcentaje de que la temperatura varie: ", min_value=0,max_value=100,step=1)
            st.divider()
            temperaturaMin = st.slider("Temperatura minima del habitat: ", min_value= 30,max_value=40,step=1)
            temperaturaMax = st.slider("Temperatura maxima del habitat: ", min_value=41,max_value=50,step=1)

        elif tipoDeHabitat == "Acuatico":
            diversidadBiologica = st.slider("Cual es el porcentaje de diversidad biologica de este habitat: ", min_value=0,max_value=100,step=1)
            presenciaAgua = st.slider("Cual es el nivel de agua de esta habitat: ",min_value=0,max_value=10,step=1)
            st.divider()
            temperaturaMin = st.slider("Temperatura minima del habitat: ", min_value= 15,max_value=25,step=1)
            temperaturaMax = st.slider("Temperatura maxima del habitat: ", min_value=26,max_value=35,step=1)

        elif tipoDeHabitat == "Polar":
            bajasTemperaturas = st.slider("Probabilidad que esta zona sufra de muy bajas temperaturas: ", min_value=0,max_value=10,step=1)
            presenciaHieloNieve = st.slider("De que grado es la presencia de nieve y hielo es este habitat: ", min_value=0,max_value=10,step=1)
            st.divider()
            temperaturaMin = st.slider("Temperatura minima del habitat: ", min_value=-40,max_value=-20,step=1)
            temperaturaMax = st.slider("Temperatura maxima del habitat: ", min_value=-19,max_value=0,step=1)

        elif tipoDeHabitat == "Selvatico":
            vegetacionDensa = st.slider("Porcentaje de una densa vegetacion en la zona: ", min_value=0,max_value=100,step=1)
            biodiversidad = st.slider("Porcentaje de biodiversidad en el habitat: ", min_value=0,max_value=100,step=1)
            st.divider()
            temperaturaMin = st.slider("Temperatura minima del habitat: ", min_value= 10,max_value=20,step=1)
            temperaturaMax = st.slider("Temperatura maxima del habitat: ", min_value=21,max_value=35,step=1)
            max = 35
            min = 10

        botonCrear = st.button("Ingresar habitat")

        if botonCrear:
            if self._zoologico.obtenerHabitat(nombre,zoologico.habitats) == 1:
                self.mensaje_error("Lo sentimos, ya existe un habitat con el mismo nombre")
            else:
                if tipoDeHabitat == "Desertico":
                    nuevoHabitat = habitatModel.desertico(nombre,dieta,temperaturaMax,temperaturaMin,capacidad,escasezDeAgua,variacionDeTemperatura)
                elif tipoDeHabitat == "Acuatico":
                    nuevoHabitat = habitatModel.desertico(nombre,dieta,temperaturaMax,temperaturaMin,capacidad,diversidadBiologica,presenciaAgua)
                elif tipoDeHabitat == "Polar":
                    nuevoHabitat = habitatModel.desertico(nombre,dieta,temperaturaMax,temperaturaMin,capacidad,bajasTemperaturas,presenciaHieloNieve)
                elif tipoDeHabitat == "Selvatico":
                    nuevoHabitat = habitatModel.desertico(nombre,dieta,temperaturaMax,temperaturaMin,capacidad,vegetacionDensa,biodiversidad)
                st.success("El habitat se agrego exitosamente")
                return nuevoHabitat


    def menu_agregar_animal_habitat(self,animales,habitat,zoologico):
        st.subheader("Menu para agregar animales a habitats")
        st.divider()
        with st.container():
            if len(animales) == 0:
                self.mensaje_error("No hay animales disponibles")






    def mensaje_error(self,mensaje):
        st.error(mensaje)