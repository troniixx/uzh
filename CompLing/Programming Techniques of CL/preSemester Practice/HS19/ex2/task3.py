print("Enter first name: ")
first_name = input()
print("Enter last name: ")
last_name = input()
print("Enter your field of study: ")
field_of_study = input()

print("Hello, my name is " +first_name.capitalize() +" " +last_name.capitalize() +". I am studying " +field_of_study.capitalize() +".")
if len(first_name) == len(last_name):
    print(first_name.upper() + " " + last_name.capitalize() + " " + field_of_study.capitalize())
else:
    print(first_name.upper() + " " + last_name.upper() + " " + field_of_study.upper())