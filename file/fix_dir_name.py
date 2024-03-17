#! env python

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--target-dir", "-d", required=True, help="The target directory")
args = parser.parse_args()

target_dir = args.target_dir

for subdir in os.listdir(target_dir):
  p = os.path.join(target_dir, subdir)
  if os.path.isdir(p):
    for subdir2 in os.listdir(p):
      if "@" in subdir2:
        p2 = os.path.join(p, subdir2)
        model_name = subdir2.split("@")[0]
        p3 = os.path.join(p, model_name)
        os.rename(p2, p3)
        if os.path.isdir(p3):
          print("Renamed {} -> {}".format(p2, p3))

# Double-check
for subdir in os.listdir(target_dir):
  p = os.path.join(target_dir, subdir)
  if os.path.isdir(p):
    for subdir2 in os.listdir(p):
      print(subdir2)
