import argparse

parser=argparse.ArgumentParser()
parser.add_argument("package")
parser.add_argument("totalEvent")
args=parser.parse_args()
param=vars(args)
v={}
for key,value in param.items():
    v[key]=value
print(v)