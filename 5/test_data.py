import pdb


class Test(object):
    def run(self, computer):
        pass

    def assert_(self, a, b):
        assert a == b, '{} <> {}'.format(a,b)


class Day2Tests(Test):
    def run(self, computer):
        computer.reset('1,0,0,0,99')
        computer.run()
        self.assert_(computer.get_program_str(), '2,0,0,0,99')

        computer.reset('2,3,0,3,99')
        computer.run()
        self.assert_(computer.get_program_str(), '2,3,0,6,99')

        computer.reset('2,4,4,5,99,0')
        computer.run()
        self.assert_(computer.get_program_str(), '2,4,4,5,99,9801')

        computer.reset('1,1,1,4,99,5,6,0,99')
        computer.run()
        self.assert_(computer.get_program_str(), '30,1,1,4,2,5,6,0,99')

        computer.reset('1,9,10,3,2,3,11,0,99,30,40,50')
        computer.run()
        self.assert_(computer.get_program_str(), '3500,9,10,70,2,3,11,0,99,30,40,50')

        computer.reset('1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,2,19,9,23,1,23,5,27,2,6,27,31,1,31,5,35,1,35,5,39,2,39,6,43,2,43,10,47,1,47,6,51,1,51,6,55,2,55,6,59,1,10,59,63,1,5,63,67,2,10,67,71,1,6,71,75,1,5,75,79,1,10,79,83,2,83,10,87,1,87,9,91,1,91,10,95,2,6,95,99,1,5,99,103,1,103,13,107,1,107,10,111,2,9,111,115,1,115,6,119,2,13,119,123,1,123,6,127,1,5,127,131,2,6,131,135,2,6,135,139,1,139,5,143,1,143,10,147,1,147,2,151,1,151,13,0,99,2,0,14,0')
        computer.run()
        self.assert_(computer.program[0], 4576384)

        computer.reset('1,53,98,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,2,19,9,23,1,23,5,27,2,6,27,31,1,31,5,35,1,35,5,39,2,39,6,43,2,43,10,47,1,47,6,51,1,51,6,55,2,55,6,59,1,10,59,63,1,5,63,67,2,10,67,71,1,6,71,75,1,5,75,79,1,10,79,83,2,83,10,87,1,87,9,91,1,91,10,95,2,6,95,99,1,5,99,103,1,103,13,107,1,107,10,111,2,9,111,115,1,115,6,119,2,13,119,123,1,123,6,127,1,5,127,131,2,6,131,135,2,6,135,139,1,139,5,143,1,143,10,147,1,147,2,151,1,151,13,0,99,2,0,14,0')
        computer.run()
        self.assert_(computer.program[0], 19690720)

        computer.reset('1002,4,3,4,33')
        computer.run()
        self.assert_(computer.program[4], 99)

        computer.reset('1101,100,-1,4,0')
        computer.run()
        self.assert_(computer.program[4], 99)

        computer.reset('3,0,4,0,99', input_values=[1234567])
        computer.run()
        self.assert_(computer.output_values[0], 1234567)

        computer.reset('3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1101, 69, 55, 225, 1001, 144, 76, 224, 101, -139, 224, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 3, 224, 1, 223, 224, 223, 1102, 60, 49, 225, 1102, 51, 78, 225, 1101, 82, 33, 224, 1001, 224, -115, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 3, 224, 1, 224, 223, 223, 1102, 69, 5, 225, 2, 39, 13, 224, 1001, 224, -4140, 224, 4, 224, 102, 8, 223, 223, 101, 2, 224, 224, 1, 224, 223, 223, 101, 42, 44, 224, 101, -120, 224, 224, 4, 224, 102, 8, 223, 223, 101, 3, 224, 224, 1, 223, 224, 223, 1102, 68, 49, 224, 101, -3332, 224, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 4, 224, 1, 224, 223, 223, 1101, 50, 27, 225, 1102, 5, 63, 225, 1002, 139, 75, 224, 1001, 224, -3750, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 3, 224, 1, 223, 224, 223, 102, 79, 213, 224, 1001, 224, -2844, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 4, 224, 1, 223, 224, 223, 1, 217, 69, 224, 1001, 224, -95, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 5, 224, 1, 223, 224, 223, 1102, 36, 37, 225, 1101, 26, 16, 225, 4, 223, 99, 0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0, 99999, 1105, 227, 247, 1105, 1, 99999, 1005, 227, 99999, 1005, 0, 256, 1105, 1, 99999, 1106, 227, 99999, 1106, 0, 265, 1105, 1, 99999, 1006, 0, 99999, 1006, 227, 274, 1105, 1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101, 294, 0, 0, 105, 1, 0, 1105, 1, 99999, 1106, 0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1, 99999, 1107, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 329, 1001, 223, 1, 223, 1108, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 344, 1001, 223, 1, 223, 107, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 359, 101, 1, 223, 223, 1008, 226, 226, 224, 102, 2, 223, 223, 1005, 224, 374, 1001, 223, 1, 223, 1107, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 389, 1001, 223, 1, 223, 1008, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 404, 1001, 223, 1, 223, 7, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 419, 1001, 223, 1, 223, 1008, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 434, 1001, 223, 1, 223, 108, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 449, 1001, 223, 1, 223, 108, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 464, 1001, 223, 1, 223, 107, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 479, 101, 1, 223, 223, 1108, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 494, 1001, 223, 1, 223, 107, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 509, 101, 1, 223, 223, 7, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 524, 1001, 223, 1, 223, 1007, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 539, 1001, 223, 1, 223, 8, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 554, 101, 1, 223, 223, 8, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 569, 101, 1, 223, 223, 7, 226, 677, 224, 102, 2, 223, 223, 1006, 224, 584, 1001, 223, 1, 223, 1007, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 599, 1001, 223, 1, 223, 1107, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 614, 1001, 223, 1, 223, 1108, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 629, 1001, 223, 1, 223, 1007, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 644, 1001, 223, 1, 223, 108, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 659, 101, 1, 223, 223, 8, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 674, 1001, 223, 1, 223, 4, 223, 99, 226', input_values=[1])
        computer.run()
        self.assert_(computer.output_values[-1], 7157989)

        computer.reset('3,9,8,9,10,9,4,9,99,-1,8', input_values=[8])
        computer.run()
        self.assert_(computer.output_values[0], 1)

        computer.reset('3,9,8,9,10,9,4,9,99,-1,8', input_values=[7])
        computer.run()
        self.assert_(computer.output_values[0], 0)

        computer.reset('3,9,8,9,10,9,4,9,99,-1,8', input_values=[9])
        computer.run()
        self.assert_(computer.output_values[0], 0)

        computer.reset('3,9,7,9,10,9,4,9,99,-1,8', input_values=[7])
        computer.run()
        self.assert_(computer.output_values[0], 1)

        computer.reset('3,9,7,9,10,9,4,9,99,-1,8', input_values=[8])
        computer.run()
        self.assert_(computer.output_values[0], 0)

        computer.reset('3,3,1108,-1,8,3,4,3,99', input_values=[8])
        computer.run()
        self.assert_(computer.output_values[0], 1)

        computer.reset('3,3,1108,-1,8,3,4,3,99', input_values=[7])
        computer.run()
        self.assert_(computer.output_values[0], 0)

        computer.reset('3,3,1108,-1,8,3,4,3,99', input_values=[9])
        computer.run()
        self.assert_(computer.output_values[0], 0)

        computer.reset('3,3,1107,-1,8,3,4,3,99', input_values=[8])
        computer.run()
        self.assert_(computer.output_values[0], 0)

        computer.reset('3,3,1107,-1,8,3,4,3,99', input_values=[7])
        computer.run()
        self.assert_(computer.output_values[0], 1)

        computer.reset('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9', input_values=[123])
        computer.run()
        self.assert_(computer.output_values[0], 1)

        computer.reset('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9', input_values=[0])
        computer.run()
        self.assert_(computer.output_values[0], 0)

        computer.reset('3,3,1105,-1,9,1101,0,0,12,4,12,99,1', input_values=[123])
        computer.run()
        self.assert_(computer.output_values[0], 1)

        computer.reset('3,3,1105,-1,9,1101,0,0,12,4,12,99,1', input_values=[0])
        computer.run()
        self.assert_(computer.output_values[0], 0)

        computer.reset('3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99', input_values=[7])
        computer.run()
        self.assert_(computer.output_values[0], 999)

        computer.reset(
            '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99',
            input_values=[8])
        computer.run()
        self.assert_(computer.output_values[0], 1000)

        computer.reset(
            '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99',
            input_values=[9])
        computer.run()
        self.assert_(computer.output_values[0], 1001)

        computer.reset(
            '3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1101, 69, 55, 225, 1001, 144, 76, 224, 101, -139, 224, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 3, 224, 1, 223, 224, 223, 1102, 60, 49, 225, 1102, 51, 78, 225, 1101, 82, 33, 224, 1001, 224, -115, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 3, 224, 1, 224, 223, 223, 1102, 69, 5, 225, 2, 39, 13, 224, 1001, 224, -4140, 224, 4, 224, 102, 8, 223, 223, 101, 2, 224, 224, 1, 224, 223, 223, 101, 42, 44, 224, 101, -120, 224, 224, 4, 224, 102, 8, 223, 223, 101, 3, 224, 224, 1, 223, 224, 223, 1102, 68, 49, 224, 101, -3332, 224, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 4, 224, 1, 224, 223, 223, 1101, 50, 27, 225, 1102, 5, 63, 225, 1002, 139, 75, 224, 1001, 224, -3750, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 3, 224, 1, 223, 224, 223, 102, 79, 213, 224, 1001, 224, -2844, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 4, 224, 1, 223, 224, 223, 1, 217, 69, 224, 1001, 224, -95, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 5, 224, 1, 223, 224, 223, 1102, 36, 37, 225, 1101, 26, 16, 225, 4, 223, 99, 0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0, 99999, 1105, 227, 247, 1105, 1, 99999, 1005, 227, 99999, 1005, 0, 256, 1105, 1, 99999, 1106, 227, 99999, 1106, 0, 265, 1105, 1, 99999, 1006, 0, 99999, 1006, 227, 274, 1105, 1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101, 294, 0, 0, 105, 1, 0, 1105, 1, 99999, 1106, 0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1, 99999, 1107, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 329, 1001, 223, 1, 223, 1108, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 344, 1001, 223, 1, 223, 107, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 359, 101, 1, 223, 223, 1008, 226, 226, 224, 102, 2, 223, 223, 1005, 224, 374, 1001, 223, 1, 223, 1107, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 389, 1001, 223, 1, 223, 1008, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 404, 1001, 223, 1, 223, 7, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 419, 1001, 223, 1, 223, 1008, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 434, 1001, 223, 1, 223, 108, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 449, 1001, 223, 1, 223, 108, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 464, 1001, 223, 1, 223, 107, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 479, 101, 1, 223, 223, 1108, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 494, 1001, 223, 1, 223, 107, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 509, 101, 1, 223, 223, 7, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 524, 1001, 223, 1, 223, 1007, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 539, 1001, 223, 1, 223, 8, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 554, 101, 1, 223, 223, 8, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 569, 101, 1, 223, 223, 7, 226, 677, 224, 102, 2, 223, 223, 1006, 224, 584, 1001, 223, 1, 223, 1007, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 599, 1001, 223, 1, 223, 1107, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 614, 1001, 223, 1, 223, 1108, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 629, 1001, 223, 1, 223, 1007, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 644, 1001, 223, 1, 223, 108, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 659, 101, 1, 223, 223, 8, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 674, 1001, 223, 1, 223, 4, 223, 99, 226',
            input_values=[5])
        computer.run()
        self.assert_(computer.output_values[-1], 7873292)


class TestSuite(object):
    def __init__(self):
        self.tests = []
        self.tests.append(Day2Tests())

    def run(self, computer):
        for test in self.tests:
            test.run(computer)
