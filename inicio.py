
import streamlit as st
import base64
import os
import html

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
@import url('https://fonts.googleapis.com/css2?family=Delicious+Handrawn&family=Nunito:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap');

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
}

/* ============================================================
   ESTILO GENERAL
   ============================================================ */

html, body, .stApp,
[data-testid="stAppViewContainer"] {
    font-family: 'Nunito', sans-serif !important;
}

.stApp {
    background:
        radial-gradient(ellipse at 0% 0%, rgba(246,182,206,0.20), transparent 35%),
        radial-gradient(ellipse at 100% 50%, rgba(253,229,238,0.45), transparent 35%),
        var(--bg) !important;
    color: var(--text);
    background-attachment: fixed;
}

#MainMenu, footer {
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

.hero-h1,
.hero-h1 em,
.project-title,
.portrait-caption,
.footer-text,
.footer-ornament {
    font-family: 'Delicious Handrawn', cursive !important;
    font-weight: 400 !important;
}

.hero-h1 {
    font-size: 5rem !important;
    line-height: 1.12 !important;
    letter-spacing: 0 !important;
    margin: 0 0 1.5rem 0 !important;
    color: var(--text) !important;
}

.hero-h1 em {
    color: var(--pink);
    font-style: normal;
}

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
   NOTA PRINCIPAL
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
    max-width: 650px;
    font-family: 'Nunito', sans-serif;
    font-size: 0.92rem;
    line-height: 1.85;
    color: var(--text-secondary);
}

.hero-note .icon {
    color: var(--pink);
    font-size: 1.4rem;
    flex-shrink: 0;
}

.hero-note b {
    color: var(--pink-dark);
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
    font-size: 1.4rem;
    color: var(--muted);
}

.portrait-caption .star {
    color: var(--pink);
    margin: 0 9px;
}

/* ============================================================
   TARJETAS DE PROYECTOS
   ============================================================ */

.project-row {
    display: flex;
    align-items: stretch;
    gap: 28px;
    width: 100%;
    margin: 0 0 38px 0;
}

.project-row.reverse {
    flex-direction: row-reverse;
}

/* Enlace que contiene la imagen */

.project-link-area {
    display: block;
    flex: 1 1 50%;
    min-width: 0;
    align-self: stretch;
    color: inherit;
    text-decoration: none !important;
}

/* Contenedor de la imagen */

.project-image {
    position: relative;
    width: 100%;
    height: 100%;
    min-height: 290px;
    aspect-ratio: 16 / 10;
    box-sizing: border-box;
    background: #fff0f5;
    border: 1px solid var(--border);
    border-radius: 17px;
    overflow: hidden;
    isolation: isolate;
    box-shadow: 0 10px 28px rgba(169,47,100,0.06);
    transition:
        transform 0.35s ease,
        box-shadow 0.35s ease,
        border-color 0.35s ease;
    transform-origin: center;
}

/* Imagen original: siempre visible */

.project-image img {
    display: block;
    width: 100%;
    height: 100%;
    min-height: 290px;
    position: absolute;
    inset: 0;
    object-fit: cover;
    object-position: center;
    transition: transform 0.45s ease;
    z-index: 1;
}

/* ============================================================
   HOVER ROSADO TRANSPARENTE
   La imagen sigue siendo visible debajo de la capa.
   ============================================================ */

.project-image::after {
    content: '';
    position: absolute;
    inset: 0;
    background: rgba(217, 79, 135, 0.34);
    opacity: 0;
    transition: opacity 0.35s ease;
    pointer-events: none;
    z-index: 2;
}

/* ============================================================
   FLOR CENTRAL ROSA OSCURO
   ============================================================ */

.project-image::before {
    content: '✿';
    position: absolute;
    top: 50%;
    left: 50%;
    right: auto;
    color: #a92f64;
    font-family: 'Delicious Handrawn', cursive;
    font-size: clamp(4rem, 7vw, 6rem);
    line-height: 1;
    opacity: 0;
    z-index: 3;
    pointer-events: none;
    transform: translate(-50%, -50%) scale(0.55) rotate(-25deg);
    transform-origin: center;
    transition:
        opacity 0.3s ease,
        transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
    text-shadow:
        0 2px 0 rgba(255,255,255,0.4),
        0 5px 20px rgba(112,22,63,0.18);
}

/* Al pasar el cursor, aparece la capa rosa */

.project-row:hover .project-image::after,
.project-link-area:focus-visible .project-image::after {
    opacity: 1;
}

/* La flor aparece en el centro */

.project-row:hover .project-image::before,
.project-link-area:focus-visible .project-image::before {
    opacity: 1;
    transform: translate(-50%, -50%) scale(1) rotate(0deg);
}

/* Inclinación suave de las imágenes */

.project-row:hover .project-image {
    transform: rotate(-1.2deg) translateY(-4px);
    border-color: var(--pink-light);
    box-shadow: 0 18px 36px rgba(169,47,100,0.16);
}

.project-row.reverse:hover .project-image {
    transform: rotate(1.2deg) translateY(-4px);
}

/* Zoom sutil de la imagen */

.project-row:hover .project-image img {
    transform: scale(1.045);
}

/* ============================================================
   BURBUJA DE TEXTO
   ============================================================ */

.project-bubble {
    display: flex;
    flex-direction: column;
    justify-content: center;
    flex: 1 1 50%;
    min-width: 0;
    box-sizing: border-box;
    padding: 34px 36px;
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 17px;
    box-shadow: 0 10px 28px rgba(169,47,100,0.045);
    position: relative;
    transition:
        box-shadow 0.35s ease,
        border-color 0.35s ease;
}

.project-bubble::before {
    content: '✿';
    position: absolute;
    top: 17px;
    right: 20px;
    color: var(--pink-light);
    font-family: 'Delicious Handrawn', cursive;
    font-size: 1.6rem;
    opacity: 0.8;
}

.project-row:hover .project-bubble {
    border-color: var(--border-strong);
    box-shadow: 0 14px 32px rgba(169,47,100,0.08);
}

/* Categoría */

.project-kicker {
    display: block;
    font-family: 'Space Mono', monospace;
    font-size: 0.64rem;
    line-height: 1.7;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    color: var(--pink);
    margin-bottom: 12px;
}

/* Títulos manuscritos */

.project-title {
    font-size: 2.4rem !important;
    line-height: 1.2 !important;
    color: var(--text) !important;
    margin: 0 0 15px 0 !important;
    padding: 0 !important;
    overflow-wrap: anywhere;
}

/* Descripciones */

.project-desc {
    font-family: 'Nunito', sans-serif !important;
    font-size: 0.95rem;
    line-height: 1.85;
    color: var(--text-secondary);
    margin: 0 0 25px 0 !important;
    padding: 0 !important;
}

/* Enlaces */

.project-link {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    align-self: flex-start;
    color: var(--pink-dark) !important;
    font-family: 'Space Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    font-weight: 700;
    text-decoration: none !important;
    transition: gap 0.25s ease;
}

.project-link:hover {
    gap: 16px;
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
    font-size: 2rem;
    letter-spacing: 0.65rem;
    margin-bottom: 1rem;
}

.footer-text {
    font-size: 2rem;
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
   TABLET
   ============================================================ */

@media (max-width: 900px) {
    .hero-h1 {
        font-size: 3.8rem !important;
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

    .project-row {
        gap: 18px;
    }

    .project-bubble {
        padding: 24px;
    }

    .project-title {
        font-size: 2rem !important;
    }

    .project-image,
    .project-image img {
        min-height: 250px;
    }
}

/* ============================================================
   MÓVIL
   ============================================================ */

@media (max-width: 650px) {
    .hero-h1 {
        font-size: 3.2rem !important;
    }

    .hero-note {
        font-size: 0.88rem;
    }

    .project-row,
    .project-row.reverse {
        flex-direction: column;
        gap: 0;
        margin-bottom: 32px;
    }

    .project-link-area {
        flex: none;
        width: 100%;
    }

    .project-image {
        width: 100%;
        height: auto;
        min-height: 230px;
        aspect-ratio: 16 / 10;
        border-radius: 17px 17px 0 0;
    }

    .project-image img {
        min-height: 230px;
    }

    .project-bubble {
        width: 100%;
        flex: none;
        padding: 25px 22px;
        border-radius: 0 0 17px 17px;
    }

    .project-title {
        font-size: 2rem !important;
    }

    .project-desc {
        font-size: 0.9rem;
    }

    .portrait-caption {
        font-size: 1.25rem;
    }

    .footer-text {
        font-size: 1.7rem;
    }
}

/* ============================================================
   ACCESIBILIDAD: REDUCIR ANIMACIONES
   ============================================================ */

@media (prefers-reduced-motion: reduce) {
    .project-image,
    .project-image img,
    .project-bubble,
    .project-image::before,
    .project-image::after {
        transition: none !important;
    }
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def get_image_base64(path):
    """Convierte una imagen local en Base64."""

    if not os.path.exists(path):
        return ""

    try:
        with open(path, "rb") as file:
            data = base64.b64encode(file.read()).decode("utf-8")

        extension = os.path.splitext(path)[1].lower()

        mime_types = {
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".webp": "image/webp",
            ".avif": "image/avif",
            ".jfif": "image/jpeg",
        }

        mime_type = mime_types.get(extension, "image/png")
        return f"data:{mime_type};base64,{data}"

    except OSError:
        return ""


def project_card(number, kicker, title, desc, url, image_path, reverse=False):
    """Renderiza una tarjeta HTML con imagen, hover y texto."""

    safe_number = html.escape(str(number))
    safe_kicker = html.escape(kicker)
    safe_title = html.escape(title)
    safe_desc = html.escape(desc)
    safe_url = html.escape(url, quote=True)

    image_data = get_image_base64(image_path)

    if image_data:
        image_html = (
            f'<img src="{image_data}" alt="{safe_title}" loading="lazy">'
        )
    else:
        image_html = ""

    reverse_class = " reverse" if reverse else ""

    card_html = f"""
    <div class="project-row{reverse_class}">
        <a class="project-link-area"
           href="{safe_url}"
           target="_blank"
           rel="noopener noreferrer"
           aria-label="Abrir proyecto: {safe_title}">
            <div class="project-image">
                {image_html}
            </div>
        </a>

        <div class="project-bubble">
            <span class="project-kicker">
                Proyecto {safe_number} · {safe_kicker}
            </span>

            <h3 class="project-title">{safe_title}</h3>

            <p class="project-desc">{safe_desc}</p>

            <a class="project-link"
               href="{safe_url}"
               target="_blank"
               rel="noopener noreferrer">
                Explorar proyecto <span>↗</span>
            </a>
        </div>
    </div>
    """

    st.html(card_html)


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
                    font-family:'Delicious Handrawn',cursive;
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

        <div class="hero-note">
            <span class="icon">✿</span>
            <span>
                Una recopilación que hemos desarrollado en la clase de
                <b>Interfaces Multimodales</b>, donde experimentamos cómo
                conectar la tecnología con el mundo físico, cómo usar la
                inteligencia artificial como apoyo para estas interfaces
                y cómo desarrollar interfaces táctiles.
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown(
    "<div style='height: 1.5rem;'></div>",
    unsafe_allow_html=True,
)


# ============================================================
# PORTAFOLIO — NUEVE PROYECTOS
# ============================================================

project_card(
    1,
    "Procesamiento de texto",
    "ChatPDF",
    "Una exploración de cómo los sistemas de inteligencia artificial "
    "analizan, comprenden y producen contenido en lenguaje natural.",
    "https://chatpdf-19.streamlit.app/",
    "imagen.avif",
    reverse=False,
)

project_card(
    2,
    "Análisis de imágenes",
    "Procesamiento de imágenes",
    "Una aplicación que explora el reconocimiento visual mediante "
    "modelos capaces de interpretar imágenes y encontrar patrones.",
    "https://vision-app1.streamlit.app/",
    "ojotecnologico.webp",
    reverse=True,
)

project_card(
    3,
    "Predicciones de números",
    "Tablero inteligente",
    "Un espacio de aula de clase donde la inteligencia artificial "
    "predice el número escrito en el tablero.",
    "https://prediccion-numeros.streamlit.app/",
    "numeros.jpg",
    reverse=False,
)

project_card(
    4,
    "Dibujo",
    "Diseño de modas digital",
    "Diseña prendas únicas a tu estilo y para todos.",
    "https://tablerodemodas.streamlit.app/",
    "moda.png",
    reverse=True,
)

project_card(
    5,
    "Visión + ChatGPT",
    "Tablero inteligente",
    "Dibuja lo que te imagines y la inteligencia artificial lo interpretará.",
    "https://tablerointeligente.streamlit.app/",
    "analisisia.jpg",
    reverse=False,
)

project_card(
    6,
    "Dibujo · Creatividad",
    "Lienzo interactivo",
    "Un lienzo donde puedes plasmar tus ideas y la inteligencia artificial "
    "se encarga de crear una imagen con un estilo artístico.",
    "https://tableroartistico.streamlit.app/",
    "arte.jfif",
    reverse=True,
)

project_card(
    7,
    "Voz · Accesibilidad",
    "Control por voz",
    "Una experiencia de interacción que permite dar instrucciones por voz "
    "y enviar la información a Wokwi.",
    "https://control-devoz.streamlit.app/",
    "voz.jpg",
    reverse=False,
)

project_card(
    8,
    "Sensores · MQTT",
    "De Wokwi a Streamlit",
    "Un sensor simulado transmite información a una interfaz digital "
    "mediante el protocolo de comunicación MQTT.",
    "https://receptorwokwi.streamlit.app/",
    "MQTT.jpg",
    reverse=True,
)

project_card(
    9,
    "Automatización · MQTT",
    "De Streamlit a Wokwi",
    "Una interfaz permite enviar instrucciones y controlar dispositivos "
    "simulados a través de una conexión MQTT.",
    "https://enviarwokwi.streamlit.app/",
    "mqtt.jfif",
    reverse=False,
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
