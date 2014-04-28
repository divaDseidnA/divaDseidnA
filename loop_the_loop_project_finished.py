#### Mechanical Engineering Mini Project Loop-the-loop version (2014 Spring)
#### by David Nagy

Mass = 0.00547 #(kg)
Radius = 0.0158/2.0 #(m)
g = 9.8158 #(m/s^2)

import matplotlib 
import numpy
import math
import matplotlib.pyplot

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
                        
def r_trajectory(velocity,height_of_track,angle):
	'''
	(int)-> plot

	Return plot of trajectory of marble.
	'''
        
	x = []
	y = []
	x1 = []
	l = []
        
	b = -split_vy(velocity,angle)
	a = 0.5*g
	c = -height_of_track

	fall_time = (-b+math.sqrt(b**2-4*a*c))/float(2*a)

	for time in numpy.arange(0,fall_time,0.0001):
		x.append((split_vx(velocity, angle)*time)*100)
		x1.append((split_vx(velocity, angle)*time)*100)
		y.append((split_vy(velocity,angle)*time+height_of_track-0.5*g*time**2)*100)
		l.append(0)
        
        fig = matplotlib.pyplot.figure()
        ax = fig.add_subplot(111)
    
	matplotlib.pyplot.annotate('Height of release '+str(height_of_track*100)+' cm', xy=(x[0], y[0]),  xycoords='data',
               xytext=(x[3]-1/3.0*x[3],y[3]-1/3.0*y[3]), textcoords='data', 
               arrowprops=dict(arrowstyle="->"),
               )
	#matplotlib.pyplot.annotate('Impact point', xy=(x[-1], y[-1]),  xycoords='data',
        #      xytext=(x[-3]-1/3.0*x[-3],y[-3]+1/3.0*y[-3]), textcoords='data', arrowprops=dict(arrowstyle="->"),
        #       )
               
        matplotlib.pyplot.annotate('Ground', xy=(x[len(x)/2],-height_of_track),  xycoords='data',
               xytext=(x[len(x)/2]-5.0*x[10],y[10]*1/4.0), textcoords='data', arrowprops=dict(arrowstyle="->"),
               )
        
        x_distance = round(abs(x[-1]-x[0]),2)
               
        matplotlib.pyplot.annotate('s = '+ str(x_distance)+' cm', xy=(x[-1], y[-1]),  xycoords='data',
               xytext=(4*x[len(x)/5],-y[len(y)/3]/5), textcoords='data', arrowprops=dict(arrowstyle="->"),
               )
    
	matplotlib.pyplot.axis('equal')
	matplotlib.pyplot.plot(x,y,'ro')
        matplotlib.pyplot.plot(x1,l,'g-')
	matplotlib.pyplot.xlabel('Distance [cm]')
	matplotlib.pyplot.ylabel('Height [cm]')
	matplotlib.pyplot.title('Trajectory of marble (m = '+str(Mass*1000)+'g, r = '+str(Radius*1000)+'mm,' + 'v = '+str(round(velocity,2))+'m/s)')

	matplotlib.pyplot.show()
	
def find_original_height(velocity):
        '''
        (int) -> int
        
        Return the height needed to reach velocity.
        '''
        
        high = 1000*velocity
        low = 0
        guess = (high+low) / 2.0
        epsilon = 0.000000001
        
        while abs(th_velocity(guess)-velocity) > epsilon: 
            if th_velocity(guess) > velocity:
                high = guess
                guess = (high+low) / 2.0
            else:
                low = guess
                guess = (high+low) / 2.0
        
        print 'Height needed to reach velocity: ',guess, 'm'
        return guess

def main():
    '''
    Handle of these functions.
    
    Expectations:
    Height of the end of track relative to target. 
    Measure_height is given relative to the end of track. 
    Height of release is given relative to the end of track.
    '''       

    height_of_track_str = raw_input('Height of edge (m):')
    sx_str = raw_input('Travelled distance in x direction (m):')
    angle_str = raw_input('Angle of elevation (deg):')
    measured_height_str = raw_input('Measured height of release (m): ')
    
    measured_height = float(measured_height_str)
    height_of_track = float(height_of_track_str)
    sx = float(sx_str)
    angle = float(angle_str)
    measured_height = float(measured_height_str)
    rad = math.pi * angle /180.0
    
    print '-----------------'
    
    velocity = th_initial_velocity(height_of_track,sx,angle)
    height = find_original_height(velocity)
    print '-----------------'
    print 'Height of release from theory: ',round(height,4),'m'
    print 'Velocity of marble at beginning of its trajectory: ',round(velocity,2),'m/s'
    print 'Per cent of energy being lost on track: ', round(100-(height/measured_height*100),2), '%'
    print 'Height from theory has to be multiplied by ', round(measured_height/height,3)
    r_trajectory(velocity,height_of_track,angle)

def velocity_to_height(velocity):
    '''
    (int)-> int
    
    Return height from marble released accelerates to velocity.
    '''
    
    h = 0.7*velocity**2/g
    
    return h
    
    
'''
Available functions:

	th_KEtrans(v)
	th_KErot(v)
	th_height(R)
	th_PE(height)
	th_PE_for_loop(R)
	falling_time(height)
	th_minimal_distance(R, height)
	th_velocity(height) 
	th_trajectory(height,height_of_track)
	split_vy(V, angle)
	split_vx(V, angle)
	th_initial_velocity(height,sx,angle)
	r_trajectory(velocity,height_of_track,angle)
	find_original_height(velocity)
	main()
	velocity_to_height(velocity)

	
'''
#r_trajectory(1.9,0.11,0)