#            File containing all classes used in the desktop assistant home view.

class daHomeScreen():

    """
        This class determines the layout of the homescreen of the desktop
        assistant. With methods to control:

            (i) View
            (ii) Option presentation
            (iii) Option selection/action

    """

    def __init__(self):

        """
            This method defines the key attributes of an instance of this class.
            In particular an instance as the state name which designates this class and
            an attribute to store the user's option for the next action.

        """

        self.state = "daHome"
        self.option = ""

    def options(self):

        """
            This method presents all of the options to the user: each of the programs
            that the assistant will link them to. User will enter a string.

            If the string is not in the list of possible options, then the program
            will ask them to renter the command.

        """

        # Shortcuts for aesthetics.
        x = "|||"
        y = "-"
        z = " "
        w = "\n"

        option_prompt = "Which of the following would you like to visit: "
        option_1 = "[D]: Daily Planner"
        option_2 = "[L]: Library"
        option_3 = "[P]: Projects"
        option_4 = "[U]: Updates Newsfeed"
        option_5 = "[M]: Memory Augmentation Program"
        option_6 = "[R]: Recipes"
        option_7 = "[B]: Budget"
        option_8 = "[I]: Inspiration"
        option_9 = "[Q]: Quit"

        options = [option_1,
                    option_2,
                    option_3,
                    option_4,
                    option_5,
                    option_6,
                    option_7,
                    option_8,
                    option_9]

        # Start printing the options for the user.
        print(w*2)
        print(z*15 + option_prompt + w)
        for o in options:
            print(z*20 + o)

        # Use the following to make sure input is sensible.
        allowed_input = ["D","L","P","U","M","R","B","I","Q"]
        option_sensible = False

        while not option_sensible:

            print(w)
            user_option = input(z*15 + "Option: ")

            if user_option in allowed_input:
                option_sensible = True
            else:
                print(z*15 + "This is not an allowed option. Please enter one of the options above.")

        self.option = user_option
        
        return user_option

    def continue_program(self):

        """
            This method is used to keep track of whether or not the user
            is finished accessing the database and wishes to close the console.
        """

        return True


class daClose():

    """
        This class is used to close the program and print an exit statement.
    """

    def __init__(self):

        """
            This class is used to define the homescreen of the project
            manager console. This class stores the options available to the
            user at the homescreen.
        """

        self.state = "Close"
        self.option = ""


    def continue_program(self):

        """
            This method is used to keep track of whether or not the user
            is finished accessing the database and wishes to close the console.
        """

        return False
