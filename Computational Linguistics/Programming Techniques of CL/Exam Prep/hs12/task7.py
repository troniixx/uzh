#a)
# Schreibe die Anweisungen, welche nötig sind, um den Inhalt dieser Datei in einer Liste namens es_tts abzuspeichern, welche aus Paaren der Form (Wort, Wortart) besteht.
def tuple_creator(path):
    es_tts = []
    with open(path, "r", encoding = "utf-8") as p:
        for line in p:
            line = line.strip()
            if line:
                word, tag = line.split(" ")
                es_tts.append((word, tag))
                
    return es_tts

#b)
# Erzeuge ein Dictionary/Hash pos_stats, das zählt, wie oft jede Wortart vorkommt.
def pos_stats(path):
    stats = {}
    with open(path, "r", encoding = "utf-8") as p:
        for line in p:
            line = line.strip()
            if line:
                word, tag = line.split(" ")
                if tag in stats:
                    stats[tag] += 1
                else:
                    stats[tag] = 1
                    
    return stats

#c)
# Gebe die Anzahl unterschiedlicher Wortarten in diesem Korpus aus mit print.
def unique(path):
    es_tts = []
    with open(path, "r", encoding = "utf-8") as p:
        for line in p:
            line = line.strip()
            if line:
                word, tag = line.split(" ")
                es_tts.append(tag)
                
    return len(set(es_tts))

#d)
# Erzeuge ein Dictionary, das als Wortartenlexikon dient. D.h. es enthält als Schlüssel eine Wortform und als dazugehöriger Wert die Liste aller möglichen Wortarten-Tags.
def lexicon(path):
    lex = {}
    with open(path, "r", encoding = "utf-8") as p:
        for line in p:
            line = line.strip()
            if line:
                word, tag = line.split(" ")
                if word in lex:
                    continue
                else:
                    lex[word] = tag
                    
    return lex

if __name__ == '__main__':
    PATH = "Computational Linguistics/Programming Techniques of CL/Exam Prep/hs12/es.tts"
    print("a)")
    print(tuple_creator(PATH))
    print("b)")
    print(pos_stats(PATH))
    print("c)", unique(PATH))
    print("d)")
    print(lexicon(PATH))