#!/usr/bin/env python3


class MyPoint(object):
  def __init__(self, x,y):
    self.x=float(x)
    self.y=float(y)
  def __repr__(self):
    return '(%7.2f,%7.2f)'%(self.x,self.y)
  def Length(self,point):
    return ( (self.x-point.x)**2+(self.y-point.y)**2 )**0.5
def TextPoint(line):
  words=line.split()
  return MyPoint(words[-2],words[-1])  
def ConvertToMiniGantry( point ):
  newx = point.y * -1
  newy = point.x
  return MyPoint(newx,newy)
  
def SortingPoints(pointList):
  pDir = { idx:point for idx,point in enumerate(pointList) }
  idxs = { idx:False for idx in pDir.keys() }
  print(pDir)
  
if __name__ == "__main__":
  import sys
  if len(sys.argv) != 2: raise IOError('input a text file!')
  print ( 'input file : %s' % sys.argv[1] )
  
  lines = [ line.strip() for line in open(sys.argv[1], 'r').readlines() if 'CIRCLE' in line ]
  points = ( TextPoint(line) for line in lines )
  convertedPoints = ( ConvertToMiniGantry(point) for point in points )
  SortingPoints( convertedPoints )
  #for cPoint in convertedPoints: print('Point is : %s' % cPoint)