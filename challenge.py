import streamlit as st
from streamlit_option_menu import option_menu

# Données des utilisateurs en dur dans le code
users_data = {
    "root": {
        "password": "rootMDP",
        "email": "root@gmail.com",
        "failed_login_attempts": 0,
        "logged_in": False,
        "role": "administrateur"
    },
    "utilisateur": {
        "password": "userMDP",
        "email": "user@gmail.com",
        "failed_login_attempts": 0,
        "logged_in": False,
        "role": "utilisateur"
    }
}

# Fonction d'authentification
def authenticate(username, password):
    if username in users_data:
        user = users_data[username]
        if user["password"] == password:
            users_data[username]["logged_in"] = True
            return True
        else:
            users_data[username]["failed_login_attempts"] += 1
            return False
    return False

# Afficher la page d'authentification
def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username and password:
            if authenticate(username, password):
                st.session_state["username"] = username
                st.session_state["logged_in"] = True
                st.success("Connexion réussie !")
            else:
                st.error("Nom d'utilisateur ou mot de passe incorrect")
        else:
            st.warning("Les champs username et mot de passe doivent être remplis")

# Page d'accueil pour les utilisateurs connectés
def home_page():
    st.title("Bienvenue sur ma page")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=300)
    st.markdown("Bienvenue sur ma page d'accueil !")
    
# Page des photos de chat
def photo_page():
    st.title("Les photos de mon chat")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("https://static.streamlit.io/examples/cat.jpg", caption="Chat 1")
    with col2:
        st.image("https://static.streamlit.io/examples/cat.jpg", caption="Chat 2")
    with col3:
        st.image("https://static.streamlit.io/examples/cat.jpg", caption="Chat 3")
        
# Déconnexion
def logout():
    st.session_state["logged_in"] = False
    st.session_state["username"] = None
    st.success("Vous êtes déconnecté !")

# Structure de la sidebar et du menu
def sidebar_menu():
    if st.session_state.get("logged_in"):
        menu = option_menu(
            menu_title=None,
            options=["Accueil", "Les photos de mon chat"],
            icons=["house", "cat"],
            default_index=0,
            orientation="vertical",
        )
        
        if menu == "Accueil":
            home_page()
        elif menu == "Les photos de mon chat":
            photo_page()

        # Affichage du message de bienvenue et du bouton de déconnexion
        st.sidebar.write(f"Bienvenue {st.session_state['username']}")
        if st.sidebar.button("Déconnexion"):
            logout()
    else:
        login_page()

# Fonction principale
def main():
    # Vérifier si l'utilisateur est connecté
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    
    # Affichage du menu
    sidebar_menu()

if __name__ == "__main__":
    main()
