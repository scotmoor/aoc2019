from abc import abstractmethod


class OpCode:
    def __init__(self, noun, verb):
        self.noun = noun
        self.verb = verb

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def instruction_size(self):
        pass

    def __repr__(self):
        return f"Code: {self.code} Noun: {self.noun} Verb: {self.verb} Result: {self.result}"


class AddOp(OpCode):
    def __init__(self):
        super().__init__(1, 2)
        self.size = 4
        self.opcode = 1

    def execute(self):
        return self.noun + self.verb




class MultiplyOp(OpCode):
    def __init__(self, noun, verb):
        super().__init__(noun, verb)
        self.size = 4
        self.code = 2

        self.result = self.noun * self.verb

class OpCodeFactory:
    OPCODE_ADD = 1
    OPCODE_MULTIPLY = 2

    @classmethod
    def getOp(cls, code, noun, verb):
        if code == cls.OPCODE_ADD:
            return AddOp(noun=noun, verb=verb)
        elif code == cls.OPCODE_MULTIPLY:
            return MultiplyOp(noun=noun, verb=verb)
        else:
            raise NameError(f"Invalid OpCode: {code}")
