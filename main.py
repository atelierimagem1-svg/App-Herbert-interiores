import streamlit as st

st.set_page_config(page_title="Herbert Martins - Design Experience", layout="wide")

# Sidebar com informações do profissional
st.sidebar.title("Herbert Martins")
st.sidebar.write("Design de Interiores | 3D Art")
st.sidebar.image("https://via.placeholder.com/150") # Link para sua foto ou logo

# Menu de Navegação
menu = st.sidebar.radio("Navegar", ["Meus Projetos", "Shopping List", "Diário de Obra"])

if menu == "Meus Projetos":
    st.title("🖼 Meus Projetos: Residência Alpha")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Sala de Estar - Render 3D")
        st.image("https://via.placeholder.com/600x400", caption="Estilo Japandi Moderno")
    with col2:
        st.subheader("Planta Baixa")
        st.info("O arquivo PDF da planta executiva está disponível para download abaixo.")
        st.button("Download Planta.pdf")

elif menu == "Shopping List":
    st.title("🛒 Lista de Especificações")
    st.table({
        "Item": ["Sofá Minimalista", "Pendente Bronze", "Revestimento Amadeirado"],
        "Marca": ["Loja X", "Marca Y", "Portobello"],
        "Status": ["Aprovado", "Pendente", "Em Orçamento"]
    })

elif menu == "Diário de Obra":
    st.title("🏗 Acompanhamento da Obra")
    st.progress(65)
    st.write("Fase atual: Instalação de iluminação e marcenaria.")
