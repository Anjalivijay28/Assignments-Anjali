#commit

from abc import ABC, abstractmethod


class RBI(ABC):
    @abstractmethod
    def getROI(self):
        pass


class SBI(RBI):
    def __init__(self):
        print("This is SBI class")
    def getROI(self):
        print("ROI is 2%")


class HDFC(RBI):
    def __init__(self):
        print("This is HDFC class")

    def getROI(self):
        print("ROI is 4%")



c1= SBI()
c1.getROI()

c2=HDFC()
c2.getROI()
