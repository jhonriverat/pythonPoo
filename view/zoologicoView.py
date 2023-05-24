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
        self.zoologico = zoologicoModel.Zoologico(0)
        self.controlador = ZoologicoController.zoologicoController(self.zoologico, self)
#Funcion de implementacion del menu principal en streamlit, se adicionan botones y se definen opciones por cada boton que los llevara al controller
    def menu(self):
        st.title("Bienvenido al RHLMZoo 🐾👹")

        with st.sidebar:
            st.header("Elige una opcion:")

            botonCrearAnimal = st.button("Crear animal", key=1, use_container_width=True)
            botonCrearHabitat = st.button("Crear habitat", key=2, use_container_width=True)
            botonAgregarAnimalHabitat = st.button("Agregar animal a un habitat", key=3, use_container_width=True)
            botonListarAnimales = st.button("Listar animales por habitats", key=4,use_container_width=True)
            botonComidas = st.button("Controlar dietas", key=5,use_container_width=True)
            botonInteractuar = st.button("Interactuar con animales",key=6,use_container_width=True)

        if botonCrearAnimal:
            st.session_state["opcion"] = 1
        elif botonCrearHabitat:
            st.session_state["opcion"] = 2
        elif botonAgregarAnimalHabitat:
            st.session_state["opcion"] = 3
        elif botonListarAnimales:
            st.session_state["opcion"] = 4
        elif botonComidas:
            st.session_state["opcion"] = 5
        elif botonInteractuar:
            st.session_state["opcion"] = 6
        if "opcion" in st.session_state:
            self.controlador.ejecutarOpciones(st.session_state["opcion"])
#Menu que maneja la creacion del animal en el registro, este pide datos del animal y este retorna el animal creado
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
                nuevoAnimal = animalesModel.animales(idAnimal,nombre,edad,especie,habitat,claseDeAlimentacion,horasMinimasDormir,temperatura)
                st.success("Se creo el animal con exito")
                st.success("RECORDAR: ingresarlo en un habitat")
                return nuevoAnimal
#Menu de creacion de un habitat nueva, en este se le pediran datos al usuario para agregar un nuevo habitat cpn las especificaciones dadas y este retorna el habitat creada
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
            presenciaHieloNieve = st.slider("De que grado es la presencia de nieve y hielo en este habitat: ", min_value=0,max_value=10,step=1)
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
            if self.zoologico.obtenerHabitat(nombre,zoologico.habitats) == 1:
                self.mensaje_error("Lo sentimos, ya existe un habitat con el mismo nombre")
            else:
                if tipoDeHabitat == "Desertico":
                    nuevoHabitat = habitatModel.desertico(nombre,dieta,temperaturaMax,temperaturaMin,capacidad, "Desertico",escasezDeAgua,variacionDeTemperatura)
                elif tipoDeHabitat == "Acuatico":
                    nuevoHabitat = habitatModel.desertico(nombre,dieta,temperaturaMax,temperaturaMin,capacidad,"Acuatico",diversidadBiologica,presenciaAgua)
                elif tipoDeHabitat == "Polar":
                    nuevoHabitat = habitatModel.desertico(nombre,dieta,temperaturaMax,temperaturaMin,capacidad,"Polar",bajasTemperaturas,presenciaHieloNieve)
                elif tipoDeHabitat == "Selvatico":
                    nuevoHabitat = habitatModel.desertico(nombre,dieta,temperaturaMax,temperaturaMin,capacidad,"Selvatico",vegetacionDensa,biodiversidad)
                st.success("El habitat se agrego exitosamente")
                return nuevoHabitat

# en esta funcion definimos el menu de agregar un animal existente a un habitat existente, verificando que sea habitable para el animal, esta funcion maneja selectores de opciones en as cuales tiene respuesta inmediata
    def menu_agregar_animal_habitat(self,animales,habitats,zoologico):
        st.subheader("Menu para agregar animales a habitats")
        st.divider()
        with st.container():
            if len(animales) == 0:
                self.mensaje_error("No hay animales disponibles")
            else:
                obtenerAnimales = self.obtenerAnimal(animales)
                animalObtenido = st.selectbox("Animal que desea agregar: ", obtenerAnimales)
                animalSelec = animales[obtenerAnimales.index(animalObtenido)]
                datosA = pd.DataFrame(
                    [[animalSelec.id, animalSelec.nombreAnimal, animalSelec.habitat, animalSelec.claseAlimentacion, animalSelec.temperaturaAnimal]],
                    columns=["Id del animal", "Nombre", "Habitat", "Dieta", "Temperatura adaptativa"]
                )
                st.table(datosA)
                obtenerHabitas = self.obtenerHabitas(habitats)
                habitatObtenido = st.selectbox("Habitat al que desea agregar el animal: ", obtenerHabitas)
                habitatSelec = habitats[obtenerHabitas.index(habitatObtenido)]
                datosH = pd.DataFrame(
                    [[habitatSelec.nombreHabitat,habitatSelec.dieta,habitatSelec.temperaturaMax,habitatSelec.temperaturaMin,habitatSelec.capacidadAnimales]],
                    columns=["Nombre habitat", "dieta", "Temperatura maxima", "Temperatura minima", "Capacidad de habitat"]
                )
                st.table(datosH)
                if self.verificarAdaptabilidad(animalSelec,habitatSelec) == 1:
                    botonIngresarAnimal = st.button("Ingresar Animal al habitat")

                    if botonIngresarAnimal:
                        habitatSelec.agregarAnimalH(animalSelec)
                        zoologico.eliminarAnimal(animalSelec.id)

#En este menu listaremos los animales por habitat, siendo asi un selector de opciones de habitat existentes en el zoologico y este determinara si existen animales o no, en caso de que no, no aparece el botom de listar
    # y aparecera una alerta, de lo contrario se activara el boton y listara a los animales dentro de dicha habitat seleccionada
    def menu_listar_animales(self, animales,habitats, zoologico):
        st.subheader("Listado de animales por habitats")
        st.divider()
        with st.container():
            obtenerHabitas = self.obtenerHabitas(habitats)
            habitatObtenido = st.selectbox("Habitat que desea listar: ", obtenerHabitas)
            habitatSelec = habitats[obtenerHabitas.index(habitatObtenido)]
            if len(habitatSelec.animalesDic) == 0:
                self.mensaje_error("No hay animales para listar en este habitat")
            else:
                botonListarAnimales = st.button("Listar animales")
                if botonListarAnimales:
                    datosAnimales = pd.DataFrame(
                        self.controlador.aplicarFormatoA(habitatSelec.animalesDic.values()),
                        columns = ["ID animal", "Nombre", "Especie", "Tipo de habitat","Dieta", "Horas minimas que debe dormir"]
                    )
                    st.table(datosAnimales)
                    if habitatSelec.tipoHabitat == "Desertico":
                        st.text("Porcentaje de escasez de agua: {}%".format(habitatSelec.atributo1))
                        st.text("Porcentaje de temperatura variante: {}%".format(habitatSelec.atributo2))
                    if habitatSelec.tipoHabitat == "Acuatico":
                        st.text("Porcentaje de diversidad biologica: {}%".format(habitatSelec.atributo1))
                        st.text("Nivel de agua en este habitat: {}".format(habitatSelec.atributo2))
                    if habitatSelec.tipoHabitat == "Polar":
                        st.text("Probabilidad que este habitat sugra de bajas temperaturas: {}".format(habitatSelec.atributo1))
                        st.text("Grado de presencia de nieve y hielo: {}".format(habitatSelec.atributo2))
                    if habitatSelec.tipoHabitat == "Selvatico":
                        st.text("Porcentaje de densa vegetacion en el habitat: {}%".format(habitatSelec.atributo1))
                        st.text("Porcentaje de biodiversidad en el habitat: {}%".format(habitatSelec.atributo2))
    def menu_comidas(self, zoologico):
        st.subheader("Menu controlador de dietas")
        st.divider()
        with st.container():
            accion = st.selectbox("Seleccione la accion con los alimentos: ", zoologico.opcionesComida)

            if accion == "Agregar":
                st.subheader("Agregar Alimentos")
                tipoDieta = st.selectbox("Seleccione el tipo de dieta: ", zoologico.tiposAlimentacion)
                nuevoAlimento = st.text_input("Ingrese el alimento nuevo: ")
                if zoologico.obtenerAlimento(tipoDieta,nuevoAlimento) == 1:
                    self.mensaje_error("Esta alimento ya se encuentra en tu dieta")
                else:
                    botonAgregar = st.button("Agregar Alimento")
                    if botonAgregar:
                        zoologico.agregarComida(tipoDieta,nuevoAlimento)

            if accion == "Eliminar":
                st.subheader("Eliminar alimentos")
                tipoDieta = st.selectbox("Seleccione el tipo de dieta: ", zoologico.tiposAlimentacion)
                alimentoEliminar = st.selectbox("Seleccione el alimento a eliminar de la dieta: ", zoologico.alimentos[tipoDieta])
                botonEliminar = st.button("Eliminar alimento")
                if botonEliminar:
                    zoologico.eliminarComida(tipoDieta,alimentoEliminar)

            if accion == "Modificar":
                st.subheader("Modificar alimentos")
                tipoDieta = st.selectbox("Seleccione el tipo de dieta: ", zoologico.tiposAlimentacion)
                alimentoEliminar = st.selectbox("Seleccione el alimento a modificar de la dieta: ", zoologico.alimentos[tipoDieta])
                nuevoAlimento = st.text_input("Ingrese el nuevo alimento: ")
                if zoologico.obtenerAlimento(tipoDieta,nuevoAlimento) == 1:
                    self.mensaje_error("Esta alimento ya se encuentra en tu dieta")
                else:
                    botonModificar = st.button("Modificar alimento")
                    if botonModificar:
                        zoologico.eliminarComida(tipoDieta,alimentoEliminar)
                        time.sleep(2)
                        zoologico.agregarComida(tipoDieta,nuevoAlimento)



    def menu_acciones(self,habitats,zoologico):
        st.subheader("Haz acciones con nuestros animales")
        st.divider()
        with st.container():
            obtenerHabitas = self.obtenerHabitas(habitats)
            habitatObtenido = st.selectbox("Habitat que desea listar: ", obtenerHabitas)
            habitatSelec = habitats[obtenerHabitas.index(habitatObtenido)]
            if len(habitatSelec.animalesDic) == 0:
                self.mensaje_error("No hay animales para listar en este habitat")
            else:
                botonListarAnimales = st.button("Listar animales")
                if botonListarAnimales:
                    datosAnimales = pd.DataFrame(
                        self.controlador.aplicarFormatoB(habitatSelec.animalesDic.values()),
                        columns = ["ID animal", "Nombre","Dieta", "Horas minimas que debe dormir", "Disponibilidad de jugar"]
                    )
                    st.table(datosAnimales)
                    obtenerAnimales = self.obtenerAnimalH(habitatSelec.animalesDic)
                    animalObtenido = st.selectbox("Animal que desea agregar: ", obtenerAnimales)
                    animalSelec = habitatSelec[obtenerAnimales.index(animalObtenido)]
                    if animalSelec:
                        accion = st.selectbox("Seleccione la accion a ejecutar", zoologico.opcionesInteractuar)

                        if accion == "Dormir":
                            st.subheader("Menu hacer dormir al animal")

                        if accion == "Comer":
                            st.subheader("Menu alimentar al animal")

                        if accion == "Jugar":
                            st.subheader("Menu jugar con el animal")


#funciones de error de mensaje
    def mensaje_error(self,mensaje):
        st.error(mensaje)
# funcion que obtiene al animal para ser mostrado en los selecbox de la pagina
    def obtenerAnimal(self, animales):
        lista = []
        for animal in animales:
            animalTemp = "nombre: {} - especie: {}".format(animal.nombreAnimal, animal.especie)
            lista.append(animalTemp)
        return lista
    def obtenerAnimalH(self, habitats):
        lista = []
        for habitat in habitats:
            animalTemp = "nombre: {} - especie: {}".format(habitat.id, habitat.nombreAnimal)
            lista.append(animalTemp)
        return lista

#Funcion que obtiene habitat para ser mostrada en el selecbox de la pagina
    def obtenerHabitas(self, habitats):
        listaHabitats = []
        for habitat in habitats:
            habitatTemp = "Habitat: {}".format(habitat.nombreHabitat)
            listaHabitats.append(habitatTemp)
        return listaHabitats
#Funcion que verifica si el animal permite ser ingresado en dicha habitat seleccionada, este hace una verificacion uno a uno y retorna 0 en casos negativos y su respectivo motivo en mensaje de error
    #de lo contrario retorna 1 y aparece el boton en el cual deje ingresar al animal al habitat
    def verificarAdaptabilidad(self,animalSelec,habitatSelec):
        if animalSelec.habitat == habitatSelec.tipoHabitat:
            if animalSelec.claseAlimentacion == habitatSelec.dieta:
                if (animalSelec.temperaturaAnimal >= habitatSelec.temperaturaMin) and (animalSelec.temperaturaAnimal <= habitatSelec.temperaturaMax):
                    if len(habitatSelec.animalesDic) < habitatSelec.capacidadAnimales:
                        return 1
                    else:
                        self.mensaje_error("No hay suficiente capacidad")
                        return 0
                else:
                    self.mensaje_error("La temperatura del animal no se adecua")
                    return 0
            else:
                self.mensaje_error("La alimentacion del habitat no se adapta al animal")
                return 0
        else:
            self.mensaje_error("El animal no se adecua a este habitat")
            return 0

