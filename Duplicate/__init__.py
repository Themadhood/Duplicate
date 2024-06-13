__Program__     = "Duplicate.__init__"    
__programer__   = "Themadhood Pequot"
__Date__        = "2/27/2024"
__Version__     = "0.0.1"
__update__      = ""
__info__        = ""   

try:
    from . import Clone
    from . import Blank
    from . import Same
except:
    import Clone
    import Blank
    import Same

VersionLst = [f"{__Program__}: {__Version__}"]
VersionLst += Clone.VersionLst
VersionLst += Blank.VersionLst
VersionLst += Same.VersionLst

Error = Clone.Error


if __name__ == "__main__":
    Error.VersionRecordsLog(pyName=__Program__,msg=VersionLst)











