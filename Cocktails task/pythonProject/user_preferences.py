import re

user_preferences = {}

ingredient_list = [
    "vodka", "rum", "gin", "tequila", "whiskey", "brandy", "lemon", "lime", "mint",
    "sugar", "honey", "orange", "pineapple", "coconut", "strawberry", "blueberry",
    "coffee", "cream", "vanilla", "chocolate"
]

def update_user_preferences(user, text):
    """Updating user info"""
    if user not in user_preferences:
        user_preferences[user] = {"likes": set(), "dislikes": set(), "allergies": set()}

    detected_likes = {ing for ing in ingredient_list if re.search(rf'\b{ing}\b', text.lower())}
    detected_dislikes = set()
    detected_allergies = set()

    if any(keyword in text.lower() for keyword in ["i don’t like", "i don't like", "i dislike", "avoid"]):
        detected_dislikes = {ing for ing in ingredient_list if re.search(rf'\b{ing}\b', text.lower())}

    if any(keyword in text.lower() for keyword in ["i'm allergic to", "i am allergic to"]):
        detected_allergies = {ing for ing in ingredient_list if re.search(rf'\b{ing}\b', text.lower())}

    detected_likes -= detected_dislikes
    detected_likes -= detected_allergies

    user_preferences[user]["likes"].update(detected_likes)
    user_preferences[user]["dislikes"].update(detected_dislikes)
    user_preferences[user]["allergies"].update(detected_allergies)

    return detected_likes, detected_dislikes, detected_allergies