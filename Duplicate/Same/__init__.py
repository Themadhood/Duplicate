__Program__     = "Duplicate.Same.__init__"    
__programer__   = "Themadhood Pequot"
__Date__        = "2/27/2024"
__Version__     = "0.0.1"
__update__      = ""
__info__        = ""   

try:
    from .CntSameStr import CntSameStr,Error,VersionLst as _CSSVL
    from .SameLst import SamelstDifrentOrder as SameLst,RemoveEqivlentLsts,\
         VersionLst as _SDOVL
except:
    from CntSameStr import CntSameStr,Error,VersionLst as _CSSVL
    from SameLst import SamelstDifrentOrder as SameLst,RemoveEqivlentLsts,\
         VersionLst as _SDOVL

VersionLst = [f"{__Program__}: {__Version__}"]
VersionLst += _CSSVL
VersionLst += _SDOVL




if __name__ == "__main__":
    Error.VersionRecordsLog(pyName=__Program__,msg=VersionLst)










