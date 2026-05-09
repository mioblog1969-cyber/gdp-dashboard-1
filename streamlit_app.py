import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="NEXUS MARTUCCI V6 PRO", page_icon="🛡️")
st.title("🛡️ NEXUS MARTUCCI V6 PRO")

# La tua nuova chiave
api_key = "AIzaSyCsMcZkBLIkVLjnXaTvvGokICmvO5K8t1c"
genai.configure(api_key=api_key)

# Forza l'uso del modello stabile senza prefissi complicati
try:
    # Proviamo a usare il nome semplice senza 'models/'
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception as e:
    st.error(f"Errore: {e}")

user_input = st.text_area("Inserisci il testo per l'analisi:")

if st.button("ESEGUI ANALISI"):
    if user_input:
        try:
            # Usiamo stream=False per evitare problemi di protocollo
            response = model.generate_content(user_input, stream=False)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Dettaglio tecnico: {e}")
            st.info("Se leggi ancora 404, scrivi 'gemini-pro' al posto di 'gemini-1.5-flash-latest' nel codice.")
    else:
        st.warning("Scrivi qualcosa!")
