# Step tracker
class StepTracker:
    def track_steps(self):
        print("Steps tracked: 8500")


# Heart rate tracker
class HeartRateTracker:
    def track_heart_rate(self):
        print("Heart Rate: 72 BPM")


# Sleep tracker
class SleepTracker:
    def track_sleep(self):
        print("Sleep Duration: 7 hours")


# Calorie tracker
class CalorieTracker:
    def track_calories(self):
        print("Calories Burned: 450 kcal")


# Smart Watch
class SmartWatch:
    def __init__(self):
        self.steps = StepTracker()
        self.heart = HeartRateTracker()
        self.sleep = SleepTracker()
        self.calories = CalorieTracker()

    def show_fitness_data(self):
        self.steps.track_steps()
        self.heart.track_heart_rate()
        self.sleep.track_sleep()
        self.calories.track_calories()


# Object
watch = SmartWatch()
watch.show_fitness_data()