import streamlit as st
import google.generativeai as genai

# Configurazione Pagina
st.set_page_config(page_title="NEXUS MARTUCCI V6 PRO", page_icon="🛡️")
st.title("🛡️ NEXUS MARTUCCI V6 PRO")

# Configurazione API con la tua NUOVA chiave
api_key = "AIzaSyCsMcZkBLIkVLjnXaTvvGokICmvO5K8t1c"
genai.configure(api_key=api_key)

# Inizializzazione Modello (usiamo Flash che è il più veloce)
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Errore inizializzazione: {e}")

# Interfaccia Utente
user_input = st.text_area("Cosa desideri analizzare, Roberto?", placeholder="Scrivi qui il tuo messaggio...")

if st.button("ESEGUI ANALISI"):
    if user_input:
        try:
            with st.spinner("Il Nexus sta elaborando..."):
                response = model.generate_content(user_input)
                st.markdown("### Risposta del Nexus:")
                st.write(response.text)
        except Exception as e:
            st.error(f"Dettaglio Errore: {e}")
            st.info("Se l'errore è ancora 404, Google sta attivando i permessi sulla tua nuova chiave. Attendi 5 minuti.")
    else:
        st.warning("Inserisci un comando per procedere.")
