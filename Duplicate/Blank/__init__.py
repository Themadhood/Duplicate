__Program__     = "Duplicate.Blank.__init__"    
__programer__   = "Themadhood Pequot"
__Date__        = "2/27/2024"
__Version__     = "0.0.1"
__update__      = ""
__info__        = ""   

try:
    from . import CopyFormatsBlank
except:
    import CopyFormatsBlank

VersionLst = [f"{__Program__}: {__Version__}"]
VersionLst += CopyFormatsBlank.VersionLst




if __name__ == "__main__":
    Error.VersionRecordsLog(pyName=__Program__,msg=VersionLst)









