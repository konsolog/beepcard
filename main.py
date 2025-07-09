#this will be fun
load = 0.0

print(f"Welcome to the LRT-1 System!\n")
def main():
    print(f"""
****************************
Load Balance: PHP {load:.2f}
Choices
1-Load Beep Card
2-Display All Stations
3-Trip and Fare
4-Transaction History
5-Exit
    """)
    call = input("Choose from the options: ")

    try:
        call = int(call)
    except:
        print("⚠️ ACHTUNG! THE CHOICE IS INVALID")
        return 0

    return call # This returns (outputs) the selected choice

on = True
while on: # infinite looping
    sel = main()

    if sel == 5:
        print("Thank you for using the LRT-1 System!")
        on = False # graceful exit
    elif sel == 2:
            print("""****************************
    All LRT-1 Stations
    1-Baclaran
    2-EDSA
    3-Libertad
    4-Gil Puyat
    5-Vito Cruz 
    6-Quirino 
    7-Pedro Gil 
    8-UN Avenue 
    9-Central Terminal 
    10-Carriedo""")

    elif sel == 1:
        print(f"\n****************************\nLoad Balance: PHP {load:.2f}")
        a = input("Enter the amount (greater than 0) to load on your beep card: ")
        try:
            v = int(a)
            if v > 0:
                q = input("Complete the transaction (Y/N)? ")
                if q.upper() == "Y":
                    load += v
                    print(f"PHP {v:.2f} successfully loaded to your beep card.")
                elif q.upper() == "N":
                    print("Cancelled Transaction")
                else:
                    print("Invalid input")
            else:
                print("Amount must be greater than 0")
        except:
            print("Invalid amount")

    elif sel == 0:
        pass  # invalid input previously handled in main (this is rather important)

    else:
        print("⚠️ ACHTUNG! Not in the given choices.")