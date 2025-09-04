# --- CSS para mejorar los botones ---
st.markdown(
    """
    <style>
    div.stButton > button {
        width: 120px;      /* ancho fijo */
        height: 50px;      /* alto fijo */
        font-size: 16px;   /* tamaño del texto */
        white-space: nowrap; /* evitar salto de línea */
    }
    </style>
    """,
    unsafe_allow_html=True
)s

carrusel = [
   "static/image/1.png"  ,
   "static/image/2.png"  ,
   "static/image/3.png"  ,
   "static/image/4.png"  , 
   "static/image/5.png"  
]


if "index" not in st.session_state:
    st.session_state.index = 0

# Mostrar imagen actual
st.image(carrusel[st.session_state.index], use_container_width=True)

# 3 columnas: left - spacer - right
left_col, spacer, right_col = st.columns([1, 6, 1])

with left_col:
    if st.button("⬅️ Anterior"):
        st.session_state.index = (st.session_state.index - 1) % len(carrusel)

with right_col:
    if st.button("Siguiente ➡️"):
        st.session_state.index = (st.session_state.index + 1) % len(carrusel)
