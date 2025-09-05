import streamlit as st

# --- Configuracion de Pagina ---
def configuraciones():
    st.set_page_config(
        page_title="CinemaRV",
        page_icon= "static/image/cinemarv_logo.png",
        initial_sidebar_state="collapsed"  # "expanded" o "auto" también son opciones
        )
    
    hide_footer_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    ._link_gzau3_10 {visibility: hidden;}
    ._profilePreview_gzau3_63 {visibility: hidden;}
    .reportview-container .main footer {visibility: hidden;}
    </style>
    """
    st.markdown(hide_footer_style, unsafe_allow_html=True)
    
    
    st.markdown(
    '<meta name="google-site-verification" content="iD53tEKNy4HKZzPMbhgjzjZtWopHedXzuDN9frfXOWI" />',
    unsafe_allow_html=True
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
    pg = st.navigation([pagina_1, pagina_3])

    return pg


if __name__ == "__main__":
    configuraciones()
    pg = paginas()
    pg.run()
    
    
    





