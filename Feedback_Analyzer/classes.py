# Bu dosyada CRUD işlemleri ve basit algoritmalar eklendi.

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def update_name(self, new_name):
        # CRUD -> Update
        self.name = new_name

    # Hatırlatma (Stage 3):
    # Web arayüzü gelince müşteri işlemleri sayfa üzerinden yapılacak.


class Feedback:
    def __init__(self, customer, text, rating):
        self.customer = customer
        self.text = text
        self.rating = rating
        self.sentiment = None  # Stage 2'de hesaplanacak

    def update_text(self, new_text):
        # CRUD -> Update
        self.text = new_text

    # Hatırlatma (Stage 3):
    # Zaman bilgisi (tarih) eklenirse trend analizi yapılabilir.


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
    def delete_feedback(self, feedback):
        if feedback in self.feedback_list:
            self.feedback_list.remove(feedback)

    # Hatırlatma (Stage 3):
    # Ürün puanına göre sıralama burada yapılabilir.


class ReviewAnalyzer:
    def __init__(self):
        self.positive_words = ["good", "great", "excellent", "perfect", "nice"]
        self.negative_words = ["bad", "poor", "terrible", "awful", "worst"]

    def analyze_sentiment(self, feedback):
        """
        Basit sentiment analizi:
        Positive / Neutral / Negative
        """
        text = feedback.text.lower()

        positive_count = 0
        negative_count = 0

        for word in self.positive_words:
            if word in text:
                positive_count += 1

        for word in self.negative_words:
            if word in text:
                negative_count += 1

        if positive_count > negative_count:
            feedback.sentiment = "Positive"
        elif negative_count > positive_count:
            feedback.sentiment = "Negative"
        else:
            feedback.sentiment = "Neutral"

        return feedback.sentiment

    def word_frequency(self, feedback_list):
        """
        Yorumlardan kelime frekansı çıkarır.
        """
        frequency = {}

        for feedback in feedback_list:
            words = feedback.text.lower().split()
            for word in words:
                if word in frequency:
                    frequency[word] += 1
                else:
                    frequency[word] = 1

        return frequency

    def sort_feedback_by_rating(self, feedback_list):
        """
        Rating değerine göre sıralama
        """
        return sorted(feedback_list, key=lambda f: f.rating, reverse=True)

    def sort_feedback_by_sentiment(self, feedback_list):
        """
        Sentiment değerine göre sıralama
        """
        order = {"Positive": 3, "Neutral": 2, "Negative": 1}
        return sorted(
            feedback_list,
            key=lambda f: order.get(f.sentiment, 0),
            reverse=True
        )

    # Hatırlatma (Stage 3):
    # - Zaman bazlı trend analizi burada yapılacak
    # - En sık şikayet edilen kelimeler buradan çıkarılacak
    # - Grafikler bu analiz sonuçlarını kullanacak
