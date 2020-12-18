from prac_6.guitar import Guitar

guitar_list = []
program_started = 1
print("My guitars!")

while program_started == 1:

    guitar_name = input("Name: ")
    if guitar_name == "" or guitar_name.isspace():
        program_started = 2
    else:
        guitar_year = input("Year: ")
        if guitar_year.isdigit() == False:
            print("That's not a valid year!")
            guitar_year = input("Year: ")
        guitar_cost = input("Cost: ")
        guitar_cost.strip("$")
        clean_guitar_cost = guitar_cost.replace(".","")
        if clean_guitar_cost.isdigit() == False:
            print("That's not a valid cost!")
            guitar_cost = input("Cost: ")
        guitar_list.append(Guitar(guitar_name, guitar_year, float(guitar_cost)))




guitar_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitar_list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("\n" +"These are my guitars:")
for i, guitar in enumerate(guitar_list, 1):
    if Guitar.is_vintage(guitar):
        print("Guitar {}: {:20} ({}), worth ${:<10,.2f} (vintage)".format(i, guitar.name, guitar.year, guitar.cost))
    else:
        print("Guitar {}: {:20} ({}), worth ${:<10,.2f}".format(i, guitar.name, guitar.year, guitar.cost))
