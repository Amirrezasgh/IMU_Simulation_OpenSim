import os
os.add_dll_directory("D:/OpenSim 4.4/bin")  # Add the OpenSim DLL directory
import opensim as osim

import numpy as np
import pandas as pd
import time
import math
from datetime import datetime

from data import df
from config import joint_name

with open("orientation.py") as f: # Creating oriantation.sto and oriantation_calib.sto
    exec(f.read()) # Execute orientation.py

# === Calibration using IMUPlacer ===
imuPlacer = osim.IMUPlacer()
imuPlacer.set_model_file('Rajagopal_2015.osim')
imuPlacer.set_orientation_file_for_calibration("oriantation_calib.sto")
imuPlacer.set_sensor_to_opensim_rotations(osim.Vec3(0, 0, 0))
imuPlacer.set_base_imu_label('pelvis_imu')
imuPlacer.set_base_heading_axis('z')
imuPlacer.run(False)
model = imuPlacer.getCalibratedModel()
model.printToXML('calibrated_Rajagopal_2015.osim')
model = osim.Model('calibrated_Rajagopal_2015.osim')

# === Create OrientationsReference from oriantation.sto ===
quatTable = osim.TimeSeriesTableQuaternion("oriantation.sto")
orientationsData = osim.OpenSenseUtilities.convertQuaternionsToRotations(quatTable)
oRefs = osim.OrientationsReference(orientationsData)
mRefs = osim.MarkersReference()
coordinateReferences = osim.SimTKArrayCoordinateReference()

# Enable the visualizer so the model is shown in 3D.
model.setUseVisualizer(True)
state = model.initSystem()

# === Set up the Inverse Kinematics Solver ===
ikSolver = osim.InverseKinematicsSolver(model, mRefs, oRefs, coordinateReferences, 10)
ikSolver.setAccuracy(1e-3)

# Get the time vector from the orientation table.
times = quatTable.getIndependentColumn()
numFrames = len(times) // 5
print("Animating %d frames." % numFrames)

# === Animate the Model ===
# Loop through each time step in the orientation data, update state, run IK, update the visualizer and update the joint angles.
joint_angle = {}

try:
    for i in range(numFrames):
        t = times[i*5]
        state.setTime(t)
        ikSolver.assemble(state)
        # Update the visualizer to show the current state.
        model.getVisualizer().show(state)
        model.getVisualizer().getSimbodyVisualizer().setShowSimTime(True)
    #########################################################################################
        # Get the JointSet from the model.
        jointSet = model.getJointSet()

        # Loop through every joint in the set.
        for i in range(jointSet.getSize()):
            joint = jointSet.get(i)
            
            # Loop through all coordinates for this joint.
            for j in range(joint.numCoordinates()):
                coord = joint.get_coordinates(j)
                if coord.getName() in joint_name:
                    angle = coord.getValue(state)
                    # print("   Coordinate:", coord.getName(), "Angle:", angle)
                    joint_angle.setdefault(coord.getName(), []).append(angle) ## coordination name: angle ## 
except Exception as e:
    print(f"Error at frame {i}: {e}") 


now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output = pd.DataFrame(joint_angle)
output.to_csv(f"Outputs/Joint_Angles_{now}.csv")