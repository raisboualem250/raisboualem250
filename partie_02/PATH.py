from pathlib import Path
path = Path.home() #to get the user folder
print(path)
path1 = Path.cwd() #ti get curent  worked directory
print(path1)
path = Path.is_dir(path) #is directoty
print(path)

#.....
path1 = Path.cwd() #to get curent  worked directory
print(path1)
path = path1 / "f0" #concatenate two path with /
print(path)
path = path.joinpath("f1","f2","qqq.txt") # concatenate using joinpath
print(path)
ext = path.suffix #get suffixe (extension)
print(ext)