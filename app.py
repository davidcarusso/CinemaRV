import streamlit as st

# --- Configuracion de Pagina ---
def configuraciones():
    st.set_page_config(
        page_title="CinemaRV",
        #page_icon= "" ,
        initial_sidebar_state="expanded"
)
    
# --- Crea el objeto pagina para luego agrupparlos --- 
def paginas():

    pagina_1 = st.Page(
    page= "views/pag_home.py",
    title="Home",
    default=True
    )
        
    pagina_2= st.Page(
    page="views/pag_presentacion.py",
    title="Presentación"
    )

    pagina_3 = st.Page(
    page= "views/pag_negocio.py",
    title= "Plan de Negocio"
    )
    
    # --- Crear un diccionario para agrupar en un indice --- 
    pages =  {
    "Inicio" : [pagina_2] , 
    "Plan de Negocios" : [pagina_1 , pagina_3]
    }

    # --- Crea el objeto multipagina --- 
    pg = st.navigation([pagina_1, pagina_2, pagina_3])

    return pg


if __name__ == "__main__":
    configuraciones()
    pg = paginas()
    pg.run()
    
    
    





