# Stuart Daniells
# Date: 2021-12-14

def reserveSeats(theatreArray, numberOfSeats, preference):
    global reservationNum
    num = 0
    seatsAdded = 0
    lastSeatRow = len(theatreArray[0]) - 1
    
    # back seating
    if preference == 1 and theatreArray[0].count(0) >= numberOfSeats:
        while(seatsAdded < numberOfSeats and num <= 10):
            if theatreArray[0][num] == 0:
                theatreArray[0][num] = reservationNum
                seatsAdded += 1
            num += 1
    
    # front seating        
    elif preference == 2 and theatreArray[7].count(0) >= numberOfSeats:
        while(seatsAdded < numberOfSeats and num <= 10):
            if theatreArray[7][lastSeatRow - num] == 0:
                theatreArray[7][lastSeatRow - num] = reservationNum
                seatsAdded += 1
            num += 1
    else:
        print("\n--- The reservation cannot be made, due to unavailability of seats for your row choice ---") 
        reservationNum -= 1
        
    return theatreArray    


def reserveSpecificSeats(theatreArray , numberOfSeats, row, column):   
    global reservationNum
    actualRow = len(theatreArray) - row 
    actualColumn = column - 1
    seatsAdded = 0
    oldTheatreArray = theatreArray.copy()
    
    # counting the number of vacant seats remaining
    # vacantSeats = sum(element == 0 for element in theatreArray[actualRow])
    
    if theatreArray[actualRow][actualColumn] == 0:
        while(seatsAdded < numberOfSeats):
            if theatreArray[actualRow][actualColumn] != 0:
                print("\n--- The reservation cannot be made, due to unavailability of seats for your row choice ---") 
                reservationNum -= 1
                return oldTheatreArray                    
            else:
                theatreArray[actualRow][actualColumn] = reservationNum
                seatsAdded += 1
            actualColumn += 1
            
    else:
        print("\n--- The reservation cannot be made, due to unavailability of seats for your row choice ---") 
        reservationNum -= 1
        
    return theatreArray
    

def cancelSeats(theatreArray, reservationNum):
    countCheck = 0
    # Checking each row for booking number
    for i,row in enumerate(theatreArray):
        for j,element in enumerate(row):
            if element == reservationNum:
                theatreArray[i][j] = 0
                countCheck += 1
        
    if countCheck == 0:
        print("\n  --- The reservation number doesn't match our records, please enter the correct one ---")
        return theatreArray
    else:
        return theatreArray

def removeEmptySeatsRow(theatreArray,rowShift):
    actualRow = len(theatreArray) - rowShift
    
    for element in theatreArray[actualRow]:
        if element == 0:
            theatreArray[actualRow].append(theatreArray[actualRow].pop(0))
            
        if theatreArray[actualRow][0] != 0:
            return theatreArray

def search(theatreArray, reservationNum):
    print("\nSEATS INCLUDED:")
    
    countCheck = 0
    
    # Checking each row for booking number
    for i,row in enumerate(theatreArray):
        for j,element in enumerate(row):
            if element == reservationNum:
                print("Row:", len(theatreArray) - i, "Seat:", j + 1)
                countCheck += 1
        
    if countCheck == 0:
        print("\n  --- No seats with specified booking number could be located. ---")
        return theatreArray
    else:
        return theatreArray

def totalBooked(theatreArray):
    countCheck = 0
    
    for row in (theatreArray):
        for element in (row):
            if element != 0:
                countCheck += 1
        
    if countCheck == 0:
        print("\n  --- No seats with specified booking number could be located. ---")
        return theatreArray
    else:
        print("\n ---> The total number of seats reserved in the theatre is", countCheck)
        return theatreArray
    

def displayMap(theatreArray):
    count = 0
    
    print("\n\t\t\t******* Theatre Seating Map *******\n")
    for i in theatreArray[0]:
        count += 1
        print("\tSeat", count, end = ' ')
    print()
    count = 9
    for i in theatreArray:
        count -= 1
        print("Row", count, end = '')
        for j in i:
            print('\t', j, end = '')
        print()

def displayMenu():
    print("\n***********************")
    print("MENU:\n")
    print("\t1. Reserve seats\n")
    print("\t2. Reserve seats with specific starting row and column\n")
    print("\t3. Cancel reservation\n")
    print("\t4. Remove empty seats from specific row\n")
    print("\t5. Search for reservation\n")
    print("\t6. Total seats booked\n")
    print("\t7. Display theatre map\n")
    print("\t8. Exit application")
    print("***********************")
    
    
def inputValidation(choice, inputType):
    while(choice):
        try:
            choice = int(choice)
            
            # for user input of menu choice
            if inputType == 'menu/row' and (choice <= 8 and choice >= 1):
                return choice
            elif inputType == 'menu/row':
                while(choice > 8 or choice < 1):
                    choice = int(input("Make a selection (between 1 and 8) only: "))
            
            # for user input of seating choice   
            if inputType == 'seating/column' and (choice <= 10 and choice >= 1):
                return choice
            elif inputType == 'seating/column':
                while(choice > 10 or choice < 1):
                    choice = int(input("Make a selection (between 1 and 10) only: "))
            
            # for user input of preference choice   
            if inputType == 'preference' and (choice <= 2 and choice >= 1):
                return choice
            elif inputType == 'preference':
                while(choice > 2 or choice < 1):
                    choice = int(input("Make a selection (between 1 and 2) only: "))
            elif inputType == 'numberValidation':
                return(choice)
                    
        except ValueError:
            choice = input("Please enter a number not a string: ")
            
        except TypeError:
            choice = input("Please enter a number not a string or empty space: ")
            
        except Exception:
            choice = input("Please enter a number (between 1 and 8) only: ")
    
    
if __name__ == '__main__':
        
    reservationNum = 0
    
    # initialising theatre 2D array with values - 0 
    theatreArray = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
    ]
        
    # Constantly loop to display Menu and options till user chhoose option - 8 (exit)
    while(True):
        # Displaying menu choices for user to choose from
        displayMenu()
        
        # Prompting for user choice 
        menuChoice = input("\nFrom the list of Menu options make a selection (between 1 and 8): ")
        
        # input validation for menu choice
        menuChoice = inputValidation(menuChoice, 'menu/row')
        
        
        # user based choice decisions
        
        # Reserve seats
        if menuChoice == 1:
            reservationNum += 1
            
            numberOfSeats = inputValidation(input(
                "\nEnter number of adjacent seats you require: "), 'seating/column')
            
            preference = inputValidation(input(
                "\nPreference of seating (1 for back, 2 for front): "), 'preference')
            
            theatreArray = reserveSeats(theatreArray, numberOfSeats, preference)
        
        # Reserve seats with specific starting row and column
        elif menuChoice == 2:
            reservationNum += 1
        
            numberOfSeats = inputValidation(input(
                "\nEnter number of adjacent seats you require: "), 'seating/column')
        
            rowNum = inputValidation(input(
                "\nEnter row number you wish to book your seats: "), 'menu/row')
            
            columnNum = inputValidation(input(
                "\nEnter column/seat number you want your seats to begin at: "), 'seating/column')
        
            theatreArray = reserveSpecificSeats(theatreArray , numberOfSeats, rowNum, columnNum)
        
        # Cancel reservation
        elif menuChoice == 3:
            userResNum = input("\nEnter the reservation number you'd like to cancel: ")
            userResNum = inputValidation(userResNum, 'numberValidation')
            
            theatreArray = cancelSeats(theatreArray, userResNum)
        
        # Remove empty seats from specific row
        elif menuChoice == 4:
            rowShift = input("\nEnter the row number where you'd like to shift the empty seats: ")
            rowShift = inputValidation(rowShift, 'numberValidation')
            
            theatreArray = removeEmptySeatsRow(theatreArray,rowShift)
        
        # Search for reservation
        elif menuChoice == 5:
            reservationNum = input("\nEnter the reservation number you'd like to search for: ")
            reservationNum = inputValidation(reservationNum, 'numberValidation')
            
            theatreArray = search(theatreArray, reservationNum)
        
        # Total seats booked
        elif menuChoice == 6:
            theatreArray = totalBooked(theatreArray)
        
        # Display theatre map
        elif menuChoice == 7:
            displayMap(theatreArray)
        
        # Exit application
        elif menuChoice == 8:
            print("\n------------- Thanks for using the application! -------------")
            exit()
        
        
    
    
    
    