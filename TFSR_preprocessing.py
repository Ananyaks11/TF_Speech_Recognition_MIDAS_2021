import os
import librosa
import numpy as np
from sklearn.model_selection import train_test_split

path = "./train2/"
print("The data path is:", path)

# def wav2specgram(file_path):
#     samples, sample_rate = librosa.load(file_path, mono=True, sr=None)
#     samples = librosa.resample(samples, sample_rate, 8000)
#     if(len(samples)== 8000):

# Function to produce train and validation set
def Get_Data(split_ratio=0.9, random_state=42):
    
    X = np.load("data_X.npy")
    Y = np.load("data_Y.npy")

    return train_test_split(X, Y, test_size= (1 - split_ratio), random_state=random_state, shuffle=True)

# Function to convert WAV file to MFCC
def wav2mfcc(file_path, n_mfcc=20, sample_size=11):
    wave, sr = librosa.load(file_path, mono=True, sr=None)
    wave = np.asfortranarray(wave[::3])
    mfcc = librosa.feature.mfcc(wave, sr=16000, n_mfcc=n_mfcc)

    # If maximum length exceeds mfcc lengths then pad the remaining ones
    if (sample_size > mfcc.shape[1]):
        pad_width = sample_size - mfcc.shape[1]
        mfcc = np.pad(mfcc, pad_width=((0, 0), (0, pad_width)), mode='constant')

    # Else cutoff the remaining parts
    else:
        mfcc = mfcc[:, :sample_size]
    
    return mfcc

# Function to produce npy files from the given raw dataset files
def Make_data_matrix(path=path, sample_size=11, n_mfcc=20):
    labels = os.listdir(path)

    for label in labels:
        print(label)
        vectors = []
        wavfiles = [path + label + '/' + wavfile for wavfile in os.listdir(path + '/' + label)]
        
        for wavfile in wavfiles:
            mfcc = wav2mfcc(wavfile, sample_size=sample_size, n_mfcc=n_mfcc)
            vectors.append(mfcc)
        
        np.save(label + '.npy', vectors)
    
    # Getting first arrays
    X = np.load(labels[0] + '.npy')
    y = np.zeros(X.shape[0])

    # Append all of the dataset into one single array, same goes for y
    for i, label in enumerate(labels[1:]):
        x = np.load(label + '.npy')
        X = np.vstack((X, x))
        y = np.append(y, np.full(x.shape[0], fill_value= (i + 1)))
    
    np.save("data_X.npy", X)
    np.save("data_Y.npy", y)

