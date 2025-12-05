# Stage 1 – Design Overview

## Purpose
This system collects feedback from customers about various products. 
Stage 1 focuses only on architecture.

## Note for myself:
- Stage 2’de algoritmalar geleceği için sınıfları temel halinde bırak.
- ReviewAnalyzer şu an boş, ileride doldurulacak.

## Class Descriptions

### Customer
- Holds customer info.

### Product
- Holds product info.
- Aggregates multiple Feedback objects.
- Not: ileride Product içinde CRUD operasyonları için fonksiyonları yazman gerek.

### Feedback
- Stores text & rating.
- Not: sentiment analizi için metin önemli.

### ReviewAnalyzer
- Currently empty.
- Not: Stage 2’de word frequency ve sentiment işlemleri buraya gelecek.

## Aggregation
Product -> many Feedback

## Simple Scenario
1. Create customer
2. Create product
3. Customer writes feedback
4. Add feedback to product

## Note for myself:
- Stage 2’de bu senaryoya ek olarak sıralama, filtreleme gibi işlemler gelecek.
