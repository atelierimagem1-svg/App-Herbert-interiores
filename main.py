import streamlit as st

# Configuração da página
st.set_page_config(page_title="Herbert Martins - Design & IA", layout="wide")

# Aplicação da sua Paleta de Cores via CSS
st.markdown(f"""
    <style>
    .stApp {{ background-color: #FAFAFA; }}
    [data-testid="stSidebar"] {{ background-color: #2C3E50; }}
    [data-testid="stSidebar"] * {{ color: #EDE3D9 !important; }}
    h1, h2, h3 {{ color: #2C3E50; font-family: 'Segoe UI', sans-serif; }}
    .stButton>button {{
        background-color: #A7B6A7;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        border: none;
    }}
    .stExpander {{ background-color: white; border-radius: 10px; border: 1px solid #EDE3D9; }}
    </style>
    """, unsafe_allow_html=True)

# Sidebar com sua Logo
with st.sidebar:
    # Tentativa de link direto da sua logo no GitHub
    st.image("https://raw.githubusercontent.com/atelierimagem1-svg/App-Herbert-interiores/main/MARCA%20COMPLETA%20HM.png)
    st.markdown("---")
    menu = st.radio("MENU", ["✨ Meus Projetos", "🛒 Shopping List", "🤖 IA Style Consultant"])

# --- LÓGICA DE NAVEGAÇÃO ---

if menu == "✨ Meus Projetos":
    st.title("🖼 Meus Projetos: Residência Alpha")
    st.write("Acompanhe a evolução do seu sonho.")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Sala de Estar - Render Final")
        st.image("https://images.unsplash.com/photo-1618221195710-dd6b41faaea6")
    with col2:
        st.subheader("Documentação Técnica")
        st.info("Clique no botão abaixo para acessar o caderno técnico.")
        st.button("Download Planta.pdf")

elif menu == "🛒 Shopping List":
    st.title("🛒 Curadoria de Itens")
    st.write("Especificações de materiais e mobiliário.")
    st.table({
        "Item": ["Sofá Minimalista", "Pendente Bronze", "Revestimento Amadeirado"],
        "Marca": ["Loja X", "Marca Y", "Portobello"],
        "Status": ["Aprovado", "Pendente", "Em Orçamento"]
    })

elif menu == "🤖 IA Style Consultant":
    st.title("🤖 Consultoria de Estilo com IA")
    st.info("Copie os prompts abaixo e utilize em ferramentas como Midjourney ou Adobe Firefly para explorar variações.")
    
    with st.expander("🌟 Estilo Japandi (O escolhido para seu projeto)"):
        st.write("Ideal para testar variações de iluminação e texturas naturais.")
        st.code("Interior design of a living room, Japandi style, neutral tones, light oak wood furniture, minimalist aesthetic, soft sunlight, 8k resolution.")
        
    with st.expander("🌿 Estilo Contemporâneo Relax"):
        st.write("Use para ver como o ambiente fica com mais plantas e tons terrosos.")
        st.code("Modern living room, earth tones, linen textures, many indoor plants, large windows, cozy atmosphere, photorealistic.")

    with st.expander("🌙 Versão Noturna (Mood Lighting)"):
        st.write("Veja como seu espaço se comporta com iluminação artificial quente.")
        st.code("Living room interior, night time, warm indirect LED lighting, moody atmosphere, elegant shadows, cinematic lighting.")

    st.warning("Dica do Prof. Herbert: Ao usar a IA, você pode trocar cores no texto (ex: trocar 'neutral' por 'sage green') para ver novas possibilidades!")
