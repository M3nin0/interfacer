import pandas as pd

from rpy2.robjects import pandas2ri
from rpy2.robjects.packages import importr 

pandas2ri.activate()
try:
    fitdistrplus = importr('fitdistrplus')
except:
    raise ModuleNotFoundError("É necessário instalar o pacote fitdistrplus no ambiente R")

def descdist(data: pd.Series, **kwargs):
    """descdist
    See:
        https://cran.r-project.org/web/packages/fitdistrplus/fitdistrplus.pdf
    """
    rdf = pandas2ri.py2rpy(data)
    fitdistrplus.descdist(rdf,  **kwargs)
