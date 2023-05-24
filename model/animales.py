import streamlit as st

class animales():
    def __init__(self,id,nombreAnimal,edad,especie,habitat,claseAlimentacion, horasMinimasDormir,temperaturaAnimal,horasDormidas = 0, yaJugo = False):
        self.id = id
        self.nombreAnimal = nombreAnimal
        self.edad = edad
        self.especie = especie
        self.habitat = habitat
        self.claseAlimentacion = claseAlimentacion
        self.horasMinimasDormir = horasMinimasDormir
        self.temperaturaAnimal = temperaturaAnimal
        self.yaJugo = yaJugo
        self.arregloCarnivoro = ["aves","insectos","pescado"]
        self.arregloHerbivoro = ["hojas","corteza","frutos"]
        self.arregloOmnivoro = ["pescado","hojas","aves"]



