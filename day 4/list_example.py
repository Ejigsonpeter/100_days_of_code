states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                      "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", 
                      "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", 
                      "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", 
                      "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                        "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america)

print(f"first state of join the union is the state of  {states_of_america[0]}")

#overwriting a list
states_of_america[0] = "Delawares"
print(states_of_america)

#adding to a list 
states_of_america.append("Abuja")

print(states_of_america)

#extend a  list
states_of_america.extend(["Lagos","Kaduna","Enugu"])
print(states_of_america)

fruits = ["Strawberries","Spinach","Kale","Nectarines","Apples","Grapes","Peaches","Cherries","Pears","Tomatoes","Celery","Potatoes"]
vegetables = ["Avocados",
"Sweet corn",
"Pineapples",
"Cabbages",
"Onions",
"Sweet peas (frozen)",
"Papayas",
"Asparagus",
"Mangoes",
"Eggplants",
"Honeydew melons",
"Kiwis",
"Cantaloupes",
"Cauliflower",
"Broccoli"]

dirty_veg = [fruits,vegetables]
print(dirty_veg)
print(dirty_veg[0][0])
