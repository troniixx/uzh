
from gensim.models import KeyedVectors

# enter the full path to where the downloaded file is located (I was lazy and left it in downloads)
full_path = "C:/Users/Dominic-Asus/Downloads"

model = KeyedVectors.load_word2vec_format(f"{full_path}/cc.en.300.vec.gz", binary=False, limit=500000)

# down here, you work your magic (i.e., you follow the instructions in the assignment, amounting to
# 3 to 7 lines of code, depending on how advanced your tech wizardry is :))