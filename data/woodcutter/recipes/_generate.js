const fs = require('fs')

const woodtypes = ['oak', 'spruce', 'birch', 'jungle', 'acacia', 'dark_oak', 'mangrove', 'crimson', 'warped']
const objects = {
    'stairs': 1,
    'slab': 2,
    'fence': 1,
    'fence_gate': 1,
    'door': 1,
    'trapdoor': 1,
    'pressure_plate': 1,
    'button': 1,
    'sign': 1
}

function recipe(from, to, count) {
    fs.writeFileSync(
        `${to}.json`,
        JSON.stringify(
            {
                type: 'minecraft:stonecutting',
                ingredient: {item: `minecraft:${from}`},
                result: `minecraft:${to}`,
                count
            }
        )
    )
}

const isNetherWood = (w) => ['crimson', 'warped'].includes(w)

for(const wood of woodtypes) {
    for(const object in objects) {
        recipe(`${wood}_planks`, `${wood}_${object}`, objects[object])
    }
    recipe(
        `${wood}_${isNetherWood(wood) ? 'stem' : 'log'}`,
        `${wood}_${isNetherWood(wood) ? 'hyphae' : 'wood'}`,
        1
    )
    recipe(
        `stripped_${wood}_${isNetherWood(wood) ? 'stem' : 'log'}`,
        `stripped_${wood}_${isNetherWood(wood) ? 'hyphae' : 'wood'}`,
        1
    )
}