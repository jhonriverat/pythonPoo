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
                self.vista.mensaje_error("Se presento un error al crear el animal")

        if opcion == 2:
             try:
                 nuevoHabitat = self.vista.menu_creacion_habitat(self.modelo)
                 if nuevoHabitat:
                     self.modelo.agregarHabitat(nuevoHabitat)
             except ValueError:
                 self.vista.mensaje_error("Se presento un error al crear el habitat")

        if opcion == 3:
            self.vista.menu_agregar_animal_habitat(self.modelo.animales,self.modelo.habitats,self.modelo)

