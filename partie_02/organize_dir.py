from pathlib import Path
dirs = {
    ".png" :"IMAGES",
    ".jpg" :"IMAGES",
    ".jpeg":"IMAGES",
    ".gif" :"IMAGES",
    ".txt" :"DOC",
    ".pdf" :"DOC",
    ".doc" :"DOC",
    ".json":"DOC"
}
tri_downloads = Path.home() / "Downloads"
files = [f for f in tri_downloads.iterdir() if f.is_file()]
print(files)
for f in files:
    output_dir = tri_downloads / dirs.get(f.suffix,"Autres")
    output_dir.mkdir(exist_ok = True)
    f.rename(output_dir / f.name)