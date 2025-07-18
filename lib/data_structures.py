spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    """
    Return a list of the names of each spicy food.
    """
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """
    Return a list of spicy foods with heat_level > 5.
    """
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    """
    Print each spicy food in the format:
    "Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶"
    where the number of pepper emojis equals the heat level.
    """
    for food in spicy_foods:
        peppers = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {peppers}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """
    Return the first spicy food whose cuisine matches the given cuisine.
    """
    for food in spicy_foods:
        if food["cuisine"].lower() == cuisine.lower():
            return food
    return None

def print_spiciest_foods(spicy_foods):
    """
    Print only the spicy foods with heat_level > 5 using the same
    format as print_spicy_foods().
    """
    print_spicy_foods(get_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    """
    Return the average heat level (an int) for the list of spicy foods.
    """
    if not spicy_foods:
        return 0
    total = sum(food["heat_level"] for food in spicy_foods)
    return int(total / len(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    """
    Return a new list containing the original spicy foods plus the new one.
    Does NOT mutate the original list.
    """
    new_list = spicy_foods.copy()
    new_list.append(spicy_food)
    return new_list
