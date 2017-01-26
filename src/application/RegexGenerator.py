

class RegexGenerator(object):

    def __init__(self):
        pass

    NUMBER_DICTIONARY = {
        0: "(0|cero)",
        1: "(1|uno)",
        2: "(2|dos)",
        3: "(3|tres)",
        4: "(4|cuatro)",
        5: "(5|cinco)",
        6: "(6|seis)",
        7: "(7|siete)",
        8: "(8|ocho)",
        9: "(9|nueve)"
    }

    NUMBER_SEPARATOR = "(.|\n|\t)*"

    def build_phones_regex(self, phone_list):

        if len(phone_list) == 1:
            regex = self.build_phone_regex(phone_list[0])
            #self.__print_regex(regex)
            return regex

        regex = "("
        first = True

        for phone in phone_list:
            if first:
                regex += "("
                regex += self.build_phone_regex(phone)
                regex += ")"
                first = False
            else:
                regex += "|("
                regex += self.build_phone_regex(phone)
                regex += ")"

        regex += ")"
        print("\nGlobal regex that matches all in one:")
        self.__print_regex(regex)
        print("END")
        return regex

    def build_phone_regex(self, phone):

        regex = ""

        splitted_phone = [int(char) for char in str(phone)]

        first = True
        for number in splitted_phone:
            if first:
                regex += self.NUMBER_DICTIONARY[number]
                first = False
            else:
                regex += self.NUMBER_SEPARATOR
                regex += self.NUMBER_DICTIONARY[number]

        self.__print_regex(regex)
        return regex

    def __print_regex(self, regex):
        print(repr(regex))
