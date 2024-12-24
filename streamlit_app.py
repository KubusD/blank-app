import streamlit as st

def main():
    # Ustawienie białego tła i usunięcie menu
    st.set_page_config(
        layout="wide",
        page_title="Proxy Display",
        initial_sidebar_state="collapsed"
    )

    # Ukrycie domyślnych elementów Streamlit
    hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    # Pobranie parametrów z URL
    query_params = st.experimental_get_query_params()
    
    # Wyświetlenie parametrów
    for key, value in query_params.items():
        st.write(f"{key}: {value[0]}")

if __name__ == "__main__":
    main()