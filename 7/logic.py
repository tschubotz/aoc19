import itertools

class Computer(object):

    def __init__(self):
        self.program = None
        self.program_counter = None
        self.output_values = None
        self.input_values = None
        self.verbose = False
        self.debug = False
        self.pause_on_output = False

    def get_program_str(self):
        return ','.join([str(x) for x in self.program])

    def reset(self, program_str, input_values=[], pause_on_output=False):
        self.program = [int(x) for x in program_str.split(',')]
        self.program_counter = 0
        self.input_values = input_values
        self.output_values = []
        self.pause_on_output = pause_on_output

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
            if self.pause_on_output and opcode == 4:
                return self.output_values


class Amplifier(object):
    def __init__(self):
        self.computer = Computer()

    def reset(self, program, phase_setting):
        self.computer.reset(program, input_values=[phase_setting])

    def run(self, input_signal=None):
        if input_signal is not None:
            self.computer.input_values.append(input_signal)
        self.computer.run()
        return self.computer.output_values[-1]


class AmpRunner(object):
    def __init__(self, num_amps):
        self.amps = []
        for i in range(num_amps):
            self.amps.append(Amplifier())

    def find_max_thruster(self, program):
        num_amps = len(self.amps)
        if num_amps != 5:
            print('not supported, yet')
            exit(0)

        highest = 0
        permutations = list(itertools.permutations([0,1,2,3,4]))
        for phase_setting in permutations:
            thruster_signal = self.run(program, phase_setting)
            # print('{},{},{},{},{}'.format(a, b, c, d, e))
            # print(thruster_signal)
            if thruster_signal > highest:
                highest = thruster_signal
        return highest

    def run(self, program, phase_settings):
        last_out = 0
        for i in range(5):
            amp = self.amps[i]
            amp.reset(program[:], phase_setting=phase_settings[i])
            last_out = amp.run(input_signal=last_out)
        return last_out


class FeedbackAmpRunner(AmpRunner):
    def run(self, program, phase_settings):
        pass
