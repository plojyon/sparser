import math

import matplotlib.pyplot as plt

import sparser


def weighted_euclidean(point1, point2=(0, 0), weights=(1, 1)):
    diff_x = point1[0] - point2[0]
    diff_y = point1[1] - point2[1]
    return math.sqrt(weights[0] * (diff_x ** 2) + weights[1] * (diff_y ** 2))


def performance_metric(item):
    """Return the greatness measure of a product (higher is better)."""
    # currently using a weighted euclidean distance as a performance metric
    x = item.ratio("protein", "price")
    y = item.ratio("protein", "kcal")
    return weighted_euclidean((x, y), weights=(1, 1))


products = sparser.data()

# filter non-food items, items priced per piece and items with incomplete data
filtered_products = list(
    filter(lambda x: x.has_values(["protein", "kcal", "price"]), products)
)

x = [item.ratio("protein", "price") for item in filtered_products]
y = [item.ratio("protein", "kcal") for item in filtered_products]
plt.scatter(x, y)
plt.xlabel("protein per price")
plt.ylabel("protein per kcal")

# top 10 products according to the current metric
filtered_products.sort(key=performance_metric, reverse=True)
print("Top 10 products:")
for i, product in enumerate(filtered_products[:150]):
    print(i + 1, product.name)
    plt.text(
        product.ratio("protein", "price"), product.ratio("protein", "kcal"), str(i)
    )

plt.show()
