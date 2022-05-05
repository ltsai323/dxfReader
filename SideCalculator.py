mesg='Side points in mini gantry coordinate with inner point 1/3'

class MyPoint(object):
  def __init__(self, x,y):
    self.x=float(x)
    self.y=float(y)
  def __repr__(self):
    return '(%7.2f,%7.2f)'%(self.x,self.y)
  def Length(self,point):
    return ( (self.x-point.x)**2+(self.y-point.y)**2 )**0.5

def TransformIntoMiniGantry(point):
  return MyPoint( -1.*point.y, point.x)

def MidPoint(p0,p1):
    x = (p0.x+p1.x)/2.
    y = (p0.y+p1.y)/2.
    return MyPoint(x,y)
def InnerOneThird(pInner,pOuter):
    x = ( 2. * pInner.x + 1. * pOuter.x ) / 3.
    y = ( 2. * pInner.y + 1. * pOuter.y ) / 3.
    return MyPoint(x,y)

class mesgOutput:
  def __init__(self, oName, mesg, printSep = True):
    self.printSep = printSep
    self.f = open(oName,'w')
    self.f.write( mesgOutput.MESG(mesg) )
  def Write(self, points):
    for idx,cPoint in enumerate(points):
      self.f.write( mesgOutput.MESG(('No.%2d: %s'%(idx,cPoint))))
    if self.printSep and idx%5==5-1: self.f.write(mesgOutput.MESG(('---- 5 sep ----')))
  def __del__(self):
    self.f.close()
  @staticmethod
  def MESG(word): return word+'\n'

if __name__ == "__MAIN__".lower():
    rawdata_inner = [
      (-34.42, 81.86),
      ( 34.28, 81.86),
      ( 49.87, 77.18),
      ( 53.62, 70.70),
      ( 87.97, 11.20),
      ( 91.71,  4.71),
      ( 87.97,-11.12),
      ( 53.61,-70.62),
      ( 41.76,-81.78),
      ( 34.29,-81.78),
      (-34.42,-81.78),
      (-41.90,-81.78),
      (-53.75,-70.62),
      (-88.10,-11.12),
      (-91.84,  4.72),
      (-88.10, 11.12),
      (-53.75, 70.70),
      (-50.01, 77.17),
    ]
    rawdata_outer = [
      (-34.42, 82.87),
      ( 34.29, 82.87),
      ( 50.74, 77.68),
      ( 54.49, 71.20),
      ( 88.84, 11.70),
      ( 92.58,  5.21),
      ( 88.84,-11.62),
      ( 54.49,-71.13),
      ( 41.77,-82.78),
      ( 34.29,-82.79),
      (-34.42,-82.79),
      (-41.90,-82.78),
      (-54.62,-71.12),
      (-88.97,-11.63),
      (-92.71,  5.22),
      (-88.98, 11.70),
      (-54.62, 71.20),
      (-50.87, 77.68),
    ]
    innerpoints = [ MyPoint(p[0], p[1]) for p in rawdata_inner ]
    outerpoints = [ MyPoint(p[0], p[1]) for p in rawdata_outer ]
    
    import matplotlib.pyplot as plt
    inner_x = [ point[0] for point in rawdata_inner ]
    inner_y = [ point[1] for point in rawdata_inner ]
    outer_x = [ point[0] for point in rawdata_outer ]
    outer_y = [ point[1] for point in rawdata_outer ]
    
    plt.scatter(inner_x, inner_y, marker="^")
    plt.scatter(outer_x, outer_y, marker="o")

    # show check plots
    #plt.show()
    plt.savefig('check_sideposition.png')

    
    outPoint_orig = ( InnerOneThird(p0,p1) for p0,p1 in zip(innerpoints,outerpoints) )
    outPoint_trans= ( TransformIntoMiniGantry(p) for p in outPoint_orig )
    textOutput = mesgOutput('MiniGantryCoordinate_SidePoint_InnerOneThirdAlgos.txt', mesg)
    textOutput.Write( outPoint_trans )