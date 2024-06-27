#******************************************************************
# Justin Snyder Lab6
# Programmer: Justin Snyder
# Completed : 4/7/2024
# Status    : Complete
#
# This program takes in amount of tickets you want to generate and
# displays powerball or mega million ticket numbers
#******************************************************************

# Importing modules
from tkinter import *
from tkinter import messagebox
import random
import datetime

# Defining how the window will look
root = Tk()
root.geometry("1024x1024")
root.title("Lottery Project")


# Function loadPowerBall
#
# Purpose: removes main menu objects and loads all of the powerball display objects
def loadPowerBall():
    # Destorys main menu objects
    button1.destroy()
    button2.destroy()

    # Changes background image to powerball background
    label1.configure(image= powerballBackground)
    
    # Makes all powerball objects global
    global label2
    global numEntry
    global button3
    global button4
    global checkBox
    global checkBoxValue

    # Powerball title
    label2 = Label(root, text="How many PowerBall Tickets do you want to buy?", font=("Arial", 30))
    label2.pack()

    # Powerball input box
    numEntry = Entry(root, text= "Number of Tickets", font=("Arial", 30))
    numEntry.place(x=290, y=100)

    # Power play check box
    checkBoxValue = IntVar()
    checkBox = Checkbutton(root, text = "Power Play?", font=("Arial", 14),variable=checkBoxValue, onvalue=1, offvalue=0)
    checkBox.place(x=440, y=149)

    # Submit button
    button3 = Button(root,text="Submit", command= lambda: checkPowerballInput(numEntry.get()), font=("Arial", 15)) 
    button3.place(x=470, y=185)

    # Main menu button
    button4 = Button(root,text="Main Menu", command= lambda: loadMainMenu(), font=("Arial", 20), bg='#c40233') 
    button4.place(x=73, y=50)


# Function loadMegaMillions
#
# Purpose: removes main menu objects and loads all of the mega millions display objects
def loadMegaMillions():
    # Destroys main menu objects
    button1.destroy()
    button2.destroy()

    # Changes background image to mega millions background
    label1.configure(image= megaMillionsBackground)

    # Makes all mega millions objects global
    global label2
    global numEntry
    global button3
    global button4
    global checkBox
    global checkBoxValue

    # Mega millions title
    label2 = Label(root, text="How many Mega Millions Tickets do you want to buy?", font=("Arial", 30))
    label2.pack()

    # Mega millions input box
    numEntry = Entry(root, text= "Number of Tickets", font=("Arial", 30))
    numEntry.place(x=50, y=200)

    # Megaplier check box
    checkBoxValue = IntVar()
    checkBox = Checkbutton(root, text = "Megaplier?", font=("Arial", 14),variable=checkBoxValue, onvalue=1, offvalue=0)
    checkBox.place(x=210, y=249)

    # Mega millions submit button
    button3 = Button(root,text="Submit", command= lambda: checkMegaMillionsInput(numEntry.get()), font=("Arial", 15)) 
    button3.place(x=230, y=285)

    # Mega millions main menu button
    button4 = Button(root,text="Main Menu", command= lambda: loadMainMenu(), font=("Arial", 20), bg='#c40233') 
    button4.place(x=42, y=50)


# Function loadMainMenu
#
# Purpose: removes powerball or mega millions objects and loads all main menu objects
def loadMainMenu():
    # Destroys powerball or mega millions objects
    label2.destroy()
    numEntry.destroy()
    button3.destroy()
    button4.destroy()
    checkBox.destroy()

    # Changes background image to main menu background
    label1.configure(image= mainMenu)

    # Makes menu buttons global
    global button1
    global button2

    # Powerball menu option
    button1 = Button(root,text="Power Ball",command=loadPowerBall, font=("Arial", 55)) 
    button1.place(x=300, y=300)
    
    # Mega millions menu option
    button2 = Button(root, text = "Mega Millions",command=loadMegaMillions, font=("Arial", 55)) 
    button2.place(x=255, y=600)


# Function checkPowerballInput
#
# Purpose: protects the input then prints 10 displays of numbers per powerball ticket
def checkPowerballInput(powerballInput):
    try:
        powerballInput = int(powerballInput)
        if powerballInput > 100:
            messagebox.showinfo("Tickets", f'The Maximum amount of tickets that can be generated is 100!')
        elif powerballInput >= 1:
            if powerballInput > 10:
                printPowerballTickets(10)
                powerballInput = powerballInput - 10
                checkPowerballInput(powerballInput)
            elif powerballInput == 10:
                printPowerballTickets(10)
            elif powerballInput < 10:
                printPowerballTickets(powerballInput)
        else:
            displayError()
    except:
        displayError()


# Function checkMegaMillionsInput
#
# Purpose: protects the input then prints 10 displays of numbers per mega million ticket
def checkMegaMillionsInput(megaMillionsInput):
    try:
        megaMillionsInput = int(megaMillionsInput)
        if megaMillionsInput > 100:
            messagebox.showinfo("Tickets", f'The Maximum amount of tickets that can be generated is 100!')
        elif megaMillionsInput >=1:
            if megaMillionsInput > 10:
                printMegaMillionTickets(10)
                megaMillionsInput = megaMillionsInput - 10
                checkMegaMillionsInput(megaMillionsInput)
            elif megaMillionsInput == 10:
                printMegaMillionTickets(10)
            elif megaMillionsInput < 10:
                printMegaMillionTickets(megaMillionsInput)
        else:
            displayError()
    except:
        displayError()


# Function displayError
#
# Purpose: displays an error
def displayError():
    messagebox.showinfo("Tickets", 'Please only input positive whole numbers!')

# Function printPowerballTickets
#
# Purpose: opens new window and displays the powerball tickets
def printPowerballTickets(powerballInput):
    # Creates a new window
    top = Toplevel()
    top.geometry('350x512')
    top.title('Printed Powerball Tickets')

    # Powerball image
    Label(top, image = powerballImage).pack()

    # Displays current time
    Label(top, text = currentTime(), font='Arial 11 bold').pack()

    # Odds info
    Label(top, text = "POWERBALL GRAND PRIZE ODDS\n 1 IN 292,201,338 OVERALL ODDS 1 IN 24.9\n THANKS FOR SUPPORTING TEXAS\n EDUCATION AND VETERANS!\n --------------------------------------------------------------------------------------------------------------").pack()
    Label(top, text = " ", font='Arial 5 bold').pack()

    # Powerball indicator
    label1 = Label(top, text="POWERBALL", font="Arial 9") 
    label1.place(x = 200, y = 170) 

    # loop that displays powerball numbers
    for ticket in range(powerballInput):
        Label(top, text = Powerball(ticket), font='Arial 11 bold').pack()
    Label(top, text = "------------------------------------------------------------------------------------------------------------------------------------------").pack()

    # Checks the value of the checkbox and changes the values of cost and megaplier
    localBoxValue = checkBoxValue.get()
    costMultiplier = 2
    powerPlay = ''
    if localBoxValue == 1:
        costMultiplier = 3
        powerPlay = 'YES'
    elif localBoxValue == 0:
        costMultiplier = 2
        powerPlay = 'NO'
    
    # Total cost of the ticket
    Label(top, text = f"POWERPLAY - {powerPlay}                 ${powerballInput*costMultiplier:.2f}", font='Arial 15 bold').pack()


# Function printMegaMillionTickets
#
# Purpose: opens new window and displays the mega millions tickets
def printMegaMillionTickets(megaMillionsInput):
    # Creates a new window
    top = Toplevel()
    top.geometry('350x512')
    top.title('Printed Mega Million Tickets')

    # Mega millions image
    Label(top, image = megaMillionsImage).pack()

    # Displays current time
    Label(top, text = currentTime(), font='Arial 11 bold').pack()

    # Odds info
    Label(top, text = "MEGA MILLIONS GRAND PRIZE ODDS\n 1 IN 302,575,350 OVERALL ODDS 1 IN 24.0\n (INCLUDING BREAK EVEN PRIZES)\n --------------------------------------------------------------------------------------------------------------").pack()
    Label(top, text = " ", font='Arial 5 bold').pack()

    # Megaball indicator
    label1 = Label(top, text="MEGABALL", font="Arial 9") 
    label1.place(x = 200, y = 170) 

    # loop that displays mega million numbers
    for ticket in range(megaMillionsInput):
        Label(top, text = megaMillions(ticket), font='Arial 11 bold' ).pack()
    Label(top, text = "------------------------------------------------------------------------------------------------------------------------------------------").pack()

    # Checks the value of the checkbox and changes the values of cost and megaplier
    localBoxValue = checkBoxValue.get()
    costMultiplier = 2
    megaplier = ''
    if localBoxValue == 1:
        costMultiplier = 3
        megaplier = 'YES'
    elif localBoxValue == 0:
        costMultiplier = 2
        megaplier = 'NO'
    
    # Total cost of the ticket
    Label(top, text = f"MEGAPLIER - {megaplier}                 ${megaMillionsInput*costMultiplier:.2f}", font='Arial 15 bold').pack()


# Function megaMillions
#
# Purpose: generates the 5 mega million numbers then the megaball and returns them
def megaMillions(ticket):
    # Generates 5 random numbers from 1-70 and sorts them
    numbers = sorted(random.sample(range(1, 71), 5))
    numbersFixed = []
    
    for num in numbers:
        numbersFixed.append(format(num, '02d'))

    # Assigns each random number a variable
    ran1 = numbersFixed[0]
    ran2 = numbersFixed[1]
    ran3 = numbersFixed[2]
    ran4 = numbersFixed[3]
    ran5 = numbersFixed[4]

    # Generates a random number from 1-25 which is the megaball
    megaball = format(random.randint(1, 25), '02d')

    # Returns the formated mega million numbers
    return f"{alpha[ticket]}: {ran1} {ran2} {ran3} {ran4} {ran5} - {megaball}"


# Function Powerball
#
# Purpose: generates the 5 powerball numbers then the last powerball and returns them
def Powerball(ticket):
    
    powerball_numbers = []
    
     # Generate 5 random numbers from 1 to 69 for the main numbers
    main_numbers = sorted(random.sample(range(1, 70), 5))
    mainNumbersFixed = []


    for num in main_numbers:
        mainNumbersFixed.append(format(num, '02d'))

    # Generate a random number from 1 to 26 for the Powerball
    power_ball = format(random.randint(1, 26), '02d')
    # Append the main numbers and the Powerball to the list of Powerball numbers
    powerball_numbers.append((mainNumbersFixed, power_ball))
    
    main_numbers_str = ' '.join(map(str, mainNumbersFixed))
    # Return the list of Powerball numbers
    
    final_main_numbers = (f"{alpha[ticket]}: {main_numbers_str} - {power_ball}")
    return final_main_numbers


# Function currentTime
#
# Purpose: gets the current time and date and formats them
def currentTime():
    # Gets the current time
    now = datetime.datetime.now()

    # Gets abbreviated day, month, day of the month
    day = now.strftime('%a') 
    month = now.strftime('%b')
    dayMonth = now.strftime('%d') 

    # Gets hour, minute, second, and timezone
    hour = now.strftime('%H')
    min = now.strftime('%M') 
    sec = now.strftime('%S')
    timeZone = "CT"

    # Formats the current time and date
    formatTime = f"PRINTED ON {day.upper()} {month.upper()}{dayMonth} {now.year} {hour}:{min}:{sec} {timeZone}"

    return formatTime


# Trys to load all of the images used and displays an error if it fails
try:
    megaMillionsBackground = PhotoImage(file="pictures/megaMillionsBackground.png")
    powerballBackground = PhotoImage(file="pictures/powerballBackground.png")
    mainMenu = PhotoImage(file="pictures/mainMenu.png")
    powerballImage = PhotoImage(file="pictures/powerball.png")
    megaMillionsImage = PhotoImage(file="pictures/megaMillions.png")
except:
    print("ERROR: MISSING 1 OR MORE PICTURES")
    messagebox.showinfo("Tickets", 'ERROR: MISSING 1 OR MORE PICTURES')

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] # 10 letters of the alphabet

# Displays main menu background image
label1 = Label( root, image= mainMenu) 
label1.place(x = 0, y = 0) 

# PowerBall menu option
button1 = Button(root,text="Power Ball",command=loadPowerBall, font=("Arial", 55)) 
button1.place(x=300, y=360)
  
# Mega millions menu option
button2 = Button(root, text = "Mega Millions",command=loadMegaMillions, font=("Arial", 55)) 
button2.place(x=255, y=648)


# Keeps all windows open
root.mainloop()