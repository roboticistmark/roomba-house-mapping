"""
    Name: occupancy_grid
    Purpose: Create an occupancy grid for Roomba mapping
    Author: Erin
"""
#import matplotlib
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

class CreateOccupancyGrid(object):
    
    def __init__(self):
        # Define data point vectors
        self.X = []
        self.Y = []
        self.Z = []
        pass


    def get_data_points(self):
        """ Return reliable data points, calculated for trustworthiness """
        pass


    def add_data_point(self, data_point, map_number):
        """ Collect a data point and save it to the map """
        # Data point should be an X, Y tuple and game_number = Z
        # because that will be the 'layer' to help determine the accuracy 
        # of a certain point
        # Format: X = [[1,2,3,4], [1,2,3,4]] etc
        self.X.(len(self.X)-1).append(data_point[0])
        self.Y.(len(self.Y)-1).append(data_point[0])
        self.Z.(len(self.X)-1).append(map_number)
        pass


    def weigh_data_point(self, map_number):
        """ Determine a point's weight """
        # Look @ how many points on that X,Y spot through various Z positions
        # If most recent positions show obstacle, probably obstacle
        for range(map_number-5, map_number):
            # Find X, Y for that map number...
            pass
        pass


    def create_map(self):
        """ Return a reliable map """
        # TODO: After experimenting, this is not actually the plot I want to use..
        # a scatter plot would be more appropriate. To be implemented
        # ASAP when I return home and have proper internet/access to docs again
        self.get_data_points()
        # Put map into Matplotlib, return chart & data
        # Return map
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	X, Y, Z = axes3d.get_test_data(5)
	#X, Y, Z = axes3d.get_test_data(0.05)
        #X = [[-1.1 -2.1 -3.1 -4.1 -5.1 -5.1 -5.1 -5.1 -5.1 -5.1][-1.1 -2.1 -3.1 -4.1 -5.1 -5.1 -5.1 -5.1 -5.1 -5.1][-1.1 -2.1 -3.1 -4.1 -5.1 -5.1 -5.1 -5.1 -5.1 -5.1][-1.1 -2.1 -3.1 -4.1 -5.1 -5.1 -5.1 -5.1 -5.1 -5.1]]
        #Y = [[3.1 3.1 3.1 3.1 3.1 2.1 1.1 0.1 -1.1 -2.1][3.1 3.1 3.1 3.1 3.1 2.1 1.1 0.1 -1.1 -2.1][3.1 3.1 3.1 3.1 3.1 2.1 1.1 0.1 -1.1 -2.1][3.1 3.1 3.1 3.1 3.1 2.1 1.1 0.1 -1.1 -2.1]]
        #Z = [[0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1][1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1][2.1 2.1 2.1 2.1 2.1 2.1 2.1 2.1 2.1 2.1][3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1]]
        X = [[-30,  -20], [30, -20]]
        Y = [[-30, -30], [30, -30]]
        Z = [[ 0, 0], [5, 5]]
        print "X: ", X
        print "Y: ", Y
        print "Z: ", Z
	ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
	cset = ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
	cset = ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
	cset = ax.contourf(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)

	ax.set_xlabel('X')
	ax.set_xlim(-40, 40)
	ax.set_ylabel('Y')
	ax.set_ylim(-40, 40)
	ax.set_zlabel('Z')
	ax.set_zlim(-100, 100)

	plt.show()
        print "Showing plot"
        pass

