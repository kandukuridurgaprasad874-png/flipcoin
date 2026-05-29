# Base class
class Subscriber:
    def __init__(self, name):
        self.name = name

    def watch_movie(self):
        print(f"{self.name} can stream movies with ads")


# Derived class
class PremiumSubscriber(Subscriber):
    def watch_movie(self):
        print(f"{self.name} can stream movies without ads")

    def download_movie(self):
        print(f"{self.name} can download movies for offline watching")


# Objects
user1 = Subscriber("Ravi")
user2 = PremiumSubscriber("Priya")

# Normal subscriber
user1.watch_movie()

print("------------")

# Premium subscriber
user2.watch_movie()
user2.download_movie()