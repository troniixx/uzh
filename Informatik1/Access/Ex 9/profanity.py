class ProfanityFilter:

    def __init__(self, keywords, template):
        self.__keywords = keywords
        self.__template = template

    def __clean(self, length):
        import math as math
        output = ""
        temp_resultado = length % len(self.__template)
        temp_largo = math.floor(length/len(self.__template))
        output = self.__template*temp_largo+self.__template[0:temp_resultado]
        return output

    def __find_badwords(self, msg):
        badwords = []
        for badword in self.__keywords:
            if badword.lower() in msg.lower():
                found = [i for i in range(len(msg.lower())) if msg.lower().startswith(badword.lower(), i)]
                for i_start in found:
                    i_end = i_start + len(badword)
                    badword_sensitive = msg[i_start:i_end]
                    badwords.append(badword_sensitive)

        badwords = sorted(badwords, key=len)
        badwords.reverse()

        return badwords

    def filter(self, msg):
        found_badwords = self.__find_badwords(msg)

        for w in found_badwords:
            r = self.__clean(len(w))
            msg = msg.replace(w, r)

        return msg


if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shit", "mashitard", "mastard"], "?#$")
    #offensive_msg = "ABC shit Shit mashitard jklmno"
    offensive_msg = "xxduckxx"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno
