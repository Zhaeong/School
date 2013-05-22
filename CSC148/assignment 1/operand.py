class InvalidNumeralStringError(Exception):
    '''Raise exception if Operand string does not conform to specifications.'''
    pass


class Operand:
    '''A string in the form of DDDDDDDDDbXX where every D represents a
    digit, and XX represents the base of a positive integer up to and
    including base 16. Digits above 9 wrepresented by capitalized
    letters A through F.'''

    def __init__(self, string):
        '''(Operand) -> None
        A new Operand object.'''

        if "b" not in string:
            try:
                self._number = int(string)
            except ValueError:
                raise InvalidNumeralStringError()
            self._base = "default"
            # for base 10
        elif string[len(string) - 2] == "b":
            try:
                self._base = int(string[len(string) - 1])
            except ValueError:
                raise InvalidNumeralStringError()
            self._number = string[:len(string) - 2]
        elif string[len(string) - 3] == "b":
            try:
                self._base = int(string[len(string) - 2:])
            except ValueError:
                raise InvalidNumeralStringError()
            self._number = string[:len(string) - 3]
        else:
            raise InvalidNumeralStringError()
        # if 'b' invalidly placed elsewhere in string

        # check to make sure no non-digit is present in digit string
        list_of_values = ['0', '1', '2', '3', '4', '5', '6', '7', '8',
                          '9', "A", "B", "C", "D", "E", "F"]

        if self._base != "default":
            for digit in self._number:
                if digit not in list_of_values[:self._base]:
                    raise InvalidNumeralStringError()

        # check to make sure base is between 2 and 16 inclusive
            if self._base < 2 or self._base > 16:
                raise InvalidNumeralStringError()

    def value(self):
        '''(Operand) -> int
        Return integer value of Operand instance.'''

        self._accu = 0
        self._flist = []
        hexdict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                   '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13,
                   'E': 14, 'F': 15}

        if self._base == "default":
            return self._number
        else:
            for num in self._number:
                self._flist.append(hexdict[num])

            self._power = 0
            self._flist = self._flist[::-1]

            for digit in self._flist:
                self._accu += digit * self._base ** self._power
                self._power += 1

            return self._accu
