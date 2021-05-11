# TODO: FIX SOME BUGS WITH FLAGS

import random
import itertools
import fire
import os
import subprocess
from sys import stderr, stdout
from typing import List, Union, Any, Set, Optional


def _write(obj: Union[int, str]):
    stdout.write(str(obj))


def endl() -> None:
    _write("\n")


def animate(done: bool, filename: str) -> None:
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        stdout.write(f'\rCompiling {filename} {c}')
        stdout.flush()
    stdout.write('\rDone!     ')


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
    '''Helper class.'''
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
                 lower: bool, mixed: bool, binary: bool,
                 size: Optional[None]) -> List[str]:
        a: List[str] = []

        for _ in range(amount):
            n = self._randomInt(low, high)

            if size is not None:
                n = size

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

    def _listOfIntegers(self, amount: int, low: int, high: int,
                        size: Optional[int]) -> List[List[int]]:
        a: List[List[int]] = []
        for _ in range(amount):
            n = self._randomInt(low, high)
            if size is not None:
                n = size
            b: List[int] = []
            for _ in range(n):
                b.append(self._randomInt(low, high))
            a.append(b)

        return a

    def _listOfUniqueIntegers(self, amount: int, low: int, high: int,
                              size: Optional[int]) -> List[List[int]]:
        a: List[List[int]] = []
        for _ in range(amount):
            n = self._randomInt(low, high)

            if size is not None:
                n = size

            b: Set[int] = set()
            while len(b) < n:
                b.add(self._randomInt(low, high))
            a.append(list(b))

        return a

    def _listOfStrings(self, amount: int, low: int, high: int, upper: bool,
                       lower: bool, mixed: bool, binary: bool,
                       size: Optional[int]) -> List[List[str]]:
        a = []
        for _ in range(amount):
            n = self._randomInt(low, high)
            b = []
            for _ in range(n):
                length = self._randomInt(low, high)
                if size is not None:
                    length = size
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


class Tester:
    '''Main testing class.'''
    def generate(self,
                 low: int = 1,
                 high: int = 10,
                 size: Optional[int] = None,
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
            low: int, optional
                Lower bound of the numbers that are generated randomly.
            high: int, optional
                Upper bound of the numbers that are generated randomly.
            size: int, optional
                Size of the list/string generated.
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

        cases = 1
        if integers is True:
            if unique is True:
                lst = helper._uniqueIntegers(cases, low, high)
                printSin(cases, lst, printLen)
            else:
                lst = helper._integers(cases, low, high)
                printSin(cases, lst, printLen)
        elif strings is True:
            lst = helper._strings(cases, low, high, upper, lower, mixed,
                                  binary, size)
            printSin(cases, lst, printLen)
        elif loi is True:
            if unique is True:
                lst = helper._listOfUniqueIntegers(cases, low, high, size)
                printList(cases, lst, printLen)
            else:
                lst = helper._listOfIntegers(cases, low, high, size)
                printList(cases, lst, printLen)
        elif los is True:
            lst = helper._listOfStrings(cases, low, high, upper, lower, mixed,
                                        binary, size)
            printList(cases, lst, printLen)

    def test(self,
             low: int = 1,
             high: int = 10,
             size: Optional[int] = None,
             integers: bool = False,
             strings: bool = False,
             loi: bool = False,
             los: bool = False,
             upper: bool = False,
             lower: bool = False,
             mixed: bool = False,
             binary: bool = False,
             unique: bool = False,
             printLen: bool = True,
             brute: str = 'brute.cpp',
             soln: str = 'main.cpp',
             genOutput: str = 'stressInput') -> None:
        '''
        Randomly generate test cases and test them against your solution.

         Parameters
        -----------
            low: int, optional
                Lower bound of the numbers that are generated randomly.
            high: int, optional
                Upper bound of the numbers that are generated randomly.
            size: int, optional
                Size of the list/string generated.
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
            brute: str, optional
                Filename of the your correct brutefore solution.
            soln: str, optional
                Filename of the your solution.
            genOutput: str, optional
                Name of the file in which the output of the generator is written.
        '''

        args: List[str] = [
            f'--size={size}', f'--low={low}', f'--high={high}',
            f'--integers={integers}', f'--strings={strings}', f'--loi={loi}',
            f'--los={los}', f'--upper={upper}', f'--lower={lower}',
            f'--mixed={mixed}', f'--binary={binary}', f'--unique={unique}',
            f'--printLen={printLen}'
        ]

        if integers is False and strings is False and loi is False and los is False:
            stderr.write(f'''
ERROR: No flags/arguments passed.

For help, please use python3 {os.path.basename(__file__)} test --help command.
''')

        if strings is True or los is True:
            if upper is False and mixed is False and lower is False and binary is False:
                stderr.write(f'''
ERROR: No string arguments passed.

Please use any of the following flags while using string generation:
--uppper
--lower
--mixed
--binary

For more information use python3 {os.path.basename(__name__)} generate --help command.
''')

        cmd: List[str] = [
            'python3', f'{os.path.basename(__file__)}', 'generate'
        ]
        cmd.extend(args)

        if not os.path.exists(brute) or not os.path.isfile(brute):
            _write(f'Could not find {brute}')
            return

        if not os.path.exists(soln) or not os.path.isfile(soln):
            _write(f'Could not find {soln}')
            return

        _write(f'Compilng {brute}...')
        endl()
        subprocess.run(
            ['g++', '--std=c++17', brute, '-o',
             brute.split('.')[0]],
            cwd=os.getcwd())
        _write(f'Done compiling {brute}')
        endl()
        _write(f'Compilng {soln}...')
        endl()
        subprocess.run(['g++', '--std=c++17', soln, '-o',
                        soln.split('.')[0]],
                       cwd=os.getcwd())
        _write(f'Done compiling {soln}')
        endl()

        _write('Starting testing...')
        endl()
        _write('Use CTRL + C to stop the testing anytime.')
        endl()

        n: int = 1
        bruteOutput = 'bruteOutput'
        solnOutput = 'mainOutput'

        while True:
            try:
                f = open(genOutput, 'w')
                subprocess.run(args=cmd, cwd=os.getcwd(), stdout=f)
                f.close()

                bo = open(bruteOutput, 'w')
                go = open(genOutput, 'r')
                subprocess.run(['./brute'],
                               stdin=go,
                               stdout=bo,
                               cwd=os.getcwd())
                bo.close()

                so = open(solnOutput, 'w')
                subprocess.run(['./main'],
                               stdin=go,
                               stdout=so,
                               cwd=os.getcwd())
                so.close()
                go.close()

                bo = open(bruteOutput, 'r')
                bos = bo.readlines()
                so = open(solnOutput, 'r')
                sos = so.readlines()
                go = open(genOutput, 'r')
                gos = go.readlines()

                bo.close()
                so.close()
                go.close()

                areEq = bos == sos
                OKGREEN = '\033[92m'
                FAIL = '\033[91m'
                ENDC = '\033[0m'

                if areEq:
                    _write(f'CASE #{n}: ')
                    _write(f'{OKGREEN}PASSED{ENDC}')
                    endl()
                else:
                    _write(f'CASE #{n}: ')
                    _write(f'{FAIL}FAILED{ENDC}')
                    endl()
                    _write('INPUT: ')
                    endl()
                    endl()
                    _write(''.join(gos))
                    endl()
                    endl()
                    _write('EXPECTED OUTPUT: ')
                    endl()
                    endl()
                    _write(''.join(bos))
                    endl()
                    endl()
                    _write('SOLUTION OUTPUT: ')
                    endl()
                    endl()
                    _write(''.join(sos))
                    endl()
                    break
            except KeyboardInterrupt():
                exit(0)


if __name__ == "__main__":
    fire.Fire(Tester)
