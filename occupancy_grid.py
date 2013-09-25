"""
    Name: occupancy_grid
    Purpose: Create an occupancy grid for Roomba mapping
    Author: Erin
"""
#import matplotlib
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pickle
from pykalman import KalmanFilter
import os


class CreateOccupancyGrid(object):
    
    def __init__(self):
        # Define data point vectors
        self.X = []
        self.Y = []
        self.Z = []
        pass


    def get_data_points(self, map_number):
        """ Return reliable data points, calculated for trustworthiness """
        self.weigh_data_points(map_number)
        pass


    def add_data_point(self, x, y, map_number):
        """ Collect a data point and save it to the map """
        # Data point should be an X, Y tuple and game_number = Z
        # because that will be the 'layer' to help determine the accuracy 
        # of a certain point
        self.X.append(x)
        self.Y.append(y)
        self.Z.append(map_number)
        pass


    def weigh_data_point(self, map_number):
        """ Determine a point's weight """
        # Look @ how many points on that X,Y spot through various Z positions
        # If most recent positions show obstacle, probably obstacle
        #for range(map_number-5, map_number):
            # Find X, Y for that map number...
        #    pass
        # Load up pickles
        X, Y, Z = self.get_pickles()
        # Perform Kalman filters
        # Initial state = 0 because we're starting off at coords 0,0
        kf = KalmanFilter(initial_state_mean = 0, n_dim_obs=2)
        measurements = kf.em(measurements.smooth(measurements)
        # TODO: Deal w/ updating locations
        # means, covars = self.update_data_points(measurements)
        # measurements = means
        # Return data points
        return measurements
        # TODO: The above should be in localization


    def update_data_point(self, measurements):
        """ Determine newest data points """
        # TODO: Move to localization
        means, covariances = kf.filter(measurements)
	next_mean, next_covariance = kf.filter_update(
	    means[-1], covariances[-1], new_measurement)
        return means, covariances
    

    def get_pickles(self):
        """ Get any relevant pickles, load into lists and return """
        # Get pwd
        # Get all pickles in the current folder
        X = []
        Y = []
        Z = []
        pwd = os.system('pwd')
        pickles = os.path.walk(pwd)
        for p in pickles:
            if p.endswith('pkl'):
		opened_pickle = pickle.load(open(p, "rb"))
		X.append(opened_pickle['X'])
		Y.append(opened_pickle['Y'])
		Z.append(opened_pickle['Z'])
        return X, Y, Z


    def home_safe(self, map_number):
        """ When the Roomba reaches home base, pickle data """
        name = "pickle_%s.pkl", map_number
        dictionary = {'X': self.X, 'Y', self.Y, 'Z', self.Z}
        pickle.dump(dictionary, open(name, "wb")


    def create_map(self):
        """ Return a reliable map """
        self.get_data_points()
        # Put map into Matplotlib, return chart & data
        # Return map
	fig = plt.figure()
	ax = fig.gca(projection='3d')
        #X = np.array([[-30,  -20], [30, -20]])
        #Y = np.array([[-30, -30], [30, -30]])
        #Z = np.array([[ 0, 0], [5, 5]])
        # Turn the list of lists into numpy arrays to submit to the 3D plot
        fullX, fullY, fullZ = self.get_pickles()
        X = np.array(fullX)
        Y = np.array(fullY)
        Z = np.array(fullZ)
        print "X: ", X
        print "Y: ", Y
        print "Z: ", Z
	ax.scatter3D(X, Y, Z)

	ax.set_xlabel('X')
	ax.set_xlim(-40, 40)
	ax.set_ylabel('Y')
	ax.set_ylim(-40, 40)
	ax.set_zlabel('Z')
	ax.set_zlim(-100, 100)

	plt.show()
        print "Showing plot"
        pass

