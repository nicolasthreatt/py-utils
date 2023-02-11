# demonstrate template string functions

from string import Template


def main():
    # Usual string formatting with format()
    str1 = "My favorite NBA Player is {0} and is number {1}".format("Lebron James", "23")
    print(str1)
    
    # create a template with placeholders
    templ = Template("My favorite NBA Player is ${player} and is number ${number}")
    
    # use the substitute method with keyword arguments
    str2 = templ.substitute(player="Lebron James", number="23")
    print(str2)
    
    # use the substitute method with a dictionary
    data = { 
        "player": "Lebron James",
        "number": "23"
    }
    str3 = templ.substitute(data)    
    print(str3)

    
if __name__ == "__main__":
    main()
    