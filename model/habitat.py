import streamlit as st
import model.animales as animales
class habitat():
    def __init__(self,nombreHabitat,dieta,temperaturaMax,temperaturaMin,capacidadAnimales, tipoHabitat):
        self.nombreHabitat = nombreHabitat
        self.temperaturaMax = temperaturaMax
        self.temperaturaMin = temperaturaMin
        self.capacidadAnimales = capacidadAnimales
        self.dieta = dieta
        self.cantidadAnimales = 0
        self.tipoHabitat = tipoHabitat
        self.animalesDic = {}
        # self._arregloHabitas = []
        # self._arregloDesertico = []
        # self._arregloAcuatico = []
        # self._arregloPolar = []
        # self._arregloSelvatico = []

    def agregarAnimalH(self,animales):
        tempId = animales.id
        self.animalesDic[tempId] = animales
        self.cantidadAnimales += 1
        st.success("Se agrego correctamente al animal al habitat")

    def eliminarAnimal(self,id):
        self.animalesDic.pop(id)
        self.cantidadAnimales -= 1




class desertico(habitat):
    def __init__(self,nombreHabitat,dieta,temperaturaMax,temperaturaMin ,cantidadAnimales,tipoHabitat,atributo1,atributo2):
        super().__init__(nombreHabitat,dieta,temperaturaMax,temperaturaMin,cantidadAnimales,tipoHabitat)
        self.atributo1 = atributo1
        self.atributo2 = atributo2

class acuatico(habitat):
    def __init__(self,nombreHabitat,dieta,temperaturaMax,temperaturaMin, cantidadAnimales,tipoHabitat,atributo1,atributo2):
        super().__init__(nombreHabitat,dieta,temperaturaMax,temperaturaMin,cantidadAnimales,tipoHabitat)
        self.atributo1 = atributo1
        self.atributo2 = atributo2

class polar(habitat):
    def __init__(self,nombreHabitat,dieta,temperaturaMax,temperaturaMin, cantidadAnimales,tipoHabitat,atributo1,atributo2):
        super().__init__(nombreHabitat,dieta,temperaturaMax,temperaturaMin,cantidadAnimales,tipoHabitat)
        self.atributo1 = atributo1
        self.atributo2 = atributo2

class selvatico(habitat):
    def __init__(self,nombreHabitat,dieta,temperaturaMax,temperaturaMin, cantidadAnimales,tipoHabitat,atributo1,atributo2):
        super().__init__(nombreHabitat,dieta,temperaturaMax,temperaturaMin,cantidadAnimales,tipoHabitat)
        self.atributo1 = atributo1
        self.atributo2 = atributo2
