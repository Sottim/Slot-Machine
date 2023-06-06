import random 

MAX_LINES = 3 #Initialize the constant which remains same throughtout 
MAX_BET_VALUE = 100
MIN_BET_VALUE = 1

ROWS = 3
COLUMNS = 3

symbolsCount = {"A": 2, "B": 4, "C": 6, "D": 8}

def spin_slot_machine(rows, colms, symbols):
    all_symbols = []
    #This fills the list with all the symbols according to the count of each symbols
    #all_symbols = ['A', 'A', 'B', 'B', 'B', 'B', 'B', 'C', ........]
    for key, value in symbolsCount.items():
        for _ in range(value): #If we dont need i here, we just use '_' empty to use less memory
            all_symbols.append(key)
    
    #This will find value for each row of the specific column.
    #If there are three columns and three rows, so for each column it will pick 3 values to insert in the rows of that column in the first iteration  
    columns = []
    for col in range(colms):
        column = []
        #making a copy of list so that we can remove the item if once chosen
        current_symbols = all_symbols[:]  #Use slice ':' operator so that both list have different object. Modification in one doesnot affect the other.
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    #Since the columns are stored as lists within a list, we need to transpose the matrix to correct
    #and get the elements of columns in that same column
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i < len(columns) - 1:
                print(column[row], end = " | ")
            else: # Donot print pipe for the last index
                print(column[row], end="")
        print()
            
def deposit():
    while True:
        amount = input("Enter deposit amount : $")
        if amount.isdigit(): #digit make sure entered amt is a +ve value
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print("Please, enter the valid amount.")
        else: 
            print("Invalid Amount ! It should be a number.")
    return amount 

def getNumberOfLines():
    while True:
        lines = input("Enter number of lines to bet upon (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit(): #digit make sure entered amt is a +ve value
            lines = int(lines)
            if lines >= 1 and lines <= MAX_LINES:
                break
            else: 
                print("Please, enter the valid number of lines.")
        else: 
            print("Invalid ! Input should be a number.")
    return lines

def get_bet():
    while True:
        amount = input("How much you want to bet on each line? $ ")
        if amount.isdigit(): #digit make sure entered amt is a +ve value
            amount = int(amount)
            if amount >= MIN_BET_VALUE and amount <= MAX_BET_VALUE:
                break
            else:
                # f helps to display multiple values and automatically converts those 
                # values to strings if necessary. They should be enclosed with curly braces.
                print(f"Amount must be between ${MIN_BET_VALUE} - {MAX_BET_VALUE}") 
        else: 
            print("Invalid ! Input should be a number.")
    return amount




def main():
    totalBalance = deposit() #calling the function to update the balance
    lines = getNumberOfLines()
    # To check the current balance the player has.
    while True: #while the condition executes if block, run the loop till then.
        bet = get_bet()
        if(bet * lines > totalBalance):
            print(f"You donot have enough amount. Your current balance is {totalBalance}.")
        else:
            break

    print(f"Your bet amount ${bet} on {lines} lines. Total bet is : ${bet * lines}")

    slots = spin_slot_machine(ROWS, COLUMNS, symbolsCount)
    print_slot_machine(slots)

main()


