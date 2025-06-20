import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Operation:
    
    def read_csv(self, file):
        df = pd.read_csv(file)
        