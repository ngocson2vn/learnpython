import os
import sys
import glob

path = sys.argv[1]
if not os.path.isdir(path):
  print("{} doesn't exist!".format(path))
  sys.exit(1)

if path[len(path) - 1] != '/':
  path += '/'

for f in glob.glob(path + "**/staging/iam.tf", recursive=True):
  print(f)