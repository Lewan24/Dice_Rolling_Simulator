# Functions

import random # import random to python
from OtherFunctions import *

class Game(): # main class for game
    
    def __init__(self): # just init, work when class is creating new object
        self.__state = "NOT"
        self.__programmerName = "Artur"
        self.__programmerSurname = "Lewandowski"
        self.__developer = "Uncle_Bob_Games"
        
        # default min and max roll
        self.__minDice = 1
        self.__maxDice = 6
    
    @staticmethod
    def getRandomRoll(minRoll, maxRoll): # function for selecting random number
        return random.randint(minRoll, maxRoll)
        
    def getDiceRoll(self): # get minimum roll, and max roll
        print("Min roll: {}, max roll: {}".format(self.__minDice, self.__maxDice))
    
    def startRolling(self):
        if self.__state == "RUNGAME":
            # Start main game project
            
            diceRoll = self.getRandomRoll(self.__minDice, self.__maxDice) # make random roll
            
            clear() # clear screen
            print("=======================================================\n")
            print("               Dice Rolling Simulator\n")
            print("=======================================================\n\n")
            
            self.getDiceRoll() # get min and max roll
            
            print("\nYour roll: {}".format(diceRoll))
            
            print("\n\n1. Roll again\n") # little menu
            print("2. Back to menu\n")
            print("3. Change size of dice\n")
            
            try: # try get number (int)
                option = int(input("Your choose: "))
            except: # only when user write any character or enter etc
                input("\nI think you did not select number, try again...")
                self.menu()
                
            if option == 1: # little menu if statement
                self.startRolling()
                
            elif option == 2:
                self.menu()
                
            elif option == 3: # change min and max roll
                clear()
                self.__minDice = int(input("Min roll: "))
                self.__maxDice = int(input("Max roll: "))
                self.startRolling()
                
            else:
                input("\n\nHmm.. Something just went wrong, try again...") # if user write another number
                                                                # which is not in menu
                self.menu()
        else:
            input("You don't have permissions to start any other function before runGame()...")
            self.exit()
            
    def myCredits(self): # simple credits for game
        if self.__state == "RUNGAME":
            clear()
            print("=======================================================\n")
            print("                     Honor Table\n")
            print("=======================================================\n\n")
            
            # get programmer name and surname, print it
            print("Programmer: {} {}".format(self.__programmerName, self.__programmerSurname))
            # get developer
            print("Developer: {}".format(self.__developer))
            
            input("\n\nClick anything to continue...")
            self.menu()
        else:
            input("You don't have permissions to start any other function before runGame()...")
            self.exit()
        
    @staticmethod
    def exit(): # simple function for exit
        exit("Exiting from Program...")
    
    def menu(self): # main menu statement
        if self.__state == "RUNGAME":
            clear()
            print("=======================================================\n")
            print("Hello I am Python and I want to roll some dices for you\n")
            print("=======================================================\n\n")
            
            print("1. Start Rolling\n")
            print("2. Credits\n")
            print("3. Exit\n\n")
            
            try: 
                option = int(input("Your choose: "))
            except:
                input("\nI think you did not select number, try again...")
                self.menu()
            
            if option == 1:
                self.startRolling()
                
            elif option == 2:
                self.myCredits()
                
            elif option == 3:
                self.exit() 
                
            else:
                input("\n\nHmm.. Something just went wrong, try again...")
                self.menu()       
        else:
            input("You don't have permissions to start any other function before runGame()...")
            self.exit()
    
    def runGame(self): # main function for run game
        self.__state = "RUNGAME"
        self.menu()