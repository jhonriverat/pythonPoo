import streamlit as st
import view.zoologicoView as ZoologicoView

def main():
    st.set_page_config(
        page_title="RHLM",
        layout="wide"
    )
    zoologico = ZoologicoView.zoologicoView()
    zoologico.menu()
main()



