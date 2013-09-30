"""
    Name: run_roomba.py
    Purpose: Handle all calls to other classes to run the Roomba
             on its house-mapping quest
    Author: Erin
"""

from occupancy_grid import CreateOccupancyGrid
#from kalman_filters import CreateKalmanFilters 
#from landmark_a_star import CreateRoombaPath
import pyrobot
import time

# TODO: everything in Main needs to be run continuously
# TODO: Wall-following should be moved to mapping soon

# I know how horrible this is :( 
# TODO: Move wall following to a proper Mapping class
grid = CreateOccupancyGrid()
grid_roomba = CreateOccupancyGrid()

def back_up_from_base(r):
    """ Back up a few inches from base """
    r.Drive(-200, -25)
    print "Back up from base!"
    time.sleep(2)
    find_grid_marks(-200, -25, 2, 'Roomba')

def find_a_wall(r):
    """ Drive until we hit some sensor """
    s = refresh_sensors(r)
    while True:
        if s.data['wall']: break
        if s.data['bump-right']: break
        if s.data['bump-left']: break
        r.Drive(200, -500)
        time.sleep(1)
        find_grid_marks(200, -500, 1, 'Roomba')
        r.DriveStraight(200)
        time.sleep(3)
        find_grid_marks(200, None, 3, 'Roomba')
        print "Wall finding"
	s = refresh_sensors(r)
	print_sensors(s)
 
    print "Found something!"
    return r.sensors.data

def continue_on_wall(r):
    """ Follow the found wall until a corner is hit """
    s = refresh_sensors(r)
    while (s.data['wall'] and
           not s.data['bump-right'] and 
           not s.data['bump-left']):
        r.DriveStraight(200)
        find_grid_marks(200, None, None, 'Roomba')
        r.sensors.GetAll()
	s = refresh_sensors(r)
        print "Following wall"
        print_sensors(s)

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
    r.TurnInPlace(200, 'ccw')
    time.sleep(3)
    # TODO: Acocunt for turn direction
    find_grid_marks(200, 100, 3, 'Obstacle')
    r.Stop()

def turn_and_drive(r, rad):
    """ Turn the specified amount and drive """
    print "Turning and driving "
    r.Drive(200, rad)
    find_grid_marks(200, rad, None, 'Roomba')
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
    print_sensors(s)
    back_up_from_base(r)
    for x in range(0, 20):
        sensor_input = find_a_wall(r)
        print "Found a wall!"
        if (sensor_input['wall'] and 
            not sensor_input['bump-right'] and
            not sensor_input['bump-left']):
            continue_on_wall(r)
        elif sensor_input['bump-right'] and sensor_input['bump-left']:
            turn_corner(r)
        elif sensor_input['bump-right']:
            print "Hit right sensor-- turning..."
            # back up a bit and turn left
            r.Drive(200, 100)
            time.sleep(2)
            find_grid_marks(200, 100, 2, 'Obstacle')
        elif sensor_input['bump-left']:
            print "Hit left sensor-- turning..."
            #turn_and_drive(r, 50)
            r.Drive(200, -100)
            time.sleep(2)
            find_grid_marks(200, -100, 2, 'Obstacle')
        elif sensor_input['wall']:
            continue_on_wall(r)
    r.Stop()

def find_grid_marks(drive_time, drive_radius=None, sleep=None, roomba='Roomba'):
    """ Return probable map point """
    # TODO: I clearly had no idea what I was doing here and 
    # should figure out the math to actually allow for variations
    # TODO: Account for Roomba size
    last_x = grid.X
    last_y = grid.Y
    # Must fix to get grid from proper location-- Roomba grid or obstacle grid
    # Should those even be separate?
    # TODO: This math is all wrong and simply being brought back to basics
    # to try to figure out metric for new Roomba
    x = last_x + drive_time*sleep
    if drive_radius > 0:
        y = last_y + drive_radius*sleep
    else:
        y = last_y - drive_radius*sleep
    
    if roomba == 'Roomba':
        map_roomba_place(x, y)
    elif roomba == 'Obstacle':
        map_obstacle_place(x, y)
    return

def map_roomba_place(x, y):
    """ Send points to map for Roomba's theoretical location """
    z = find_map_number()
    grid_roomba.add_data_point(x, y, z)
    pass

def map_obstacle_place(x, y):
    """ Sent points to map to represent Roomba's hits """
    z = find_map_number()
    grid.add_data_point(x, y, z)
    pass

def find_map_number():
    """ Return the map number """
    return 1 # TODO: Make this a real number

if __name__ == "__main__":
    # create Roomba
    r = pyrobot.Roomba()
    follow_walls(r)
    find_map_number()
    #grid = CreateOccupancyGrid.create_map()
    #location = CreateKalmanFilters.locate_roomba(grid)
    #path = CreateRoombaPath.plan_path(grid, location)
    
    

