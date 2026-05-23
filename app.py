import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from gtts import gTTS
import io
import PyPDF2
from dotenv import load_dotenv

load_dotenv()

# Page Config
st.set_page_config(
    page_title="Expert Machine Translation System",
    page_icon="🤖",
    layout="centered"
)

# Title and Description
st.title("🤖 Expert Machine Translation")
st.markdown("""
This system acts as an expert **Transformer encoder–decoder** architecture.
It translates your English text accurately while preserving meaning, grammar, and fluency.
""")

# Load Local HuggingFace Model
@st.cache_resource(show_spinner="Loading Transformer Model (This may take a moment)...")
def load_translator_model():
    model_name = "facebook/nllb-200-distilled-600M"
    tokenizer = AutoTokenizer.from_pretrained(model_name, src_lang="eng_Latn")
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

try:
    tokenizer, model = load_translator_model()
except Exception as e:
    st.error(f"Failed to load the model: {e}")
    st.stop()

# Sidebar
with st.sidebar:
    st.header("Configuration")
    st.markdown("**Supported Languages:**")
    st.markdown("- Telugu")
    st.markdown("- Hindi")
    st.markdown("- French")

# Main Interface
col1, col2 = st.columns([1, 1])

target_language = col1.selectbox("Target Language", ["Telugu", "Hindi", "French"])

# File Upload 
uploaded_file = col2.file_uploader("Upload a file (Optional, TXT/PDF)", type=["txt", "pdf"])

extracted_text = ""
if uploaded_file is not None:
    file_type = uploaded_file.name.split('.')[-1].lower()
    try:
        if file_type == 'txt':
            extracted_text = uploaded_file.read().decode("utf-8")
        elif file_type == 'pdf':
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            extracted_text = " ".join([page.extract_text() or "" for page in pdf_reader.pages])
            
        if not extracted_text.strip():
            st.error("Uploaded file appears to be empty or unreadable.")
    except Exception as e:
        st.error(f"Error extracting text: {e}")

if extracted_text.strip():
    st.markdown("### Extracted Text Preview:")
    preview_limit = 500
    st.text(extracted_text[:preview_limit] + ("..." if len(extracted_text) > preview_limit else ""))
    english_text = extracted_text
else:
    english_text = st.text_area("English Text", height=150, placeholder="Enter text to translate...")

def get_translation(text, language):
    lang_map = {
        "Telugu": "tel_Telu",
        "Hindi": "hin_Deva",
        "French": "fra_Latn"
    }
    tgt_lang = lang_map.get(language, "fra_Latn")
    
    # NLLB input encoding
    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
    forced_bos_token_id = tokenizer.convert_tokens_to_ids(tgt_lang)
    
    outputs = model.generate(
        **inputs, 
        forced_bos_token_id=forced_bos_token_id, 
        max_length=512
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Action
if st.button("Translate", type="primary"):
    if not english_text.strip():
        st.warning("Please enter some text or upload a valid file to translate.")
    else:
        with st.spinner("Translating..."):
            try:
                translated_text = get_translation(english_text, target_language)
                
                st.markdown("### User Output:")
                st.markdown(f"**Translated Text ({target_language}):**")
                st.success(translated_text)

                # Text-to-Speech
                st.markdown("---")
                st.markdown(f"**Listen ({target_language}):**")
                
                lang_codes = {"Telugu": "te", "Hindi": "hi", "French": "fr"}
                lang_code = lang_codes.get(target_language, "en")
                
                # Generate Audio
                tts = gTTS(text=translated_text, lang=lang_code)
                audio_bytes = io.BytesIO()
                tts.write_to_fp(audio_bytes)
                audio_bytes.seek(0)
                
                # Display Streamlit Audio Player
                st.audio(audio_bytes, format="audio/mp3")
                
                # Download Button for the audio file
                st.download_button(
                    label="⬇️ Download Audio (.mp3)",
                    data=audio_bytes,
                    file_name=f"translation_{lang_code}.mp3",
                    mime="audio/mp3"
                )
            except Exception as e:
                st.error(f"Error during translation or audio generation: {e}")

# Footer
st.markdown("---")
st.caption("Powered by HuggingFace Transformers | Offline Encoder-Decoder Architecture")
