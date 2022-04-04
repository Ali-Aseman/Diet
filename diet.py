from pdb import find_function


print("""                      (
                        )     (
                 ___...(-------)-....___
             .-""       )    (          ""-.
       .-'``'|-._             )         _.-|
      /  .--.|   `""---...........---""`   |
     /  /    |                             |
     |  |    |                             |
      \  \   |                             |
       `\ `\ |                             |
         `\ `|                             |
         _/ /\                             /
        (__/  \                           /
     _..---""` \                         /`""---.._
  .-'           \                       /          '-.
 :               `-.__             __.-'              :
 :                  ) ""---...---"" (                 :
  '._               `"--...___...--"`              _.'
GHSOTE""--..__                              __..--
""")
print()

class dient:
    def __init__(self, breakfast_calories, lunch_calories, dinner_calories, exercise, bmr):
        self.breakfast_calories = breakfast_calories
        self.lunch_calories = lunch_calories
        self.dinner_calories = dinner_calories
        self.exercise = exercise
        self.bmr = bmr
    
    def calories_deficit(self):
        deficit = self.bmr + self.exercise - (self.breakfast_calories + self.lunch_calories + self.dinner_calories)
        return deficit
    
try: 
    breakfast_calories = int(input("[?] How Many Calories Did You Have For Breakfast >>> ")) # برای صبحانه چند کالری مصرف کردید؟
    lunch_calories = int(input("[?] How Many Calories Did You Have For Lunch >>> ")) # برای ناهار چند کالری داشتی؟
    dinner_calories = int(input("[?] How Many Calories Did You Have For Dinner >>> ")) # برای شام چقدر کالری داشتید؟
    exercise = int(input("[?] How Many Calories Did You Burn Xecising >>> ")) # با ورزش چند کالری سوزاندی؟
    bmr = int(input("[?] What Is Your Basic Metabolic Rate >>> ")) # میزان متابولیسم پایه شما چقدر است؟
except ValueError:
    print("The Value Entered Must Be A Number")
except NameError:
    print("The value entered must be a number")


fitness = dient(breakfast_calories, lunch_calories, dinner_calories, exercise, bmr)
weekly_deficit = 7 * fitness.calories_deficit()


print()
if weekly_deficit > 0:
    print(f"[+] => You Will Lose {weekly_deficit / 3600} Lbs. Per Week")

elif weekly_deficit == 0:
    print(f"[+] => Your Weight Will Stay the Same")

else:
    print(f"[+] => You Will Gain {-1 * weekly_deficit / 3600} Lbs. Per Week")

