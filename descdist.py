import pandas as pd

from rpy2.robjects import pandas2ri
from rpy2.robjects.packages import importr 

pandas2ri.activate()
fitdistrplus = importr('fitdistrplus')

def descdist(data: pd.Series, **kwargs):
    rdf = pandas2ri.py2rpy(data)
    fitdistrplus.descdist(rdf,  **kwargs)
