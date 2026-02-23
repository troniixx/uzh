#Creates a mini book rating system where one can enter the name of the book, the rating out of 10 and the
#program will display the rating in stars and a comment on the rating.
#Comments by: Mert Erol, Ishana Rana

print("Welcome to the Mini Book Rating System!")

continue_rating = True

#start the main loop
while continue_rating:
    
    #input the book title and rating
    book_title = input("\nEnter the title of the book: ")
    rating = float(input(f"How would you rate the book '{book_title}' out of 10? "))

    #check if the integer used for rating is valid
    if rating < 0:
        rating = 0
        print("Rating cannot be below 0. It has been set to 0.")
    elif rating > 10:
        rating = 10
        print("Rating cannot be above 10. It has been set to 10.")

    #display the rating in stars
    stars_to_display = int(rating)
    print("Your rating: ", end="")
    while stars_to_display > 0:
        print("★", end="")
        stars_to_display -= 1
    print()

    #display a comment on the rating
    if rating >= 8:
        print(f"You seem to have enjoyed '{book_title}' a lot!")
    elif rating >= 5:
        print(f"'{book_title}' seems to be an average read for you.")
    else:
        print(f"You didn't seem to like '{book_title}' much.")

    #ask if the user wants to rate another book, if yes, continue the loop, if not, end the loop.
    another_book = input("Would you like to rate another book? (yes/no): ").lower()
    if another_book != 'yes':
        continue_rating = False


