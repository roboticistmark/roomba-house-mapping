"""
    Name: run_roomba.py
    Purpose: Handle all calls to other classes to run the Roomba
             on its house-mapping quest
    Author: Erin
"""

import CreateOccupancyGrid from occupancy_grid
import CreateKalmanFilters from kalman_filters
import CreateRoombaPath from landmark_a_star

# TODO for next week:
# import pyserial, roomba modules
# create roomba (for real), add wall-following as first
# step in occupancy grid data collection
# TODO: everything in Main needs to be run continuously

if __name__ == "__main__":
    # create Roomba
    grid = CreateOccupancyGrid.create_map()
    location = CreateKalmanFilters.locate_roomba(grid)
    path = CreateRoombaPath.plan_path(grid, location)
    
    

