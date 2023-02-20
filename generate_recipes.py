from beet import Context, Recipe

woodtypes = ['oak', 'spruce', 'birch', 'jungle', 'acacia', 'dark_oak', 'mangrove', 'crimson', 'warped', 'bamboo', 'cherry']
objects = {
    'stairs': 1,
    'slab': 2,
    'fence': 1,
    'fence_gate': 1,
    'door': 1,
    'trapdoor': 1,
    'pressure_plate': 1,
    'button': 1,
    'sign': 1,
    'hanging_sign': 1
}

def isNetherWood(wood):
  return wood in ['crimson', 'warped']

def create_recipe(ctx, input, output, count):
  ctx.data[f'woodcutter:{output}'] = Recipe({
    'type': 'minecraft:stonecutting',
    'ingredient': {'item': f'minecraft:{input}'},
    'result': f'minecraft:{output}',
    'count': count
  })

def beet_default(ctx: Context):
  for woodtype in woodtypes:
    # log -> wood
    create_recipe(
      ctx,
      f'{woodtype}_{isNetherWood(woodtype) and "stem" or "log"}',
      f'{woodtype}_{isNetherWood(woodtype) and "hyphae" or "wood"}',
      1
    )
    # stripped_log -> stripped_wood
    create_recipe(
      ctx,
      f'stripped_{woodtype}_{isNetherWood(woodtype) and "stem" or "log"}',
      f'stripped_{woodtype}_{isNetherWood(woodtype) and "hyphae" or "wood"}',
      1
    )
    # objects
    for obj, count in objects.items():
      create_recipe(ctx, f'{woodtype}_planks', f'{woodtype}_{obj}', count)