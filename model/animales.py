import streamlit as st

class animales():
    def __init__(self,id,nombreAnimal,edad,especie,habitat,claseAlimentacion, horasMinimasDormir,horasDormidas = 0, yaJugo = False):
        self._id = id
        self._nombreAnimal = nombreAnimal
        self._edad = edad
        self._especie = especie
        self._habitat = habitat
        self._claseAlimentacion = claseAlimentacion
        self._horasMinimasDormir = horasMinimasDormir
        self._arregloCarnivoro = ["aves","insectos","pescado"]
        self._arregloHerbivoro = ["hojas","corteza","frutos"]
        self._arregloOmnivoro = ["pescado","hojas","aves"]


