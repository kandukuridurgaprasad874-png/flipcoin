class SocialMediaPost:
    def __init__(self, post_title):
        self.post_title = post_title
        self.__likes = 0   # Private variable

   
    def like(self):
        self.__likes += 1
        print(f"Post liked. Total Likes: {self.__likes}")
    def unlike(self):
        if self.__likes > 0:
            self.__likes -= 1
            print(f"Like removed. Total Likes: {self.__likes}")
        else:
            print("Likes cannot go below zero")

    def show_likes(self):
        print(f"'{self.post_title}' Likes: {self.__likes}")
post = SocialMediaPost("Python OOP Concepts")
post.like()
post.like()
post.like()
print()
post.unlike()
post.unlike()
post.unlike()
post.unlike()   

print()
post.show_likes()