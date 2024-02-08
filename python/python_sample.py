def books():
    books = input("Enter the book name :")
    print("book name is :" + books)
    if books==("ponniyin selvan"):
        character = input("enter the characters: ").split(",")
        print("The characters are :", character)
        for i in character:
            print(i)
    else:
        print("book name is invalid")
books()