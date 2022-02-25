import json
import os
import re

from .blacklist import blacklist

# unit histogram
# {'kos': 2286, '': 6, 'ml': 7, 'kg': 867, 'g': 7353, 'l': 4641, 'm': 27}


class Item:
    def __init__(self, item):
        self.data = item

    @property
    def id(self):
        regex = r"https://www\.spar\.si/online/.+/p/(\d+).*"
        match = re.search(regex, self.url)
        if match is not None:
            return int(match.group(1))

    def is_blacklisted(self):
        """Check if product is known to contain bad data.

        Such products are filtered out by default, so normally this should
        always return False.
        """
        return self.id in blacklist

    @classmethod
    def normalize_weight_string(cls, weight_string):
        """Convert weight string to float in grams."""
        weight = float("".join(re.findall("[0-9\,]+", weight_string)).replace(",", "."))

        if "kg" in weight_string or "l" in weight_string:
            return weight * 1000

        if "G" in weight_string or "g" in weight_string or "ml" in weight_string:
            return weight

        # print("Invalid weight string", weight_string)
        return None

    @classmethod
    def normalize_price_string(cls, price_string):
        """Convert price string to float in eur/g.

        Accept a string representing the price per unit weight or volume, e.g.
        "12 eur/kg" and returns a float in units of eur/g.

        If the product is priced per piece, return None.
        """
        if len(price_string.split()) < 2:
            return None
        price = float(price_string.split()[0].replace(",", "."))
        unit = price_string.split()[1]

        if "kg" in unit or "l" in unit:
            return price / 1000

        if "ml" in unit or "g" in unit:
            return price

        if "kos" not in unit and "m" not in unit and "Pieces" not in unit:
            # print("Invalid price string", price_string)
            pass

        return None

    @property
    def url(self):
        return self.data.get("url", "")

    @property
    def price(self):
        """Return the price in EUR."""
        data = self.data.get("product-priceperunit")
        if data is None:
            return None
        return Item.normalize_price_string(data)

    @property
    def weight(self):
        """Return the weight in grams. Water density is assumed for liquids."""
        data = (
            self.data.get("product-info", {})
            .get("product-net-cont", {})
            .get("neto-količina")
        )
        if data is None:
            return None
        return Item.normalize_weight_string(data)

    def _get_nutritional_info(self, attribute):
        data = (
            self.data.get("product-info", {})
            .get("povprečna-hranilna-vrednost", {})
            .get(attribute)
        )
        if data is None:
            return None

        if attribute not in ["kcal", "kj"]:  # normalize unit (if there is one)
            return Item.normalize_weight_string(data)
        else:
            return float(data.replace(",", "."))

    @property
    def name(self):
        """Return the unmodified full name of the product."""
        data = self.data.get("title", "Untitled product")
        return data

    def ratio(self, attr1, attr2):
        """Return a ratio of two attributes or None."""
        a1 = getattr(self, attr1)
        a2 = getattr(self, attr2)
        if a1 is None or a2 is None or a2 == 0:
            return None
        return a1 / a2

    def has_values(this, fields, allow_zero=False):
        """Check if Item has nonzero data in given fields.

        If allow_zero is True, only check if data is present.
        """
        for field in fields:
            if not hasattr(this, field):
                return False
            if getattr(this, field) is None:
                return False
            if getattr(this, field) == 0 and not allow_zero:
                return False
        return True

    def has_value(this, field, allow_zero=False):
        """Same as has_values, but for one field only."""
        return this.has_values([field], allow_zero)


nutritional_info = {
    "sugar": "Sugar",
    "carbohydrates": "Total Carbohydrate",
    "saturated_fat": "Saturated fat",
    "protein": "Protein",
    "fat": "Total Fat",
    "kcal": "kcal",
    "salt": "Salt",
    "kj": "kJ",
}
# add nutrirional attributes
for attr in nutritional_info:
    attr_name = nutritional_info[attr]
    setattr(
        Item,
        attr,
        property(
            lambda this, attr_name=attr_name: this._get_nutritional_info(attr_name)
        ),
    )


def data(location="./sparsed/", use_blacklist=True, parse=True):
    """Fetch spar data from a local source.

    :param use_blacklist: use a provided blacklist to ignore bad products
    :param parse: return an array of Item objects instead of raw JSON
    """
    # fetch local data
    products = []
    for filename in os.listdir(location):
        with open(os.path.join(location, filename), "r") as file:
            data = json.loads(file.read())
            data["local_path"] = os.path.join(location, filename)

            if not parse:
                products.append(data)
                continue

            item = Item(data)

            if not use_blacklist or not item.is_blacklisted():
                products.append(item)

    return products
