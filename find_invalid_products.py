import sparser

all_products = sparser.data(use_blacklist=False)

# filter products with a defined neto weight
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

for item in products:
    for quantity in quantities:
        if item.has_value(quantity):
            if getattr(item, quantity) > 100:
                print(
                    "{id}: {name} ima {value}g {quantity} na 100g produkta".format(
                        id=item.id,
                        name=item.name,
                        value=getattr(item, quantity),
                        quantity=nutri_slo[quantity],
                        weight=item.weight,
                    )
                )
    if item.has_values(["fat", "saturated_fat"]) and item.fat < item.saturated_fat:
        print(
            "{id}: {name} ima {fat}g mascob, od tega {saturated}g nasicenih".format(
                id=item.id,
                name=item.name,
                fat=item.fat,
                saturated=item.saturated_fat,
            )
        )
    if item.has_values(["carbohydrates", "sugar"]) and item.carbohydrates < item.sugar:
        print(
            "{id}: {name} ima {ch}g ogljikovih hidratov, od tega {sugar}g sladkorjev".format(
                id=item.id,
                name=item.name,
                ch=item.carbohydrates,
                sugar=item.sugar,
            )
        )
