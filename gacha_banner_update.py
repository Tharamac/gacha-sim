import json
from os import write

with open("gacha_config.json","r") as file:
    json_str = file.read()
gacha_config = json.loads(json_str)
print(gacha_config)

with open("README.md", "w+") as file:
    file.write("# Gacha Simulator\nDisclaimer: Not accurate in any games, just a edutainment purpose\n")
    for rarity in gacha_config.values():
        file.write("## %d stars character\n" % rarity["rarity"] )
        if "featured_probability" in rarity and "featured_items" in rarity:
            file.write("(Standard rate: %s; Chance to get featured character: %s; Remaining chance of each item are uniform)\n"
            % (rarity["probability"], rarity["featured_probability"])
            )
            for item in rarity["featured_items"]:
                file.write("- %s (UP)\n" % item)
            for item in rarity["items"]: 
                if item not in rarity["featured_items"]:
                    file.write("- %s\n" % item)
        else:
            file.write("(Standard rate: %s; Chances of each item are uniform)\n"
            % (rarity["probability"])
            )
            for item in rarity["items"]: 
                file.write("- %s\n" % item)
