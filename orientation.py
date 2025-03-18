from data import df, id_to_body, csv_to_df
from config import cal_file_name
from scipy.spatial.transform import Rotation
import numpy as np

##=========================== Orientation ===========================##
def get_body_quaternions(df)->dict: #{body: [quaternion]}
    body_quaternions = {}
    for _, row in df.iterrows():
        part = id_to_body[row['ID']]
        quat = (row['Quaternion w'], row['Quaternion x'], row['Quaternion y'], row['Quaternion z'])
        if part not in body_quaternions:
            body_quaternions[part] = []
        body_quaternions[part].append(quat) # Each body part has its own quat values
    return body_quaternions

body_quaternions = get_body_quaternions(df)


# Building oriantation
t = 0
dt = 1

num_rows = len(next(iter(body_quaternions.values())))

with open("oriantation.sto", 'w') as f:
    f.write("DataRate=200.000000\n")
    f.write("DataType=Quaternion\n")
    f.write("version=3\n")
    f.write("OpenSimVersion=4.4-2022-07-23-0e9fedc\n")
    f.write("endheader\n")
    
    # Write header: "time" followed by each body part name
    header = '\t'.join(["time"] + list(body_quaternions.keys()))
    f.write(header + "\n")
    
    # Write each row of data
    for i in range(num_rows):
        # Start each line with the current time value
        row = [str(t)]
        
        # For each body part, get the i-th quaternion and format it as a comma-separated string
        for body in body_quaternions.keys():
            q = body_quaternions[body][i]
            q_str = f"{q[0]},{q[1]},{q[2]},{q[3]}"
            row.append(q_str)
        
        # Join the row values with a tab and write to file
        f.write('\t'.join(row) + "\n")
        t += dt
        # print(i)




##=========================== Calibration ===========================##
cal_df = csv_to_df(cal_file_name)
cal_quat = get_body_quaternions(cal_df)

mean_cal_quat = {}
for key, value in cal_quat.items():
    mean = Rotation.from_quat(value).mean().as_quat() # Calculate the mean
    mean_cal_quat.setdefault(key, []).append(mean)    # Add to the dict



# Building oriantation_calib
t = 0
with open("oriantation_calib.sto", 'w') as f:
                    f.write("DataRate=200.000000\n")
                    f.write("DataType=Quaternion\n")
                    f.write("version=3\n")
                    f.write("OpenSimVersion=4.4-2022-07-23-0e9fedc\n")
                    f.write("endheader\n")
                    f.write('\t'.join(["time"] + list(mean_cal_quat.keys())))
                    f.write('\n')
                    f.write(str(t))
                    for key in mean_cal_quat:
                        f.write('\t')
                        f.write(f"{mean_cal_quat[key][0][0]}, {mean_cal_quat[key][0][1]}, {mean_cal_quat[key][0][2]}, {mean_cal_quat[key][0][3]}")
