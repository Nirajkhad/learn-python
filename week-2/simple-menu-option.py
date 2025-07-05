while True:
    print("Select an option:");
    print("1. Say Namaste");
    print("2. Say Hello");
    print("3. Exit");

    choice = input("Enter your choice: ");
    
    match(choice):
        case "1":
            print("Namaste");
        case "2":
            print("Hello");
        case "3":
            break;
        case _:
            print("Invalid choice");
            

