import wikipedia

def main():
    program_started = 1
    while program_started == 1:
        choice = input("(P)age or (S)earch?" + "\n" + ">>> ")
        if choice.isspace() or choice == "":
            break
        elif choice.upper() not in ("P", "S"):
            print("Please enter a valid choice")
        elif choice.upper() == "P":
            try:
                page = input("What page would you like the summary for?" + "\n" + ">>> ")
                print(wikipedia.summary(page))
            except wikipedia.exceptions.DisambiguationError as e:
                print("Did you mean:")
                for i in range(len(e.options)):
                    print(e.options[i])
        else:
            search = input("What would you like to search for?" + "\n" + ">>> ")
            search_list = wikipedia.search(search)
            for i in range(len(search_list)):
                print("{}".format(search_list[i]))
            print(" ")
main()