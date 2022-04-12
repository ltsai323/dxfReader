#!/usr/bin/env python3
mesg='Shortest distance algorithm in mini gantry coordinate'

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
  pool=[ p for p in pointList ]
  p0=pool[0]
  pool.pop(0)
  return ShortedLength(p0,pool)
  
  
def ShortedLength(currentPoint, PointPool):
  if len(PointPool)==0: return []
  

  leng=9999.
  idxFound=-1
  for idx,nextPoint in enumerate(PointPool):
    if currentPoint.Length(nextPoint) < leng:
      leng=currentPoint.Length(nextPoint)
      idxFound=idx
  pointFound=PointPool[idxFound]
  PointPool.pop(idxFound)
  resultlist=ShortedLength( pointFound, PointPool )
  resultlist.append(pointFound)
  return resultlist
  
  

if __name__ == "__main__":
  import sys
  if len(sys.argv) != 2: raise IOError('input a text file!')
  print ( 'input file : %s' % sys.argv[1] )
  
  lines = [ line.strip() for line in open(sys.argv[1], 'r').readlines() if 'CIRCLE' in line ]
  points = ( TextPoint(line) for line in lines )
  convertedPoints = ( ConvertToMiniGantry(point) for point in points )
  print(mesg)
  for idx,cPoint in enumerate(SortingPoints(convertedPoints)):
    print('No.%2d: %s'%(idx,cPoint))
    if idx%5==5-1: print('---- 5 sep ----')
  #for cPoint in convertedPoints: print('Point is : %s' % cPoint)