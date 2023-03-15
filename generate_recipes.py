from beet import Context, Recipe
import yaml

with open('config.yml', 'r') as file:
  config = yaml.safe_load(file)

def create_recipe(ctx, input, output, count):
  ctx.data[f'woodcutter:{output}'] = Recipe({
    'type': 'minecraft:stonecutting',
    'ingredient': {'item': f'minecraft:{input}'},
    'result': f'minecraft:{output}',
    'count': count
  })

def beet_default(ctx: Context):
  for wood in config["types"]:
    if type(wood) is str:
      wood = {
        'name': wood,
        'type': 'normal'
      }

    # log -> wood
    create_recipe(
      ctx,
      f'{wood["name"]}_{wood["type"] == "nether" and "stem" or "log"}',
      f'{wood["name"]}_{wood["type"] == "nether" "hyphae" or "wood"}',
      config["counts"]["wood"]
    )

    # stripped_log -> stripped_wood
    create_recipe(
      ctx,
      f'stripped_{wood["name"]}_{wood["type"] == "nether" and "stem" or "log"}',
      f'stripped_{wood["name"]}_{wood["type"] == "nether" and "hyphae" or "wood"}',
      config["counts"]["stripped_wood"]
    )

    # items
    for item in config["items"]:
      if type(item) is str:
        item = {
          'name': item,
          'count': 1
        }
      create_recipe(ctx, f'{wood["name"]}_planks', f'{wood["name"]}_{item["name"]}', item["count"])