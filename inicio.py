import streamlit as st
import base64
import os

# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================
st.set_page_config(
    page_title="Salomé Arango | Portafolio Multimodales",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# ESTILOS — ROSÉ STUDIO
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Space+Mono:wght@400;700&display=swap');

:root {
    --bg: #fff9fb;
    --white: #ffffff;
    --surface: #fff0f5;
    --surface-hover: #ffe3ed;
    --pink: #d94f87;
    --pink-dark: #a92f64;
    --pink-light: #f6b6ce;
    --pink-soft: #fde5ee;
    --border: #f1d2df;
    --border-strong: #e9a7c2;
    --text: #38232e;
    --text-secondary: #755663;
    --muted: #9c7c8a;
    --green: #628d76;
}

html, body, [class*="css"], .stApp, button, input, textarea, select {
    font-family: 'DM Sans', sans-serif !important;
}

.stApp {
    background:
        radial-gradient(ellipse at 0% 0%, rgba(246,182,206,0.20), transparent 35%),
        radial-gradient(ellipse at 100% 50%, rgba(253,229,238,0.45), transparent 35%),
        var(--bg) !important;
    color: var(--text);
    background-attachment: fixed;
}

#MainMenu,
footer {
    visibility: hidden;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1250px !important;
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
}

/* ============================================================
   TIPOGRAFÍA
   ============================================================ */

h1, h2, h3, h4, h5 {
    font-family: 'Playfair Display', serif !important;
    color: var(--text) !important;
    font-weight: 400 !important;
}

p {
    color: var(--text-secondary);
}

/* ============================================================
   PRESENTACIÓN PRINCIPAL
   ============================================================ */

.hero-kicker {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    color: var(--pink);
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 1.5rem;
}

.hero-kicker::before {
    content: '';
    display: inline-block;
    width: 28px;
    height: 2px;
    background: var(--pink);
}

.hero-h1 {
    font-family: 'Playfair Display', serif !important;
    font-size: 4.2rem !important;
    line-height: 1.08 !important;
    font-weight: 400 !important;
    letter-spacing: -0.04em !important;
    margin: 0 0 1.5rem 0 !important;
    color: var(--text) !important;
}

.hero-h1 em {
    color: var(--pink);
    font-weight: 400;
    font-style: italic;
}

.hero-desc {
    font-family: 'DM Sans', sans-serif;
    font-size: 1rem;
    line-height: 1.9;
    color: var(--text-secondary);
    max-width: 570px;
    margin-bottom: 1.5rem;
    font-weight: 400;
}

.hero-desc strong {
    color: var(--text);
    font-weight: 700;
}

.part-badge {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: var(--white);
    border: 1px solid var(--border);
    padding: 7px 15px 7px 8px;
    border-radius: 50px;
    color: var(--pink-dark);
    font-family: 'Space Mono', monospace;
    font-size: 0.66rem;
    letter-spacing: 0.07em;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 15px rgba(169,47,100,0.04);
}

.part-badge .num {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 25px;
    height: 25px;
    border-radius: 50%;
    background: var(--pink);
    color: white;
    font-size: 0.75rem;
    font-weight: 700;
}

/* ============================================================
   NOTA DESTACADA
   ============================================================ */

.hero-note {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    background: var(--white);
    border: 1px solid var(--border);
    border-left: 4px solid var(--pink);
    border-radius: 4px 14px 14px 4px;
    padding: 17px 19px;
    margin: 1.5rem 0;
    max-width: 570px;
    font-size: 0.88rem;
    line-height: 1.75;
    color: var(--text-secondary);
}

.hero-note .icon {
    color: var(--pink);
    font-size: 1.15rem;
    flex-shrink: 0;
}

.hero-note b {
    color: var(--pink-dark);
}

/* ============================================================
   ETIQUETAS
   ============================================================ */

.chips {
    display: flex;
    flex-wrap: wrap;
    gap: 9px;
    margin-top: 1.2rem;
}

.chip {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    padding: 9px 13px;
    border: 1px solid var(--border);
    border-radius: 8px;
    background: rgba(255,255,255,0.85);
    color: var(--text-secondary);
    font-size: 0.78rem;
}

.chip::before {
    content: '✿';
    color: var(--pink);
    font-size: 0.75rem;
}

.chip strong {
    color: var(--text);
    font-weight: 700;
}

/* ============================================================
   RETRATO
   ============================================================ */

.st-key-portrait_card {
    background: var(--white) !important;
    border: 1px solid var(--border) !important;
    border-radius: 180px 180px 22px 22px !important;
    padding: 10px !important;
    position: relative;
    min-height: 520px;
    overflow: hidden;
    box-shadow: 0 20px 55px rgba(169,47,100,0.10) !important;
}

.st-key-portrait_card [data-testid="stImage"] {
    width: 100% !important;
    min-height: 500px;
    display: flex !important;
    align-items: center;
    justify-content: center;
}

.st-key-portrait_card [data-testid="stImage"] > div {
    width: 100% !important;
}

.st-key-portrait_card img {
    width: 100% !important;
    max-height: 520px !important;
    object-fit: contain !important;
    border-radius: 170px 170px 14px 14px !important;
}

.portrait-caption {
    text-align: center;
    margin-top: 1.2rem;
    font-family: 'Space Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--muted);
}

.portrait-caption .star {
    color: var(--pink);
    margin: 0 9px;
}

/* ============================================================
   ENCABEZADOS DE SECCIÓN
   ============================================================ */

.section-head {
    display: flex;
    align-items: center;
    gap: 15px;
    padding-bottom: 17px;
    margin: 4.5rem 0 2rem 0;
    border-bottom: 1px solid var(--border);
}

.section-num {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-width: 43px;
    height: 39px;
    padding: 0 8px;
    border-radius: 11px;
    background: var(--pink-soft);
    color: var(--pink-dark);
    font-family: 'Space Mono', monospace;
    font-size: 0.78rem;
    font-weight: 700;
}

.section-title {
    font-family: 'Playfair Display', serif !important;
    font-size: 1.8rem !important;
    margin: 0 !important;
    color: var(--text) !important;
    flex: 1;
}

.section-count {
    color: var(--muted);
    font-family: 'Space Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}

/* ============================================================
   TARJETAS DE PROYECTOS
   ============================================================ */

.app-card {
    display: flex !important;
    flex-direction: column;
    height: 100%;
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 17px;
    overflow: hidden;
    color: var(--text) !important;
    text-decoration: none !important;
    transition: transform 0.3s ease, box-shadow 0.3s ease,
                border-color 0.3s ease;
    margin-bottom: 0.5rem;
}

.app-card:hover {
    transform: translateY(-6px);
    border-color: var(--pink-light);
    box-shadow: 0 16px 36px rgba(169,47,100,0.12);
    color: var(--text) !important;
    text-decoration: none !important;
}

.app-thumb {
    width: 100%;
    aspect-ratio: 16 / 10;
    background: #fff5f8;
    border-bottom: 1px solid var(--border);
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
}

.app-thumb img {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top center;
    z-index: 1;
    transition: transform 0.4s ease;
}

.app-card:hover .app-thumb img {
    transform: scale(1.04);
}

.app-thumb::after {
    content: '✿';
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    color: var(--pink-light);
    opacity: 0.9;
}

.app-body {
    display: flex;
    flex-direction: column;
    flex: 1;
    padding: 22px 22px 20px;
}

.app-kicker {
    display: block;
    font-family: 'Space Mono', monospace;
    font-size: 0.64rem;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    color: var(--pink);
    margin-bottom: 11px;
}

.app-title {
    font-family: 'Playfair Display', serif !important;
    font-size: 1.38rem !important;
    line-height: 1.35 !important;
    font-weight: 500 !important;
    margin: 0 0 11px 0 !important;
    color: var(--text) !important;
}

.app-desc {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.87rem;
    line-height: 1.75;
    color: var(--text-secondary);
    margin: 0 0 22px 0;
    flex: 1;
}

.app-link {
    display: inline-flex;
    align-items: center;
    gap: 9px;
    color: var(--pink-dark);
    font-family: 'Space Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    font-weight: 700;
    transition: gap 0.25s ease;
}

.app-card:hover .app-link {
    gap: 15px;
}

/* ============================================================
   PIE DE PÁGINA
   ============================================================ */

.footer {
    text-align: center;
    padding: 3rem 0 1rem;
    margin-top: 5rem;
    border-top: 1px solid var(--border);
}

.footer-ornament {
    display: block;
    color: var(--pink);
    font-size: 1.5rem;
    letter-spacing: 0.65rem;
    margin-bottom: 1rem;
}

.footer-text {
    font-family: 'Playfair Display', serif;
    font-size: 1.35rem;
    font-style: italic;
    color: var(--text);
    margin-bottom: 0.7rem;
}

.footer-sub {
    font-family: 'Space Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    color: var(--muted);
}

/* ============================================================
   ENLACES Y BARRA DE DESPLAZAMIENTO
   ============================================================ */

.stMarkdown a {
    text-decoration: none !important;
}

::-webkit-scrollbar {
    width: 9px;
}

::-webkit-scrollbar-track {
    background: var(--bg);
}

::-webkit-scrollbar-thumb {
    background: var(--pink-light);
    border-radius: 20px;
    border: 2px solid var(--bg);
}

::-webkit-scrollbar-thumb:hover {
    background: var(--pink);
}

/* ============================================================
   DISEÑO ADAPTABLE
   ============================================================ */

@media (max-width: 900px) {
    .hero-h1 {
        font-size: 2.8rem !important;
    }

    .section-title {
        font-size: 1.35rem !important;
    }

    .section-count {
        display: none;
    }

    .st-key-portrait_card {
        min-height: 350px;
        border-radius: 120px 120px 20px 20px !important;
    }

    .st-key-portrait_card [data-testid="stImage"] {
        min-height: 330px;
    }

    .st-key-portrait_card img {
        max-height: 350px !important;
        border-radius: 110px 110px 12px 12px !important;
    }

    .block-container {
        padding-top: 1.5rem !important;
    }
}

@media (max-width: 500px) {
    .hero-h1 {
        font-size: 2.4rem !important;
    }

    .hero-desc {
        font-size: 0.92rem;
    }

    .section-head {
        gap: 10px;
    }

    .section-title {
        font-size: 1.2rem !important;
    }

    .app-body {
        padding: 18px;
    }
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def get_image_base64(path):
    """Convierte una imagen local en Base64 para mostrarla en HTML."""
    if os.path.exists(path):
        with open(path, "rb") as file:
            data = base64.b64encode(file.read()).decode("utf-8")

        extension = os.path.splitext(path)[1].lower()

        mime_types = {
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".webp": "image/webp",
        }

        mime_type = mime_types.get(extension, "image/png")
        return f"data:{mime_type};base64,{data}"

    return ""


def section_header(num, title, count):
    """Crea el encabezado visual de cada categoría."""
    st.markdown(
        f"""
        <div class="section-head">
            <span class="section-num">{num}</span>
            <h2 class="section-title">{title}</h2>
            <span class="section-count">{count}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def app_card(kicker, title, desc, url, image_path):
    """Construye una tarjeta con enlace, descripción e imagen."""

    b64_img = get_image_base64(image_path)

    img_tag = (
        f'<img src="{b64_img}" alt="{title}">'
        if b64_img
        else ""
    )

    return f"""
        <a href="{url}" target="_blank" rel="noopener noreferrer"
           class="app-card">

            <div class="app-thumb">
                {img_tag}
            </div>

            <div class="app-body">
                <span class="app-kicker">{kicker}</span>

                <h3 class="app-title">{title}</h3>

                <p class="app-desc">{desc}</p>

                <span class="app-link">
                    Explorar proyecto <span>↗</span>
                </span>
            </div>
        </a>
    """


# ============================================================
# PRESENTACIÓN PRINCIPAL
# ============================================================

col_left, col_right = st.columns(
    [1.05, 1.3],
    gap="large",
    vertical_alignment="center",
)

with col_left:

    with st.container(key="portrait_card"):
        image_path = "yo.jpeg"

        if os.path.exists(image_path):
            st.image(image_path, use_container_width=True)
        else:
            st.markdown(
                """
                <div style="
                    min-height:480px;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    font-size:5rem;
                    color:#d94f87;
                ">
                    ✿
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
        <div class="portrait-caption">
            Salomé Arango
            <span class="star">✿</span>
            Portafolio 2026
        </div>
        """,
        unsafe_allow_html=True,
    )


with col_right:

    st.markdown(
        """
        <div class="part-badge">
            <span class="num">02</span>
            <span>Segunda entrega · 2026</span>
        </div>

        <div class="hero-kicker">
            Interfaces Multimodales
        </div>

        <h1 class="hero-h1">
            Hola, soy<br>
            <em>Salomé Arango.</em>
        </h1>

        <p class="hero-desc">
            Soy estudiante de <strong>Diseño Interactivo</strong>
            en <strong>EAFIT</strong>, interesada en explorar nuevas
            formas de conectar a las personas con la tecnología.
            En esta segunda entrega de mi portafolio de
            <strong>Interfaces Multimodales</strong>, presento una
            selección de los trabajos desarrollados durante el
            semestre, desde experiencias basadas en inteligencia
            artificial hasta propuestas que integran dispositivos
            físicos y visión por computadora.
        </p>

        <div class="hero-note">
            <span class="icon">✿</span>
            <span>
                Una recopilación de experimentos, aprendizajes y
                soluciones interactivas que exploran cómo el lenguaje,
                las imágenes, el tacto y otros medios pueden ampliar
                nuestra manera de interactuar con los sistemas digitales.
            </span>
        </div>

        <div class="chips">
            <span class="chip">
                <strong>EAFIT</strong> Diseño Interactivo
            </span>

            <span class="chip">
                <strong>Medellín</strong> Colombia
            </span>

            <span class="chip">
                <strong>2026</strong> Interfaces Multimodales
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown(
    "<div style='height: 1rem;'></div>",
    unsafe_allow_html=True,
)


# ============================================================
# SECCIÓN 01 — INTELIGENCIA ARTIFICIAL Y LENGUAJE NATURAL
# ============================================================

section_header(
    "01",
    "Lenguaje e inteligencia artificial",
    "2 proyectos",
)

c1, c2 = st.columns(2, gap="medium")

with c1:
    st.markdown(
        app_card(
            "Procesamiento de texto",
            "ChatPDF",
            "Una exploración de cómo los sistemas de inteligencia artificial "
            "analizan, comprenden y producen contenido en lenguaje natural.",
            "https://chatpdf-19.streamlit.app/",
            "imagen.avif",
        ),
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        app_card(
            "Análisis de imagenes",
            "Procesamiento de imagenes",
            "Una aplicación que explora el reconocimiento visual mediante "
            "modelos capaces de interpretar imágenes y encontrar patrones.",
            "https://vision-app1.streamlit.app/",
            "ojotecnologico.webp",
        ),
        unsafe_allow_html=True,
    )


# ============================================================
# SECCIÓN 02 — EXPERIENCIAS TÁCTILES
# ============================================================

section_header(
    "02",
    "Experiencias de interacción táctil",
    "4 proyectos",
)

# Fila 1
c1, c2 = st.columns(2, gap="medium")

with c1:
    st.markdown(
        app_card(
            "predicciones de números",
            "Tablero inteligente",
            "Un espacio de aula de clase "
            "donde la ia predice el numero escrito en el tablero",
            "https://prediccion-numeros.streamlit.app/",
            "numeros.jpg",
        ),
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        app_card(
            "dibujo",
            "diseño de modas digital",
            "Diseña prendas unicas a tu estilo y para todos",
             "https://tablerodemodas.streamlit.app/",
            "moda.png",
            ),
             unsafe_allow_html=True,
    )

# Fila 2
c1, c2 = st.columns(2, gap="medium")

with c1:
    st.markdown(
        app_card(
            "vision + chatgpt",
            "tablero inteligente",
            "dibuja lo que te imagines y la ia lo interpretara",
            "https://tablerointeligente.streamlit.app/",
            "analisisia.jpg",
        ),
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        app_card(
            "Dibujo · Creatividad",
            "Lienzo interactivo",
            "Un lienzo donde puedes plasmar tus ideas "
            "y la ia se encarga de crear una imagen con un estilo artistico.",
            "https://tableroartistico.streamlit.app/",
            "arte.jfif",
        ),
        unsafe_allow_html=True,
    )


# ============================================================
# SECCIÓN 03 — INTERNET DE LAS COSAS
# ============================================================

section_header(
    "03",
    "Conexiones entre dispositivos",
    "3 proyectos",
)

c1, c2, c3 = st.columns(3, gap="medium")

with c1:
    st.markdown(
        app_card(
            "Voz · Accesibilidad",
            "Control por voz",
            "Una experiencia de interacción que permite dar instrucciones "
            "donde se habla por un dispositivo y envia la informacion a wokwi",
            "https://control-devoz.streamlit.app/",
            "voz.jpg",
        ),
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        app_card(
            "Sensores · MQTT",
            "De Wokwi a Streamlit",
            "Un sensor simulado transmite información a una interfaz "
            "digital mediante el protocolo de comunicación MQTT.",
            "https://receptorwokwi.streamlit.app/",
            "MQTT.jpg",
        ),
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        app_card(
            "Automatización · MQTT",
            "De Streamlit a Wokwi",
            "Una interfaz permite enviar instrucciones y controlar "
            "dispositivos simulados a través de una conexión MQTT.",
            "https://enviarwokwi.streamlit.app/",
            "mqtt.jfif",
        ),
        unsafe_allow_html=True,
    )


# ============================================================
# PIE DE PÁGINA
# ============================================================

st.markdown(
    """
    <div class="footer">
        <span class="footer-ornament">✿ ♡ ✿</span>

        <p class="footer-text">
            Ideas que florecen a través de la tecnología.
        </p>

        <p class="footer-sub">
            Salomé Arango · EAFIT · Diseño Interactivo · 2026
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
