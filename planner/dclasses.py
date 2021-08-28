# Classes for daily planner module.
class dHomeScreen():

    """
        This class defines the presentation and function of the landing
        screen for the daily planner.

    """

    def __init__(self):

        """
        """

        self.state = "Home"
        self.option = ""

    def header(self):

        """
            This method controls the header for the homsecreen
            of the daily planner Console.
        """

        x = "|||"
        y = "-"
        z = " "
        w = "\n"

        welcome_message = " Welcome to your Daily Planner Console "
        l_welcome = len(welcome_message)

        print(x + 170*y + x)
        print(3*w)

        print(z*65 + x + l_welcome*y + x)
        print(z*65 + x + welcome_message + x)
        print(z*65 + x + l_welcome*y + x)
        print(w)
        

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

        explanation_message_1 = z*10 + "This console can be used to access the daily planner."
        explanation_message_2 = z*10 + "The user may view the daily planner database, mark tasks as complete,"
        explanation_message_3 = z*10 + "enter new tasks, or refresh the list for the day."
        explanation_message_4 = z*10 + "See below for a full list of options."
        print(w*3)
        print(explanation_message_1)
        print(explanation_message_2)
        print(explanation_message_3)
        print(explanation_message_4)
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

        option_1 = "[C]: Complete task e.g. ct2.1.2"
        option_2 = "[A]: Add task"
        option_3 = "[R]: Remove task e.g. rt2.1"
        option_4 = "[N]: New day refresh"
        option_5 = "[Q]: Quit the daily planner console."

        options = [option_1,
                   option_2,
                   option_3,
                   option_4,
                   option_5]

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



class dClose():

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

        exit_message = " Thank you for visiting the daily planner."
        l_exit = len(exit_message)

        print(x + 170*y + x)
        print(3*w)

        print(z*65 + x + l_exit*y + x)
        print(z*65 + x + exit_message + x)
        print(z*65 + x + l_exit*y + x)

    def continue_program(self):

        """
            This method is used to determine whether or not the user is finished
            and hence that the daily planner console should close.
        """

        return False
