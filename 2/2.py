def run(program, pos=0):
    opcode = program[pos]
    i1 = program[pos + 1]
    i2 = program[pos + 2]
    dest = program[pos + 3]

    if opcode == 1:
        # add
        program[dest] = program[i1] + program[i2]
        return run(program, pos + 4)

    elif opcode == 2:
        # mul
        program[dest] = program[i1] * program[i2]
        return run(program, pos + 4)

    elif opcode == 99:
        # halt
        return program
    else:
        return None

def main():

    with open('./input.txt') as f:
        program = [int(x) for x in f.readline().split(',')]

        desired_output = 19690720

        for i1 in range (0,100):
            for i2 in range(0,100):


                test_program = program[:]
                test_program[1] = i1
                test_program[2] = i2
                program_result = run(test_program)
                result = program_result[0] if program_result else -1

                print('i1={} i2={} result={}'.format(i1,i2, result))

                if (result == desired_output):
                    print('RESULT={}'.format(i1 * 100 + i2))
                    return
        # import pdb;pdb.set_trace()

        print(result)

if __name__ == '__main__':
    main()