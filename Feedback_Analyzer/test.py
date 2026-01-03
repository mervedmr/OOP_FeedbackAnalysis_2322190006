from classes import Customer, Product, Feedback, ReviewAnalyzer

p1 = Product(1, "Headphones")
p2 = Product(2, "Laptop")
p3 = Product(3, "Mobile Phone")
p4 = Product(4, "Powerbank")

products = {1: p1, 2: p2, 3: p3, 4, p4}

analyzer = ReviewAnalyzer()
customer_id_counter = 1

while True:
    name = input("\nEnter your name (or 'q' to quit): ")
    if name.lower() == "q":
        break

    customer = Customer(customer_id_counter, name)
    customer_id_counter += 1

    print("\nSelect product:")
    print("1 - Headphones")
    print("2 - Laptop")
    print("3 - Mobile Phone")
    print("4 - Powerbank")

    choice = int(input("Your choice: "))
    product = products.get(choice)

    if not product:
        print("Invalid product.")
        continue

    rating = int(input("Give rating (1-5): "))
    text = input("Write your feedback: ")

    feedback = Feedback(customer, text, rating)
    analyzer.analyze_sentiment(feedback)

    product.add_feedback(feedback)

    print("\nCurrent Average Rating:", product.get_average_rating())
    print("Sentiment Trend:",
          analyzer.detect_sentiment_trend(product.get_all_feedback()))
