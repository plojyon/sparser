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
            if getattr(item, quantity) > item.weight:
                print(
                    "{id}: {name} ima {value}g {quantity}, skupno {weight:.0f}g".format(
                        id=item.id,
                        name=item.name,
                        value=getattr(item, quantity),
                        quantity=nutri_slo[quantity],
                        weight=item.weight,
                    )
                )
