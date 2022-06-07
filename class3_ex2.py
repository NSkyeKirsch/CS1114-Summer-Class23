# learning about scope of a variable

def function_1(my_name):
    print(my_name, id(my_name))  # second print
    my_name = "Roberto"  # changes my_name to "Roberto" within the function
    print(my_name, id(my_name))  # third print, after my_name changed to "Roberto"


def main():
    my_name = "Slim Shady"
    print(my_name, id(my_name))  # first print
    vehicle = "Honda Passport"
    function_1(my_name)

    print(my_name, id(my_name))  # fourth print. when it prints, my_name is not changed to "Roberto" because scope


if __name__ == "__main__":
    main()
