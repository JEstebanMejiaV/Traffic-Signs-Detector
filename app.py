# -*- coding: utf-8 -*-
"""

@author: Juan Esteban Mejía


"""


import click
import glob
import zipfile, urllib.request, shutil, os


Dir_to_remove = 'C:/Users/admin/Desktop/GitHub/German-Traffic-Signs-Detector/timage/train/FullIJCNN2013'
localfile = 'C:/Users/admin/Desktop/GitHub/German-Traffic-Signs-Detector/images/train'
url = 'http://benchmark.ini.rub.de/Dataset_GTSDB/FullIJCNN2013.zip' 


# Auxiliary functions

### Remove files
def remove_extra_files(Dir_to_remove = Dir_to_remove):
    Dir_to_remove = os.chdir(Dir_to_remove)
    types = ('*.ppm', '*.txt')
    files_to_remove = []
    for files in types:
        files_to_remove.extend(glob.glob(files))
     
    # print("Files to remove: ", files_to_remove)    
    for file2 in files_to_remove:
         os.remove(file2)



@click.group()
def cli():
    pass

@click.command()
@click.option( '-url', default=url,
               help='url of a zip file to download and decompress' )
@click.option( '-dir', default = localfile,
               help='path for decompressed images' )

def download(localfile=localfile, url=url):

    with urllib.request.urlopen(url) as response, open(localfile, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    with zipfile.ZipFile(localfile) as zf:
        zf.extractall()
    remove_extra_files()

