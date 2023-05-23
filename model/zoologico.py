import streamlit as st
import pandas as pd
class Zoologico():
    def __init__(self, idAnimal):
        if "idAnimal" in st.session_state:
            self.idAnimal = st.session_state["idAnimal"]
        else:
            self.idAnimal = 0
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

        self.tiposHabitats = ["Polar","Selvatico","Acuatico","Desertico"]
        self.tiposAlimentacion = ["Carnivoro","Herbivoro","Omnivoro"]


    def agregarAnimal(self,animal):
        self.animales.append(animal)
        st.session_state["idAnimal"] = self.idAnimal
        st.session_state["animales"] = self.animales
        self.idAnimal += 1
        return True
    def eliminarAnimal(self,idAnimal):
        del self.animales[idAnimal]
        st.session_state["animales"] = self.animales
        return True

    def agregarHabitat(self,habitat):
        self.habitats.append(habitat)
        st.session_state["habitats"] = self.habitats
        return True

    def obtenerHabitat(self,nombreHabitat,habitats):
        for habitat in habitats:
            if nombreHabitat == habitat._nombreHabitat:
                return 1
            else:
                return 0
