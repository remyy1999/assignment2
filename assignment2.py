import socket

class Assignment2:
    def __init__(self, year):
        self.year = year

    def tellAge(self, currentYear):
        birthYear = currentYear - self.year
        print(f'Your age is {birthYear}')

    def listAnniversaries(self):
        today = 2022  
        return [i for i in range(10, today - self.year, 10)]

    def modifyYear(self, n):
        year_str = str(self.year)
        result = year_str[:2] * n + year_str[0::2][::2] * n
        return result

    @staticmethod
    def checkGoodString(string):
        return len(string) >= 9 and string[0].islower() and string.count("1") == 1

    @staticmethod
    def connectTcp(host, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            sock.close()
            return True
        except (socket.error, OSError):
            return False

a = Assignment2(2000)
a.tellAge(2024)

ret = a.listAnniversaries()
print(ret)

ret = a.modifyYear(5)
print(ret)

ret = Assignment2.checkGoodString("f1obar0more")
print(ret)

ret = Assignment2.checkGoodString("f1obar0more")
print(ret)

retval = Assignment2.connectTcp("www.google.com", 80)
if retval:
    print("Connection established correctly")
else:
    print("Some error")
