import os

def shutAll():
    v = open('aliveHostList.txt', 'r')
    for line in v:
        wordList = line.split()
        command = "shutdown -s -t 30 -c \"please save all your works, your computer" \
                  " will shutdown in 30 seconds\" -m \\\\" + wordList[1]
        os.system(command)


def restartAll():
    v = open('aliveHostList.txt', 'r')
    for line in v:
        wordList = line.split()
        command = "shutdown -r -t 30 -c \"please save all your works, your " \
                  "computer will shutdown in 30 seconds\" -m \\\\" + wordList[1]
        os.system(command)


def shutUser(userName):
    command = "shutdown -s -t 30 -c \"please save all your works," \
              " your computer will shutdown in 30 seconds\" -m \\\\" + userName
    os.system(command)


def restartUser(userName):
    command = "shutdown -r -t 30 -c \"please save all your works," \
              " your computer will shutdown in 30 seconds\" -m \\\\" + userName
    print(command)
    os.system(command)
