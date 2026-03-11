text = '''Hii!
hallo world
wellcome to python'''
# text = ["Hii!\n","hallo world \n", "wellcome to python \n"]

with open("Assets\\data.txt",'w') as w:
    w.write(text)
    # w.writelines(text)
with open("Assets\\data.txt",'r') as r:
    print(r.read())
    r.seek(0)
    print(r.readlines())