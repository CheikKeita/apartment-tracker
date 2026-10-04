import json

print("Welcome to Apartment Tracker")

# Load saved apartments
try:
    with open("apartments.json", "r") as file:
        apartments = json.load(file)
except FileNotFoundError:
    apartments = []

# Keep menu running
while True:
    # Display menu
    print("1. Add apartment")
    print("2. View apartments")
    print("3. Search apartments")
    print("4. Filter apartments")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        # Get apartment information
        name = input("Apartment name: ")
        area = input("Area: ")

        # Make sure rent is a number
        try:
            rent = float(input("Monthly rent: $"))
        except ValueError:
            print("Invalid rent. Please enter a number.")
            continue
        bedrooms = input("Bedrooms: ")

        # Check if apartment was already added
        already_exists = False

        for apartment in apartments:
            if (apartment["name"].lower() == name.lower()
                    and apartment["area"].lower() == area.lower()
                    and apartment["rent"] == rent
                    and apartment["bedrooms"] == bedrooms):
                already_exists = True

        if already_exists:
            print("You've already added this apartment.")
        else:
            status = input("Status: ")
            notes = input("Notes: ")

            # Store apartment information together
            apartment = {
                "name": name,
                "area": area,
                "rent": rent,
                "bedrooms": bedrooms,
                "status": status,
                "notes": notes
            }

            # Add apartment to the list
            apartments.append(apartment)

            # Save apartments to the file
            with open("apartments.json", "w") as file:
                json.dump(apartments, file, indent=4)

    elif choice == "2":
        # Check if there are any apartments
        if len(apartments) == 0:
            print("No apartments have been added yet.")
        else:
            # Show all apartments
            for apartment in apartments:
                print("Name:", apartment["name"])
                print("Area:", apartment["area"])
                print("Rent: $", apartment["rent"], sep="")
                print("Bedrooms:", apartment["bedrooms"])
                print("Status:", apartment["status"])
                print("Notes:", apartment["notes"])
                print()

    elif choice == "3":
        # Search for an apartment
        search_name = input("Enter apartment name: ")

        # Track if apartment is found
        found = False
        # Check each stored apartment
        for apartment in apartments:
            # Show apartment if names match
            if apartment["name"].lower() == search_name.lower():
                found = True
                print("Apartment found!")
                print("Name:", apartment["name"])
                print("Area:", apartment["area"])
                print("Rent: $", apartment["rent"], sep="")
                print("Bedrooms:", apartment["bedrooms"])
                print("Status:", apartment["status"])
                print("Notes:", apartment["notes"])
                print()

        # Show message if no match was found
        if found == False:
            print("Apartment not found.")


    elif choice == "4":
        # Display filter options
        print("1. Maximum rent")
        print("2. Area")
        print("3. Bedrooms")

        # Get the user's filter choice
        filter_choice = input("Choose a filter: ")

        # Filter apartments by maximum rent
        if filter_choice == "1":

            # Make sure maximum rent is a number
            try:
                max_rent = float(input("Enter maximum rent: $"))
            except ValueError:
                print("Invalid rent. Please enter a number.")
                continue

            # Track if any apartments match the filter
            found = False

            # Check each apartment's rent
            for apartment in apartments:
                if apartment["rent"] <= max_rent:
                    found = True

                    # Show apartment if rent is within budget
                    print("Name:", apartment["name"])
                    print("Area:", apartment["area"])
                    print("Rent: $", apartment["rent"], sep="")
                    print("Bedrooms:", apartment["bedrooms"])
                    print("Status:", apartment["status"])
                    print("Notes:", apartment["notes"])
                    print()

            # Show message if no apartments match the budget
            if found == False:
                print("No apartments found within that budget.")

        # Filter apartments by area
        elif filter_choice == "2":
            # Get the area to search for
            area_search = input("Enter area: ")

            # Track if any apartments match the area
            found = False

            # Check each apartment's area
            for apartment in apartments:
                if apartment["area"].lower() == area_search.lower():
                    found = True

                    # Show apartment if area matches
                    print("Name:", apartment["name"])
                    print("Area:", apartment["area"])
                    print("Rent: $", apartment["rent"], sep="")
                    print("Bedrooms:", apartment["bedrooms"])
                    print("Status:", apartment["status"])
                    print("Notes:", apartment["notes"])
                    print()

            # Show message if no apartments match the area
            if found == False:
                print("No apartments found in that area.")

        # Filter apartments by bedrooms
        elif filter_choice == "3":
            # Get the number of bedrooms to search for
            bedroom_search = input("Enter number of bedrooms: ")

            # Track if any apartment match the bedroom amount
            found = False

            # Check each apartment's bedrooms
            for apartment in apartments:
                if apartment["bedrooms"] == bedroom_search:
                    found = True

                    # Show apartment if bedrooms match
                    print("Name:", apartment["name"])
                    print("Area:", apartment["area"])
                    print("Rent: $", apartment["rent"], sep="")
                    print("Bedrooms:", apartment["bedrooms"])
                    print("Status:", apartment["status"])
                    print("Notes:", apartment["notes"])
                    print()

            # Show message if no apartments match the bedroom amount
            if found == False:
                print("No apartments found with that number of bedrooms.")

        # Handle invalid filter choices
        else:
            print("Invalid filter. Please choose 1-3.")



    # Exit the program
    elif choice == "5":
        break

    # Handle invalid menu choices
    else:
        print("Invalid option. Please choose 1-5.")