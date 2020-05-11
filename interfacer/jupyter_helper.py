from contextlib import contextmanager
from rpy2.robjects.lib import grdevices
from IPython.display import Image, display


@contextmanager
def cellplot(width=600, height=600, dpi=100):
    """Função para permitir a visualização dos gráficos gerados no R com rpy2
    nas células do Jupyter Notebook

    See:
        Código adaptado de: https://stackoverflow.com/questions/43110228/how-to-plot-inline-with-rpy2-in-jupyter-notebook
    """

    with grdevices.render_to_bytesio(grdevices.png, 
                    width=width, height=height, res=dpi) as b:
        yield

    data = b.getvalue()
    display(Image(data=data, format='png', embed=True))
