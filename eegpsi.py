import pyeeg
import numpy
import pandas

def Calc_AlphaPSI(array):
    Band = [0.5,4,7,12,30]
    Fs = 1024 
    lst=[]
    num_rows,num_cols = array.shape
    for i in range(int(num_rows/1024)):
        for j in range((num_cols)):
            psi = pyeeg.bin_power(array[i*1024:(i+1)*1024,j],Band,Fs)
            lst.append(psi[0][2])
    lst_reshaped = numpy.reshape(lst,(-1,34))
    AlphaPSI_df = pandas.DataFrame(lst_reshaped)
    return AlphaPSI_df    
