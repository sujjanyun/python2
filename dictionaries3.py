murakami = {
    "animal": "cat",
    "setting": "japan",
    "music": "classical",
    "genre": "surrealism"
}

print(murakami)

murakami["animal"] = "dog"

if "setting" in murakami:
    del murakami["setting"]

print(murakami)