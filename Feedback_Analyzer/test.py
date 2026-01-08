from classes import Customer, Product, Feedback, ReviewAnalyzer

p1 = Product(1, "Headphones")
p2 = Product(2, "Laptop")
p3 = Product(3, "Mobile Phone")
p4 = Product(4, "Powerbank")

products = {1: p1, 2: p2, 3: p3, 4: p4}

analyzer = ReviewAnalyzer()
customer_id_counter = 1

while True:
    print("\n==============================")
    print("   CUSTOMER FEEDBACK SYSTEM")
    print("==============================")
    print("1 - Add Feedback")
    print("2 - View Product Report")
    print("3 - Delete Feedback")
    print("q - Exit")

    choice = input("Select option: ")

    if choice.lower() == "q":
        print("Exiting system...")
        break

    elif choice == "1":
        name = input("\nEnter your name: ")
        customer = Customer(customer_id_counter, name)
        customer_id_counter += 1

        print("\nSelect product:")
        print("1 - Headphones")
        print("2 - Laptop")
        print("3 - Mobile Phone")
        print("4 - Powerbank")

        product_choice = int(input("Your choice: "))
        product = products.get(product_choice)

        if not product:
            print("Invalid product.")
            continue

        rating = int(input("Give rating (1-5): "))
        if rating < 1 or rating > 5:
            print("Invalid rating.")
            continue
   
        text = input("Write your feedback: ")

        feedback = Feedback(customer, text, rating)
        analyzer.analyze_sentiment(feedback)

        product.add_feedback(feedback)
        print("\nFeedback added.")
        print("Current Average Rating:", product.get_average_rating())
        print("Sentiment Trend:",
            analyzer.detect_sentiment_trend(product.get_all_feedback()))
        input("\nPress Enter to return to menu...")

    elif choice == "2":
        print("\n--- PRODUCT REPORT ---")

        for product in products.values():
            feedbacks = product.get_all_feedback()

            print("\nProduct:", product.name)
            print("Average Rating:", product.get_average_rating())

            if feedbacks:
                print("Sentiment Trend:",
                    analyzer.detect_sentiment_trend(feedbacks))

                print("Most Common Complaint Words:")
                complaints = analyzer.most_common_complaints(feedbacks)
                for word, count in complaints:
                    print("-", word, "(", count, ")")
            else:
                print("No feedback yet.")

    elif choice == "3":
        print("\nSelect product:")
        print("1 - Headphones")
        print("2 - Laptop")
        print("3 - Mobile Phone")
        print("4 - Powerbank")

        product_choice = int(input("Your choice: "))
        product = products.get(product_choice)

        if not product:
            print("Invalid product.")
            continue

        feedbacks = product.get_all_feedback()

        if not feedbacks:
            print("No feedback to delete.")
            continue

        print("\nFeedback list:")
        for i in range(len(feedbacks)):
            print(i + 1, "-", feedbacks[i].text)

        delete_choice = int(input("Select feedback number: "))

        if delete_choice < 1 or delete_choice > len(feedbacks):
            print("Invalid selection.")
            continue

        product.remove_feedback(feedbacks[delete_choice - 1])
        print("Feedback deleted.")
        input("\nPress Enter to return to menu...")

    else:
        print("Invalid menu option.")
