from pathlib import Path

def parse_folder(path):
    d = Path(path)
    files = []
    folders = []
    res = list()
    
    for p in d.iterdir():
        if p.is_dir():
            folders.append(p.name)
        else:  
            files.append(str(p.name)[:-3])
    
    res.append(files)
    res.append(folders)
    t = tuple(res)
    print(t)
    return t #files, folders

parse_folder('C:\Goit\Goit_repo')