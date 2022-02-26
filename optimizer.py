import scipy
from scipy.optimize import linprog

import sparser

daily_recommended = {
    "kcal": 2000,
    "carbohydrates": 260,
    "fat": 70,
    "saturated_fat": 20,
    "sugar": 89,
    "protein": 50,
    "salt": 6,
}
max_variance = 0.1

products = list(
    filter(
        lambda x: x.has_values(
            ["price"] + [nutri for nutri in daily_recommended.keys()]
        ),
        sparser.data(),
    )
)

# objective function (to be minimized): sum cost[i] * count[i] for all products
objective_coefficients = [product.price for product in products]


# inequalities coefficients: for every nutri, sum: nutri[i] * count[i] for all products
nutri_coefficients_min = [
    [-getattr(product, nutri) for product in products] for nutri in daily_recommended
]
nutri_coefficients_max = [
    [getattr(product, nutri) for product in products] for nutri in daily_recommended
]
# on the rhs, we have the bounding values
nutri_content_min = [value * (max_variance - 1) for value in daily_recommended.values()]
nutri_content_max = [value * (1 + max_variance) for value in daily_recommended.values()]

lhs_inequalities = nutri_coefficients_min + nutri_coefficients_max
rhs_inequalities = nutri_content_min + nutri_content_max

# commence optimization
optimum = linprog(
    c=objective_coefficients,
    A_ub=lhs_inequalities,
    b_ub=rhs_inequalities,
    # A_eq=lhs_equalities,
    # b_eq=rhs_equalities,
    bounds=[(0, float("inf")) for product in products],
    method="revised simplex",
)


print(f"After {optimum.nit} iterations, {optimum.message}")

if not optimum.success:
    exit(1)

print(f"Optimal price: {optimum.fun}")

with open("optimum.txt", "w", encoding="utf-8") as f:
    f.write(str(list(optimum.x)))
print("Saved to optimum.txt")

print()
print(f"Your daily meal costs only {optimum.fun:.4f} EUR:")
for item, count in enumerate(optimum.x):
    # Some coefficients end up in sub-nanogram quantities, so we ignore them
    if count < 0.1:
        # if count != 0:
        #     print(f"A bit of {products[item].name}")
        continue
    print(f"{count:.2f}g of {products[item].name}")
print(f"You will consume a total of {sum(optimum.x):.2f}g of food.")
