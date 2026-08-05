from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

sentence = input("Enter a sentence: ")

result = classifier(sentence)

print("\nPrediction:")
print(result)