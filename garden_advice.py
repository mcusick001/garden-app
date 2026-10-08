def get_user_input():
    season = input("Enter the season (e.g. summer, winter): ").strip().lower()
    plant_type = input("Enter the plant type (e.g. flower, vegetable): ").strip().lower()
    return season, plant_type

def get_gardening_advice(season, plant_type):
    advice = ""

    # Determine advice based on the season
    if season == "summer":
        advice += "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        advice += "Protect your plants from frost with covers.\n"
    else:
        advice += "No advice for this season.\n"

    # Determine advice based on the plant type
    if plant_type == "flower":
        advice += "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        advice += "Keep an eye out for pests!"
    else:
        advice += "No advice for this type of plant."

    return advice

if __name__ == "__main__":
    user_season, user_plant = get_user_input()
    generated_advice = get_gardening_advice(user_season, user_plant)
    print(f"\n{generated_advice}")