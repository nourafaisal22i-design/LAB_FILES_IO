while True:
    answer = input("Do you want to add a new To-Do item? (y/n): ")

    if answer == "y":
        item = input("Enter your new To-Do item: ")

        with open("to_do.txt", "a") as file:
            file.write(item + "\n")

    elif answer == "n":
        show_list = input("Do you want to list your To-Do items? (y/n): ")

        if show_list == "y":
            try:
                with open("to_do.txt", "r") as file:
                    print("\nYour To-Do List:")

                    for item in file:
                        print(item.strip())

            except FileNotFoundError:
                print("Your To-Do list is empty.")

    elif answer == "exit":
        print("Thank you for using the To-Do program, come back again soon.")
        break

    else:
        print("Please enter y, n, or exit.")