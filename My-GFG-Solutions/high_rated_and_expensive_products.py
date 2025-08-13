
'''
High-Rated and Expensive Products
Difficulty: MediumAccuracy: 54.97%Submissions: 273+Points: 4Average Time: 20m
Problem Description:
A product is considered high-rated and expensive if it meets the following conditions:

The product has a rating of at least 4.5.

The product is available in stock (quantity greater than 0).

The product price is at least $300.

Pandas Schema:
+---------------------+--------+
| Column Name         | Type   |
+---------------------+--------+
| product_id          | int    |
| product_name        | string |
| rating              | float  |
| quantity_in_stock   | int    |
| price               | float  |
+---------------------+--------+

product_id: Unique ID for each product (Primary key).

product_name: The name of the product.

rating: The rating of the product (float, ranging from 1 to 5).

quantity_in_stock: The number of units available in stock.

price: The price of the product.

Task:
Write a solution to find the product_id, product_name, rating, quantity_in_stock, and price of all products that are high-rated, in stock, and expensive based on the criteria above.

Return the result table in any order.

Example :
Input table:

+------------+---------------------+--------+--------------------+---------+
| product_id | product_name        | rating | quantity_in_stock  | price   |
+------------+---------------------+--------+--------------------+---------+
| 101        | iPhone 13           | 4.8    | 10                 | 999.99  |
| 102        | Samsung Galaxy S21  | 4.2    | 0                  | 799.99  |
| 103        | MacBook Pro 16      | 4.7    | 5                  | 2399.99 |
| 104        | AirPods Pro         | 4.4    | 3                  | 249.99  |
| 105        | Sony WH-1000XM4     | 4.9    | 2                  | 349.99  |
| 106        | LG OLED TV          | 4.6    | 15                 | 1499.99 |
| 107        | Samsung QLED TV     | 4.7    | 12                 | 1799.99 |
| 108        | Dell XPS 13         | 4.8    | 8                  | 1499.99 |
| 109        | Microsoft Surface   | 4.6    | 4                  | 1299.99 |
| 110        | Bose QuietComfort   | 4.9    | 7                  | 399.99  |
+------------+---------------------+--------+--------------------+---------+

Expected Output :

+-------------+--------------+--------+------------------+----------+
| product_id  | product_name | rating | quantity_in_stock| price    |
+-------------+--------------+--------+------------------+----------+
| 101         | iPhone 13    | 4.8    | 10               | 999.99   |
| 103         | MacBook Pro 16| 4.7    | 5                | 2399.99  |
| 105         | Sony WH-1000XM4| 4.9    | 2                | 349.99   |
| 107         | LG OLED TV   | 4.7    | 12               | 1799.99  |
| 108         | Samsung QLED TV| 4.6   | 15               | 1499.99  |
| 109         | Dell XPS 13  | 4.8    | 8                | 1499.99  |
| 110         | Microsoft Surface| 4.6 | 4                | 1199.99  |
| 111         | Bose QuietComfort| 4.9 | 7                | 399.99   |
+-------------+--------------+--------+------------------+----------+

'''

import pandas as pd # type: ignore

def filter_high_rated_expensive(df):
    filtered_df = df[
        (df['rating'] >= 4.5) & 
        (df['quantity_in_stock'] > 0) & 
        (df['price'] >= 300)
    ]
    
    return filtered_df[['product_id', 'product_name', 'rating', 'quantity_in_stock', 'price']]