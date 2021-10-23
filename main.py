#create main loop
def main():
    #create a list of the menu options
    menu = ["1. Add a new car", "2. Remove a car", "3. View all cars", "4. Quit"]
    #create a loop to display the menu
    while True:
        #display the menu
        for item in menu:
            print(item)
        #get the user's choice
        choice = input("Enter your choice: ")
        #check the choice
        if choice == "1":
            #add a new car
            add_car()
        elif choice == "2":
            #remove a car
            remove_car()
        elif choice == "3":
            #view all cars
            view_cars()
        elif choice == "4":
            #quit the program
            break
        else:
            print("Invalid choice")


#create a function to add a new car
def add_car():
    #get the car's information
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    year = input("Enter the year: ")
    #create a dictionary for the car
    car = {"make": make, "model": model, "year": year}
    #open the file
    file = open("cars.txt", "a")
    #write the car to the file
    file.write(str(car) + "\n")
    #close the file
    file.close()

def remove_car():
    #open the file
    file = open("cars.txt", "r")
    #read the file
    cars = file.readlines()
    #close the file
    file.close()
    #create a list of the cars
    car_list = []
    #create a loop to get the car's information
    for car in cars:
        car = eval(car)
        car_list.append(car)
    #get the car's information
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    year = input("Enter the year: ")
    #create a dictionary for the car
    car = {"make": make, "model": model, "year": year}
    #create a loop to find the car
    found = False
    for i in range(len(car_list)):
        if car_list[i] == car:
            found = True
            break
    #check if the car was found
    if found:
        #remove the car
        car_list.pop(i)
        #open the file
        file = open("cars.txt", "w")
        #write the car to the file
        for car in car_list:
            file.write(str(car) + "\n")
        #close the file
        file.close()
    else:
        print("Car not found")

def view_cars():
    #open the file
    file = open("cars.txt", "r")
    #read the file
    cars = file.readlines()
    #close the file
    file.close()
    #create a list of the cars
    car_list = []
    #create a loop to get the car's information
    for car in cars:
        car = eval(car)
        car_list.append(car)
    #create a loop to display the cars
    for car in car_list:
        print(car)

main()