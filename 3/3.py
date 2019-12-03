def get_extent(path, direction):
    length_positive = 0
    length_negative = 0
    counter = 0
    for step in path:
        if direction == step[:1]:
            counter += int(step[1:])
            if length_negative > counter:
                length_negative = counter
            if counter > length_positive:
                length_positive = counter
    return (length_negative, length_positive)


def main():
    with open('./input2.txt') as f:
        (path1, path2) = [l.rstrip('\n').split(',') for l in f.readlines()[:2]]
        print(get_extent(path1, 'U'))

        import pdb;pdb.set_trace()


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