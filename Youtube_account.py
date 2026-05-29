class YouTubeAccount:
    def __init__(self, channel_name):
        self.channel_name = channel_name
        self.__subscribers = 0   # Private variable

    def subscribe(self):
        self.__subscribers += 1
        print(f"1 subscriber added to {self.channel_name}")

    def unsubscribe(self):
        if self.__subscribers > 0:
            self.__subscribers -= 1
            print(f"1 subscriber removed from {self.channel_name}")
        else:
            print("No subscribers to remove")

    def show_subscribers(self):
        print(f"{self.channel_name} Subscribers: {self.__subscribers}")

channel = YouTubeAccount("Python Master")

channel.subscribe()
channel.subscribe()
channel.subscribe()

channel.show_subscribers()

print()

channel.unsubscribe()
channel.show_subscribers()