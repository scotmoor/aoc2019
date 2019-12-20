from resources.intcode import IntCodeProgram


def run(code: list, noun: int, verb: int) -> int:
    program = IntCodeProgram(code)
    program.codes[1] = noun
    program.codes[2] = verb
    program.execute()

    return program.codes[0]


def get_result(code: list, target: int) -> int:
    for i in range(100):
        for j in range(100):
            if target == run(code, i, j):
                return i * 100 + j


def get_input_codes() -> list:
    path = './input'
    with open(path) as f:
        codes = f.read()

    return list(map(lambda x: int(x), codes.split(',')))


if __name__ == '__main__':
    inputCodes = get_input_codes()

    print(f"Day 2 step 1: {run(inputCodes,12,2)}")
    print(f"Day 2 step 2: {get_result(inputCodes, 19690720)}")
