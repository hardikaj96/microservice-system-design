from nltk.sentiment.vader import SentimentIntensityAnalyzer


def analyze_sentiment(text):
    # Create a SentimentIntensityAnalyzer object
    sid = SentimentIntensityAnalyzer()

    # Get the sentiment scores for the input text
    sentiment_scores = sid.polarity_scores(text)

    # Determine the sentiment label based on the compound score
    if sentiment_scores["compound"] >= 0.05:
        sentiment = "Positive"
    elif sentiment_scores["compound"] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment
