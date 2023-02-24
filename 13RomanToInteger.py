from collections import OrderedDict

class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN = OrderedDict([('CM',900), ('CD',400), ('XC',90), ('XL',40), ('IX',9), ('IV',4), ('M',1000), ('D',500), ('C',100), ('L',50), ('X',10), ('V',5), ('I',1)])
        num = 0
        for key, value in ROMAN.items():
            num += value * s.count(key)
            s = s.replace(key, '')
        return num