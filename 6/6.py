class Object(object):
    def __init__(self, name, orbiting=None):
        self.name = name
        self.orbiting = orbiting

    def calc_orbits(self):
        return 0 if self.orbiting is None else (self.orbiting.calc_orbits() + 1)

    def calc_chain_to_com(self):
        if self.name == 'COM':
            return [self.name]
        else:
            path = self.orbiting.calc_chain_to_com()
            path.insert(0,self.name)
            return path


def main():

    with open('./input.txt') as f:
        orbits = []
        for l in f.readlines():
            s = l.rstrip('\n').split(')')
            orbits.append([s[0], s[1]])

        object_directory = {}
        for o in orbits:
            name0 = o[0]
            name1 = o[1]

            if not name0 in object_directory:
                object_directory[name0] = Object(name0)
            if not name1 in object_directory:
                object_directory[name1] = Object(name1, orbiting=object_directory[name0])
            elif object_directory[name1].orbiting is None:
                object_directory[name1].orbiting = object_directory[name0]
            else:
                import pdb;pdb.set_trace()
                # More than 1 oribtiings?

        # calc
        # num = 0
        # for name in object_directory:
        #     o = object_directory[name]
        #     num += o.calc_orbits()

        path_you = object_directory['YOU'].calc_chain_to_com()
        path_san = object_directory['SAN'].calc_chain_to_com()

        # find first in you from the right that occurs in path_san
        for i in range(len(path_you)):
            if path_you[i] in path_san:
                # found!
                path_you[i]
                n = path_san.index(path_you[i]) + i
                print(n)
                import pdb;pdb.set_trace()
                return


if __name__ == '__main__':
    main()