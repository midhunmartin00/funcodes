import os
images=[]
images=os.listdir("/home/xenial/Downloads/prank")
#print images
#cwd=os.getcwd()
os.chdir("/home/xenial/Downloads/prank")
for names in images:
    name=names.translate(None,"0123456789")
    os.rename(names,name)
    print name