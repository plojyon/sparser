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
            ["price", "weight"] + [nutri for nutri in daily_recommended.keys()]
        ),
        sparser.data(),
    )
)

# objective function (to be minimized): sum cost[i] * count[i] for all products
# (price is in eur/g, but nutri is per 100g, so multiply each price by 100)
objective_coefficients = [product.price * 100 for product in products]


# inequalities coefficients: for every nutri, sum: nutri[i] * count[i] for all products
nutri_coefficients_min = [
    [-getattr(product, nutri) for product in products] for nutri in daily_recommended
]
nutri_coefficients_max = [
    [+getattr(product, nutri) for product in products] for nutri in daily_recommended
]
# on the rhs, we have the bounding values (recommended intake +- variance)
nutri_content_min = [value * (max_variance - 1) for value in daily_recommended.values()]
nutri_content_max = [value * (1 + max_variance) for value in daily_recommended.values()]

# demand at least 1.5kg of food per day
neto_min_lhs = [[-100 for product in products]]  # every food weighs 100g
neto_min_rhs = [-1500]

# demand at least one bounty a day
bounty_lhs = [[0 for product in products]]
bounty_lhs[0][sparser.index_of(products, name="bounty, 228g")] = -100
bounty_rhs = [-28.5]  # one bounty is 57g, contains 2 bars


lhs_inequalities = (
    nutri_coefficients_min + nutri_coefficients_max + neto_min_lhs + bounty_lhs
)
rhs_inequalities = nutri_content_min + nutri_content_max + neto_min_rhs + bounty_rhs

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

print()
print(f"Your daily meal costs only {optimum.fun:.2f} EUR:")
for item, count in enumerate(optimum.x):
    # Some coefficients end up in sub-nanogram quantities, so we ignore them
    if count * 100 < 1:
        # if count != 0:
        #     print(f"A bit of {products[item].name}")
        continue
    print(
        f"{count*100:.2f}g of {products[item].name} (full price: {products[item].price*products[item].weight:.2f} eur for {products[item].weight:.0f}g)"
    )
print(f"You will consume a total of {sum(optimum.x)*100:.2f}g of food.")
