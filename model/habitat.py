import streamlit as st
import model.animales as animales
class habitat():
    def __init__(self,temperaturaMin,temperaturaMax,capacidadAnimales):
        self._temperaturaMin = temperaturaMin
        self._temperaturaMax = temperaturaMax
        self._capacidadAnimales = capacidadAnimales
        self._cantidadAnimales = 0
        self._animalesMap = {}
        # self._arregloHabitas = []
        # self._arregloDesertico = []
        # self._arregloAcuatico = []
        # self._arregloPolar = []
        # self._arregloSelvatico = []

    def agregarAnimal(self,animales):
        tempId = animales._id
        self._animalesMap[tempId] = animales
        self._cantidadAnimales += 1

    def eliminarAnimal(self,id):
        self._animalesMap.pop(id)
        self._cantidadAnimales -= 1




class desertico(habitat):
    def __init__(self, temperaturaMin, temperaturaMax, cantidadAnimales,atributo1,atributo2):
        super().__init__(temperaturaMin,temperaturaMax,cantidadAnimales)
        self._atributo1 = atributo1
        self._atributo2 = atributo2

class acuatico(habitat):
    def __init__(self, temperaturaMin, temperaturaMax, cantidadAnimales, atributo1, atributo2):
        super().__init__(temperaturaMin, temperaturaMax, cantidadAnimales)
        self._atributo1 = atributo1
        self._atributo2 = atributo2

class polar(habitat):
    def __init__(self, temperaturaMin, temperaturaMax, cantidadAnimales, atributo1, atributo2):
        super().__init__(temperaturaMin, temperaturaMax, cantidadAnimales)
        self._atributo1 = atributo1
        self._atributo2 = atributo2

class selvatico(habitat):
    def __init__(self, temperaturaMin, temperaturaMax, cantidadAnimales, atributo1, atributo2):
        super().__init__(temperaturaMin, temperaturaMax, cantidadAnimales)
        self._atributo1 = atributo1
        self._atributo2 = atributo2
