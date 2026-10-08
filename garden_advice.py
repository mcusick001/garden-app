def get_user_input():
    season = input("Enter the season (e.g. summer, winter): ").strip().lower()
    plant_type = input("Enter the plant type (e.g. flower, vegetable): ").strip().lower()
    return season, plant_type

def get_gardening_advice(season, plant_type):
    SEASON_ADVICE = {
        "summer": "Water your plants regularly and provide some shade.\n",
        "winter": "Protect your plants from frost with covers.\n"
    }

    PLANT_ADVICE = {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests!"
    }

    advice = ""
    advice += SEASON_ADVICE.get(season, "No advice for this season.\n")
    advice += PLANT_ADVICE.get(plant_type, "No advice for this type of plant.")

    return advice

if __name__ == "__main__":
    user_season, user_plant = get_user_input()
    generated_advice = get_gardening_advice(user_season, user_plant)
    print(f"\n{generated_advice}")