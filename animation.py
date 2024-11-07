import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#reading data
file_path = '/Users/diyapottangadi/Desktop/User-1-experimental.csv'
data = pd.read_csv(file_path)
data.columns = data.columns.str.strip()

#initializing body parts with columns
body_parts = ['CHip', 'Spine', 'CShoulder', 'Head', 'LShoulder', 'LElbow', 'LWrist', 'LHand', 
              'RShoulder', 'RElbow', 'RWrist', 'RHand', 'LHip', 'LKnee', 'LAnkle', 'LFoot',
              'RHip', 'RKnee', 'RAnkle', 'RFoot']

#figure for animation
fig, ax = plt.subplots(figsize=(8, 8))

#updating frames
def update(frame_number):
    ax.clear()
    frame_data = data[data['Movement'] == frame_number]
    
    for part in body_parts:
        x_col = f'{part}_x'
        y_col = f'{part}_y'
        ax.scatter(frame_data[x_col], frame_data[y_col])

    connections = [
        ('CHip', 'Spine'), ('Spine', 'CShoulder'), ('CShoulder', 'Head'),
        ('CShoulder', 'LShoulder'), ('LShoulder', 'LElbow'), ('LElbow', 'LWrist'), ('LWrist', 'LHand'),
        ('CShoulder', 'RShoulder'), ('RShoulder', 'RElbow'), ('RElbow', 'RWrist'), ('RWrist', 'RHand'),
        ('CHip', 'LHip'), ('LHip', 'LKnee'), ('LKnee', 'LAnkle'), ('LAnkle', 'LFoot'),
        ('CHip', 'RHip'), ('RHip', 'RKnee'), ('RKnee', 'RAnkle'), ('RAnkle', 'RFoot')
    ]
    for start, end in connections:
        ax.plot(
            [frame_data[f'{start}_x'].values[0], frame_data[f'{end}_x'].values[0]],
            [frame_data[f'{start}_y'].values[0], frame_data[f'{end}_y'].values[0]],
            'bo-'
        )
    
    ax.set_title(f'Frame {frame_number}')
    ax.invert_yaxis()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

#loading animation
ani = animation.FuncAnimation(fig, update, frames=data['Movement'].unique(), repeat=False)
plt.show()
