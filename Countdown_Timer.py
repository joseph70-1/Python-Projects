import time

def set_countdown():
    seconds = int(input("Enter the number of seconds: "))
    print("The countdowun starts now.")
    temp = seconds

    while temp > 0:
        print(f'\r{temp}', end='', flush=True)
        time.sleep(1)
        temp -= 1
        # print(temp, end='')
        # print("Countdown ended.\n")

    print("\n ******WELCOME TO THE CONTDOWN******")

    while 1:
        selection = input("Want to set a countdown? (yes/no): ").lower()
        if "yes" in selection:
            set_countdown()
        elif "no" in selection:
            print("Exit.")
            break
        else:
            print("Invalid input.")
set_countdown()