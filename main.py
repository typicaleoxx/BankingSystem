import register
import login


def main():
    print("Namaste, welcome to THE SNEHA BANK.")
    user = input("Are you an existing user? (y/n) ").strip().lower()
    try:
        if user == "y":
            login.login()
        elif user == "n":
            register.register()
    except:
        print("Login/registration error. Please try again!")
        try_again = input("Do you want to try again? (y/n)").strip().lower()
        if try_again == "y":
            main()
        else:
            print("Okay, have a great day sir/ma'am.")


main()
