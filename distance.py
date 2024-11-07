import pandas as pd
import matplotlib.pyplot as plt

#reading data
file_path = '/Users/diyapottangadi/Desktop/User-1-experimental.csv'
data = pd.read_csv(file_path)
data.columns = data.columns.str.strip()

#initializing body parts with columns
body_parts = ['CHip', 'Spine', 'CShoulder', 'Head', 'LShoulder', 'LElbow', 'LWrist', 'LHand', 
              'RShoulder', 'RElbow', 'RWrist', 'RHand', 'LHip', 'LKnee', 'LAnkle', 'LFoot',
              'RHip', 'RKnee', 'RAnkle', 'RFoot']

#computing distance            
def compute_distance(row):
    x_diff = row['LShoulder_x'] - row['RShoulder_x']
    y_diff = row['LShoulder_y'] - row['RShoulder_y']
    z_diff = row['LShoulder_z'] - row['RShoulder_z']
    return (x_diff**2 + y_diff**2 + z_diff**2) ** 0.5

first_frame = data.iloc[0]
shoulder_distance = compute_distance(first_frame)

#output
print(f"Distance between left and right shoulder in the first frame: {shoulder_distance}")