import datetime
__author__ = "Mert Erol"

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
begin_time = datetime.datetime.now()

def preprocess(records):
    titanic1 = []
    titanic_final = []
    alive_values = ["Yes", "yes", "Survived", "survived", "True", "true", "Survived=alive", "Alive", "alive", "T", "t"]
    dead_values = ["No", "no", "Dead", "dead", "False", "false", "F", "f", "Survived=dead"]
    male_values = ["Male", "male", "M", "m"]
    female_values = ["Female", "female", "F", "f"]
    undefined_values = ["", "undefined", "unknown"]
    
    #titanic1.append(list(records[0]))

    for i in records[1:]:
        i = list(i)

        if i[0] == "":
            continue
        elif i[0] in alive_values:
            i[0] = True
        elif i[0] in dead_values:
            i[0] = False
        else:
            continue
        
        if i[1] == "":
            continue
        elif int(i[1]) in range(1,4):
            i[1] = int(i[1])
        else:
            continue

        #insert expression for name here
        if i[2] == "":  
            continue

        if i[3] == "":
            continue
        elif i[3] in male_values:
            i[3] = "male"
        elif i[3] in female_values:
            i[3] = "female"
        elif i[3] in undefined_values:
            continue
        
        if i[4] == "":
            continue
        elif i[4] in undefined_values:
            continue
        elif float(i[4]) in range(1, 101):
            i[4] = float(i[4])
        else:
            continue
        
        #this is the fare expression
        if i[5] in undefined_values:
            i[5] = 25.0
        elif float(i[5]) < 0:
            i[5] = float(i[5]) * -1
        elif float(i[5]) > 0:
            i[5] = float(i[5])
        else:
            i[5] = 25.0

        titanic1.append(i)
    
    for item in titanic1:
        item = tuple(item)
        titanic_final.append(item)

    y = (tuple(records[0]), titanic_final)

    return y

if __name__ == '__main__':

    titanic = [
                ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
                ('no', '3', 'Braund Mr. Owen Harris', 'male', '22', '7.25'),
                ('Dead', '3', 'Braund Ms. Maria', 'Female', '21', ''),
                ('Yes', '1', 'Cumings Mrs. John Bradley (Florence Briggs Thayer)', 'F', '38', '71.28'),
                ('', '3', 'Vander Planke Miss. Augusta', 'female', '', ''),
                ('Dead', '4', 'Lennon Mr. Denis', 'male', '13', '15.5')]
    
    print(preprocess(titanic))
    
    print(datetime.datetime.now() - begin_time)

