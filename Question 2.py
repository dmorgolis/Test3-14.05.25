
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("Current working directory:", os.getcwd())


customers = pd.read_csv("customers.csv")
items = pd.read_csv("Items.csv")
order_items = pd.read_csv("order_item.csv")
orders = pd.read_csv("orders.csv")

print("Customers:")
print(customers.head())

print("\nItems:")
print(items.head())

print("\nOrder Items:")
print(order_items.head())

print("\nOrders:")
print(orders.head())


# תשובות לשאלה 2
# 1. מה מחיר ממוצע של פריט?

average_price = items["item_price"].mean()
print("\nמחיר ממוצע של פריט:", round(average_price, 2))

#  תשובה ‣ המחיר הממוצע הוא: 2222.08

# 2. מי הלקוח שרכש הכי הרבה מוצרים?

merged = pd.merge(order_items, orders, on="order_id")

merged = pd.merge(merged, customers, on="customer_id")

customer_totals = merged.groupby(["first_name", "last_name"])["quantity"].sum()

top_customer = customer_totals.idxmax()
top_quantity = customer_totals.max()

print("\nהלקוח שרכש הכי הרבה מוצרים:", top_customer, "סה\"כ כמות:", top_quantity)


# תשובה ‣ הלקוח הוא: Ellary Ledner, שרכש 45 מוצרים


# 3.עמודת total_price המחושבת (מחיר × כמות):

order_items_merged = pd.merge(order_items, items, on="item_id")

order_items_merged["total_price"] = order_items_merged["quantity"] * order_items_merged["item_price"]

print("\nטבלת Order Items עם total_price:")
print(order_items_merged.head())



# חלק שני בשאלה 2

customers_clean = customers.dropna()

# חלק 1: פילוג לקוחות לפי gender
plt.figure(figsize=(6, 4))
sns.countplot(data=customers_clean, x='gender')
plt.title("פילוג לקוחות לפי מגדר")
plt.xlabel("מגדר")
plt.ylabel("כמות לקוחות")
plt.show()

# חלק 2: פילוג לפי לאום (nationality)
plt.figure(figsize=(8, 5))
sns.countplot(data=customers_clean, x='nationality', order=customers_clean['nationality'].value_counts().index)
plt.title("פילוג לקוחות לפי לאום")
plt.xlabel("לאום")
plt.ylabel("כמות")
plt.xticks(rotation=45)
plt.show()

# חלק 3: היסטוגרמה לפי גיל
plt.figure(figsize=(6, 4))
sns.histplot(data=customers_clean, x='age', bins=10, kde=True)
plt.title("התפלגות גיל לקוחות")
plt.xlabel("גיל")
plt.ylabel("כמות")
plt.show()
