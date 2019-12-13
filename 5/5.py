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
        self.output = None

    def get_program_str(self):
        return ','.join([str(x) for x in self.program])

    def reset(self, program_str):
        self.program = [int(x) for x in program_str.split(',')]
        self.program_counter = 0
        self.output = []

    def get_value(self, position):
        mode = self.param_mode(position)
        if mode == 0:  # position mode
            return self.program[self.program[self.program_counter + position]]
        elif mode == 1:  #immediate mode
            return self.program[self.program[self.program_counter + position]]
        else:
            import pdb;pdb.set_trace()

    def get_opcode(self):
        return self.program[self.program_counter] % 100

    def param_mode(self, position):
        return self.program[self.program_counter] // (10 * position) % 10

    def add(self):
        a = self.get_value(1)
        b = self.get_value(2)
        self.program[self.program[self.program_counter + 3]] = a + b
        self.program_counter += 4

    def mul(self):
        a = self.get_value(1)
        b = self.get_value(2)
        self.program[self.program[self.program_counter + 3]] = a * b
        self.program_counter += 4

    def store(self):
        pass

    def output(self):
        pass

    def run(self):

        while True:
            opcode = self.get_opcode()

            step = None

            if opcode == 99:  # stop
                return self.output
            elif opcode == 1:  # add
                step = self.add
            elif opcode == 2:  # mul
                step = self.mul
            elif opcode == 3:  # store
                step = self.store
            elif opcode == 4:  # output
                step = self.output
            else:
                import pdb;pdb.set_trace()

            step()


def main():

    computer= Computer()

    suite = TestSuite()
    suite.run(computer)




if __name__ == '__main__':
    main()