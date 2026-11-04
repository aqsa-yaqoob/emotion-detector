# 😄 Emotion Detector

Classifies a short English sentence into one of six emotions: sadness, joy, love, anger, fear and surprise. It is a fine-tuned DistilBERT model deployed as a Streamlit web app.

**Live app:**https://emotion-detector-4oulmdi5n6ciqkwpu7n24r.streamlit.app
**Model on Hugging Face:** https://huggingface.co/Aqsa55/emotion-distilbert

## Problem Statement
People express feelings in short written messages. This project predicts the emotion in a sentence, with a confidence score and an emoji.

## Dataset
- **Source:** [dair-ai/emotion](https://huggingface.co/datasets/dair-ai/emotion) on Hugging Face (English Twitter messages)
- **Labels:** sadness, joy, love, anger, fear, surprise
- **Used:** 3,000 randomly selected training samples, plus the full validation (2,000) and test (2,000) sets

## Model
- **Pretrained model:** [distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased)
- **Fine-tuned model:** [Aqsa55/emotion-distilbert](https://huggingface.co/Aqsa55/emotion-distilbert)
- **Training:** 3 epochs, batch size 32, learning rate 5e-5, max length 64, on a Google Colab T4 GPU

## Results (test set)
| Metric | Score |
|---|---|
| Accuracy | 0.895 |
| Macro F1 | 0.843 |

Macro F1 is lower than accuracy because rare emotions (love, surprise) have fewer training examples.

## How to Run Locally
```bash
git clone https://github.com/aqsa-yaqoob/emotion-detector.git
cd emotion-detector
pip install -r requirements.txt
streamlit run app.py
```

## Project Files
- `app.py`: Streamlit application
- `requirements.txt`: Python dependencies

## Example
Input: `I am so angry at you for lying to me!`
Output: 😠 Anger (97%)

## Limitations
- Trained on only 3,000 samples
- No neutral class, so neutral sentences get a low-confidence emotion
- English only

## Author
Aqsa Yaqoob
