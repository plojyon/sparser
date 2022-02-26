from pulp import LpMinimize, LpProblem, LpStatus, lpSum, LpVariable, PULP_CBC_CMD

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

model = LpProblem(name="diet", sense=LpMinimize)
variables = []
for product in products:
    # use category: "Continuous" | "Integer"
    variables.append(LpVariable(name=product.name, lowBound=0, cat="Continuous"))

# objective function (to be minimized): sum cost[i] * count[i] for all products
# (price is in eur/g, but nutri is per 100g, so multiply each price by 100)
total_price = lpSum([prod.price * 100 * var for prod, var in zip(products, variables)])
# add the objective function to the model
model += total_price

# add constraints
for nutri, recommended_amount in daily_recommended.items():
    total_nutri = lpSum(
        [getattr(prod, nutri) * var for prod, var in zip(products, variables)]
    )
    max = recommended_amount * (1 + max_variance)
    min = recommended_amount * (1 - max_variance)
    model += (total_nutri <= max, f"max {nutri} constraint")
    model += (total_nutri >= min, f"min {nutri} constraint")

# commence optimization
status = model.solve(PULP_CBC_CMD(msg=0))
print(f"Status: {model.status}, {LpStatus[model.status]}")

print()
print(f"Your daily meal costs only {model.objective.value():.2f} EUR:")
for i, var in enumerate(model.variables()):
    count = var.value()
    # Some coefficients end up in sub-nanogram quantities, so we ignore them
    if count * 100 < 1:
        # if count != 0:
        #     print(f"A bit of {products[item].name}")
        continue
    print(
        f"{count*100:.2f}g of {var.name} (full price: {products[i].price*products[i].weight:.2f} eur for {products[i].weight:.0f}g)"
    )
print(
    f"You will consume a total of {sum([v.value() for v in model.variables()])*100:.2f}g of food."
)
