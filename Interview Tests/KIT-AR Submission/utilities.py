
# coding: utf-8

# In[ ]:



# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from scipy import stats
from scipy.signal import butter, lfilter, freqz


# In[2]:

def store_label_data(name):
    """ label the data after call the read_data function"""
    all_data = pd.DataFrame()
    for i in range (1,33):
        file_prefix = './data/Trial'
        data = read_data(file_prefix, name, i)

        file_name = file_prefix + str(i) + '/sample' + str(i) + '.csv'
        mark_df = pd.read_csv(file_name,header = None)
        mark_df.columns = ['timestamp','markevent','label']

        for j in range(int(len(mark_df)/2)):
            if mark_df.iloc[2*j,1] == 'screwing_screw-type-1_start_':
                data.loc[data.index[(data.iloc[:,0] > mark_df.iloc[2*j,0]) &
                                    (data.iloc[:,0] < mark_df.iloc[2*j+1,0])],'label'] = 2

            elif mark_df.iloc[2*j,1] == 'screwing_screw-type-1_':
                data.loc[data.index[(data.iloc[:,0] > mark_df.iloc[2*j,0]) &
                                    (data.iloc[:,0] < mark_df.iloc[2*j+1,0])],'label'] = 2

            elif mark_df.iloc[2*j,1] == 'screwing_screw-type-2_start_':
                data.loc[data.index[(data.iloc[:,0] > mark_df.iloc[2*j,0]) &
                                    (data.iloc[:,0] < mark_df.iloc[2*j+1,0])],'label'] = 2

            elif mark_df.iloc[2*j,1] == 'screwing_screw-type-2_start_cannot_seen':
                data.loc[data.index[(data.iloc[:,0] > mark_df.iloc[2*j,0]) &
                                    (data.iloc[:,0] < mark_df.iloc[2*j+1,0])],'label'] = 2

            elif mark_df.iloc[2*j,1] == 'pick_screw-type-1_start_':
                data.loc[data.index[(data.iloc[:,0] > mark_df.iloc[2*j,0]) &
                                    (data.iloc[:,0] < mark_df.iloc[2*j+1,0])],'label'] = 1

            elif mark_df.iloc[2*j,1] == 'pick_screw-type-2_start_':
                data.loc[data.index[(data.iloc[:,0] > mark_df.iloc[2*j,0]) &
                                    (data.iloc[:,0] < mark_df.iloc[2*j+1,0])],'label'] = 1

            elif mark_df.iloc[2*j,1] == 'pick_slider_start_':
                data.loc[data.index[(data.iloc[:,0] > mark_df.iloc[2*j,0]) &
                                    (data.iloc[:,0] < mark_df.iloc[2*j+1,0])],'label'] = 1

            elif mark_df.iloc[2*j,1] == 'pick_slider_':
                data.loc[data.index[(data.iloc[:,0] > mark_df.iloc[2*j,0]) &
                                    (data.iloc[:,0] < mark_df.iloc[2*j+1,0])],'label'] = 1

            elif mark_df.iloc[2*j,1] == 'pick_large-Board_start_':
                data.loc[data.index[(data.iloc[:,0] > mark_df.iloc[2*j,0]) &
                                    (data.iloc[:,0] < mark_df.iloc[2*j+1,0])],'label'] = 1

            elif mark_df.iloc[2*j,1] == 'pick_long-board_start_':
                data.loc[data.index[(data.iloc[:,0] > mark_df.iloc[2*j,0]) &
                                    (data.iloc[:,0] < mark_df.iloc[2*j+1,0])],'label'] = 1

            elif mark_df.iloc[2*j,1] == 'pick_small-metal-part_start_':
                data.loc[data.index[(data.iloc[:,0] > mark_df.iloc[2*j,0]) &
                                    (data.iloc[:,0] < mark_df.iloc[2*j+1,0])],'label'] = 1

            elif mark_df.iloc[2*j,1] == 'place_slider_start_':
                data.loc[data.index[(data.iloc[:,0] > mark_df.iloc[2*j,0]) &
                                    (data.iloc[:,0] < mark_df.iloc[2*j+1,0])],'label'] = 4

            elif mark_df.iloc[2*j,1] == 'place_large-Board_start_':
                data.loc[data.index[(data.iloc[:,0] > mark_df.iloc[2*j,0]) &
                                    (data.iloc[:,0] < mark_df.iloc[2*j+1,0])],'label'] = 4

            elif mark_df.iloc[2*j,1] == 'place_small-metal-part_':
                data.loc[data.index[(data.iloc[:,0] > mark_df.iloc[2*j,0]) &
                                    (data.iloc[:,0] < mark_df.iloc[2*j+1,0])],'label'] = 4

            elif mark_df.iloc[2*j,1] == 'place_small-metal-part_start_':
                data.loc[data.index[(data.iloc[:,0] > mark_df.iloc[2*j,0]) &
                                    (data.iloc[:,0] < mark_df.iloc[2*j+1,0])],'label'] = 4

            elif mark_df.iloc[2*j,1] == 'place_left_panel_start_':
                data.loc[data.index[(data.iloc[:,0] > mark_df.iloc[2*j,0]) &
                                    (data.iloc[:,0] < mark_df.iloc[2*j+1,0])],'label'] = 3

            elif mark_df.iloc[2*j,1] == 'pick_left_panel_start_':
                data.loc[data.index[(data.iloc[:,0] > mark_df.iloc[2*j,0]) &
                                    (data.iloc[:,0] < mark_df.iloc[2*j+1,0])],'label'] = 3

            elif mark_df.iloc[2*j,1] == 'place_long-board_start_':
                data.loc[data.index[(data.iloc[:,0] > mark_df.iloc[2*j,0]) &
                                    (data.iloc[:,0] < mark_df.iloc[2*j+1,0])],'label'] = 4

            else:
                data = data.drop(data.index[(data.iloc[:,0] > mark_df.iloc[2*j,0])
                                            & (data.iloc[:,0] < mark_df.iloc[2*j+1,0])])
#                 print('There is no matched label',mark_df.iloc[2*j,1])
#                 data.loc[data.index[(data.timestamp > mark_df.iloc[2*i,0]) &
#                                     (data.timestamp < mark_df.iloc[2*i+1,0])],'label'] = 5

        all_data = all_data.append(data)
    data = all_data
    data = data.reset_index(drop=True)
    return data


def read_data(file_path, name, j):
    """ read data from each raw dataset according their name, and only read the data from the timestamp
        file sample.csv, other non timestamp duration dataset regard as NULL"""
    valid_value = pd.DataFrame()
    data = pd.read_csv(file_path + str(j) + '/' + name + '.csv',header = None)
    file_name = file_path + str(j) + '/sample' + str(j) + '.csv'
    mark_df = pd.read_csv(file_name,header = None)
    for i in range(int(len(mark_df)/2)):
        values = data[(data.iloc[:,0] > mark_df.iloc[2*i,0]) & (data.iloc[:,0] < mark_df.iloc[2*i+1,0])]
        valid_value = valid_value.append(values)
    valid_value["label"] = np.nan
    return valid_value

def windows(data, window_size):
    """ window size used for define its size and control the overlapping percentage"""
    start = 0
    while start < len(data):
        yield start, start + window_size   # only change window_size to window_size/2 for overlapping 50%
        start += (window_size)


def extract_segments(data, window_size, header):
    """ If overlapping used then this function should be active, not just reshape to get the segaments.
        then the next method extract_labels is not useful."""
    segments = np.empty((0,(window_size)))
    labels = np.empty((0))
    for (start,end) in windows(data,window_size):
        if(len(data.iloc[start:end]) == (window_size)):
            signal = data.iloc[start:end][header]
            segments = np.vstack([segments, signal])
            labels = np.append(labels,stats.mode(data.iloc[start:end]['label'])[0][0])
    return segments, labels

def extract_labels(data, window_size):
    """ Used for non overlap window, return the label get from the last column of pandaframe"""
    labels = np.empty((0))
    for (start,end) in windows(data,window_size):
        if(len(data.iloc[start:end]) == (window_size)):
            labels = np.append(labels,stats.mode(data.iloc[start:end]['label'])[0][0])
    return labels

def get_batches(X, y, batches_size):
    """ Used in the LSTM for batch split
        Return a generator for batches """
    n_batches = len(X)//batches_size
    X = X[:n_batches*batches_size]
    y = y[:n_batches*batches_size]
    # Loop over batches and yield
    for b in range(0,len(X),batches_size):
        yield X[b:b+batches_size], y[b:b+batches_size]


""" lowpass filter for emg and imu """
order = 6
fs = 200.0       # sample rate, Hz
fss = 50.0       # sample rate, Hz
cutoff = 10  # desired cutoff frequency of the filter, Hz
emg_cutoff = 20
# lowcut = 20
# highcut = 40

def butter_lowpass(cutoff, fss, order):
    nyq = 0.5 * fss
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fss, order):
    b, a = butter_lowpass(cutoff, fss, order=order)
    y = lfilter(b, a, data)
    return y

def emg_butter_lowpass(emg_cutoff, fs, order):
    nyq = 0.5 * fs
#     low = lowcut/nyq
#     high = highcut/nyq
    emg_normal_cutoff = emg_cutoff / nyq
    b, a = butter(order, emg_normal_cutoff, btype='low', analog=False) # normal_cutoff
    return b, a

def emg_butter_lowpass_filter(data, emg_cutoff, fs, order):
    b, a = emg_butter_lowpass(emg_cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y
