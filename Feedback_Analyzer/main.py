from collections import Counter

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def update_name(self, new_name):
        # CRUD -> Update
        self.name = new_name


class Feedback:
    def __init__(self, customer, text, rating, sentiment=None):
        self.customer = customer
        self.text = text
        self.rating = rating
        self.sentiment = sentiment

    def update_text(self, new_text):
        # CRUD -> Update
        self.text = new_text

class Product:
    def __init__(self, product_id, name):
        self.product_id = product_id
        self.name = name
        self.feedback_list = []  # Aggregation

    # CRUD -> Create
    def add_feedback(self, feedback):
        self.feedback_list.append(feedback)

    # CRUD -> Read
    def get_all_feedback(self):
        return self.feedback_list

    # CRUD -> Delete
    def remove_feedback(self, feedback):
        if feedback in self.feedback_list:
            self.feedback_list.remove(feedback)

    def get_average_rating(self):
        if not self.feedback_list:
            return 0
        total = sum(f.rating for f in self.feedback_list)
        return total / len(self.feedback_list)


class ReviewAnalyzer:
    def __init__(self):
        self.positive_words = ["good", "great", "excellent", "perfect", "nice"]
        self.negative_words = ["bad", "poor", "terrible", "awful", "worst"]

    def analyze_sentiment(self, feedback):
        text = feedback.text.lower()

        if any(word in text for word in self.positive_words):
            feedback.sentiment = "positive"
        elif any(word in text for word in self.negative_words):
            feedback.sentiment = "negative"
        else:
            feedback.sentiment = "neutral"

        return feedback.sentiment

    def word_frequency(self, feedback_list):
        all_words = []
        for feedback in feedback_list:
            words = feedback.text.lower().split()
            all_words.extend(words)

        return Counter(all_words)
        
    def detect_sentiment_trend(self, feedback_list):
        positive = sum(1 for f in feedback_list if f.sentiment == "positive")
        negative = sum(1 for f in feedback_list if f.sentiment == "negative")

        if positive > negative:
            return "improving"
        elif negative > positive:
            return "declining"
        else:
            return "stable"

    def rank_products(self, feedback_list):
         return sorted(
            product_list,
            key=lambda product: product.get_average_rating(),
            reverse=True
            )

    def most_common_complaints(self, feedback_list):
        frequencies = self.word_frequency(feedback_list)
        return frequencies.most_common(5)
        


