class Robot:
    """ Represents a robot, with a name.

    """
    population = 0

    def __init__(self,name):
        """ Initializes the data """
        self.name = name
        print ('Intializing{}').format(self.name)
        Robot.population += 1

    def die(self):
        """ I'm dying.
        """
        print ("{}is being destroyed!").format(self.name)
        Robot.population -= 1

        if Robot.population == 0:
            print ("{}was the last one.").format(self.name)
        else:
            print ("There are still {:d} roboots working").format(Robot.population)

    def say_hi(self):
        """ Greeting by the robot.

        Yes, they can do that.
        """
        print ("Greetings, my master call me {}.").format(self.name)

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print ("We have {:d} robots.").format(cls.population)

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print ("\n Robots can do some work here.\n")

droid1.die()
droid2.die()

Robot.how_many()

