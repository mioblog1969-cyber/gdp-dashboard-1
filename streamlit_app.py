import streamlit as st
import google.generativeai as genai

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="NEXUS MARTUCCI V6 PRO", page_icon="🛡️", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; background-color: #ff4b4b; color: white; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ NEXUS MARTUCCI V6 PRO")
st.subheader("Sistema di Intelligenza Strategica")

# --- CONFIGURAZIONE API ---
# Inseriamo la tua ultima chiave direttamente per evitare errori di lettura
API_KEY = "AIzaSyCsMcZkBLIkVLjnXaTvvGokICmvO5K8t1c"
genai.configure(api_key=API_KEY)

# --- INIZIALIZZAZIONE MODELLO ---
# Usiamo il modello stabile senza passare per la funzione list_models()
try:
    # 'gemini-1.5-flash' è il più veloce e moderno
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Errore inizializzazione driver: {e}")

# --- INTERFACCIA UTENTE ---
user_input = st.text_area("Cosa vuoi che analizzi il Nexus?", height=150, placeholder="Inserisci qui i dati o la domanda...")

if st.button("ESEGUI ANALISI"):
    if user_input:
        try:
            with st.spinner("⚡ Nexus sta elaborando i dati..."):
                # Chiamata diretta al cervello di Google
                response = model.generate_content(user_input)
                
                st.markdown("---")
                st.markdown("### 🖥️ RISULTATO ANALISI:")
                st.write(response.text)
                st.success("Analisi completata con successo.")
        except Exception as e:
            # Se l'errore è 404, mostriamo un messaggio specifico
            if "404" in str(e):
                st.error("ERRORE 404: Google non trova il modello o la chiave non è ancora attiva.")
                st.info("💡 CONSIGLIO: Vai su Google AI Studio e prova a mandare un messaggio nella chat di test per attivare la chiave.")
            else:
                st.error(f"Errore durante l'analisi: {e}")
    else:
        st.warning("⚠️ Inserisci un testo per avviare il sistema.")

st.markdown("---")
st.caption("Versione 6.0.1 - Modulo di Risposta Rapida")
