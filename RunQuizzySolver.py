from QuizzySolver import QuizzySolver
import os
import sys

inputfile = 'ringfile.txt'

if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
    inst = QuizzySolver(sys.argv[1])
    inst.solve()
elif os.path.isfile(inputfile):
    inst = QuizzySolver(inputfile, maxlen = 8)
    inst.solve()
else:
    # todo: We can't find the input file they gave us, so let's just use good ol' traditional input()
    print('Did you give the right filename?')
    sys.exit()  # temp


