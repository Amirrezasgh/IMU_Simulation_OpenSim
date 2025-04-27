
import threading
import queue
import time
import random  
import opensim as osim
import os
import threading
import data
from config import file_name

os.add_dll_directory("C:/OpenSim 4.4/bin")  
# model_path = "c:/Users/R/Documents/OpenSim/4.4/Models/Tug_of_War/Tug_of_War_Millard.osim"
model_path = r"C:\Users\R\Desktop\worksp\Fum_care_project\source code\IMU_Simulation_OpenSim\Rajagopal_2015.osim"
imu_data_queue = queue.Queue()


def IMU_data(file_name):
    df = data.csv_to_df(file_name)
    # print("hi")
    # print(df)


def run_opensim_model(model_path):
   
    model = osim.Model(model_path)
    model.setUseVisualizer(True)
    state = model.initSystem()
    model.getVisualizer().show(state)
    visualizer = model.getVisualizer()
    visualizer.getSimbodyVisualizer().setShowSimTime(True)

t1=threading.Thread(target=run_opensim_model,args=(model_path,))
t2=threading.Thread(target=IMU_data,args=(file_name,))
# run_opensim_model()
t1.start()
t2.start()