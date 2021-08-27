# This file contains the classes used for the library console.

# Auxilary methods imported here:
from library.commandLineBooks import bookShelf


class Book():

    """
        Book is a class for the storage, manipulation, and presentation
        of books in the Library interface.

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


class lHomeScreen():

    """
        This class defines the presentation and function of the landing
        screen for the library console.

    """

    def __init__(self):

        """
        """

        self.state = "Home"
        self.option = ""

    def header(self):

        """
            This method controls the header for the homsecreen
            of the Library Console.
        """

        x = "|||"
        y = "-"
        z = " "
        w = "\n"

        welcome_message = " Welcome to the Library Console "
        l_welcome = len(welcome_message)

        print(x + 170*y + x)
        print(3*w)

        print(z*65 + x + l_welcome*y + x)
        print(z*65 + x + welcome_message + x)
        print(z*65 + x + l_welcome*y + x)
        print(w)
        bookShelf()

    def explanation(self):

        """
            This method provides the user with an explanation of the
            program manager and how it can be used.
        """
        # shortcuts for aesthetic use.
        x = "|||"
        y = "-"
        z = " "
        w = "\n"

        explanation_message_1 = z*10 + "This console can be used to access the library."
        explanation_message_2 = z*10 + "The user may view the library database, search for books and authors."
        explanation_message_3 = z*10 + "See below for a full list of options."
        print(w*3)
        print(explanation_message_1)
        print(explanation_message_2)
        print(explanation_message_3)
        print(w)
        
    def options(self):

        """
            This method controls the menu for the homepage. Providing the
            user with the available options.
        """

        # shortcuts for aesthetic use.
        x = "|||"
        y = "-"
        z = " "
        w = "\n"

        prompt = "Which of the following options would you like to perform?"

        option_s = "[S]: Search the library."
        option_e = "[E]: Enter new books to the library database."
        option_l = "[L]: Loan books from the library."
        option_r = "[R]: Return books to the library."
        option_u = "[U]: Update an entry in the libary."
        option_q = "[Q]: Quit the library console."
        #option_h = "[H]: Return to the homesreen of the console."

        options = [option_s,
                   option_e,
                   option_l,
                   option_r,
                   option_u,
                   option_q]

        # Start printing the options for the user.
        print(w*2)
        print(z*15 + prompt + w)
        for o in options:
            print(z*20 + o)

        print(w)
        user_option = input(z*15 + "Option: ")

        return user_option

    def continue_program(self):

        """
            This method is used to keep track of whether or not the user
            is finished accessing the database and wishes to close the console.
        """

        return True



class lClose():

    """
    """

    def __init__(self):

        self.state = "Close"
        self.option = ""

    def header(self):

        x = "|||"
        y = "-"
        z = " "
        w = "\n"

        exit_message = " Thank you for visiting the C.P.C Library."
        l_exit = len(exit_message)

        print(x + 170*y + x)
        print(3*w)

        print(z*65 + x + l_exit*y + x)
        print(z*65 + x + exit_message + x)
        print(z*65 + x + l_exit*y + x)

    def continue_program(self):

        """
            This method is used to determine whether or not the user is finished
            and hence that the MAP console should close.
        """

        return False
