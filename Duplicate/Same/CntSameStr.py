__Program__     = "Duplicate.Same.CntSameStr"    
__programer__   = "Themadhood Pequot"
__Date__        = "11/2/2024"
__Version__     = "0.0.2"
__update__      = ""
__info__        = ""

import Error
#compile PYsInfo
VersionLst = [f"{__Program__}: {__Version__}"]
VersionLst += Error.VersionLst

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
    Error.VersionRecordsLog(pyName=__Program__,msg=VersionLst)
    lst = ["a","c","b","a","a","e","b","e","a","e","a"]
    dct = CntSameStr(lst)
    print(dct)





