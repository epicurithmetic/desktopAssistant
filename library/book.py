# This script holds the definition of the book class.
# This class is used to hold information of a book in memory and used to
# print the information for the book.
class Book():

    """
        Book is a class for the storage, manipulation, and presentation
        of books in the cpcLibrary interface.

    """

    def __init__(self,author_first,author_last,book_title):

        """


        """

        self.author_first = author_first
        self.author_last = author_last
        self.author = self.author_first + " " +  self.author_last
        self.title = book_title
        self.rating = ""
        self.loan_status = ""
        self.loanee = ""

    def printBookData(self):

        """
            This method can be called to present the book
            data in a clear manner. This function should be used
            whenever one wants to view book data, so that it is
            always presented in the same way.

        """

        x = "|||"
        y = "-"
        z = " "
        w = "\n"

        print(w)
        print(20*z + "Author: '%s'" % self.author)
        print(20*z + "Title: '%s'" % self.title)
        if self.loan_status == "":
            print(20*z + "Status: This book is currently in the library.")
        else:
            print(20*z + "Status: This book is currently on loan to '%s'" % self.loanee)
