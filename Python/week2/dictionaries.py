# dictionaries are an ordered collection of key and value pairs
capital_city = {"Kenya":"Nairobi","Rwanda":"Kigali","Uganda":"Kampala"}
print(capital_city)

# adding elements to a dictionary
capital_city["Japan"]="Tokyo"
print(capital_city)

# deleting items we use the key
del capital_city["Uganda"]
print(capital_city)

# to update we use key
capital_city["Kenyan"] = "Mombasa"
print(capital_city)

# access elements we use key
print(capital_city["Kenyan"] )

# to show if an item exists/membership we use keyword in
print("Kenya" in capital_city)

# iterating through a dictionary
for city in capital_city:
    print(capital_city[city])