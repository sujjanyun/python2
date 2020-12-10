murakami = {
    "animal": "cat",
    "setting": "japan",
    "music": "classical",
    "genre": "surrealism"
}

print(murakami)

murakami["food"] = "eggs"

print(murakami)

if "surrealism" in murakami and "surrealism" == True:
    print("Murakami loves SURREALISM")
else:
    print("MURAKAMI does not love surrealism :(")