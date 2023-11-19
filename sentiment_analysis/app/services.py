def analyze_sentiment(text):
    sum_of_ord = sum(ord(char) for char in text)

    # Map the hash value to 0 or 1 using modulo operation
    return "negative" if sum_of_ord % 2 else "positive"
