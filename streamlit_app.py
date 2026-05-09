import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="NEXUS MARTUCCI V6 PRO", page_icon="🛡️")
st.title("🛡️ NEXUS MARTUCCI V6 PRO")

# La tua chiave API
api_key = "AIzaSyCMPB2xUonWMcTACxLjhCH3Ig2_3AY15W8"
genai.configure(api_key=api_key)

# FUNZIONE DI EMERGENZA: Cerca il primo modello disponibile che supporta il testo
def get_working_model():
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                return m.name
    except Exception:
        return None
    return None

model_name = get_working_model()

if model_name:
    model = genai.GenerativeModel(model_name)
    st.success(f"✅ Connessione Stabilita: {model_name}")
else:
    st.error("❌ Nessun modello compatibile trovato. Controlla la tua API Key su Google AI Studio.")

user_input = st.text_area("Cosa vuoi analizzare?")

if st.button("ESEGUI ANALISI"):
    if user_input and model_name:
        try:
            with st.spinner("Nexus in elaborazione..."):
                response = model.generate_content(user_input)
                st.markdown(response.text)
        except Exception as e:
            st.error(f"Errore tecnico: {e}")
    else:
        st.warning("Inserisci un testo o verifica la connessione.")
