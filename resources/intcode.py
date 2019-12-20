from collections import defaultdict
from typing import List


class IntCodeProgram:
    def __init__(self, init_values: List[int]):
        self.pointer = 0
        self.codes = defaultdict(int, [(x, init_values[x]) for x in range(len(init_values))])
        self.running = False

    def arg(self, i: int) -> int:
        return self.codes[self.codes[self.pointer + i]]

    def addr(self, i: int) -> int:
        return self.codes[self.pointer + i]

    def execute(self):
        self.running = True

        while self.running:
            instr_code = self.codes[self.pointer]

            if instr_code == 1:
                self.codes[self.addr(3)] = self.arg(1) + self.arg(2)
                self.pointer += 4
            elif instr_code == 2:
                self.codes[self.addr(3)] = self.arg(1) * self.arg(2)
                self.pointer += 4
            elif instr_code == 99:
                self.running = False

        return self
