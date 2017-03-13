from numpy import *


def file2matrix(filename, columnCount, delimiter):
    fr = open(filename)
    lines = fr.readlines()
    lineCount = len(lines)
    returnMatrix = zeros((lineCount, columnCount))
    classLabelVector = []
    index = 0
    for line in lines:
      line = line.strip()
      columns = line.split(delimiter)
      returnMatrix[index,:] = columns[0:columnCount-2]
      classLabelVector.append(int(columns[-1]))
      index += 1
    return  returnMatrix, classLabelVector
