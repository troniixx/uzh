def text():
    return ["Midway upon the journey of our life I foiund myself withing a FOREST dark"
    "for the straightforward pathway had been lost", "", 
    "Ah me How hard a thing it is to say what was this forest savage rough",
    "and stern which in the very thought renews the fear So bitter is it death is", 
    "little more but of the good to treat, which there I found speak will I of"]

def read_real(path):
    with open(path, "r" ) as file:
        return file.read().split("\n")


def count_keywords(path, keywords):
    

count_keywords("/Users/merterol/Desktop/MidtermsInfk/midterms hs19/text.txt", "hi")