from nutrition_coach import NutritionCoachAgent;

coach = NutritionCoachAgent()

welcome_msg = coach.setup_user_profile(
    name="Rishabh Jain",
    age=23,
    weight=70,
    height=165,
    gender="male",
    activity_level="moderate",
    dietary_restrictions=["vegan", "gluten-free"]
)
print(welcome_msg)

goal_message = coach.set_goals(weight_goal=70, daily_calories=2000)
print(goal_message)


meal_log = coach.log_meal("breakfast", {"oats": 1.5, "banana": 1, "almonds": 0.5})
print(meal_log)

summary = coach.get_daily_summary()
print(summary)