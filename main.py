#this will be fun

fare

def main():
    print(f"Welcome to the LRT-1 System!\n\n****************************\nLoad Balance: PHP {fare}\nChoices\n1-Load Beep Card\n2-Display All Stations\n3-Trip and Fare\n4-Transaction History\n5-Exit")
    call = input("Choose from the options: ")

    return call # This returns (outputs) the selected choice

if main() == 5:
    exit()