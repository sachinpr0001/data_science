# argv - list of command line argunemt
import sys

def printData():
    print(sys.argv)

def printsum():
    print(int(sys.argv[1]) + int(sys.argv[2]))


#printsum()

print(sys.version)
# interpretere will search for packages in these paths
print(sys.path)

print(type(sys.stdin))
print(sys.stdout)
print(sys.maxsize)
#print(sys.maxint)