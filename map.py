######################################################################
# Author:Obed Amissah
#
# Purpose: to creating a map of locations
# where the user is originally from or has visited,
# and to use tuples and lists correctly.


import turtle

def place_pin(window, place):
    """
    This function places a pin on the world map
    :param window: the window object where the pin will be placed
    :param place: a tuple object describing a place to be put on the map with
    [0]: A string representing the user's name
    [1]: A string representing the name of the location (e.g., Eiffel Tower)
    [2]: A float representing the latitude of the location (e.g., 41.156537)
    [3]: A float representing the longitude of the location (e.g., -93.710720)
    [4]: A string representing the user's color
    example: ("Dr. Scott", "Childhood Home", 41.156537, -93.7107200, "blue")
    
    """
    pin = turtle.Turtle()
    pin.penup()
    pin.color(place[4])  # Set the pin to user's chosen color
    pin.shape("circle")  # Sets the pin to a circle shape
    # logically, the denominator for longitude should be 360; lat should be 180.
    # These values were determined through testing to account for the extra white space on the edges of the map
    pin.goto((place[3] / 195) * window.window_width() / 2, (place[2] / 120) * window.window_height() / 2)
    pin.stamp()  # Stamps on the location
    pin.write(place[0] + "'s place:\n    " + place[1], font=("Arial", 10, "bold"))  # Stamps the text describing the location


def raw_build_userlist():
    """
    An interactive function to match user to a user_color for the map
    :return: a list of tuples: (user, user_color) where both user and user_color are strings
    example: [('Jan', 'green'), ('Scott', 'blue')]
    """
    userlist=[]
    num_users=int(raw_input("How many users will be using this map? "))
    for i in range(num_users):
        user=raw_input("Please enter user "+str(i)+" name: ")
        color=raw_input("Please enter user "+user+"'s color: ") 
        userlist.append((user, color)) #appends (user, color) tuple to userlist
    
    print("Userlist built.\n")
    return userlist
        
def raw_build_places_list(userlist):
    """
    An interactive mode for adding places to the map
    param userlist: is a list of tuples: (user, user_color) where both user and user_color are strings
    example: [('Jan', 'green'), ('Scott', 'blue')]
    
    :return: a list of tuples where each tuple is a place to put on the map
    The tuple order is:
    [0]: A string representing the user's name
    [1]: A string representing the name of the location (e.g., Eiffel Tower)
    [2]: A float representing the latitude of the location (e.g., 41.156537)
    [3]: A float representing the longitude of the location (e.g., -93.710720)
    [4]: A string representing the user's color
    example: [("Dr. Scott", "Childhood Home", 41.156537, -93.7107200, "blue")
              ("Dr. Jan", "Southernmost city", -54.801912, -68.302951, "green")
              ("Dr. Jan", "Seattle, WA", 47.606209, -122.332071, "green")]
    """
    places_list = []
    
    keep_going = 'y'
    userdict=dict(userlist) #converts to dictionary for easy lookup
    
    print("Please enter location information for each user.")
    
    while keep_going == 'y' or keep_going == 'yes':
        username = raw_input("Please enter user name: ")
        location = raw_input("Please enter the name of the place: ")
        latitude = float(raw_input("Please enter the latitude of the place: "))
        longitude = float(raw_input("Please enter the longitude of the place: "))
        if username in userdict:
            usercolor=userdict[username] #set usercolor by tuple lookup
        else:
            usercolor='black' # If the user doesn't exist, use black
        places_list.append((username, location, latitude, longitude, usercolor))
        keep_going = raw_input("Would you like to add an additional place? (y or n): ").lower()

    return places_list

def write_out(placelist, filename):
    ''' This function does not ask for input from the user.
        param: placelist is a list of tuples as described below. 
        param: filename should be a string including extension such as "outfile.txt"
        This funciton opens filename for writing then
        writes out the number of tuples found in placelist followed by
        each tuple element of placelist on individual line
        for example if placelist is the following list of tuples:
            [("Dr. Scott", "Childhood Home", 41.156537, -93.7107200, "darkblue")
             ("Dr. Jan", "Southernmost city in the world", -54.801912, -68.302951, "green"),
             ("Dr. Jan", "Seattle, WA", 47.606209, -122.332071, "green")]
              is written out in filename as:
              3
              Dr. Scott
              Childhood home
              41.156537
              -93.7107200
              darkblue
              Dr. Jan
              Southernmost city in the world
              -54.801912
              -68.302951
              green
              Dr. Jan
              Seattle, WA
              47.606209
              -122.332071
              green
    '''
 
    
    print("Opening " + filename + " for writing.")
    
    myfile=open(filename, "w")   # Opens filename for writing
    length = len(placelist)          # Finds the length of placelist
    myfile.write(str(length))     # Writes the length of the string 
    myfile.write("\n")
    for i in placelist:        # Creates a loop
        for element in i: 
            myfile.write(str(element))
            myfile.write("\n")
    myfile.close()                      # Closes the file
    

    print(filename +" written.")
    
def read_in(filename):
    '''
    This function does not ask for input from the user. 
    param: filename should be the name of the file. 
    This function opens filename for reading. It reads the file line by line and appends the 
    information to places_list and returns places_list.
    '''
    mynewhandle = open(filename, 'r') #opens file for reading
    
    str_num = mynewhandle.readline()
    str_num = int(str_num[0:len(str_num)-1]) # The '/n' characters need to be removed

    places_list=[]
    for i in range(str_num):
        name = mynewhandle.readline()
        name = name[0:len(name)-1]  # The '/n' characters need to be removed and converted to int
        location = mynewhandle.readline()
        location = location[0:len(location)-1] # The '/n' characters need to be removed
        latitude = mynewhandle.readline()
        latitude = float(latitude[0:len(latitude)-1]) # The '/n' characters need to be removed and converted to float
        longitude = mynewhandle.readline()
        longitude = float(longitude[0:len(longitude)-1]) # The '/n' characters need to be removed and converted to float
        usercolor = mynewhandle.readline()
        usercolor = usercolor[0:len(usercolor)-1] # The '/n' characters need to be removed
        places_list.append((name, location, latitude, longitude, usercolor)) # append appropraite tuple to list
    mynewhandle.close()

    print("places_list created.")
    return places_list

def main():
    """
    This program is designed to place pins on a world map. 
    Each place is represented as a tuple.
    Each tuple is then added to a list 
    to make iterating through all the places and adding them to the map easier.
    """

    # The next three lines set up the world map
    wn = turtle.Screen()
    wn.setup(width=1100, height=650, startx=0, starty=0)
    wn.bgpic("world-map.gif")
    
    myuserlist=[]
    place_list=[]

    mode = raw_input("Using a file? If yes, please enter the full filename, if no, please enter 'n' ")
    if mode =='n':
        myuserlist = raw_build_userlist()
        place_list = raw_build_places_list(myuserlist)  # an interactive mode of building place_list
    else:
        place_list=read_in(mode) # generates place_list from file named mode

    # Iterates through each item in the list,  calling the place_pin() function
    for place in place_list:    
        place_pin(wn, place)  # Adds ONE place to the map for each loop iteration

    write_out(place_list, "newplacelist.txt")    
    
    wn.exitonclick()


main()