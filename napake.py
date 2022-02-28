import sparser

all_products = sparser.data(use_blacklist=False)

# filter products with a defined net weight
products = list(filter(lambda x: x.has_value("weight"), all_products))

nutri_slo = {
    "sugar": "sladkorjev",
    "carbohydrates": "ogljikovih hidratov",
    "saturated_fat": "nasicenih mascob",
    "protein": "beljakovin",
    "fat": "mascob",
    "salt": "soli",
}

quantities = ["sugar", "carbohydrates", "fat", "saturated_fat", "protein", "salt"]
invalid = []
for item in products:
    for quantity in quantities:
        if item.has_value(quantity):
            if getattr(item, quantity) > 100:
                invalid.append(item.id)
    if item.has_values(["fat", "saturated_fat"]) and item.fat < item.saturated_fat:
        invalid.append(item.id)
    if item.has_values(["carbohydrates", "sugar"]) and item.carbohydrates < item.sugar:
        invalid.append(item.id)

print(list(set(invalid)))
