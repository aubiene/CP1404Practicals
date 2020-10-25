from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose, d)rive"


def main():
    total_cost = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose Taxi: "))
            current_taxi = taxis[taxi_choice]
            print("Bill to date ${:.2f}".format(taxis[taxi_choice].get_fare()))
        elif choice == "D":
            current_taxi.start_fare()
            distance_to_drive = float(input("Drive how far? "))
            current_taxi.drive(distance_to_drive)
            trip_cost = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
            total_cost += trip_cost

        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()

    print("Total trip cost: ${:.2f}".format(total_cost))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {} ".format(i, taxi))


main()
