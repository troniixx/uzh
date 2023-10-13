

print("Welcome to the Mini Book Rating System!")

continue_rating = True

while continue_rating:

    book_title = input("\nEnter the title of the book: ")
    rating = float(input(f"How would you rate the book '{book_title}' out of 10? "))


    if rating < 0:
        rating = 0
        print("Rating cannot be below 0. It has been set to 0.")
    elif rating > 10:
        rating = 10
        print("Rating cannot be above 10. It has been set to 10.")


    stars_to_display = int(rating)
    print("Your rating: ", end="")
    while stars_to_display > 0:
        print("★", end="")
        stars_to_display -= 1
    print()


    if rating >= 8:
        print(f"You seem to have enjoyed '{book_title}' a lot!")
    elif rating >= 5:
        print(f"'{book_title}' seems to be an average read for you.")
    else:
        print(f"You didn't seem to like '{book_title}' much.")


    another_book = input("Would you like to rate another book? (yes/no): ").lower()
    if another_book != 'yes':
        continue_rating = False


