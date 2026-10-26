
import streamlit as st
import paho.mqtt.client as mqtt
import json
import time
import html

# --------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------
st.set_page_config(
    page_title="SensorLab | Monitor MQTT",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# ESTILOS
# --------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root {
    --bg: #0b1020;
    --panel: #131b2e;
    --purple: #a78bfa;
    --cyan: #67e8f9;
    --text: #f1f5f9;
    --muted: #94a3b8;
    --border: rgba(148,163,184,0.17);
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif !important;
}

.stApp {
    background:
        radial-gradient(ellipse at 5% 0%, rgba(124,58,237,0.15), transparent 34%),
        radial-gradient(ellipse at 95% 5%, rgba(6,182,212,0.10), transparent 30%),
        var(--bg);
    color: var(--text);
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background: #0e1628;
    border-right: 1px solid var(--border);
}

[data-testid="stSidebar"] * {
    color: var(--text);
}

[data-testid="stSidebar"] input {
    background: #172238;
    border: 1px solid #2a3855;
    border-radius: 10px;
}

.block-container {
    padding-top: 2.2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}

h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif !important;
    color: var(--text) !important;
}

.hero {
    background: linear-gradient(120deg, #1b2440, #171d36 55%, #142b3b);
    border: 1px solid rgba(167,139,250,0.25);
    border-radius: 24px;
    padding: 30px 32px;
    margin-bottom: 26px;
}

.eyebrow {
    color: var(--cyan);
    font-size: 0.76rem;
    letter-spacing: 2.4px;
    font-weight: 700;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(2rem, 4vw, 3rem);
    font-weight: 700;
    line-height: 1.1;
    color: white;
    margin-bottom: 12px;
}

.hero-description {
    color: #b4c0d5;
    font-size: 1rem;
    max-width: 680px;
    line-height: 1.7;
}

.section-label {
    color: #c4b5fd;
    font-size: 0.76rem;
    font-weight: 700;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    margin: 14px 0 10px;
}

/* Tarjetas informativas */
.info-card {
    box-sizing: border-box;
    background: linear-gradient(145deg, #172139, #111a2c);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 20px;
    min-height: 125px;
    margin-bottom: 12px;
    overflow: hidden;
}

.card-label {
    font-size: 0.78rem;
    color: #9aa9c2;
    letter-spacing: 0.7px;
    text-transform: uppercase;
    margin-bottom: 12px;
    overflow-wrap: anywhere;
}

.card-value {
    color: #67e8f9;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.5rem;
    font-weight: 600;
    overflow-wrap: anywhere;
    word-break: break-word;
    line-height: 1.45;
}

.card-hint {
    color: #7f91ae;
    font-size: 0.8rem;
    margin-top: 8px;
}

.status-pill {
    display: inline-block;
    background: rgba(52,211,153,0.1);
    color: #6ee7b7;
    border: 1px solid rgba(52,211,153,0.25);
    border-radius: 50px;
    padding: 7px 12px;
    font-size: 0.8rem;
    font-weight: 600;
}

.status-idle {
    display: inline-block;
    background: rgba(148,163,184,0.09);
    color: #cbd5e1;
    border: 1px solid rgba(148,163,184,0.2);
    border-radius: 50px;
    padding: 7px 12px;
    font-size: 0.8rem;
    font-weight: 600;
}

/* Tarjetas de lecturas */
.sensor-card {
    box-sizing: border-box;
    width: 100%;
    min-height: 145px;
    height: 100%;
    background: linear-gradient(145deg, #192541, #111a2c);
    border: 1px solid rgba(103,232,249,0.2);
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 14px;
    transition: transform 0.2s ease, border-color 0.2s ease;
    overflow: hidden;
}

.sensor-card:hover {
    transform: translateY(-3px);
    border-color: rgba(167,139,250,0.65);
}

.sensor-card-label {
    color: #a5b4cc;
    font-size: 0.82rem;
    font-weight: 600;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    margin-bottom: 16px;
    overflow-wrap: anywhere;
}

.sensor-card-value {
    color: #67e8f9;
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(1.25rem, 2.2vw, 2rem);
    font-weight: 700;
    line-height: 1.35;
    overflow-wrap: anywhere;
    word-break: break-word;
}

.sensor-card-type {
    color: #8192ad;
    font-size: 0.75rem;
    margin-top: 13px;
}

.empty-panel {
    background: rgba(19,27,46,0.65);
    border: 1px dashed rgba(148,163,184,0.3);
    border-radius: 18px;
    padding: 38px 20px;
    text-align: center;
    margin-top: 12px;
}

.empty-icon {
    font-size: 2.8rem;
    margin-bottom: 12px;
}

.empty-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.2rem;
    color: #e2e8f0;
    font-weight: 600;
}

.empty-text {
    color: #94a3b8;
    font-size: 0.9rem;
    margin-top: 8px;
    line-height: 1.6;
}

.stButton > button {
    background: linear-gradient(110deg, #8b5cf6, #6366f1);
    color: white;
    border: 1px solid rgba(196,181,253,0.3);
    border-radius: 12px;
    padding: 0.8rem 1.3rem;
    font-weight: 700;
    min-height: 48px;
    box-shadow: 0 6px 24px rgba(99,102,241,0.18);
    transition: all 0.2s ease;
}

.stButton > button:hover {
    border-color: #c4b5fd;
    color: white;
    transform: translateY(-2px);
    box-shadow: 0 10px 30px rgba(139,92,246,0.25);
}

div[data-testid="stExpander"] {
    background: rgba(19,27,46,0.75);
    border: 1px solid var(--border);
    border-radius: 14px;
}

div[data-testid="stExpander"] summary {
    color: #e2e8f0;
}

hr {
    border-color: rgba(148,163,184,0.15);
}

[data-testid="stAlert"] {
    border-radius: 12px;
}

[data-testid="stCaptionContainer"] {
    color: #8494af;
}

.footer {
    color: #64748b;
    font-size: 0.8rem;
    text-align: center;
    padding-top: 28px;
}

@media (max-width: 700px) {
    .block-container {
        padding: 1rem;
    }

    .hero {
        padding: 23px 20px;
    }

    .sensor-card {
        padding: 17px;
    }
}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# ESTADO DE LA APLICACIÓN
# --------------------------------------------------
if "sensor_data" not in st.session_state:
    st.session_state.sensor_data = None

if "last_topic" not in st.session_state:
    st.session_state.last_topic = None

if "last_updated" not in st.session_state:
    st.session_state.last_updated = None


# --------------------------------------------------
# FUNCIÓN MQTT
# --------------------------------------------------
def get_mqtt_message(broker, port, topic, client_id):
    """Recibe el primer mensaje disponible en un tópico MQTT."""
    message_received = {"received": False, "payload": None}
    client = None

    def on_message(client, userdata, message):
        try:
            decoded = message.payload.decode("utf-8")

            try:
                payload = json.loads(decoded)
            except json.JSONDecodeError:
                payload = decoded

            message_received["payload"] = payload
            message_received["received"] = True

        except Exception as error:
            message_received["payload"] = {
                "error": f"No se pudo interpretar el mensaje: {error}"
            }
            message_received["received"] = True

    try:
        try:
            client = mqtt.Client(
                callback_api_version=mqtt.CallbackAPIVersion.VERSION1,
                client_id=client_id
            )
        except (AttributeError, TypeError):
            client = mqtt.Client(client_id=client_id)

        client.on_message = on_message
        client.connect(broker, int(port), 60)
        client.subscribe(topic)
        client.loop_start()

        timeout = time.time() + 5

        while not message_received["received"] and time.time() < timeout:
            time.sleep(0.1)

        if message_received["received"]:
            return message_received["payload"]

        return {
            "error": (
                "No se recibió ningún mensaje durante 5 segundos. "
                "Verifica que el sensor esté publicando en este tópico."
            )
        }

    except Exception as error:
        return {"error": str(error)}

    finally:
        if client is not None:
            try:
                client.loop_stop()
                client.disconnect()
            except Exception:
                pass


# --------------------------------------------------
# FUNCIONES PARA MOSTRAR TARJETAS
# --------------------------------------------------
def format_value(value):
    """Convierte cualquier valor recibido en texto legible."""
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False, indent=2)

    if value is None:
        return "Sin dato"

    return str(value)


def sensor_card(label, value):
    """Crea una tarjeta HTML visual, no un bloque de código."""
    safe_label = html.escape(str(label))
    safe_value = html.escape(format_value(value))

    # Los saltos de línea se conservan sin usar st.code.
    safe_value = safe_value.replace("\n", "<br>")

    st.markdown(
        f"""
        <div class="sensor-card">
            <div class="sensor-card-label">{safe_label}</div>
            <div class="sensor-card-value">{safe_value}</div>
            <div class="sensor-card-type">LECTURA RECIBIDA</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def info_card(label, value, hint=""):
    """Crea las tarjetas superiores de información."""
    safe_label = html.escape(str(label))
    safe_value = html.escape(str(value))
    safe_hint = html.escape(str(hint))

    st.markdown(
        f"""
        <div class="info-card">
            <div class="card-label">{safe_label}</div>
            <div class="card-value" style="font-size:1.05rem;">
                {safe_value}
            </div>
            <div class="card-hint">{safe_hint}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# BARRA LATERAL
# --------------------------------------------------
with st.sidebar:
    st.markdown("""
    <div style="padding:12px 0 22px 0;">
        <div style="font-size:2.3rem;">📡</div>
        <div style="font-family:'Space Grotesk',sans-serif;
                    font-size:1.4rem;font-weight:700;color:white;">
            Sensor<span style="color:#a78bfa;">Lab</span>
        </div>
        <div style="font-size:0.8rem;color:#8494af;">
            MONITOREO DE SENSORES
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown(
        '<div class="section-label">Conexión MQTT</div>',
        unsafe_allow_html=True
    )

    broker = st.text_input(
        "Servidor / Broker",
        value="broker.mqttdashboard.com",
        help="Dirección del broker MQTT"
    )

    port = st.number_input(
        "Puerto",
        value=1883,
        min_value=1,
        max_value=65535,
        step=1,
        help="El puerto más habitual es 1883"
    )

    topic = st.text_input(
        "Tópico del sensor",
        value="Sensor/THP2",
        help="Canal MQTT del que quieres recibir información"
    )

    client_id = st.text_input(
        "ID del cliente",
        value="streamlit_client",
        help="Identificador para esta conexión"
    )

    st.markdown("---")

    st.markdown("""
    <div style="font-size:0.8rem;color:#8494af;line-height:1.7;">
        <span style="color:#67e8f9;">●</span>
        Configura el broker y consulta el mensaje disponible en el tópico.
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# ENCABEZADO
# --------------------------------------------------
st.markdown("""
<div class="hero">
    <div class="eyebrow">◈ INTERNET DE LAS COSAS · IoT</div>
    <div class="hero-title">Monitor de sensores</div>
    <div class="hero-description">
        Visualiza los datos transmitidos por tus dispositivos mediante MQTT.
        Conecta con tu broker y consulta las lecturas de tus sensores
        desde un solo lugar.
    </div>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# TARJETAS DE CONEXIÓN
# --------------------------------------------------
col_broker, col_topic, col_status = st.columns([1.2, 1.2, 0.8])

with col_broker:
    info_card("◉ Broker configurado", broker, f"Puerto {int(port)}")

with col_topic:
    info_card("⌁ Tópico seleccionado", topic, "Canal de recepción MQTT")

with col_status:
    if st.session_state.last_updated:
        st.markdown(f"""
        <div class="info-card">
            <div class="card-label">Estado</div>
            <span class="status-pill">● Datos recibidos</span>
            <div class="card-hint">
                Consulta: {html.escape(st.session_state.last_updated)}
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="info-card">
            <div class="card-label">Estado</div>
            <span class="status-idle">● En espera</span>
            <div class="card-hint">Pendiente de consulta</div>
        </div>
        """, unsafe_allow_html=True)


# --------------------------------------------------
# BOTÓN DE CONSULTA
# --------------------------------------------------
st.markdown(
    '<div class="section-label">CONSULTA DE DATOS</div>',
    unsafe_allow_html=True
)

left, center, right = st.columns([1, 1.5, 1])

with center:
    consultar = st.button(
        "↻  Obtener datos del sensor",
        use_container_width=True
    )

if consultar:
    if not broker.strip() or not topic.strip() or not client_id.strip():
        st.warning("Completa el broker, el tópico y el ID del cliente.")
    else:
        with st.spinner("Conectando al broker MQTT y esperando el mensaje..."):
            result = get_mqtt_message(
                broker.strip(),
                int(port),
                topic.strip(),
                client_id.strip()
            )

        st.session_state.sensor_data = result
        st.session_state.last_topic = topic.strip()

        if not (isinstance(result, dict) and "error" in result):
            st.session_state.last_updated = time.strftime("%H:%M:%S")
        else:
            st.session_state.last_updated = None


# --------------------------------------------------
# RESULTADOS
# --------------------------------------------------
st.markdown("---")

st.markdown(
    '<div class="section-label">LECTURAS DEL DISPOSITIVO</div>',
    unsafe_allow_html=True
)

st.markdown("## 📊 Datos del sensor")

data = st.session_state.sensor_data

if data is None:
    st.markdown("""
    <div class="empty-panel">
        <div class="empty-icon">📡</div>
        <div class="empty-title">Tu panel está listo</div>
        <div class="empty-text">
            Configura la conexión en el menú lateral y pulsa
            <b>Obtener datos del sensor</b> para consultar el primer mensaje.
        </div>
    </div>
    """, unsafe_allow_html=True)

elif isinstance(data, dict) and "error" in data:
    st.error(f"⚠️ No fue posible obtener los datos: {data['error']}")
    st.caption(
        "Comprueba el broker, el puerto, el tópico y que el sensor esté publicando."
    )

else:
    if st.session_state.last_updated:
        st.caption(
            f"Última consulta: {st.session_state.last_updated} "
            f"· Tópico: {st.session_state.last_topic}"
        )

    st.success("Mensaje recibido correctamente")

    # JSON: cada campo se muestra como una tarjeta visual.
    if isinstance(data, dict):
        if not data:
            st.info("El mensaje recibido contiene un objeto JSON vacío.")
        else:
            items = list(data.items())

            # Máximo tres tarjetas por fila.
            for start in range(0, len(items), 3):
                row_items = items[start:start + 3]
                columns = st.columns(3)

                for column, (key, value) in zip(columns, row_items):
                    with column:
                        sensor_card(key, value)

        # El JSON completo solo aparece si el usuario lo solicita.
        with st.expander("⌘  Ver mensaje JSON completo"):
            st.json(data)

    # Si llega una lista, cada elemento tiene su tarjeta.
    elif isinstance(data, list):
        if not data:
            st.info("El mensaje recibido contiene una lista vacía.")
        else:
            for start in range(0, len(data), 3):
                row_items = data[start:start + 3]
                columns = st.columns(3)

                for index, value in enumerate(row_items):
                    with columns[index]:
                        sensor_card(f"Elemento {start + index + 1}", value)

        with st.expander("⌘  Ver mensaje JSON completo"):
            st.json(data)

    # Si el mensaje es texto simple, también se presenta como tarjeta.
    else:
        sensor_card("Mensaje recibido", data)


# --------------------------------------------------
# AYUDA
# --------------------------------------------------
with st.expander("ℹ️  Ayuda y solución de problemas"):
    st.markdown("""
    **¿Cómo funciona?**

    1. Introduce el servidor y el puerto del broker MQTT.
    2. Escribe el tópico donde publica tu sensor.
    3. Asigna un ID de cliente.
    4. Pulsa **Obtener datos del sensor**.
    5. Si llega un mensaje, sus campos aparecerán en tarjetas.

    **Brokers públicos para pruebas**
    - `broker.mqttdashboard.com`
    - `test.mosquitto.org`
    - `broker.hivemq.com`

    **Si no llegan datos**
    - Confirma que el sensor esté encendido y publicando.
    - Verifica que el tópico coincida exactamente, incluidas las mayúsculas.
    - Comprueba el broker y el puerto.
    - Los brokers públicos pueden tener restricciones o estar temporalmente fuera de servicio.

    **Importante:** la aplicación espera un mensaje durante un máximo de
    cinco segundos cada vez que pulsas el botón. No mantiene una suscripción
    permanente en segundo plano.
    """)


# --------------------------------------------------
# PIE DE PÁGINA
# --------------------------------------------------
st.markdown("""
<div class="footer">
    SENSORLAB · MQTT MONITOR &nbsp;•&nbsp; POWERED BY STREAMLIT
</div>
""", unsafe_allow_html=True)
