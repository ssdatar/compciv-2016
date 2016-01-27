import os
import shutil

matty = os.path.join("tempdata", "matty.shakespeare.tar.gz")
shutil.unpack_archive(matty, extract_dir = 'tempdata')
print('Unpacked', matty, 'into: tempdata')