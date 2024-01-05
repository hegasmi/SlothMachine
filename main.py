import random
MAX_LINE=3
MAX_BET=1000
MIN_BET=1
VALUE_RANGE=300

ROWS=3
COLUMNS=3
SYMBOL_DICT={
    "A":2,
    "B":6,
    "C":4,
    "D":8
}
synbol_val_dict={}
total=0
def generate_symbol_val():
    for s in SYMBOL_DICT:
        synbol_val_dict[s] = random.randrange(VALUE_RANGE)

def deposit():
    while True:
        amount=input("Enter the amount in $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Your deposit is 0!! Enter more amount")
        else:
            print("Enter a Integer")
    return amount


def get_line_number():
    while True:
        line=input("Enter the line between 1 and "+str(MAX_LINE)+":")
        if line.isdigit():
            line=int(line)
            if 1<=line<=MAX_LINE:
                break
            else:
                print("Out of range Enter correct value")
        else:
            print("Enter a Integer")
    return line


def bet_amount():
    while True:
        bet=input(f"Enter the bet ammount between ${MIN_BET} and ${MAX_BET}:")
        if bet.isdigit():
            bet=int(bet)
            if MIN_BET<=bet<=MAX_BET:
                break
            else:
                print("Out of range Enter correct value")
        else:
            print("Enter a Integer")
    return bet

def spin_slot_machine(rows,cols,symbols):
    print("Cross your finger Im spinning the slot machine!!")
    symbol_pool=[]
    for key, val in symbols.items():
        for _ in range(val):
            symbol_pool.append(key)
    combinations=[]
    for _ in range(cols):
        roll=[]
        current_pool=symbol_pool[:]
        for _ in range(rows):
            value=random.choice(current_pool)
            current_pool.remove(value)
            roll.append(value)
        combinations.append(roll)
    print_slot_machine(combinations)
    return combinations

def print_slot_machine(combinations):
    for r in range(len(combinations[0])):
        for roll in combinations:
            print(f"{roll[r]} ",end=" ")

        print()
    generate_symbol_val()
    


def check_luck(deposit, combinations,line,bet):
    total=0
    for i in range(line):
        row=combinations[i]
        for r in row:
            total+=synbol_val_dict[r]
    if bet==total:
        print(f"Congragulation you ${sum+deposit}")
    else:
        print("Better luck next time")




def start():
    balance=deposit()
    line=get_line_number()
    while True:
        bet=bet_amount()
        if (bet*line)<=balance:
            break
        else:
            print(f"You dont have balance to bet that amount!!/n Your current balance is ${balance}")
    combi=spin_slot_machine(ROWS,COLUMNS,SYMBOL_DICT)
    check_luck(balance,combi,line,bet)


def main():
    start()
    while True:
        spinAgain=input("If you want to spin again press Y Else press N:")
        if spinAgain=="Y":
            start()
        elif spinAgain=="N":
            break
        else:
            print("Only Y or N is allowed")
 
main()




        