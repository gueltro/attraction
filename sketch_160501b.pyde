from math import cos,sin,pi
dt = .01

class Particle():
  def __init__(self, x, y):
      self.x = x
      self.y = y
      self.dx = 0
      self.dy = 0
      self.lover = None
      
  def insert_lover(self):
    self.lover = lover

  def update_speed(self):
    lover = self.lover
    distance = [self.lover.x - self.x, self.lover.y - self.y]
    distance_magnitude = (distance[0] ** 2 + distance[1] ** 2) ** .5
    self.dx = distance[0] / distance_magnitude
    self.dy = distance[1] / distance_magnitude
  
  def update_location(self):
      strokeWeight(10)
      print "yo"
      line(self.x, self.y, self.x +  self.dx *  dt, self.y + self.dy  * dt )
      self.x += self.dx *  dt
      self.y += self.dy  * dt
  
  def drawit(self):
      ellipse(200 + 100 *self.x, 100 + 100 * self.y,1,1)
  
class Universe():
    def __init__(self):
        self.particles = []
    
    def insert_particle(self, angle):
        p = Particle(cos(angle), sin(angle))
        self.particles.append(p)
        
        #assign s
        prev_index = max(len(self.particles) - 2, 0)
        pp = self.particles[prev_index]
        p.lover = self.particles[0]
        pp.lover = p
        
    def insert_ngon(self,n):
        for i in range(n):
            self.insert_particle( i * 2 * pi / n)
        
    def update(self):
        for p in self.particles:
            p.update_speed()
        
        for p in self.particles:
            p.update_location()
            # p.drawit()


size(320, 240)
background(100)
u = Universe()
u.insert_ngon(4)


ellipse(200, 100, 200, 200)
for i in range(5100):
    u.update()