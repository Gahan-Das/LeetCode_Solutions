def max_key(dict, num):
    max_key = 0
    for key in dict.keys():
        if key > max_key and key <= num:
            max_key = key
    return max_key
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        symbol = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        special = {4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM'}
        number = str(num)
        length = len(number)
        roman = ""
        while( num != 0 ):
            if int(number[0]) == 4 or int(number[0]) == 9:
                high = max_key(special, num)
                num -= high
                number = str(num)
                roman += special[high]
            else:
                high = max_key(symbol, num)
                num -= high
                number = str(num)
                roman += symbol[high]
        return roman