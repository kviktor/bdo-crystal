import json
import re


with open("input.cs", "r") as f:
    data = map(lambda x: x.strip(), f.readlines())

regex = re.compile(
    '.*Name = "(.+)", ItemEffect = "(.+)", Shattering = "(.+)", '
    'Slot = Slot\.([A-Za-z]+)\.ToString\(\), .*, '
    'Rarity = Rarity\.([A-Za-z]+)\.ToString\(\).*'
)

crystals = []
for l in data:
    if not l.startswith("crystals.Add"):
        continue

    m = re.search(regex, l)
    if m:
        name, effect, shattering, slot, rarity = m.groups()
        crystals.append({
            'name': name,
            'effect': effect,
            'shattering': shattering,
            'slot': slot,
            'rarity': rarity,
        })
    else:
        print(l)

with open("crystals.json", "w") as f:
    json.dump(crystals, f, indent=4)
