# demo (test amaçlı)

customer = Customer(1, "Merve")
product = Product(101, "Book")

feedback1 = Feedback(customer, "Very good product", 5)
feedback2 = Feedback(customer, "Bad quality", 1)

product.add_feedback(feedback1)
product.add_feedback(feedback2)

analyzer = ReviewAnalyzer()
print(analyzer.analyze_sentiment(feedback1))
print(analyzer.word_frequency(feedback2))
