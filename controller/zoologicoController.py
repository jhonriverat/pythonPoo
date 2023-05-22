import streamlit as st
class zoologicoController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutarOpciones(self,opcion):
        if opcion == 1:
            try:
                nuevoAnimal = self.vista.menu_creacion_animal(self.modelo.idAnimal, self.modelo)
                if nuevoAnimal:
                    self.modelo.agregarAnimal(nuevoAnimal)
            except ValueError:
                self.vista.mostrar_mensaje_error("Se presento un error al crear el animal")

