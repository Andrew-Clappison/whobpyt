# A fundamental datastructure that is a common output and input format to various whobpyt classes
# This can contain either empirical or simulated time series

import numpy as np

class timeSeries:
    """    
        This class is responsible for holding timeseries of empirical or simulated data
            - Info about step size, length, modailty, dimension
            - The time series of model state variables
            - The time series of modality variables (EEG, fMRI)
                
        time series stored dict of: num_regions x time_steps (May want to change this later)
     
    """
    
    def __init__(self, names, step_size, numRegions):
        self.names = names #The list of names for: EEG, BOLD, or state_names
        self.step_size = 0
        self.numRegions = 0
        
        self.ts = {}
    
    def resample(self):
        pass
        
    def iterator(self):
        pass
        
    def getTS(self, name):
        return self.ts[name]
        
    def npTS(self):
        pass
        
    def reset(self):
        self.ts = {}
        
    def append(self, section, suffix = ''):
        if (self.ts == {}):
            for name in self.names:
                source_name = name + suffix
                self.ts[name] = section[source_name].detach().numpy()
        else:
            for name in self.names:
                source_name = name + suffix
                self.ts[name] = np.append(self.ts[name], section[source_name].detach().numpy(), axis = 1)
    