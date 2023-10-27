class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#green
def printGreen(mess):
    print("\033[32m" + mess + '\n')

#red
def printRed(mess):
    print("\033[31m" + mess + '\n')
  
#yellow
def printYellow(mess):
    print("\033[33m" + mess + '\n')

