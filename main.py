# This is to certify that this project is my work based on my personal
# Make efforts to study and apply the concepts learned. I have constructed
# the functions, their respective algorithms, and the corresponding code by
# myself. The program was run, tested, and debugged by my efforts. I
# further certify that I have not copied in part or whole or otherwise
# plagiarized the work of other students and/or persons.
# Gerald James Z. Tan, DLSU ID# 12470732
# David Angelo D. Torreon, DLSU ID# 12466514 
# Josh Caleb B. Aggabao, DLSU ID# 12462098

# Description: A loadable train card system
# Programmed by: Gerald James Z. Tan, STEM11-P
# Last modified: July 18, 2025
# Acknowledgements: https://docs.python.org/
load = 0.0
history = ""

print(f"Welcome to the LRT-1 System!")
def main():
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

def amnt_newlines(s):
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

def trim(s, n): 
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
            end = True # SIX SEVENNN

    # go backwards to find the (n+1)th newline
    c = 0
    i = size - 1
    stop_index = 0
    done = False

    while not done and i >= 0:
        try:
            if s[i] == '\n':
                c += 1
                if c == n + 1:
                    stop_index = i + 1
                    done = True
            i -= 1
        except IndexError:
            done = True  # fallback, though shouldnt be needed since size is known

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

    return res # God save me for I am not your strongest soldier

on = True 
while on: # infinite looping until 5 is input/main loop
    sel = main()

    if sel == 1: # top up (why is this so complicated)
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
                            load += v
                            print(f"PHP {v:.2f} successfully loaded to your beep card.")
                            history += f"Top-up     {v:.2f}     {load:.2f}\n"
                            history = trim(history, 5)
                            done = True  # exit all loops
                        elif q == "N":
                            print("Cancelled Transaction")
                            done = True  # exit all loops
                        else:
                            print("Invalid input (must be Y/N)")
                else:
                    print("Amount must be greater than 0")
            except ValueError:
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

        originStation = stations[origin-1] 
        destinationStation = stations[destination-1]

        count = abs(origin - destination)

        print(f"""
------------------------------------------- 
Fare calculation
""")
        print(f"Journey Details: {originStation} -> {destinationStation}")

            
    elif sel == 4: # most code is handled at the top outside the loop
        print("""**************************** 
Last 5 Transactions
Transaction     Amount(PHP)     Ending Balance(PHP)""")
        print(history)

    elif sel == 5: # exit
        print("Thank you for using the LRT-1 System!")
        on = False 

    else: # invalid choice made
        print("⚠️ ACHTUNG! Not in the given choices.")
