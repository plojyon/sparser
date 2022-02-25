import json

import sparser

products = sparser.data(parse=False)

with open("sparsed.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(products))
