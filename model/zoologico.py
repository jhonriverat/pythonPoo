import streamlit as st
import pandas as pd
class Zoologico():
    def __init__(self, idAnimal):
        if "idAnimal" in st.session_state:
            self.idAnimal = st.session_state["idAnimal"]
        else:
            self.idAnimal = idAnimal
            st.session_state["idAnimal"] = 0
        if "animales" in st.session_state:
            self.animales = st.session_state["animales"]
        else:
            self.animales = []
            st.session_state["animales"] = []
        if "habitats" in st.session_state:
            self.habitats = st.session_state["habitats"]
        else:
            self.habitats = []
            st.session_state["habitats"] = []
        if "alimentos" in st.session_state:
            self.alimentos = st.session_state["alimentos"]
        else:
            self.alimentos = {}
            self.alimentos["Herbivoro"] = ["aves","insectos","pescado"]
            self.alimentos["Omnivoro"] = ["hojas","corteza","frutos"]
            self.alimentos["Carnivoro"] = ["aves","insectos","pescado"]

        self.tiposHabitats = ["Polar","Selvatico","Acuatico","Desertico"]
        self.tiposAlimentacion = ["Carnivoro","Herbivoro","Omnivoro"]
        self.opcionesComida = ["Agregar","Eliminar","Modificar"]
        self.opcionesInteractuar = ["Dormir","Comer","Jugar"]


    def agregarAnimalZ(self,animal):
        self.animales.append(animal)
        self.idAnimal = self.idAnimal + 1
        st.session_state["idAnimal"] = self.idAnimal
        st.session_state["animales"] = self.animales
        return True
    def eliminarAnimal(self,idAnimal):
        del self.animales[idAnimal]
        st.session_state["animales"] = self.animales
        return True

    def agregarHabitat(self,habitat):
        self.habitats.append(habitat)
        st.session_state["habitats"] = self.habitats
        return True
    def agregarComida(self,tipoDieta,alimento):
        self.alimentos[tipoDieta].append(alimento)
        st.session_state["alimentos"] = self.alimentos
        st.success("Se agrego correctamente el alimento {} de la dieta {}".format(alimento,tipoDieta))

    def eliminarComida(self,tipoDieta,alimento):
        self.alimentos[tipoDieta].remove(alimento)
        st.session_state["alimentos"] = self.alimentos
        st.success("Se elimino correctamente el alimento {} de la dieta {}".format(alimento,tipoDieta))

    def obtenerAlimento(self,tipoDieta,alimento):
        cant = 0
        for alimentoOb in self.alimentos[tipoDieta]:
            if alimentoOb == alimento:
                cant += 1
        if cant > 0:
            return 1
        else:
            return 0

    def dormir(self, horasAnimal, horasUsuario):
        if horasUsuario >= horasAnimal:
            st.success("El animal logro dormir")
        else:
            st.error("Las horas no son suficientes para el animal, no lo lograste dormir")

    def obtenerHabitat(self,nombreHabitat,habitats):
        for habitat in habitats:
            if nombreHabitat == habitat.nombreHabitat:
                return 1
            else:
                return 0


