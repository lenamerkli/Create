from os.path import join

ROOT = '../src/generated/resources/data/create/recipes/mini_scaled/'
TEMPLATE_A = """
{
  "type": "create:mechanical_crafting",
  "acceptMirrored": false,
  "key": {
    "A": {
      "item": "minecraft:$color_stained_glass"
    },
    "P": {
      "item": "minecraft:obsidian"
    },
    "S": {
      "item": "minecraft:nether_star"
    }
  },
  "pattern": [
    " AAA ",
    "AAPAA",
    "APSPA",
    "AAPAA",
    " AAA "
  ],
  "result": {
    "count": 8,
    "item": "mini_scaled:scale_box_item",
    "data": {
      "size": 4,
      "color": "$color"
    }
  }
}
"""
TEMPLATE_B = """
{
  "type": "minecraft:crafting_shaped",
  "pattern": [
    "AAA",
    "ABA",
    "AAA"
  ],
  "key": {
    "A": {
      "item": "minecraft:$ingot"
    },
    "B": {
      "item": "mini_scaled:scale_box_item",
      "data": {
        "require": {
          "size": $org_size,
          "color": "$color"
        }
      }
    }
  },
  "result": {
    "count": 1,
    "item": "mini_scaled:scale_box_item",
    "data": {
      "size": $size,
      "color": "$color"
    }
  }
}
"""
COLORS = ["white", "yellow", "orange", "red", "pink", "magenta", "purple", "blue", "light_blue", "cyan", "lime",
          "green", "brown", "black", "gray", "light_gray"]
INGOTS = ["iron_ingot", "gold_ingot", "diamond"]


def write(size, color, data):
    path = join(ROOT, f"scale_box_item_{size}_{color}.json")
    with open(path, 'w') as f:
        f.write(data)


def main():
    for color in COLORS:
        write(4, color, TEMPLATE_A.replace('$color', color))
        for i, ingot in enumerate(INGOTS):
            org_size = str(pow(2, 2 + i))
            size = str(pow(2, 3 + i))
            write(size, color, TEMPLATE_B.replace('$size', size).replace('$org_size', org_size)
                  .replace('$color', color).replace('$ingot', INGOTS[i]))


if __name__ == '__main__':
    main()
