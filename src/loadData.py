import scipy.io as sio
import numpy as np

reflectValuesPath = '../data/Indian_pines_corrected.mat'
trainDataPath = '../data/train_data.npy'
testDataPath = '../data/test_data.npy'

print('Loading data')

reflectValues = sio.loadmat(reflectValuesPath)
trainData = np.load(trainDataPath)
testData = np.load(testDataPath)

print('Data loaded with success')

print(reflectValues)
#print(trainData)
#print(trainData.size)