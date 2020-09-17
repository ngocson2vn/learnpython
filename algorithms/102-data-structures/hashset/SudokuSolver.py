import sys
import json
import time
from HashSet import HashSet
import argparse

def reduce(matrix):
  changed = True
  groups = getGroups(matrix)
  while changed:
    changed = reduceGroups(groups)


def getGroups(matrix):
  groups = []
  for i in range(len(matrix)):
    groups.append(matrix[i])
    col = [matrix[j][i] for j in range(len(matrix))]
    groups.append(col)
  for i in range(0, len(matrix), 3):
    groups.append(matrix[i][0:3] + matrix[i + 1][0:3] + matrix[i + 2][0:3])
    groups.append(matrix[i][3:6] + matrix[i + 1][3:6] + matrix[i + 2][3:6])
    groups.append(matrix[i][6:9] + matrix[i + 1][6:9] + matrix[i + 2][6:9])
  return groups


def reduceGroups(groups):
  changed = False
  for group in groups:
    for i in range(len(group)):
      s = group[i]
      if s.numItems == 1:
        val = next(iter(s))
        for j in [y for x in (range(0, i), range(i + 1, len(group))) for y in x]:
          s2 = group[j]
          if s2.numItems > 1 and val in s2:
            s2.remove(val)
            changed = True

  for group in groups:
    for i in range(len(group)):
      s = group[i]
      foundItems = []
      for item in s:
        for j in [y for x in (range(0, i), range(i + 1, len(group))) for y in x]:
          if item in group[j]:
            foundItems.append(item)
            break
      if len(foundItems) > 0 and len(foundItems) < s.numItems:
        changed = True
        for item in foundItems:
          s.remove(item)

  return changed

def buildMatrix(file):
  matrix = []
  i = 0
  with open(file) as f:
    for line in f:
      matrix.append([])
      elements = line.split()
      if len(elements) != 9:
        raise Exception("Row does not have 9 elements")
      for e in elements:
        if e.lower() == "x":
          matrix[i].append(HashSet([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        else:
          matrix[i].append(HashSet([int(e)]))
      i += 1
  return matrix


def default(obj):
  if type(obj) == HashSet:
    retList = []
    for item in obj:
      retList.append(item)
    return retList
  json.JSONEncoder.default(obj, obj)

def printRawMatrix(matrix):
  for row in matrix:
    print(row)

def printMatrix(matrix):
  for row in matrix:
    print(json.dumps(row, default=default))

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--file", "-f", required=True, help="Sudoku file")
  args, _ = parser.parse_known_args()
  matrix = buildMatrix(args.file)
  printMatrix(matrix)
  print()
  reduce(matrix)
  printMatrix(matrix)


if __name__ == "__main__":
  main()
