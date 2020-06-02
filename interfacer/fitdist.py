import pandas as pd

from rpy2.robjects import pandas2ri
from rpy2.robjects.packages import importr 

pandas2ri.activate()
try:
    graphics = importr('graphics')
    fitdistrplus = importr('fitdistrplus')
except:
    raise ModuleNotFoundError("É necessário instalar o pacote fitdistrplus no ambiente R")


def fitdist(data: pd.Series, **kwargs):
    """fitdist
    See:
        https://cran.r-project.org/web/packages/fitdistrplus/fitdistrplus.pdf
    """
    rdf = pandas2ri.py2rpy(data)
    return fitdistrplus.fitdist(rdf,  **kwargs)


def fitdistplot(data: pd.Series, **kwargs):
    """fitdistplot
    See:
        https://cran.r-project.org/web/packages/fitdistrplus/fitdistrplus.pdf
    """
    rdf = pandas2ri.py2rpy(data)
    res = fitdistrplus.fitdist(rdf,  **kwargs)
    graphics.plot(res)
