# Personal Health Advisor

def calculate_bmi(_weight, _height):
    """Calculate BMI given weight in kg and height in meters."""
    _bmi = _weight / (_height ** 2)
    return round(_bmi, 2)

def get_bmi_recommendation(_bmi):
    """Provide BMI-based health recommendations."""
    if _bmi < 18.5:
        return "Underweight"
    elif 18.5 <= _bmi < 24.9:
        return "Normal weight"
    elif 25 <= _bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def calculate_daily_water_intake(_weight, _age):
    """Calculate daily water intake in liters based on weight and age."""
    _water_intake = _weight * 0.033
    if _age < 18:
        _water_intake += 0.5
    elif _age > 55:
        _water_intake -= 0.3
    return round(_water_intake, 2)

def recommend_calories(_age, _gender, _height_cm, _weight, _activity_level):
    """Recommend daily calorie intake based on personal factors."""
    _bmr = (10 * _weight + 6.25 * _height_cm - 5 * _age + (5 if _gender == 'male' else -161))
    _activity_factors = {'sedentary': 1.2, 'moderate': 1.55, 'active': 1.75, 'very active': 2.0}
    _multiplier = _activity_factors.get(_activity_level)
    if not _multiplier:
        return "Invalid activity level"
    return round(_bmr * _multiplier, 2)

def recommend_sleep(_age):
    """Recommend sleep duration based on age."""
    if _age < 6:
        return "Toddlers need about 11-14 hours of sleep daily."
    elif 6 <= _age <= 13:
        return "Children need 9-11 hours of sleep daily."
    elif 14 <= _age <= 17:
        return "Teenagers need 8-10 hours of sleep daily."
    elif 18 <= _age <= 64:
        return "Adults need 7-9 hours of sleep daily."
    else:
        return "Older adults need 7-8 hours of sleep daily."

def calculate_heart_rate_zones(_age, _resting_heart_rate):
    """Calculate heart rate zones based on age and resting heart rate."""
    _max_heart_rate = 220 - _age
    return {
        "Moderate (50-70%)": (
            round((_max_heart_rate - _resting_heart_rate) * 0.5 + _resting_heart_rate),
            round((_max_heart_rate - _resting_heart_rate) * 0.7 + _resting_heart_rate)),
        "Vigorous (70-85%)": (
            round((_max_heart_rate - _resting_heart_rate) * 0.7 + _resting_heart_rate),
            round((_max_heart_rate - _resting_heart_rate) * 0.85 + _resting_heart_rate)),
    }

def recommend_exercises(_bmi):
    """Recommend exercises based on BMI."""
    if _bmi < 18.5:
        return "Focus on muscle-building exercises like weightlifting and yoga."
    elif 18.5 <= _bmi < 24.9:
        return "Maintain your fitness with a mix of cardio and strength training."
    elif 25 <= _bmi < 29.9:
        return "Prioritize cardio exercises like walking, swimming, or cycling."
    else:
        return "Low-impact exercises like water aerobics or walking are recommended."

def calculate_macros(_calories):
    """Calculate macronutrient breakdown in grams."""
    return {
        "Protein (g)": round(0.3 * _calories / 4, 2),
        "Carbs (g)": round(0.4 * _calories / 4, 2),
        "Fats (g)": round(0.3 * _calories / 9, 2)
    }

def suggest_meal_plan(_bmi, _food_preference):
    """Suggest a simple meal plan based on BMI and food preference."""
    meal_plans = {
        "underweight": {
            "Breakfast": "Avocado toast with eggs (400 kcal)",
            "Lunch": "Grilled chicken salad with quinoa and nuts (600 kcal)",
            "Snack": "Banana smoothie with almond milk and protein powder (300 kcal)",
            "Dinner": "Grilled salmon with sweet potatoes and broccoli (550 kcal)"
        },
        "normal": {
            "Breakfast": "Oatmeal with fruits and nuts (350 kcal)",
            "Lunch": "Grilled chicken salad with quinoa and avocado (500 kcal)",
            "Snack": "Greek yogurt with berries and honey (200 kcal)",
            "Dinner": "Baked salmon with roasted vegetables and quinoa (450 kcal)"
        },
        "overweight": {
            "Breakfast": "Low-fat yogurt with fruits and granola (250 kcal)",
            "Lunch": "Grilled chicken salad with mixed greens and vinaigrette (400 kcal)",
            "Snack": "Carrot sticks with hummus (150 kcal)",
            "Dinner": "Grilled chicken breast with roasted vegetables and brown rice (350 kcal)"
        },
        "obese": {
            "Breakfast": "Black coffee with sugar-free sweetener (0 kcal)",
            "Lunch": "Salad with mixed greens, cherry tomatoes, and vinaigrette (200 kcal)",
            "Snack": "Raw vegetables with low-fat ranch dressing (100 kcal)",
            "Dinner": "Grilled chicken breast with steamed broccoli and brown rice (250 kcal)"
        }
    }

    if _bmi < 18.5:
        meal_plan = meal_plans["underweight"]
    elif 18.5 <= _bmi < 24.9:
        meal_plan = meal_plans["normal"]
    elif 25 <= _bmi < 29.9:
        meal_plan = meal_plans["overweight"]
    else:
        meal_plan = meal_plans["obese"]

    if _food_preference == "vegetarian":
        meal_plan["Dinner"] = "Lentil soup with whole grain bread (400 kcal)"
    elif _food_preference == "gluten-free":
        meal_plan["Lunch"] = "Grilled chicken salad with mixed greens and gluten-free vinaigrette (400 kcal)"

    return meal_plan

def main():
    """Main entry point of the script."""
    # Get user input
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ")
    height_cm = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))
    activity_level = input("Enter your activity level (sedentary/moderate/active): ")
    food_preference = input("Enter your food preference (vegetarian/gluten-free): ")

    # Convert height from cm to m
    height_m = height_cm / 100

    # Calculate BMI and provide recommendations
    bmi = calculate_bmi(weight, height_m)
    bmi_advice = get_bmi_recommendation(bmi)

    # Calculate daily water intake
    water_intake = calculate_daily_water_intake(weight, age)

    # Recommend daily calorie intake
    calorie_intake = recommend_calories(age, gender, height_m, weight, activity_level)

    # Recommend sleep duration
    sleep_advice = recommend_sleep(age)

    # Calculate macronutrient breakdown
    macros = calculate_macros(calorie_intake)

    # Suggest meal plan
    meal_plan = suggest_meal_plan(bmi, food_preference)

    # Display results
    print("\n\n\n")
    print(" === Personal Health Report === ")
    print(f"Your BMI: {bmi} (Normal weight: 18.5-24.9)")
    print(f"Health Advice: {bmi_advice}")
    print(f"Recommended Daily Water Intake: {water_intake} liters")
    print(f"Recommended Daily Calorie Intake: {calorie_intake} kcal")
    print(f"Recommended Macronutrient Breakdown: {macros}")
    print(f"Sleep Advice: {sleep_advice}")
    print(f"Meal Plan: {meal_plan}")
    print("==============================")
    print("Remember, these are just recommendations. Always consult a healthcare professional for personalized advice!")


if __name__ == "__main__":
    main()
