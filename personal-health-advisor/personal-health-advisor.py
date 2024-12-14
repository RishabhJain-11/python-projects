# Personal Health Advisor

def calculate_bmi(weight_calculate_bmi, height):
    bmi_calculation = weight_calculate_bmi / (height ** 2)
    return round(bmi_calculation, 2)

# Function to give BMI-based recommendations
def get_bmi_recommendation(bmi_recommendation_metric):
    if bmi_recommendation_metric < 18.5:
        return "Underweight"
    elif 18.5 <= bmi_recommendation_metric < 24.9:
        return "Normal weight"
    elif 25 <= bmi_recommendation_metric < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Function to calculate daily water intake.
def calculate_daily_water_intake(weight_daily_water_intake, age_daily_water_intake):
    daily_water_intake = weight_daily_water_intake * 0.033

    # Additional adjustment based on age
    if age_daily_water_intake < 18:
        daily_water_intake += 0.5  # Add 0.5L for younger individuals
    elif age_daily_water_intake > 55:
        daily_water_intake -= 0.3  # Reduce 0.3L for seniors

    return round(daily_water_intake, 2)

# Function to recommend calorie intake
def recommend_calories(age_rec_calories, gender_rec_calories, height_cm_rec_calories, weight_rec_calories,
                       activity_level_rec_calories):
    # Calculate BMR based on gender
    if gender_rec_calories == 'male':
        bmr = 10 * weight_rec_calories + 6.25 * height_cm_rec_calories - 5 * age_rec_calories + 5
    else:
        bmr = 10 * weight_rec_calories + 6.25 * height_cm_rec_calories - 5 * age_rec_calories - 161

    # Adjust BMR based on activity level
    activity_factors = {
        'sedentary': 1.2,
        'moderate': 1.55,
        'active': 1.75,
        'very active': 2.0
    }

    multiplier = activity_factors.get(activity_level_rec_calories, None)
    if multiplier is None:
        return "Invalid activity level"

    calories = bmr * multiplier
    return round(calories, 2)

# Function to recommend sleep duration
def recommend_sleep(age_rec_sleep):
    if age_rec_sleep < 6:
        return "Toddlers need about 11-14 hours of sleep daily."
    elif 6 <= age_rec_sleep <= 13:
        return "Children need 9-11 hours of sleep daily."
    elif 14 <= age_rec_sleep <= 17:
        return "Teenagers need 8-10 hours of sleep daily."
    elif 18 <= age_rec_sleep <= 64:
        return "Adults need 7-9 hours of sleep daily."
    else:
        return "Older adults need 7-8 hours of sleep daily."


if __name__ == "__main__":
    print("Welcome to the Personal Health Advisor!")

    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ")
    height_cm = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))
    activity_level = input("Enter your activity level (sedentary/moderate/active): ")

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

    # Display results
    print("\n\n\n")
    print("🎉 === Personal Health Report === 🎉")
    print(f"Your BMI: {bmi} (Normal weight: 18.5-24.9)")
    print(f"Health Advice: {bmi_advice} 😊")
    print(f"Recommended Daily Water Intake: {water_intake} liters 💧")
    print(f"Recommended Daily Calorie Intake: {calorie_intake} kcal 🍔")
    print(f"Sleep Advice: {sleep_advice} 😴")
    print("==============================")
    print("Remember, these are just recommendations. Always consult a healthcare professional for personalized advice! 💊")