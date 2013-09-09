"""
    Name: run_roomba.py
    Purpose: Handle all calls to other classes to run the Roomba
             on its house-mapping quest
    Author: Erin
"""

#from occupancy_grid import CreateOccupancyGrid
#from kalman_filters import CreateKalmanFilters 
#from landmark_a_star import CreateRoombaPath
import pyrobot
import time

# TODO: everything in Main needs to be run continuously
# TODO: Wall-following should be moved to mapping soon

def back_up_from_base(r):
    """ Back up a few inches from base """
    r.Drive(-50, -200)
    print "Back up from base!"
    time.sleep(3)

def find_a_wall(r):
    """ Drive until we hit some sensor """
    s = refresh_sensors(r)
    while True:
        if s.data['wall']: break
        #if s.data['bump-right']: break
        r.Drive(50, -200)
        time.sleep(1)
        r.DriveStraight(50)
        time.sleep(3)
        print "Wall finding"
	s = refresh_sensors(r)
 
    print "Found something!"
    return r.sensors.data

def continue_on_wall(r):
    """ Follow the found wall until a corner is hit """
    s = refresh_sensors(r)
    while (s.data['wall'] and
           not s.data['bump-right']):# and
           #not s.data['bump-left']):
        r.DriveStraight(50)
        r.sensors.GetAll()
	s = refresh_sensors(r)
        print "Following wall"

def print_sensors(s):
    """ Print wall, right and left sensors """
    print "Wall: %s" % s.data['wall']
    print "Right: %s" % s.data['bump-right']
    print "Left: %s" % s.data['bump-left']

def turn_corner(r):
    """ Turn 90 degrees to the left """
    print "Turning a corner "
    # TODO: In the future, have globals specifying
    # the velocity/time for a turn
    r.TurnInPlace(50, 'ccw')
    time.sleep(4.3)
    r.Stop()

def turn_and_drive(r, rad):
    """ Turn the specified amount and drive """
    print "Turning and driving "
    r.Drive(50, rad)
    find_a_wall(r)

def refresh_sensors(r):
    """ Clear sensors and get fresh data """
    r.sensors.Clear()
    r.sensors.GetAll()
    return r.sensors

def follow_walls(r):
    """ Follow some walls! """
    r.Control()
    s = refresh_sensors(r)
    back_up_from_base(r)
    for x in range(0, 20):
        sensor_input = find_a_wall(r)
        print "Found a wall!"
        if sensor_input['bump-right'] and sensor_input['bump-left']:
            turn_corner(r)
        elif sensor_input['bump-right']:
            # back up a bit and turn left
            r.Drive(50, -300)
            time.sleep(2)
            pass
        # TODO: Find Roomba w/ working Left sensor, or clean this one
        elif sensor_input['bump-left']:
            turn_and_drive(r, 300)
            pass
        elif sensor_input['wall']:
            continue_on_wall(r)
    r.Stop()

if __name__ == "__main__":
    # create Roomba
    r = pyrobot.Roomba()
    follow_walls(r)
    #grid = CreateOccupancyGrid.create_map()
    #location = CreateKalmanFilters.locate_roomba(grid)
    #path = CreateRoombaPath.plan_path(grid, location)
    
    

