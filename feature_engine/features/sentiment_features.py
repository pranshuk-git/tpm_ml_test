# imports
import os

from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax
from nltk.sentiment.vader import SentimentIntensityAnalyzer

MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL, resume_download=True)
model.save_pretrained(MODEL)
tokenizer.save_pretrained(MODEL)

# TODO - DEFINE YOUR FEATURE EXTRACTOR HERE
def get_sentiment(text):
    result = {}
    if os.environ['model_name'] == "VADER" :
        print("Model is VADER")
        sid = SentimentIntensityAnalyzer()
        sentiment_scores = sid.polarity_scores(text)
        total_score = sum(sentiment_scores.values())
        positive_prob = sentiment_scores['pos'] / total_score
        negative_prob = sentiment_scores['neg'] / total_score
        neutral_prob = sentiment_scores['neu'] / total_score
        result = {'positive': positive_prob, 'negative': negative_prob, 'neutral': neutral_prob}

    #Using Hugging Face
    elif os.environ['model_name'] == "ROBERTA":
        encoded_input = tokenizer(text, return_tensors='pt')
        output = model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        for i in range(scores.shape[0]):
            result[config.id2label[ranking[i]]] = scores[ranking[i]]

    return(result)