from test_data import TestSuite
#
# class Program(object):
#
#     def add(program, a, b, dest):
#         program[dest] = a + b
#         return program
#
#     def mul(program, a, b, dest):
#         program[dest] = a * b
#         return program
#
#     def get_value(program, pos, mode):
#         if mode == 0:
#             # import pdb;pdb.set_trace()
#             return program[program[pos]] if pos < len(program) and program[pos] < len(program) else None
#         elif mode == 1:
#             return program[pos]
#         else:
#             import pdb;pdb.set_trace()
#
#
#     def run(program, input_, pos=0):
#         print(program)
#         instruction = program[pos]
#
#         opcode = instruction % 100
#         mode1 = instruction // 100 % 10
#         mode2 = instruction // 1000 % 10
#         mode3 = instruction // 10000 % 10  # should always be 0
#
#         a = get_value(program, pos + 1, mode1)
#         b = get_value(program, pos + 2, mode2)
#         c = get_value(program, pos + 3, mode3)
#
#         print('opcode={} pos={} a={} b={} c={}'.format(opcode,pos,a,b,c))
#
#         # import pdb;pdb.set_trace()
#         if opcode in (1,2):
#
#             pos_c = program[pos + 3]
#
#             # print('opcode={}\na={} b={}\nwrite to pos_c={}'.format(opcode, a,b,pos_c))
#
#             if opcode == 1:
#                 program = add(program, a,b,pos_c)
#             else:
#
#                 program = mul(program, a,b,pos_c)
#             return run(program, input_, pos + 4)
#
#         elif opcode == 99:
#             # halt
#             return program
#
#         elif opcode in (3,4):
#             pos_c = program[pos + 1]
#
#             # print('opcode={}\na={}'.format(opcode,pos_c))
#             # import pdb;pdb.set_trace()
#
#             if opcode == 3:
#                 program[pos_c] = input_
#             else:
#                 # import pdb;pdb.set_trace()
#                 print('output={}'.format(a))
#             return run(program, input_, pos + 2)
#
#         elif opcode in (5,6):
#             if opcode == 5 and a != 0:
#                 return run(program, input_, b)
#             if opcode == 6 and a == 0:
#                 return run(program, input_, b)
#             else:
#                 return run(program, input_, pos + 3)
#
#         elif opcode in (7,8):
#             pos_c = program[pos + 1]
#
#             if opcode == 7 and a < b:
#                 # Might be a problem!
#                 program[pos_c] = 1
#             elif opcode == 8 and a == b:
#                 program[pos_c] = 1
#             else:
#                 program[pos_c] = 0
#             return run(program, input_, pos + 4)
#
#         else:
#             import pdb;pdb.set_trace()

class Computer(object):

    def __init__(self):
        self.program = None
        self.program_counter = None
        self.output_values = None
        self.input_values = None
        self.verbose = False
        self.debug = False

    def get_program_str(self):
        return ','.join([str(x) for x in self.program])

    def reset(self, program_str, input_values=[]):
        self.program = [int(x) for x in program_str.split(',')]
        self.program_counter = 0
        self.input_values = input_values
        self.output_values = []

    def get_value(self, position):
        mode = self.param_mode(position)
        if mode == 0:  # position mode
            return self.program[self.program[self.program_counter + position]]
        elif mode == 1:  # immediate mode
            return self.program[self.program_counter + position]
        else:
            import pdb;pdb.set_trace()

    def get_opcode(self):
        return self.program[self.program_counter] % 100

    def param_mode(self, position):
        return self.program[self.program_counter] // (10 ** (position + 1)) % 10

    def add(self):
        a = self.get_value(1)
        b = self.get_value(2)
        self.program[self.program[self.program_counter + 3]] = a + b  # never in immediate mode
        self.program_counter += 4

    def mul(self):
        a = self.get_value(1)
        b = self.get_value(2)
        self.program[self.program[self.program_counter + 3]] = a * b  # never in immediate mode
        self.program_counter += 4

    def store(self):
        value = self.input_values.pop(0)
        destination = self.program[self.program_counter + 1]  # never in immediate mode
        self.program[destination] = value
        self.program_counter += 2

    def output(self):
        value = self.get_value(1)
        self.output_values.append(value)
        if self.verbose:
            print(value)
        self.program_counter += 2

    def jump_if_non_zero(self):
        value = self.get_value(1)
        new_counter = self.get_value(2)
        if value != 0:
            self.program_counter = new_counter
        else:
            self.program_counter += 3

    def jump_if_zero(self):
        value = self.get_value(1)
        new_counter = self.get_value(2)
        if value == 0:
            self.program_counter = new_counter
        else:
            self.program_counter += 3

    def less_than(self):
        a = self.get_value(1)
        b = self.get_value(2)
        dest = self.program[self.program_counter + 3]

        result = 1 if a < b else 0
        self.program[dest] = result
        self.program_counter += 4

    def equals(self):
        a = self.get_value(1)
        b = self.get_value(2)
        dest = self.program[self.program_counter + 3]

        result = 1 if a == b else 0
        self.program[dest] = result
        self.program_counter += 4

    def run(self):
        while True:
            opcode = self.get_opcode()

            # import pdb;pdb.set_trace()

            if self.debug:
                print('program: {}'.format(self.program))
                print('program_counter: {}'.format(self.program_counter))
                print('opcode: {}\n'.format(opcode))
            step = None

            if opcode == 99:  # stop
                return self.output_values
            elif opcode == 1:  # add
                step = self.add
            elif opcode == 2:  # mul
                step = self.mul
            elif opcode == 3:  # store
                step = self.store
            elif opcode == 4:  # output
                step = self.output
            elif opcode == 5:
                step = self.jump_if_non_zero
            elif opcode == 6:
                step = self.jump_if_zero
            elif opcode == 7:
                step = self.less_than
            elif opcode == 8:
                step = self.equals

            else:
                import pdb;pdb.set_trace()

            step()


def main():

    computer= Computer()

    suite = TestSuite()
    suite.run(computer)




if __name__ == '__main__':
    main()