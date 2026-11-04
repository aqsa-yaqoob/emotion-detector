import streamlit as st
from transformers import pipeline

EMOJI = {"sadness": "😢", "joy": "😄", "love": "❤️",
         "anger": "😠", "fear": "😨", "surprise": "😲"}

@st.cache_resource
def load_model():
    return pipeline("text-classification",
                    model="Aqsa55/emotion-distilbert", top_k=None)

clf = load_model()

st.title("Emotion Detector")
text = st.text_area("Type a sentence:", placeholder="I can't believe I passed the exam!")

if st.button("Predict") and text.strip():
    scores = sorted(clf(text)[0], key=lambda x: x["score"], reverse=True)
    top = scores[0]
    st.header(f"{EMOJI[top['label']]} {top['label'].capitalize()} ({top['score']:.0%})")
    st.bar_chart({s["label"]: s["score"] for s in scores})
