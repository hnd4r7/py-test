import os

def func_kwargs(farg, **dddd):
    print("formal arg:", farg)
    for key in dddd:
        print("keyword arg: %s: %s" % (key, dddd[key]))
# func_kwargs(1 ,id=1, name='youzan', city='hangzhou',age ='20',四块五的妞是 = '来日方长的')

def find_files_by_suffix(path,suffix):
    matches=[]
    for root, subdirs, files in os.walk(path):
        for file in files:
            if file.endswith(suffix):
                matches.append(root+"/"+file)
    return matches

ss=find_files_by_suffix("/Users/mercy/tmp","08")
print(ss)


