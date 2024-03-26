#program:       CopyFormatsBlank
#purpose:       
#progamer:      Themadhood Pequot 1/11/2024

_FILE = "Duplicate.Blank.CopyFormatsBlank"
_VERSION = "0.0.1"

import Error

def CopyFormatsBlank(var):
    st = Error.time.time()
    Error.Log(f"\nwriting usable py","Log.txt")
    retar = None
    try:
        if type(var) == dict:
            Error.Log(f"\nformating dict","Log.txt")
            retar = Copy_dctBlank(var)
            
        elif type(var) == list:
            Error.Log(f"\nformating list","Log.txt")
            retar = Copy_lstBlank(var)
            
        elif type(var) == set:
            Error.Log(f"\nformating set","Log.txt")
            retar = Copy_setBlank(var)
            
        elif type(var) == tuple:
            Error.Log(f"\nformating object","Log.txt")
            retar = Copy_objBlank(var)
            
        elif type(var) == str:
            Error.Log(f"\nformating str","Log.txt")
            retar = ""
            
        elif type(var) == int:
            Error.Log(f"\nformating int","Log.txt")
            retar = 0
            
        else:
            Error.Log(f"\nformating other","Log.txt")
            retar = var
            
        Error.Log(f"writing usable py runtime: {Error.LenTime(st)}\n","Log.txt")
    except Exception as e:
        Error.UploadError([_FILE,_VERSION,"","CopyFormatsBlank",
                           f"failed to make a blank copy",e],"Functions")
        Error.Log(f"\nError ocured: {e}","Log.txt")
    return retar

def Copy_lstBlank(lst):
    retar = []
    try: 
        for o in lst:
            if type(o) == dict:
                Error.Log(f"formating dict","Log.txt")
                retar.append(Copy_dctBlank(o))
                
            elif type(o) == list:
                Error.Log(f"formating list","Log.txt")
                retar.append(Copy_lstBlank(o))
                
            elif type(o) == set:
                Error.Log(f"formating set","Log.txt")
                retar.append(Copy_setBlank(o))
                             
            elif type(o) == tuple:
                Error.Log(f"formating object","Log.txt")
                retar.append(Copy_objBlank(o))
    except Exception as e:
        Error.UploadError([_FILE,_VERSION,"","Copy_lstBlank",
                           f"filed to make blank list copy",e],"Functions")
    return retar

def Copy_dctBlank(dct):
    retar = dict()
    try:
        keys = list(dct)
        for k in keys:
            if type(dct[k]) == dict:
                Error.Log(f"formating dict","Log.txt")
                retar.update({k:Copy_dctBlank(dct[k])})
                
            elif type(dct[k]) == list:
                Error.Log(f"formating list","Log.txt")
                retar.update({k:Copy_lstBlank(dct[k])})
                
            elif type(dct[k]) == set:
                Error.Log(f"formating set","Log.txt")
                retar.update({k:Copy_setBlank(dct[k])})
                
            elif type(dct[k]) == tuple:
                Error.Log(f"formating object","Log.txt")
                retar.update({k:Copy_objBlank(dct[k])})
            
            elif type(dct[k]) == str:
                Error.Log(f"\nformating str","Log.txt")
                retar.update({k:""})
                
            elif type(dct[k]) == int:
                Error.Log(f"\nformating int","Log.txt")
                retar.update({k:0})
                
            else:
                Error.Log(f"formating other","Log.txt")
                retar.update({k:dct[k]})
    except Exception as e:
        Error.UploadError([_FILE,_VERSION,"","Copy_dctBlank",
                           f"filed to make blank dict",e],"Functions")
    return retar

def Copy_setBlank(st):
    retar = []
    try: 
        for o in st:
            if type(o) == dict:
                Error.Log(f"formating dict","Log.txt")
                retar.add(Copy_dctBlank(o))
                
            elif type(o) == list:
                Error.Log(f"formating list","Log.txt")
                retar.add(Copy_lstBlank(o))
                
            elif type(o) == set:
                Error.Log(f"formating set","Log.txt")
                retar.add(Copy_setBlank(o))
                             
            elif type(o) == tuple:
                Error.Log(f"formating object","Log.txt")
                retar.add(Copy_objBlank(o))
    except Exception as e:
        Error.UploadError([_FILE,_VERSION,"","Copy_setBlank",
                           f"filed to make blank list copy",e],"Functions")
    return retar

def Copy_objBlank(obj):
    retar = ()
    try:
        retar = Copy_lst(obj)

        retar = tuple(retar)
    except Exception as e:
        Error.UploadError([_FILE,_VERSION,"","Copy_objBlank",
                           f"filed to format to object",e],"Functions")
    return retar





if __name__=="__main__":
    pass










