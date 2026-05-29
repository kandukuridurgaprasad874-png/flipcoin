class LibraryBook:

    def __init__(self, book_name):

        self.book_name = book_name

        # private variable
        self.__issued = False


    # issue method
    def issue_book(self):

        if self.__issued == False:

            self.__issued = True

            print("Book Issued")

        else:
            print("Book already issued")


    # return method
    def return_book(self):

        if self.__issued == True:

            self.__issued = False

            print("Book Returned")

        else:
            print("Book was not issued")


    # display method
    def display(self):

        print("Book Name :", self.book_name)

        print("Issued Status :", self.__issued)



# Object Creation
b1 = LibraryBook("Python Programming")


# Initial Status
b1.display()


# Issue Book
print("\nIssue Book")
b1.issue_book()


# Try Again
print("\nIssue Again")
b1.issue_book()


# Return Book
print("\nReturn Book")
b1.return_book()


# Issue Again After Return
print("\nIssue After Return")
b1.issue_book()