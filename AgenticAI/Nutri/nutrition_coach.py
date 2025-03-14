import random
import datetime
from typing import Dict, List, Optional, Tuple, Union


class NutritionCoachAgent:
    def __init__(self):
        self.user_profile = {}
        self.food_database = self._initialize_food_database()
        self.conversation_history = []
        self.daily_logs = {}
        self.goals = {}

    def _initialize_food_database(self) -> Dict[str, Dict[str, Union[float, str]]]:
        """Initialize a simple food database with nutritional information."""
        return {
            "apple": {"calories": 95, "protein": 0.5, "carbs": 25, "fat": 0.3, "fiber": 4, "category": "fruit"},
            "banana": {"calories": 105, "protein": 1.3, "carbs": 27, "fat": 0.4, "fiber": 3.1, "category": "fruit"},
            "chicken breast": {"calories": 165, "protein": 31, "carbs": 0, "fat": 3.6, "fiber": 0,
                               "category": "protein"},
            "salmon": {"calories": 206, "protein": 22, "carbs": 0, "fat": 13, "fiber": 0, "category": "protein"},
            "brown rice": {"calories": 216, "protein": 5, "carbs": 45, "fat": 1.8, "fiber": 3.5, "category": "grain"},
            "quinoa": {"calories": 222, "protein": 8, "carbs": 39, "fat": 3.6, "fiber": 5, "category": "grain"},
            "spinach": {"calories": 23, "protein": 2.9, "carbs": 3.6, "fat": 0.4, "fiber": 2.2,
                        "category": "vegetable"},
            "broccoli": {"calories": 55, "protein": 3.7, "carbs": 11, "fat": 0.6, "fiber": 5.1,
                         "category": "vegetable"},
            "olive oil": {"calories": 119, "protein": 0, "carbs": 0, "fat": 13.5, "fiber": 0, "category": "fat"},
            "avocado": {"calories": 240, "protein": 3, "carbs": 12, "fat": 22, "fiber": 10, "category": "fat"},
            "greek yogurt": {"calories": 130, "protein": 12, "carbs": 5, "fat": 4, "fiber": 0, "category": "dairy"},
            "almonds": {"calories": 164, "protein": 6, "carbs": 6, "fat": 14, "fiber": 3.5, "category": "nuts"},
            "lentils": {"calories": 230, "protein": 18, "carbs": 40, "fat": 0.8, "fiber": 16, "category": "legume"},
            "oats": {"calories": 307, "protein": 11, "carbs": 55, "fat": 5, "fiber": 8, "category": "grain"},
            "sweet potato": {"calories": 112, "protein": 2, "carbs": 26, "fat": 0.1, "fiber": 3.8,
                             "category": "vegetable"},
        }

    def setup_user_profile(self, name: str, age: int, weight: float, height: float,
                           gender: str, activity_level: str, dietary_restrictions: List[str] = None) -> str:
        """
        Setup the user profile with basic information.

        Args:
            name: User's name
            age: User's age in years
            weight: User's weight in kg
            height: User's height in cm
            gender: User's gender ('male' or 'female')
            activity_level: User's activity level ('sedentary', 'light', 'moderate', 'active', 'very active')
            dietary_restrictions: List of dietary restrictions ('vegetarian', 'vegan', 'gluten-free', etc.)

        Returns:
            A welcome message
        """
        self.user_profile = {
            "name": name,
            "age": age,
            "weight": weight,
            "height": height,
            "gender": gender,
            "activity_level": activity_level,
            "dietary_restrictions": dietary_restrictions or [],
            "date_joined": datetime.datetime.now().strftime("%Y-%m-%d")
        }

        # Calculate BMI
        bmi = weight / ((height / 100) ** 2)
        self.user_profile["bmi"] = round(bmi, 1)

        # Calculate estimated daily caloric needs using Mifflin-St Jeor equation
        if gender.lower() == "male":
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161

        activity_multipliers = {
            "sedentary": 1.2,
            "light": 1.375,
            "moderate": 1.55,
            "active": 1.725,
            "very active": 1.9
        }

        daily_calories = bmr * activity_multipliers.get(activity_level.lower(), 1.2)
        self.user_profile["daily_calorie_needs"] = round(daily_calories)

        return f"Welcome {name}! Based on your profile, your estimated daily calorie needs are {round(daily_calories)} calories. Your BMI is {round(bmi, 1)}."

    def set_goals(self, weight_goal: Optional[float] = None,
                  daily_calories: Optional[int] = None,
                  macros: Optional[Dict[str, float]] = None) -> str:
        """
        Set nutrition and weight goals.

        Args:
            weight_goal: Target weight in kg
            daily_calories: Target daily calorie intake
            macros: Target macronutrient percentages (e.g., {"protein": 30, "carbs": 40, "fat": 30})

        Returns:
            Confirmation message
        """
        if not self.user_profile:
            return "Please set up your profile first."

        self.goals = {}

        if weight_goal:
            self.goals["weight_goal"] = weight_goal
            weight_diff = weight_goal - self.user_profile["weight"]
            if abs(weight_diff) > 0.5:
                direction = "lose" if weight_diff < 0 else "gain"
                self.goals["weight_direction"] = direction
                self.goals["weight_diff"] = abs(weight_diff)
            else:
                self.goals["weight_direction"] = "maintain"
                self.goals["weight_diff"] = 0

        if daily_calories:
            self.goals["daily_calories"] = daily_calories
        elif "weight_direction" in self.goals:
            # Adjust calories based on weight goal
            base_calories = self.user_profile["daily_calorie_needs"]
            if self.goals["weight_direction"] == "lose":
                # Create a caloric deficit (500 calories per day loses about 0.5kg per week)
                self.goals["daily_calories"] = max(1200, base_calories - 500)
            elif self.goals["weight_direction"] == "gain":
                # Create a caloric surplus
                self.goals["daily_calories"] = base_calories + 500
            else:
                self.goals["daily_calories"] = base_calories

        if macros:
            # Validate macros add up to approximately 100%
            total = sum(macros.values())
            if 98 <= total <= 102:  # Allow for small rounding errors
                self.goals["macros"] = macros
            else:
                return f"Macronutrient percentages should add up to 100%. Current total: {total}%"
        else:
            # Set default macros based on goals
            if "weight_direction" in self.goals and self.goals["weight_direction"] == "lose":
                self.goals["macros"] = {"protein": 30, "carbs": 40, "fat": 30}
            elif "weight_direction" in self.goals and self.goals["weight_direction"] == "gain":
                self.goals["macros"] = {"protein": 25, "carbs": 50, "fat": 25}
            else:
                self.goals["macros"] = {"protein": 20, "carbs": 50, "fat": 30}

        # Calculate target grams for each macro
        calories = self.goals["daily_calories"]
        protein_cals = calories * (self.goals["macros"]["protein"] / 100)
        carb_cals = calories * (self.goals["macros"]["carbs"] / 100)
        fat_cals = calories * (self.goals["macros"]["fat"] / 100)

        # Protein and carbs have 4 calories per gram, fat has 9 calories per gram
        self.goals["protein_grams"] = round(protein_cals / 4)
        self.goals["carb_grams"] = round(carb_cals / 4)
        self.goals["fat_grams"] = round(fat_cals / 9)

        response = f"Goals set successfully!\n"

        if "weight_direction" in self.goals:
            if self.goals["weight_direction"] == "maintain":
                response += f"Weight goal: Maintain current weight of {self.user_profile['weight']} kg.\n"
            else:
                response += f"Weight goal: {self.goals['weight_direction'].capitalize()} {self.goals['weight_diff']} kg to reach {weight_goal} kg.\n"

        response += f"Daily calorie target: {self.goals['daily_calories']} calories.\n"
        response += "Macronutrient targets:\n"
        response += f"- Protein: {self.goals['macros']['protein']}% ({self.goals['protein_grams']} g)\n"
        response += f"- Carbohydrates: {self.goals['macros']['carbs']}% ({self.goals['carb_grams']} g)\n"
        response += f"- Fat: {self.goals['macros']['fat']}% ({self.goals['fat_grams']} g)"

        return response

    def log_meal(self, meal_type: str, foods: Dict[str, float]) -> str:
        """
        Log a meal with specified foods and portions.

        Args:
            meal_type: Type of meal ('breakfast', 'lunch', 'dinner', 'snack')
            foods: Dictionary mapping food names to portion sizes in standard servings

        Returns:
            Summary of the logged meal
        """
        if not self.user_profile:
            return "Please set up your profile first."

        today = datetime.datetime.now().strftime("%Y-%m-%d")

        if today not in self.daily_logs:
            self.daily_logs[today] = {"meals": {},
                                      "totals": {"calories": 0, "protein": 0, "carbs": 0, "fat": 0, "fiber": 0}}

        if meal_type not in self.daily_logs[today]["meals"]:
            self.daily_logs[today]["meals"][meal_type] = []

        meal_nutrients = {"items": {}, "totals": {"calories": 0, "protein": 0, "carbs": 0, "fat": 0, "fiber": 0}}
        unknown_foods = []

        for food, portion in foods.items():
            food_lower = food.lower()

            if food_lower in self.food_database:
                food_data = self.food_database[food_lower]
                meal_nutrients["items"][food] = {
                    "portion": portion,
                    "calories": round(food_data["calories"] * portion, 1),
                    "protein": round(food_data["protein"] * portion, 1),
                    "carbs": round(food_data["carbs"] * portion, 1),
                    "fat": round(food_data["fat"] * portion, 1),
                    "fiber": round(food_data["fiber"] * portion, 1),
                    "category": food_data["category"]
                }

                # Update meal totals
                for nutrient in ["calories", "protein", "carbs", "fat", "fiber"]:
                    meal_nutrients["totals"][nutrient] += meal_nutrients["items"][food][nutrient]
                    # Update daily totals
                    self.daily_logs[today]["totals"][nutrient] += meal_nutrients["items"][food][nutrient]
            else:
                unknown_foods.append(food)

        # Round totals for better readability
        for nutrient in meal_nutrients["totals"]:
            meal_nutrients["totals"][nutrient] = round(meal_nutrients["totals"][nutrient], 1)

        # Add meal to daily log
        self.daily_logs[today]["meals"][meal_type].append(meal_nutrients)

        # Prepare response
        response = f"{meal_type.capitalize()} logged successfully!\n\n"
        response += f"Total meal nutrients:\n"
        response += f"- Calories: {meal_nutrients['totals']['calories']}\n"
        response += f"- Protein: {meal_nutrients['totals']['protein']}g\n"
        response += f"- Carbs: {meal_nutrients['totals']['carbs']}g\n"
        response += f"- Fat: {meal_nutrients['totals']['fat']}g\n"
        response += f"- Fiber: {meal_nutrients['totals']['fiber']}g\n"

        # Add daily progress if goals exist
        if self.goals:
            calories_remaining = self.goals["daily_calories"] - self.daily_logs[today]["totals"]["calories"]
            response += f"\nDaily progress:\n"
            response += f"- Calories: {self.daily_logs[today]['totals']['calories']} / {self.goals['daily_calories']} ({calories_remaining} remaining)\n"

            if "protein_grams" in self.goals:
                protein_progress = round(
                    (self.daily_logs[today]["totals"]["protein"] / self.goals["protein_grams"]) * 100)
                response += f"- Protein: {self.daily_logs[today]['totals']['protein']}g / {self.goals['protein_grams']}g ({protein_progress}%)\n"

            if "carb_grams" in self.goals:
                carb_progress = round((self.daily_logs[today]["totals"]["carbs"] / self.goals["carb_grams"]) * 100)
                response += f"- Carbs: {self.daily_logs[today]['totals']['carbs']}g / {self.goals['carb_grams']}g ({carb_progress}%)\n"

            if "fat_grams" in self.goals:
                fat_progress = round((self.daily_logs[today]["totals"]["fat"] / self.goals["fat_grams"]) * 100)
                response += f"- Fat: {self.daily_logs[today]['totals']['fat']}g / {self.goals['fat_grams']}g ({fat_progress}%)"

        if unknown_foods:
            response += f"\n\nNote: The following foods were not found in the database: {', '.join(unknown_foods)}"

        return response

    def get_daily_summary(self, date: Optional[str] = None) -> str:
        """
        Get a summary of nutrition for a specific day.

        Args:
            date: Date in format YYYY-MM-DD (defaults to today)

        Returns:
            Summary of the day's nutrition
        """
        if not date:
            date = datetime.datetime.now().strftime("%Y-%m-%d")

        if date not in self.daily_logs:
            return f"No meal data found for {date}."

        daily_totals = self.daily_logs[date]["totals"]
        response = f"Nutrition Summary for {date}:\n"
        response += f"- Calories: {daily_totals['calories']}\n"
        response += f"- Protein: {daily_totals['protein']}g\n"
        response += f"- Carbs: {daily_totals['carbs']}g\n"
        response += f"- Fat: {daily_totals['fat']}g\n"
        response += f"- Fiber: {daily_totals['fiber']}g\n"

        if self.goals:
            response += "\nDaily progress:\n"
            calories_remaining = self.goals["daily_calories"] - daily_totals["calories"]
            response += f"- Calories: {daily_totals['calories']} / {self.goals['daily_calories']} ({calories_remaining} remaining)\n"

            if "protein_grams" in self.goals:
                protein_progress = round((daily_totals["protein"] / self.goals["protein_grams"]) * 100)
                response += f"- Protein: {daily_totals['protein']}g / {self.goals['protein_grams']}g ({protein_progress}%)\n"

            if "carb_grams" in self.goals:
                carb_progress = round((daily_totals["carbs"] / self.goals["carb_grams"]) * 100)
                response += f"- Carbs: {daily_totals['carbs']}g / {self.goals['carb_grams']}g ({carb_progress}%)\n"

            if "fat_grams" in self.goals:
                fat_progress = round((daily_totals["fat"] / self.goals["fat_grams"]) * 100)
                response += f"- Fat: {daily_totals['fat']}g / {self.goals['fat_grams']}g ({fat_progress}%)\n"

        return response
