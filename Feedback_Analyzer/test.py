from classes import Customer, Product, Feedback, ReviewAnalyzer

c1 = Customer(1, "Merve")
p1 = Product(101, "Phone")

f1 = Feedback(c1, "This product is excellent", 5)
f2 = Feedback(c1, "Worst experience ever", 1)

p1.add_feedback(f1)
p1.add_feedback(f2)

analyzer = ReviewAnalyzer()
analyzer.analyze_sentiment(f1)
analyzer.analyze_sentiment(f2)

print(f1.sentiment)
print(f2.sentiment)
print(p1.get_average_rating())
print(analyzer.detect_sentiment_trend(p1.get_all_feedback()))
