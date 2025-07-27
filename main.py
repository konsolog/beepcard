# This is to certify that this project is my work based on my personal
# Make efforts to study and apply the concepts learned. I have constructed
# the functions, their respective algorithms, and the corresponding code by
# myself. The program was run, tested, and debugged by my efforts. I
# further certify that I have not copied in part or whole or otherwise
# plagiarized the work of other students and/or persons.
# Josh Caleb B. Aggabao, DLSU ID# 12462098
# Gerald James Z. Tan, DLSU ID# 12470732
# David Angelo D. Torreon, DLSU ID# 12466514 

# Description: A loadable train card system
# Programmed by: Gerald James Z. Tan, David Angelo D. Torreon, Josh Caleb B. Aggabao, STEM11-P
# Last modified: July 18, 2025
# Acknowledgements: https://docs.python.org/
load = 0.0
history = ""

print(f"Welcome to the LRT-1 System!")
def main(): # this handles the inputs for the primary part of the main menu
    print(f"""****************************
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
        return

    return call # this returns (outputs) the selected choice

def amnt_newlines(s): # this counts how many newlines (\n) there are
    count = 0
    i = 0
    end = False

    while not end:
        try:
            if s[i] == '\n': # going through the whole string, add one for every \n found
                count += 1
            i += 1
        except IndexError:
            end = True

    return count

def trim(s, n): # trim the first newline of history, keeping only the (n+1)th new line, so if n=0, it would keep everything after the last newline. if n=1, keep everything after the second to last newline, and so on.
    # get total number of newlines first
    total = amnt_newlines(s)
    if total <= n:
        return s

    # determine the length of s manually
    size = 0
    end = False
    while not end:
        try: # go through the whole string again counting the amnt of lines
            s[size] 
            size += 1
        except IndexError:
            end = True 

    # go backwards to find the (n+1)th newline
    c = 0
    i = size - 1
    stop_index = 0
    done = False

    while not done and i >= 0:
        try:
            if s[i] == '\n': # picks up the (size - 1)th's \n
                c += 1
                if c == n + 1:
                    stop_index = i + 1
                    done = True
            i -= 1
        except IndexError: # fail to get the index
            done = True  # fallback, tho shouldnt be needed since size is known

    # goes through from stop_index to the end
    res = ""
    i = stop_index
    finished = False
    while not finished:
        try:
            res = res + s[i]
            i += 1
        except IndexError:
            finished = True

    return res 

on = True 
while on: # infinite looping until 5 is input/main loop
    sel = main()

    if sel == 1: # top up 
        done = False
        while not done:
            a = input("Enter the amount (greater than 0) to load on your beep card: ")
            try:
                v = int(a)
                if v > 0:
                    # confirmation of the transaction
                    q = ""
                    while q not in ("Y", "N"):
                        q = input("Complete the transaction (Y/N)? ").upper() # covers all cases: y or Y, n or N
                        if q == "Y":
                            load += v # add up 
                            print(f"PHP {v:.2f} successfully loaded to your beep card.")
                            history += f"Top-up     +{v:.2f}     {load:.2f}\n"# append to history
                            history = trim(history, 5) # cutoff 5
                            done = True  # exit all loops
                        elif q == "N":
                            print("Cancelled Transaction")
                            done = True  # exit all loops
                        else:
                            print("Invalid input (must be Y/N)")
                else:
                    print("Amount must be greater than 0")
            except ValueError: # fail to get number
                print("Invalid amount (must be a positive number)")

    elif sel == 2: # print the stations
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
        
    elif sel == 3: # select the station and calculate the fare
        print(f"""
****************************
Load Balance: PHP {load:.2f}
Note: The origin and destination should not be the same.
""")
        stations = [
            "BACLARAN", "EDSA", "LIBERTAD", "GIL PUYAT", "VITO CRUZ", "QUIRINO", "PEDRO GIL", "UNITED NATIONS", "CENTRAL", "CARRIEDO"
        ]

        origin = int(input("Enter the station's number corresponding to your origin:"))
        destination = int(input("Enter the station's number corresponding to your destination:"))

        originStation = stations[origin-1] # this makes the first element become 1 (baclaran) and not 0
        destinationStation = stations[destination-1] # ditto

        count = abs(origin - destination) # get the absolute value of how many steps in between stations
        fare = 15.00
        finalfare = 15.00

        if count <= 3:
            finalfare = 15.00
        else:
            extrastations = count - 3
            extrafare = (extrastations // 3 + 1) * 5.00
            finalfare += extrafare

        vatsales = finalfare / 1.12
        vatamount = finalfare - vatsales

        print(f"""
------------------------------------------- 
Fare calculation
""")
        print(f"Journey Details: {originStation} -> {destinationStation}")
        print(f"Minimum fare: PHP 15.00")
        print(f"Additional fare: PHP {extrafare:.2f}")
        print(f"Total Fare: PHP {finalfare:.2f}")
        q = ""
        while q not in ("Y", "N"):
            q = input("Complete the transaction (Y/N)? ").upper() # covers all cases: y or Y, n or N
            if q == "Y":
                load -= finalfare # deduct amnt of trip
                print(f"PHP {v:.2f} was deducted for your trip from {originStation} to {destinationStation}")
                history += f"Trip     -{finalfare:.2f}     {load:.2f}\n" # append to history
                history = trim(history, 5) # cutoff when it exeeds 5 lines

                print(f"""
------------------------------------------- 
Receipt
-------------------------------------------
Journey Details: {originStation} -> {destinationStation}
Amount due: PHP {finalfare:.2f}
Vatable sales: PHP {vatsales:.2f}
VAT amount: PHP {vatamount:.2f}
------------------------------------------- 
""")
                
            elif q == "N":
                print("Cancelled Transaction")
            else:
                print("Invalid input (must be Y/N)")

            
    elif sel == 4: # most code is handled at 3 and 1
        print("""**************************** 
Last 5 Transactions
Transaction     Amount(PHP)     Ending Balance(PHP)""")
        print(history)

    elif sel == 5: # exit
        print("Thank you for using the LRT-1 System!")
        on = False 

    else: # invalid choice made
        print("Not in the given choices.")