import streamlit as st

# --- Estilos globales ---
st.markdown("""
    <style>
    /* Fondo general */
    .stApp {
        background: linear-gradient(135deg, #0a0f29, #1a1f3d);
        color: #d6d9e0;
    }

    /* Títulos */
    h1 {
        font-size: 3.5em;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    h1 .cinema {
        color: #d6d9e0;
        text-shadow: 0 0 8px #5a78ff;
    }

    h1 .rv {
        background: linear-gradient(90deg, #5a78ff, #00ffff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 12px #00ffff, 0 0 24px #5a78ff;
        animation: glow 2s infinite alternate;
    }

    @keyframes glow {
        from { text-shadow: 0 0 8px #00ffff, 0 0 16px #5a78ff; }
        to   { text-shadow: 0 0 20px #00ffff, 0 0 40px #5a78ff; }
    }

    /* Texto normal */
    p, li, span {
        color: #d6d9e0 !important;
    }

    /* Botones */
    .stButton>button {
        background: linear-gradient(90deg, #5a78ff, #00ffff);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.6em 1.2em;
        font-weight: bold;
        box-shadow: 0 0 15px #5a78ff;
        transition: 0.3s;
    }
    .stButton>button:hover {
        box-shadow: 0 0 25px #00ffff;
        transform: scale(1.05);
    }

    /* Inputs (cajas de texto, selectores, etc.) */
    .stTextInput>div>div>input,
    .stSelectbox>div>div>div>div {
        background-color: #1a1f3d;
        color: #d6d9e0;
        border-radius: 8px;
        border: 1px solid #5a78ff;
    }
    </style>
""", unsafe_allow_html=True)


# Ocultar el menú principal, el footer y el botón flotante A REVISAR
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;} /* Menú hamburguesa */
    footer {visibility: hidden;}    /* Footer "Made with Streamlit" */
    header {visibility: hidden;}    /* Encabezado superior */
    .stActionButton {visibility: hidden;} /* Botón flotante de Streamlit */
    </style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)



# --- HERO con título custom ---
st.markdown(
    """
    <div style='text-align: center; padding: 40px 0;'>
        <h1>
            <span class="cinema">CINEMA</span><span class="rv">RV</span>
        </h1>
        <p style='font-size: 1.4em;'>
            No es solo ver la peli, es <b>vivirla con tus amigos</b> desde cualquier lugar del mundo
        </p>
    </div>
    """,
    unsafe_allow_html=True
)



video = "static/video/cinemarv.mp4"

# Video reproducido con st.video
st.video(video)

st.markdown("---")


# --- PÚBLICO OBJETIVO ---
st.subheader("¿A quién está dirigido?")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 👥 Comunidad online")
    st.markdown("Amigos o parejas distanciados que buscan opciones inmersivas para compartir cine juntos.")

with col2:
    st.markdown("### 🎮 Jóvenes & Usuarios VR")
    st.markdown("Buscan experiencias nuevas: inmersivas, sociales, dinámicas y originales.")

with col3:
    st.markdown("### 💼 Empresas")
    st.markdown("Alianzas para publicidades, merchandising y espacios temáticos en salas virtuales.")

st.markdown("---")


# --- VALOR AGREGADO ---
st.subheader("Valor agregado de CinemaRV")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    - Catálogo actualizado según la cartelera oficial de **Cinemark**.  
    - Puntos, recompensas y logros por mirar películas o comprar productos.  
    - Merch oficial, snacks y cupones de descuento en cines físicos.  
    """)

with col2:
    st.markdown("""
    - Personalización de avatares y salas según tus gustos.  
    - Experiencia social en tiempo real con amigos.  
    - Mayor accesibilidad sin perder la emoción del cine.  
    """)

st.markdown("---")

# --- FEATURES ---
st.subheader("Características principales")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🎭 Salas temáticas privadas")
    st.markdown("Ej: estética *Star Wars* con trajes temáticos de personajes.")

with col2:
    st.markdown("### 🕹️ Avatares y skins exclusivos")
    st.markdown("Expresá tu estilo dentro de la experiencia VR.")

with col3:
    st.markdown("### 😍 Reacciones en vivo")
    st.markdown("Emojis, micrófono, gestos, like/dislike para compartir emociones.")

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("### 💳 Microtransacciones")
    st.markdown("Compra skins, snacks virtuales y más dentro de la app.")

with col5:
    st.markdown("### ⭐ Membresía con puntos")
    st.markdown("Recompensas y beneficios exclusivos para miembros frecuentes.")

with col6:
    st.markdown("### 📢 Publicidad interactiva")
    st.markdown("Espacios para marcas de snacks, bebidas y merchandising.")

st.markdown("---")

# --- MODELO DE NEGOCIO ---
st.subheader("Modelo de negocio")
st.markdown("""
- **Pay Per View:** Pagar entrada como en el cine físico.  
- **Membresía / Suscripción:** Acceso ilimitado a salas públicas y privadas + beneficios.  
- **Publicidad & Alianzas:** Marcas de snacks, bebidas y merchandising dentro de la experiencia.  
- **Gamificación:** recolecta puntos ⭐ para desbloquear logros y premios.  
""")

st.markdown("---")

# --- TESTIMONIAL ---
st.subheader("Lo que dicen nuestros usuarios")
st.markdown(
    """
    > *“Es como estar en un cine real, pero con la magia de la realidad virtual. Una experiencia increíble.”*  
    **– Beta tester de CinemaRV**
    """
)

st.markdown("---")

# --- CTA: Apoyar/Inversión ---
st.markdown(
    """
    <div style='text-align: center; padding: 40px;'>
        <h2>¿Querés ser parte del cine del futuro?</h2>
        <p>Apoyanos y sé parte de la experiencia CinemaRV desde el inicio.</p>
        <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank">
            <button style='background: linear-gradient(90deg,#ff424d,#f96825); color:white; 
                           padding:15px 30px; font-size:20px; border:none; border-radius:10px;
                           box-shadow: 0 0 15px #ff424d; cursor:pointer;'>
                Apoyar CinemaRV
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)



# --- ACERCA DE NOSOTROS ---
st.markdown("---")
st.subheader("Acerca de nosotros")
st.markdown("""
**CinemaRV** nace con la misión de transformar la forma en que vivimos el cine.  
Nuestro objetivo es llevar la experiencia de la pantalla grande al metaverso, 
uniendo innovación tecnológica con la emoción de compartir una película con amigos, sin importar la distancia.  

🎯 **Misión:** democratizar el acceso al cine inmersivo en VR.  
🚀 **Visión:** ser pioneros en experiencias digitales de entretenimiento en Latinoamérica.  
💡 **Valores:** innovación, accesibilidad y conexión social.
""")

# --- EQUIPO ---
st.subheader("Nuestro equipo")

# Organizamos en dos filas de 3 integrantes
row1 = st.columns(3)
row2 = st.columns(3)

# --- FILA 1 ---
with row1[0]:
    st.markdown(
        """
        <div style="border:1px solid #ddd; border-radius:10px; padding:20px; text-align:center; 
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <img src="https://via.placeholder.com/150" style="border-radius:50%; margin-bottom:10px;">
            <h4>Cardoso, Tomas Francisco</h4>
            <p style="color:gray;">tcardoso@uade.edu.ar</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with row1[1]:
    st.markdown(
        """
        <div style="border:1px solid #ddd; border-radius:10px; padding:20px; text-align:center; 
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <img src="https://via.placeholder.com/150" style="border-radius:50%; margin-bottom:10px;">
            <h4>Carle, Santiago</h4>
            <p style="color:gray;">sacarle@uade.edu.ar</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with row1[2]:
    st.markdown(
        """
        <div style="border:1px solid #ddd; border-radius:10px; padding:20px; text-align:center; 
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <img src="https://media.licdn.com/dms/image/v2/D4D03AQGckbHJt1p9yw/profile-displayphoto-shrink_200_200/B4DZZa1GXoGgAc-/0/1745280592278?e=1759968000&v=beta&t=Xd2EmioWghR-bJtiWzuAlz60wHdkEOLDqDbUN0y8fJM" style="border-radius:50%; margin-bottom:10px;">
            <h4>Carusso, David Ismael</h4>
            <p style="color:gray;">dcarusso@uade.edu.ar</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- FILA 2 ---
with row2[0]:
    st.markdown(
        """
        <div style="border:1px solid #ddd; border-radius:10px; padding:20px; text-align:center; 
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <img src="https://via.placeholder.com/150" style="border-radius:50%; margin-bottom:10px;">
            <h4>Cáceres, Mariana</h4>
            <p style="color:gray;">mariancaceres@uade.edu.ar</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with row2[1]:
    st.markdown(
        """
        <div style="border:1px solid #ddd; border-radius:10px; padding:20px; text-align:center; 
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <img src="https://via.placeholder.com/150" style="border-radius:50%; margin-bottom:10px;">
            <h4>Córdoba Bourilhon, Micaela</h4>
            <p style="color:gray;">micordoba@uade.edu.ar</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with row2[2]:
    st.markdown(
        """
        <div style="border:1px solid #ddd; border-radius:10px; padding:20px; text-align:center; 
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <img src="https://via.placeholder.com/150" style="border-radius:50%; margin-bottom:10px;">
            <h4>Di Yorio, Juan</h4>
            <p style="color:gray;">jdiyorio@uade.edu.ar</p>
        </div>
        """,
        unsafe_allow_html=True
    )