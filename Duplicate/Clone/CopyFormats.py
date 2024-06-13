__Program__     = "Duplicate.Clone.CopyFormats"    
__Programer__   = "Themadhood Pequot"
__Date__        = "1/11/2024"
__Version__     = "0.0.2"
__Update__      = ""
__Info__        = ""   

import Error
VersionLst = [f"{__Program__}: {__Version__}"]
VersionLst += Error.VersionLst

def CopyFormats(var):
    st = Error.time.time()
    Error.Log(f"\nwriting usable py","Log.txt")
    retar = None
    try:
        if type(var) == dict:
            Error.Log(f"\nformating dict","Log.txt")
            retar = Copy_dct(var)
            
        elif type(var) == list:
            Error.Log(f"\nformating list","Log.txt")
            retar = Copy_lst(var)
            
        elif type(var) == tuple:
            Error.Log(f"\nformating object","Log.txt")
            retar = Copy_obj(var)
            
        elif type(var) == set:
            Error.Log(f"\nformating set","Log.txt")
            retar = Copy_set(var)
            
        else:
            Error.Log(f"\nformating other","Log.txt")
            retar = var
            
        Error.Log(f"writing usable py runtime: {Error.LenTime(st)}\n","Log.txt")
    except Exception as e:
        Error.UploadError([__Program__,__Version__,"","pyFormats",
                           f"failed to format and write py",e],"Functions")
        Error.Log(f"\nError ocured: {e}","Log.txt")
    return retar

def Copy_lst(lst):
    try:
        retar = [] 
        for o in lst:
            if type(o) == dict:
                Error.Log(f"formating dict","Log.txt")
                retar.append(Copy_dct(o))
                
            elif type(o) == list:
                Error.Log(f"formating list","Log.txt")
                retar.append(Copy_lst(o))
                             
            elif type(o) == tuple:
                Error.Log(f"formating object","Log.txt")
                retar.append(Copy_obj(o))
                             
            elif type(o) == set:
                Error.Log(f"formating set","Log.txt")
                retar.append(Copy_set(o))
                             
            else:
                Error.Log(f"formating other","Log.txt")
                retar.append(o)
    except Exception as e:
        Error.UploadError([__Program__,__Version__,"","copy_lst",
                           f"filed to format to list",e],"Functions")
    return retar

def Copy_dct(dct):
    try:
        retar = dict()
        for k in dct:
            if type(dct[k]) == dict:
                Error.Log(f"formating dict","Log.txt")
                retar.update({k:Copy_dct(dct[k])})
                
            elif type(dct[k]) == list:
                Error.Log(f"formating list","Log.txt")
                retar.update({k:Copy_lst(dct[k])})
                
            elif type(dct[k]) == tuple:
                Error.Log(f"formating object","Log.txt")
                retar.update({k:Copy_obj(dct[k])})
                
            elif type(dct[k]) == set:
                Error.Log(f"formating set","Log.txt")
                retar.update({k:Copy_set(dct[k])})
                
            else:
                Error.Log(f"formating other","Log.txt")
                retar.update({k:dct[k]})
    except Exception as e:
        Error.UploadError([__Program__,__Version__,"","copy_dct",
                           f"filed to format to dict",e],"Functions")
    return retar

def Copy_set(st):
    try:
        retar = set()
        for i in st:
            if type(i) == dict:
                Error.Log(f"formating dict","Log.txt")
                retar.add(Copy_dct(i))
                
            elif type(i) == list:
                Error.Log(f"formating list","Log.txt")
                retar.add(Copy_lst(i))
                
            elif type(i) == tuple:
                Error.Log(f"formating object","Log.txt")
                retar.add(Copy_obj(i))
                
            elif type(i) == set:
                Error.Log(f"formating set","Log.txt")
                retar.add(Copy_set(i))
                
            else:
                Error.Log(f"formating other","Log.txt")
                retar.add(i)
    except Exception as e:
        Error.UploadError([__Program__,__Version__,"","Copy_set",
                           f"filed to format to set",e],"Functions")
    return retar

def Copy_obj(obj):
    try:
        retar = Copy_lst(obj)

        retar = tuple(retar)
    except Exception as e:
        Error.UploadError([__Program__,__Version__,"","py_obj",
                           f"filed to format to object",e],"Functions")
    return retar





if __name__=="__main__":
    pass










