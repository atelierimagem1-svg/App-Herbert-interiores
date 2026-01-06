import streamlit as st

# Configuração da página
st.set_page_config(page_title="Herbert Martins - Design & IA", layout="wide")

# Aplicação da sua Paleta de Cores via CSS
st.markdown(f"""
    <style>
    .stApp {{ background-color: #F7F7F5; }}
    [data-testid="stSidebar"] {{ background-color: #2C3E50; padding-top: 2rem; }}
    [data-testid="stSidebar"] * {{ color: #EDE3D9 !important; }}
    h1, h2, h3 {{ color: #2C3E50; font-family: 'Segoe UI', sans-serif; }}
    h1 {{ font-size: 2.5rem; }}
    p, li, span {{ color: #4E5D6C; }}
    .section-title {{ font-size: 1.4rem; font-weight: 600; margin-bottom: 0.5rem; }}
    .hero {{
        background: linear-gradient(135deg, #EDE3D9 0%, #F7F7F5 60%);
        border-radius: 18px;
        padding: 2rem 2.5rem;
        box-shadow: 0 12px 30px rgba(44, 62, 80, 0.08);
        margin-bottom: 2rem;
    }}
    .hero h1 {{ margin-bottom: 0.4rem; }}
    .hero span {{
        display: inline-block;
        background: rgba(44, 62, 80, 0.12);
        color: #2C3E50;
        padding: 0.25rem 0.75rem;
        border-radius: 999px;
        font-size: 0.85rem;
        margin-top: 0.5rem;
    }}
    .card {{
        background-color: white;
        border-radius: 16px;
        border: 1px solid #E9E2DA;
        padding: 1.5rem;
        box-shadow: 0 10px 24px rgba(44, 62, 80, 0.06);
    }}
    .card-title {{ font-size: 1.1rem; font-weight: 600; color: #2C3E50; margin-bottom: 0.4rem; }}
    .card-subtitle {{ color: #7B8A97; font-size: 0.95rem; }}
    .badge {{
        display: inline-block;
        background: #A7B6A7;
        color: white;
        padding: 0.2rem 0.6rem;
        border-radius: 999px;
        font-size: 0.8rem;
        margin-right: 0.4rem;
    }}
    .stButton>button {{
        background-color: #2C3E50;
        color: white;
        border-radius: 10px;
        padding: 0.6rem 2.2rem;
        border: none;
        transition: all 0.2s ease;
        box-shadow: 0 6px 16px rgba(44, 62, 80, 0.2);
    }}
    .stButton>button:hover {{
        background-color: #1F2E3A;
        transform: translateY(-1px);
    }}
    .stExpander {{
        background-color: white;
        border-radius: 12px;
        border: 1px solid #EDE3D9;
        box-shadow: 0 6px 16px rgba(44, 62, 80, 0.05);
    }}
    .table-wrap {{
        background: white;
        border-radius: 16px;
        padding: 1rem 1.5rem;
        border: 1px solid #EDE3D9;
        box-shadow: 0 10px 24px rgba(44, 62, 80, 0.06);
    }}
    .table-wrap table {{
        width: 100%;
        border-collapse: collapse;
        font-size: 0.95rem;
    }}
    .table-wrap th {{ text-align: left; color: #2C3E50; padding-bottom: 0.6rem; }}
    .table-wrap td {{ padding: 0.5rem 0; border-bottom: 1px solid #F0E9E2; }}
    .status-approved {{ color: #2C3E50; font-weight: 600; }}
    .status-pending {{ color: #B58B2A; font-weight: 600; }}
    .status-budget {{ color: #4C8AA3; font-weight: 600; }}
    </style>
    """, unsafe_allow_html=True)

# Sidebar com sua Logo
with st.sidebar:
    # Tentativa de link direto da sua logo no GitHub
    st.image("https://raw.githubusercontent.com/atelierimagem1-svg/App-Herbert-interiores/main/MARCA%20COMPLETA%20HM.png")
    st.markdown("---")
    menu = st.radio("MENU", ["✨ Meus Projetos", "🛒 Shopping List", "🤖 IA Style Consultant"])

# --- LÓGICA DE NAVEGAÇÃO ---

if menu == "✨ Meus Projetos":
    st.markdown("""
        <div class="hero">
            <h1>🖼 Residência Alpha</h1>
            <p>Acompanhe a evolução do seu sonho com entregas organizadas e visão clara.</p>
            <span>Projeto em andamento • Atualizado semanalmente</span>
        </div>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div class="card">
                <div class="card-title">Sala de Estar</div>
                <div class="card-subtitle">Render final aprovado</div>
            </div>
        """, unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1618221195710-dd6b41faaea6", width="stretch")
    with col2:
        st.markdown("""
            <div class="card">
                <div class="card-title">Documentação Técnica</div>
                <div class="card-subtitle">Plantas e detalhamentos executivos</div>
            </div>
        """, unsafe_allow_html=True)
        st.info("Clique no botão abaixo para acessar o caderno técnico.")
        st.button("Download Planta.pdf")
    with col3:
        st.markdown("""
            <div class="card">
                <div class="card-title">Próximas entregas</div>
                <p class="card-subtitle">Itens programados para a próxima revisão.</p>
                <p><span class="badge">20/09</span> Revisão da marcenaria</p>
                <p><span class="badge">27/09</span> Iluminação decorativa</p>
                <p><span class="badge">04/10</span> Curadoria final</p>
            </div>
        """, unsafe_allow_html=True)

elif menu == "🛒 Shopping List":
    st.markdown("""
        <div class="hero">
            <h1>🛒 Curadoria de Itens</h1>
            <p>Especificações completas de materiais e mobiliário com status atualizado.</p>
            <span>Última atualização • Hoje</span>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="table-wrap">
            <table>
                <thead>
                    <tr>
                        <th>Item</th>
                        <th>Marca</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Sofá Minimalista</td>
                        <td>Loja X</td>
                        <td class="status-approved">Aprovado</td>
                    </tr>
                    <tr>
                        <td>Pendente Bronze</td>
                        <td>Marca Y</td>
                        <td class="status-pending">Pendente</td>
                    </tr>
                    <tr>
                        <td>Revestimento Amadeirado</td>
                        <td>Portobello</td>
                        <td class="status-budget">Em orçamento</td>
                    </tr>
                </tbody>
            </table>
        </div>
    """, unsafe_allow_html=True)

elif menu == "🤖 IA Style Consultant":
    st.markdown("""
        <div class="hero">
            <h1>🤖 Consultoria de Estilo com IA</h1>
            <p>Copie os prompts abaixo e utilize em ferramentas como Midjourney ou Adobe Firefly para explorar variações.</p>
            <span>Pronto para testar novos moods</span>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        with st.expander("🌟 Estilo Japandi (O escolhido para seu projeto)"):
            st.write("Ideal para testar variações de iluminação e texturas naturais.")
            st.code("Interior design of a living room, Japandi style, neutral tones, light oak wood furniture, minimalist aesthetic, soft sunlight, 8k resolution.")
    with col2:
        with st.expander("🌿 Estilo Contemporâneo Relax"):
            st.write("Use para ver como o ambiente fica com mais plantas e tons terrosos.")
            st.code("Modern living room, earth tones, linen textures, many indoor plants, large windows, cozy atmosphere, photorealistic.")
    with col3:
        with st.expander("🌙 Versão Noturna (Mood Lighting)"):
            st.write("Veja como seu espaço se comporta com iluminação artificial quente.")
            st.code("Living room interior, night time, warm indirect LED lighting, moody atmosphere, elegant shadows, cinematic lighting.")

    st.warning("Dica do Prof. Herbert: Ao usar a IA, você pode trocar cores no texto (ex: trocar 'neutral' por 'sage green') para ver novas possibilidades!")
