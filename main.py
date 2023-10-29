import json

import requests
import streamlit as st
import weaviate
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Weaviate

WEAVIATE_URL = "https://seafood-ai-challenge-60fqjjhl.weaviate.network"
WEAVIATE_API_KEY = "YOLPVTZN9i4tzm8ZxacCmBi6oLqrvIEJJUsS"

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2", model_kwargs={"device": "cpu"})

weaviate_auth_config = weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY)
weaviate_client = weaviate.Client(url=WEAVIATE_URL, auth_client_secret=weaviate.AuthApiKey(WEAVIATE_API_KEY))

vector_store = Weaviate.from_documents([], embeddings, client=weaviate_client, by_text=False)

if "messages" not in st.session_state:
    st.session_state.messages = []


def process_input(question: str):
    documents = vector_store.similarity_search(question, by_text=False)

    context = ""
    for document in documents:
        context += f"{document[0].metadata.get('source')}/{document[0].page_content}"

    PAT = 'd935800ae4f14e0e8e7b0157e22f8fc6'
    USER_ID = 'openai'
    APP_ID = 'chat-completion'
    MODEL_ID = 'GPT-3_5-turbo'
    MODEL_VERSION_ID = 'a82b2ece788e4dafac85ca6f8c8cd0f2'
    RAW_TEXT = f"""Given a question and a context, answer the question to the best of your knowledge. Do not admit to lack of information, even if the provided document's don't have any information.

    ### BEGIN CONTEXT
    {context}
    ### END CONTEXT
    
    Question: {question}
    Answer: """

    gpt3_5_output = requests.post(f"https://api.clarifai.com/v2/models/{MODEL_ID}/versions/{MODEL_VERSION_ID}/outputs",
                                  headers={"Accept": "application/json", "Authorization": f"Key {PAT}"},
                                  json={
                                      "user_app_id": {
                                          "user_id": USER_ID,
                                          "app_id": APP_ID
                                      },
                                      "inputs": [{"data": {"text": {"raw": RAW_TEXT}}}]
                                  })

    if gpt3_5_output.status_code != 200:
        return f"Model failed to provided an response, error: {gpt3_5_output.content}"

    return json.loads(gpt3_5_output.content).get("outputs")[0].get("data").get("text").get("raw")


def main():
    st.markdown("""<style>
        p { 
            margin-bottom: 2px;
        }
    </style>""", unsafe_allow_html=True)

    st.title("Leher: The Seafood AI Challenge")

    question = st.text_input("What is your query?")
    enter_key = st.button("Enter", key="enter")

    if question and enter_key:
        answer = process_input(question)
        st.session_state.messages.append({"question": question, "answer": answer})

    st.write("## Chat Log:")
    st.markdown("---")
    for msg in st.session_state.messages:
        st.write(f"Question: {msg.get('question')}")
        st.write(f"Answer: {msg.get('answer')}")
        st.markdown("---")


if __name__ == "__main__":
    main()
