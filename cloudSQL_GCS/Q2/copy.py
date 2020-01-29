from google.cloud import storage
import os


f1 = 'folder1'
f2= 'new'

os.mkdir(fld2)

sclient = storage.Client()
sbucket = sclient.get_bucket("ad-bucket2")
blobs = sbucket.list_blobs()
for x in blobs:
    f = f2 + '/'
    if x.name.startswith(f1) and x.name[-1] != '/':
        f_strct = b.name.split('/')
        for folder in f_strct[:-1]:
            f += folder + '/'
            
        x.download_to_filename(f + f_strct[-1])
print("Download Complete.")

