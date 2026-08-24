from textblob import TextBlob

review = input("Enter Movie Review: ")

analysis = TextBlob(review)

polarity = analysis.sentiment.polarity

if polarity > 0:
    print("Positive")

elif polarity < 0:
    print("Negative")

else:
    print("Neutral")