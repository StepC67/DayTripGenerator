from errno import ENETRESET
import random


print ("Hello World")

print ("Hello World")

# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment selections in their own separate lists.
# (5 points): As a user, I want a destination to be randomly selected for my day trip.
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
# (10 points): As a user, I want to display my completed trip in the console.
# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

destinations_list = ["Dominican Republic", "Bahamas", "Turks and Caicos", "Greece"]
restaurants_list = ["Don Pepe", "El Conuco", "Cafe Matisse", "Oh Andros", "Coco Bistro", "Mango Reef", "Efcharis", "Maiandros"]
mode_of_transportation_list = ["airplane", "cruise ship", "car", "train"]
entertainment_list = ["Coco Bunga Punta Cana", "Ocean World", "Sandy Toes Adventure", "Sip N Splash," "Danny Buoys", "Casablanco Casino", "Greek National Opera", "Onassis Cultural Centre"]

def select_option(option_list, option_description):
    not_satisfied = True
    while not_satisfied == True:
        # Random select an option
        chosen_index = random.randrange(0, len(option_list)- 1)
        selected_option = option_list[chosen_index]

        # Show/display
        print(f'Your chosen {option_description} is {selected_option}')
        user_input = input("Is this okay? (y/n) ").lower()
        # Check for acceptance
        if user_input == 'y':
            not_satisfied = False
            return selected_option



chosen_dest = select_option(destinations_list, "destination")
chosen_rest = select_option(restaurants_list, "restaurant")
chosen_trans = select_option(mode_of_transportation_list, "transportation")
chosen_ent = select_option(entertainment_list, "entertainment")

# Display finalized trip







print("I am happy with my selections, my DayTripPlanner is now complete.")   

print("My trip is now complete.")








