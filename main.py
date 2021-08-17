from cat import Cat


def main():
    print('gello')
    # objects

    # access + return property
    # object_name.property_name

    # change property
    #object_name.property_name = new_value

    # add a new property
    #object_name.new_property = new_value

    # methods vs. functions
    """basically the same but there ARE some differences
        1.) methods are object specific and usually attached to an object
        2.) beause they're object specific can't be called on objects of other type
    """
    cat = Cat(a_name="bob", an_age=21, id_number=25)
    print(cat.name)
    print(cat.age)
    print(cat.id)
    cat.meow()
    print(cat.__str__())

    # return key value pairs of all properties of object
    print(vars(cat))

    # return all methods and properties
    print(dir(cat))


if __name__ == "__main__":
    main()
