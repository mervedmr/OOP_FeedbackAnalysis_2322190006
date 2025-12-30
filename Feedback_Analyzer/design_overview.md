# Design Overview
Customer Feedback and Sentiment Analysis Platform

## Purpose
This system collects feedback from customers about various products. 
It allows analyzing customer opinions using basic and advanced algorithms.

## Class Descriptions

### Customer
- Holds customer information (id, name)
>
### Product
- Holds product info.
- Aggregates multiple Feedback objects.
- Represents the main entity for analysis
>
### Feedback
- Stores text & rating.
- Linked to a Customer
>
### ReviewAnalyzer
- Designed as a separate analysis component
>
## Aggregation
- One Product contains multiple Feedback objects
Product -> many Feedback
>
## Simple Scenario
1. Create customer
2. Create product
3. Customer writes feedback
4. Add feedback to product
>


# Basic Implementation
Extends the architecture with basic functionality and algorithms.

### Added Features
- CRUD operations for Customer and Feedback
- Simple sentiment analysis (positive / neutral / negative)
- Word frequency analysis from feedback texts
- Sorting feedback by rating or sentiment

---

# Advanced Application
Completes the project by adding advanced analysis and application-level features.

### Added Features
- Trend detection over time (improving / declining sentiment)
- Product ranking based on average feedback ratings
- Detection of most frequent complaint topics
- Preparation for visualization and reporting
- Web-based CRUD operations and reporting pages (conceptual design)

---
