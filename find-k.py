from bisect import bisect_right
from copy import deepcopy

def findKthElement(k, sortedArrays):
  arraysCopy = deepcopy(sortedArrays)
  for array in arraysCopy:
    del array[k+1:]
  return recursiveSearch(k, arraysCopy)
  
def recursiveSearch(k, sortedArrays):
  longestList = max(enumerate(sortedArrays), key = lambda tup: len(tup[1]))
  middleElement = longestList[1][len(longestList[1])/2]
  mList = []        #indicies of middle elements
  numLess = 0
  
  if len(longestList[1]) == 1:
    superset = []
    for array in sortedArrays:
      superset += array
    superset.sort()
    return superset[k-1]
  
  for array in sortedArrays:
    if len(array) > 1:
      mIndex = find_le(array, middleElement)
      if array[mIndex] != middleElement:
        mIndex += 1
      mList.append(mIndex)
      numLess += mIndex
    else:
      mList.append(0)

  if k <= numLess:
    for i in range(len(sortedArrays)):
      if len(sortedArrays[i]) != 1:
        del sortedArrays[i][mList[i]:]
    return recursiveSearch(k, sortedArrays)
  elif k > numLess:
    for i in range(len(sortedArrays)):
      del sortedArrays[i][:mList[i]]
    return recursiveSearch(k-numLess, sortedArrays)
  
def find_le(a, x):
  'Find rightmost value less than or equal to x'
  i = bisect_right(a, x)
  if i:
    return i-1
  else:
    return -1
  
if __name__ == '__main__':
  test = [[1,3,7,11], [2,4,5,6,42],[1,3]]
  for i in range(1, 12):
    print findKthElement(i, test)