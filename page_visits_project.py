import codecademylib3
import pandas as pd

visits = pd.read_csv("visits.csv", parse_dates=[1])
cart = pd.read_csv("cart.csv", parse_dates=[1])
checkout = pd.read_csv("checkout.csv", parse_dates=[1])
purchase = pd.read_csv("purchase.csv", parse_dates=[1])

print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

# percent of users who visited Cool T-Shirts Inc. and not place a t-shirt in their cart
visits_cart_df = pd.merge(visits, cart, how="left")
print(visits_cart_df.shape)
print(visits_cart_df.head())

cart_time_null = len(visits_cart_df[visits_cart_df["cart_time"].isnull()])

percentage_not_place_tshirt = float(cart_time_null) / len(visits_cart_df)
print(percentage_not_place_tshirt)

# percentage of users that put items in their cart, but did not proceed to checkout
cart_checkout_left = pd.merge(cart, checkout, how="left")
checkout_time_null = len(
    cart_checkout_left[cart_checkout_left["checkout_time"].isnull()]
)
percentage_not_checkout = float(checkout_time_null) / len(cart_checkout_left)
print(percentage_not_checkout)

all_data = (
    visits.merge(cart, how="left")
    .merge(checkout, how="left")
    .merge(purchase, how="left")
)
print(all_data.head())

# percentage of users that proceeded to checkout, but did not purchase a t-shirt
checkout_purchase_left = pd.merge(checkout, purchase, how="left")
purchase_time_null = len(
    checkout_purchase_left[checkout_purchase_left["purchase_time"].isnull()]
)
percentage_not_purchase = float(purchase_time_null) / len(checkout_purchase_left)
print(percentage_not_purchase)

# calculates the time spent in the store of those who bought something
all_data["total_time"] = all_data["purchase_time"] - all_data["visit_time"]

print(all_data.head())

# average time from entering the store until buying something
average_time = all_data["total_time"].mean()
print(average_time)
