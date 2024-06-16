import streamlit as st

def app():
    st.markdown(
    """
    <style>
        div[data-testid="column"]:nth-of-type(2)
        {
            text-align: left;
        }
        div[data-testid="column"]:nth-of-type(1)
        {
            display: flex;
            justify-content: flex-end;
        }
    </style>
    """,unsafe_allow_html=True
)
    c1, c2 = st.columns(2, gap="small")
    with c1:
        st.image("img/teste.gif")
    with c2:
        st.title("Cirrosifier")
        st.header("Classificando a Cirrose")
        st.markdown("Um projeto pela Trainees 1")
        st.markdown("Rotação 2024.1")

    st.markdown("---")