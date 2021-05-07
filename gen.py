# TODO: FIX SOME BUGS WITH FLAGS

import random
import fire
from sys import stderr, stdout
from typing import List, Union, Any, Set


def _write(obj: Union[int, str]):
    stdout.write(str(obj))


def endl() -> None:
    _write("\n")


def printSin(cases: int, lst: Union[List[int], List[str]],
             printLen: bool) -> None:
    _write(cases)
    endl()
    flag = False

    if type(lst[0]) is str and printLen is True:
        flag = True

    for i in range(len(lst) - 1):
        if flag is True:
            _write(len(lst[i]))
            endl()
        _write(lst[i])
        endl()

    if flag is True:
        _write(len(lst[len(lst) - 1]))
        endl()
    _write(lst[len(lst) - 1])


def printList(cases: int, lst: List[Any], printLen: bool) -> None:
    _write(cases)
    endl()

    for i in range(len(lst)):
        arr = lst[i]
        if printLen is True:
            _write(len(arr))
            endl()

        for j in range(len(arr) - 1):
            _write(arr[j])
            _write(" ")

        _write(arr[len(arr) - 1])
        endl()


class Helper:
    '''Helper class to generate.'''
    def _randomInt(self, low: int, high: int) -> int:
        return random.randint(low, high)

    def _integers(self, amount: int, low: int, high: int) -> List[int]:
        a: List[int] = []

        for _ in range(amount):
            a.append(self._randomInt(low, high))

        return a

    def _uniqueIntegers(self, amount: int, low: int, high: int) -> List[int]:
        se: Set[int] = set()
        a: List[int] = []

        while len(se) < amount:
            se.add(self._randomInt(low, high))

        return list(se)

    def _strings(self, amount: int, low: int, high: int, upper: bool,
                 lower: bool, mixed: bool, binary: bool) -> List[str]:
        a: List[str] = []

        for _ in range(amount):
            n = self._randomInt(low, high)
            s = []
            for _ in range(n):
                char = ""
                if upper is True:
                    char = chr(self._randomInt(65, 90))
                elif lower is True:
                    char = chr(self._randomInt(97, 122))
                elif mixed is True:
                    temp = [
                        chr(self._randomInt(65, 90)),
                        chr(self._randomInt(97, 122))
                    ]
                    char = temp[self._randomInt(0, 1)]
                elif binary is True:
                    char = chr(self._randomInt(48, 49))
                s.append(char)
            a.append("".join(s))

        return a

    def _listOfIntegers(self, amount: int, low: int,
                        high: int) -> List[List[int]]:
        a: List[List[int]] = []
        for _ in range(amount):
            n: int = self._randomInt(low, high)
            b: List[int] = []
            for _ in range(n):
                b.append(self._randomInt(low, high))
            a.append(b)

        return a

    def _listOfUniqueIntegers(self, amount: int, low: int,
                              high: int) -> List[List[int]]:
        a: List[List[int]] = []
        for _ in range(amount):
            n: int = self._randomInt(low, high)
            b: Set[int] = set()
            for _ in range(n):
                b.add(self._randomInt(low, high))
            a.append(list(b))

        return a

    def _listOfStrings(self, amount: int, low: int, high: int, upper: bool,
                       lower: bool, mixed: bool,
                       binary: bool) -> List[List[str]]:
        a = []
        for _ in range(amount):
            n = self._randomInt(low, high)
            b = []
            for _ in range(n):
                length = self._randomInt(low, high)
                s = []
                for _ in range(length):
                    char = ""
                    if upper is True:
                        char = chr(self._randomInt(65, 90))
                    elif lower is True:
                        char = chr(self._randomInt(97, 122))
                    elif mixed is True:
                        temp = [
                            chr(self._randomInt(65, 90)),
                            chr(self._randomInt(97, 122))
                        ]
                        char = temp[self._randomInt(0, 1)]
                    elif binary is True:
                        char = chr(self._randomInt(48, 49))
                    s.append(char)

                b.append("".join(s))

            a.append(b)

        return a


helper = Helper()


class Generator:
    '''Class that generates random test cases.'''
    def __init__(self, low: int = 1, high: int = 10):
        '''
         Parameters
        -----------
            low: int, optional
                Lowest limit of the numbers that are generated randomly.
            high: int, optional
                Lowest limit of the numbers that are generated randomly.
        '''
        self.low = low
        self.high = high

    def generate(self,
                 cases: int = 10,
                 integers: bool = False,
                 strings: bool = False,
                 loi: bool = False,
                 los: bool = False,
                 upper: bool = False,
                 lower: bool = False,
                 mixed: bool = False,
                 binary: bool = False,
                 unique: bool = False,
                 printLen: bool = True) -> None:
        '''
         Outputs randomly generated testcases depending upon the flag passed.

         Parameters
        -----------
            cases: int, optional
                Number of testcases to be generated.
            integers: bool, optional
                Outputs randomly generated integers when this flag is passed.
            strings: bool, optional
                Outputs randomly generated strings when this flag is passed.
            loi: bool, optional
                Outputs randomly generated list of integers when this flag is passed.
            los: bool, optional
                Outputs randomly generated list of strings when this flag is passed.
            upper: bool, optional
                It is used with strings generation when this flag is passed the output will be all uppercase.
            lower: bool, optional
                It is used with strings generation when this flag is passed the output will be all lowercase.
            mixed: bool, optional
                It is used with strings generation when this flag is passed the output will be all mixed with both uppercase and lowercase.
            binary: bool, optional
                It is used with strings generation when this flag is passed the output will be randomly generated binary strings.
            unique: bool, optional
                It is used with integers generation to output unique integers without repetition.
            printLen: bool, optional
                Outputs the length of the object along with the testcases, when this flag is passed.
        '''
        if integers is True:
            if unique is True:
                lst = helper._uniqueIntegers(cases, self.low, self.high)
                printSin(cases, lst, printLen)
            else:
                lst = helper._integers(cases, self.low, self.high)
                printSin(cases, lst, printLen)
        elif strings is True:
            lst = helper._strings(cases, self.low, self.high, upper, lower,
                                  mixed, binary)
            printSin(cases, lst, printLen)
        elif loi is True:
            if unique is True:
                lst = helper._listOfUniqueIntegers(cases, self.low, self.high)
                printList(cases, lst, printLen)
            else:
                lst = helper._listOfIntegers(cases, self.low, self.high)
                printList(cases, lst, printLen)
        elif los is True:
            lst = helper._listOfStrings(cases, self.low, self.high, upper,
                                        lower, mixed, binary)
            printList(cases, lst, printLen)


if __name__ == "__main__":
    fire.Fire(Generator)
