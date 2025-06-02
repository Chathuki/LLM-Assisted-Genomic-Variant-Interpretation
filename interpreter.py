from langchain.prompts import PromptTemplate
from langchain_community.llms import GPT4All

def load_llm(model_path):
    return GPT4All(model=model_path, backend="gpt4all", verbose=False)

def interpret_variants(variant_text, question, llm):
    prompt = PromptTemplate(
        input_variables=["variant_text", "question"],
        template="""
You are a genomics AI assistant. A researcher has provided genomic variants in text format.
Interpret them and answer the question below.

Variants:
{variant_text}

Question:
{question}

Answer:"""
    )
    chain = prompt | llm
    return chain.invoke({"variant_text": variant_text[:3000], "question": question})
