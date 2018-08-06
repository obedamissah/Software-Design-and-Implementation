#Author: Obed Amissah
# Purpose: A program that implements the truck class, which models a 5 speed transmission
#   using an instance variable named truck_state, representing the state of the truck's transmission,
#   and an instance variable named self.revsound which is a string representing the
#   truck's sound.
#####################################################################


def testit(did_pass):
    """ A helper function for printing the results of tests
    :param did_pass: a boolean representing if the test passed or failed """
    import sys
    """  Prints the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def truck_test_suite():
    """  A helper function which tests the methods of the truck class. """
    print("-------------------------------------")
    print("Starting the truck test suite...\n")

    my_truck = truck()
    my_truck.shift_up()
    testit(my_truck.truck_state==1)   # The initial truck_state should be neutral which is 0, so the truck_state should now be 1
    my_truck.shift_up()
    testit(my_truck.truck_state==2)   # The truck_state should now be 2
    testit(str(my_truck)=="truck: 2")
    my_truck.shift_up()              # The truck_state should now be
    my_truck.shift_up()              # The truck_state should now be 4
    my_truck.shift_up()              # The truck_state should now be 5
    testit(my_truck.truck_state==5)   # The initial truck_state should now be 5
    my_truck.shift_up()
    testit(my_truck.truck_state==5)   # The truck_state should now be 5 because max is 5
    my_truck.shift_down()
    testit(my_truck.truck_state==4)   # The truck_state should now be 4
    
    testit(my_truck.rev(0)=="")
    testit(my_truck.rev(2)=="Varoom!Varoom!")
    testit(my_truck.rev(4)=="Varoom!Varoom!Varoom!Varoom!")

    print("\nEnding the truck test suite.")
    print("-------------------------------------")


class truck:
    def __init__(self):
        '''Initializer sets truck_state to neutral which is represented by 0'''
        self.truck_state = 0
        self.revsound ="Varoom!"

    def __str__(self):
        ''' Uses the built-in string method to return "truck: #" where number if the value of truck_state
        eg. When first initialized, this method will return "truck: 0" '''
        return "truck: {0}".format(self.truck_state)

    def shift_up(self):
        '''each time shift_up() is called, truck_state is increased by 1 until it reaches 5;
        The max truck_state is 5, so it will stay at 5 when this method is called.
        The return value is not used'''

        # TODO if truck_state instance variable is less than 5, increase it by 1.
        truck_state = 0
        while truck_state < 5:
            truck_state += 1
        else:
            return truck_state

    def shift_down(self):
        '''each time this method is called, the truck_state decreases by 1 until the truck_state reaches -1.
        There is a single reverse speed of -1, so it will remain -1 when this method is called with truck_state=-1
        The return value is not used'''

        # TODO  if the truck_state instance variable is 0 or above, decrease truck_state by 1.
        truck_state = 0
        while truck_state >= 0:                 # it removes or reduces the truck_state by 1 if it is greater than zero
            truck_state -= 1
        else:
            return truck_state

    def rev(self, n):
        '''returns a string with self.revsound repeated n times where n is an integer.
        e.g. if self.revsound ='Varoom!' and if n = 3, 'Varoom!Varoom!Varoom!' is returned'''
        returnval=self.revsound
        
        # TODO  correct returnval to use n 
        n == self.revsound
        if n == 1:                              # if the truck is in gear then then it should print one sound
            print('Varoom!')
        elif n == 2:
            print('Varoom! Varoom!')
        elif n == 3:
            print('Varoom! Varoom! Varoom!')
        elif n == 4:
            print ('Varoom! Varoom! Varoom! Varoom!')
        else:
            print('Varoom! Varoom! Varoom! Varoom! Varoom!')

        return returnval

def main():
    '''main program calls the truck_test_suite()'''
    truck_test_suite()

    # TODO print the return value from the rev method using n=3
    print(returnval)
    truck_state = self.shift_up()


main()  # TODO create a new truck object instance