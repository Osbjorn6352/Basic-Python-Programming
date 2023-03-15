#hw7.py
#Benjamin Osborn

class Volume:
    def __init__(self, vol=0):
        if vol < 0:
            self.v = 0
        elif vol > 11:
            self.v = 11
        else:
            self.v = vol
            
    def __repr__(self):
        return f"Volume({self.v})"
    
    def __eq__(self, other):
        return self.v == other.v
    
    def set(self, vol):
        if vol < 0:
            self.v = 0
        elif vol > 11:
            self.v = 11
        else:
            self.v = vol
            
    def get(self):
        return self.v
    
    def up(self, deltaup):
        if self.v + deltaup > 11:
            self.v = 11
        else:
            self.v = self.v + deltaup
            
    def down(self, deltadown):
        if self.v - deltadown < 0:
            self.v = 0
        else:
            self.v = self.v - deltadown

def partyVolume(file):
    ans = Volume(0)
    with open(file) as infile:
        contents = infile.readlines()
        for line in contents:
            if 'U' in line:
                ans.up(eval(line[1]))
                #ans.up(eval(line.strip('U /n')))
            elif 'D' in line:
                ans.down(eval(line[1]))
                #ans.down(eval(line.strip('D /n')))
            else:
                ans.set(eval(line))
    return ans
                

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw7TEST.py'))
