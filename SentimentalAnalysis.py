def sentiment_analysis(text):
    # List of positive and negative words
    positive_words = ["good", "happy", "love", "excellent", "great"]
    negative_words = ["bad", "sad", "hate", "terrible", "poor"]

    # Convert the text to lowercase and split into words
    words = text.lower().split()
    
    # Count the number of positive and negative words
    pos_count = sum(1 for word in words if word in positive_words)
    neg_count = sum(1 for word in words if word in negative_words)
    
    # Determine sentiment based on counts
    if pos_count > neg_count:
        return "Positive"
    elif pos_count < neg_count:
        return "Negative"
    else:
        return "Neutral"

text = input("Enter a sentence: ")
print("Sentiment:", sentiment_analysis(text))

