from pathlib import Path
scan_folder_path = Path.home()/"Pictures"
#scan_folder = scan_folder_path.iterdir() #iterate inside a folder
#for f in scan_folder:
#    print(f.name)

#[f for f in scan_folder if f.is_dir()] # if f is a directory
#[f for f in scan_folder if f.is_file()] # if f is a file
#scan_folder1 = scan_folder_path / "Mes images"
#scan_folder1 = scan_folder1.iterdir()
#print(scan_folder1)
#for f in scan_folder1:
    #print(f.name)
#for f in scan_folder1.glob("*.PNG"):
    #print(f)
print(scan_folder_path.glob("*.png"))
for f in scan_folder_path.glob("*.png"):
    f.rename(f.parent/(f.stem + "_python_edit_name_" + f.suffix))  #edit file name
    

