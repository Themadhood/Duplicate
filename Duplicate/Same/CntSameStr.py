#program:       CntSameStr
#purpose:       count same strings in lst
#progamer:      Themadhood Pequot 11/2/2023

#presets
_FILE = "Duplicate.Same.CntSameStr"
_VERSION = "0.0.1"

import Error


def CntSameStr(lstofstrs):
    Error.Log(f"counting string duplicats","Log.txt")
    count = dict()
    for st in lstofstrs:
        try:
            count[st] += 1
        except:
            count.update({st:1})
    return count






if __name__ == "__main__":
    lst = ["a","c","b","a","a","e","b","e","a","e","a"]
    dct = CntSameStr(lst)
    print(dct)





