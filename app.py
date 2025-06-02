import os
import streamlit as st
from interpreter import load_llm, interpret_variants

st.set_page_config(page_title="Genomic Variant Interpreter", page_icon="🧬", layout="centered")
st.title("🧬 LLM-Assisted Genomic Variant Interpretation")
st.markdown("Interpret genomic variants using an offline LLM like GPT4All.")

VARIANT_FILE = "./variants/example_variants.txt"
LLM_PATH = "./models/ggml-gpt4all-j-v1.3-groovy.bin"

if not os.path.exists(VARIANT_FILE):
    st.error("Variant file not found in `variants/` folder.")
    st.stop()

if not os.path.exists(LLM_PATH):
    st.error("GPT4All model not found in `models/` folder.")
    st.stop()

with st.spinner("Loading model..."):
    llm = load_llm(LLM_PATH)

with open(VARIANT_FILE, "r") as file:
    variant_text = file.read()

st.markdown("### Genomic Variant Data")
st.code(variant_text, language="text")

st.markdown("### Ask a question (e.g., 'Explain the clinical significance')")
query = st.text_input("Your question:")

if st.button("Interpret"):
    with st.spinner("Interpreting..."):
        result = interpret_variants(variant_text, query, llm)
        st.success("✅ Interpretation")
        st.markdown(result)
