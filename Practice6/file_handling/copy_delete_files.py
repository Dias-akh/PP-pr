#deleting
from pathlib import Path
p=Path('./Practice6/file_handling/myfile.txt')
p.unlink()

#copying
import shutil
shutil.copyfile('./myfile.txt','./myfilecopy.txt')