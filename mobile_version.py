#### Mechanical Engineering Mini Project Loop-the-loop version
#### by David Nagy

Mass = 0.00547 #(kg)
Radius = 0.0158/2.0 #(m)
g = 9.8158 #(m/s^2)

import math


def th_KEtrans(v):
	'''
	(int)-> int

	Return KE translational
	'''

	KE = 0.5*Mass*v**2
	print 'Translational kinetic energy of marble:', round(KE,3), 'joules'
	return KE

def th_KErot(v):
	'''
	(int)-> int

	Return KE rotational
	'''
	KE = 0.2*Mass*v**2 
	print 'Rotational kinetic energy of marble:', round(KE,6), 'joules'
	return KE

def th_height(R):
	'''
	(int) -> int

	Return the sufficient height relative to the lowest point of the loop radius R.
	(meter)
	'''
	v = math.sqrt((R-Radius)*g)
	height = 2.7*R-0.7*Radius
	print 'Height needed for loop the loop:', round(height,3), 'm'
	return height

def th_PE(height):
	'''
	(int)->int

	Return potential energy associated with height and Mass.
	'''
	PE = Mass*g*height
	#print 'Potential energy of the mass at height:', round(PE,3), 'joules'
	return PE

def th_PE_for_loop(R):
	'''
	(int)-> int

	Return the potential energy sufficient to loop the loop in Joules.
	'''

	PE = round(th_PE(th_height(R)),4)
	print 'Potential energy needed:', round(PE,3), 'joules'
	return PE

def falling_time(height):
	'''
	(int) -> int

	Return time of falling.
	'''

	time = math.sqrt((2*height)/float(g))
	velocity = g * time
	print 'Vertical impact velocity:', round(velocity,3), 'm/s'
	print 'Time of falling:', round(time,3), 's'
	return time

def th_velocity(height):
	'''
	(int)->int

	Return velocity of marble rolled from height relative to the end of track. It converts potential energy into kinetic. 
	'''

	
	PE = Mass*g*height

	v = math.sqrt(PE/(0.7*Mass))
	#print 'Velocity from theory:',round(v,3), 'm/s'
	return v


def split_vy(V, angle):
        '''
        (int)-> int
        
        Return vertical velocity Vy from initial velocity V
        '''
        
        
        rad = (angle*math.pi)/180
        Vy = math.sin(rad)*V
        
        #print 'initial vertical velocity =', Vy, 'm/s'
        
        return Vy
        
def split_vx(V, angle):
        '''
        (int)-> int
        
        Return horizontal velocity Vx from initial velocity V
        '''
        
        rad = (angle*math.pi)/180
        Vx = math.cos(rad)*V
        
        #print 'initial horizontal velocity =', Vx, 'm/s'
        
        return Vx
        
def th_initial_velocity(height,sx,angle):
        '''
        (int)-> int
    
        Return the initial velocity of marble at beginning of its trajectory.
        '''
        rad = math.pi*angle/180.0   
        t = math.sqrt(2*(math.tan(rad)*sx+height)/g)
        v = sx / (t*math.cos(rad))
        print 'Initial velocity:',v,'m/s'
        return v 

def th_minimal_distance(R, height, angle):
	'''
	(int)->int

	Return the minimal distance travelled in x direction after marble takes the loop.
	'height' is in y direction.
	'''

	v = th_velocity(th_height(R))
	t = falling_time(height)
	
	print 'Horizonatal velocity:', round(split_vx(v,angle),3), 'm/s'
	print 'Minimal distance travelled:', round(split_vx(v,angle)*t,3), 'm'
	return split_vx(v,angle)*t 
	
def velocity_to_height(velocity):
    '''
    (int)-> int
    
    Return height from marble released accelerates to velocity.
    '''
    
    h = 0.7*velocity**2/g
    
    return h
    
#alma = velocity_to_height(velocity)
#alma = th_minimal_distance(R, height, angle)
#alma = th_initial_velocity(height,sx,angle)
#alma = th_height(R)