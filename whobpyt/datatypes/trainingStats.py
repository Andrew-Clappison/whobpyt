import numpy as np


class trainingStats:
    """
        This class is responsible for recording stats during training including:
            - The training and validation losses over time
            - The change in parameters over time
            - changing hyperparameters over time like learing rates
            
        These are things typically recorded on a per epoch basis
        
    """

    def __init__(self, model_info):        
        model_info = model_info
        
        self.train_loss = []
        self.val_loss = []
        
        self.model_pars = {}
        self.hyper_pars = {}

    def appendTL(self):
        """ Append Hyper Parameters """
        
    def appendVL(self):
        """ Append Hyper Parameters """    

    def appendMP(self):
        """ Append Hyper Parameters """    

    def appendHP(self):
        """ Append Hyper Parameters """
        