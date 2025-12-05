# Not: Bu dosya Stage 1.
# Stage 2’de CRUD, sentiment analizi ve trend algoritmaları buraya eklenecek.

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        # Not: İleride müşteri güncelleme/silme gibi CRUD işlemleri eklenebilir.


class Product:
    def __init__(self, product_id, name):
        self.product_id = product_id
        self.name = name
        self.feedback_list = []  # Aggregation (Product birçok Feedback tutar)
        # Not: Stage 2'de bu liste üzerinde silme, güncelleme, filtreleme eklenecek.

    def add_feedback(self, feedback):
        # Not: Şu an sadece ekleme var. CRUD'un C'si.
        self.feedback_list.append(feedback)


class Feedback:
    def __init__(self, customer, text, rating):
        self.customer = customer
        self.text = text
        self.rating = rating
        # Not: rating Stage 2’de sıralama için kullanılacak.
        # Not: text sentiment analizi için kullanılacak.


class ReviewAnalyzer:
    def analyze_sentiment(self, feedback):
        # Not: Stage 2’de keyword bazlı sentiment analizi yapılacak.
        pass

    def detect_trends(self, feedback_list):
        # Not: Stage 2’de kelime frekansı, trend analizleri buraya yazılacak.
        pass
