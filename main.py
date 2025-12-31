import streamlit as st

# 1. Configuração da Página e Estilo (CSS Personalizado)
st.set_page_config(page_title="Herbert Martins | Design & IA", layout="wide")

st.markdown("""
    <style>
    /* Fundo e Cores Globais */
    .stApp {
        background-color: #F8F9FA;
    }
    /* Barra Lateral */
    [data-testid="stSidebar"] {
        background-color: #1A1A1A;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    /* Títulos e Botões */
    h1, h2, h3 {
        color: #2C3E50;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stButton>button {
        background-color: #D4AF37; /* Dourado */
        color: white;
        border-radius: 5px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Barra Lateral com sua Logo
with st.sidebar:
    # Substitua o link abaixo pelo link direto da sua imagem/logo
    st.image("https://seu-site.com.br/sua-logo.png", width=200) 
    st.markdown("---")
    menu = st.radio("Navegação Exclusiva", ["✨ Meus Projetos", "🛒 Shopping List", "🏗️ Diário de Obra", "🤖 IA Style Consultant"])

# 3. Conteúdo das Abas
if menu == "✨ Meus Projetos":
    st.title("Residência Alpha")
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Living Room - Render 3D")
        # Coloque o link da sua imagem real aqui
        st.image("https://images.unsplash.com/photo-1618221195710-dd6b41faaea6", caption="Visualização em Alta Definição")
    with col2:
        st.subheader("Planta Executiva")
        st.info("O detalhamento técnico está pronto para sua revisão.")
        st.button("📄 Baixar Projeto Completo (PDF)")

elif menu == "🛒 Shopping List":
    st.title("Seleção de Mobiliário e Acabamentos")
    st.write("Itens curados especificamente para seu estilo.")
    items = [
        {"Item": "Sofá Design", "Marca": "Artefacto", "Status": "Aprovado"},
        {"Item": "Luminária Pendente", "Marca": "Lumini", "Status": "Aguardando"},
        {"Item": "Piso Calacatta", "Marca": "Portobello", "Status": "Em Trânsito"}
    ]
    st.table(items)

elif menu == "🤖 IA Style Consultant":
    st.title("Consultoria com IA")
    st.write("Use os **Prompts de Ouro** do Prof. Herbert para explorar novas variações para seus ambientes.")
    prompt_escolhido = st.selectbox("Escolha um ambiente para testar:", ["Sala Japandi", "Cozinha Industrial", "Quarto Spa"])
    st.code("Copiado! Agora cole na sua ferramenta de IA preferida.")
