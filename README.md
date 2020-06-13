# interfacer - fitdistplus

Pacote para facilitar a utilização de algumas funcionalidades do [fitdistrplus](https://cran.r-project.org/web/packages/fitdistrplus/index.html) em Python.

### Funcionalidades

Atualmente, estão disponíveis no pacote as seguintes funcionalidades:

- [plotdist](https://www.rdocumentation.org/packages/fitdistrplus/versions/1.1-1/topics/plotdist);
- [fitdist](https://www.rdocumentation.org/packages/fitdistrplus/versions/0.1-3/topics/fitdist);
- [descdist](https://www.rdocumentation.org/packages/fitdistrplus/versions/1.1-1/topics/descdist).

### Instalação

A instalação do pacote pode ser feita via pip, como apresentado abaixo

```shell
pip install interfacer
```

### Exemplo de utilização

```python
import interfacer.descdist
import interfacer.jupyter_helper
```

```python
data_owd = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
bra = data_owd[data_owd['iso_code'] == 'BRA']

with interfacer.jupyter_helper.cellplot(width=800, height=640):
    interfacer.descdist.descdist(bra.new_cases, boot = 250)
```

<div align="center">
    <img src="https://raw.githubusercontent.com/M3nin0/interfacer/master/image/image.png">
</div>

> Note que pode ser necessário configurar o ambiente R e Python juntos, recomenda-se o Anaconda para gerenciar os pacotes de R e Python

### Sobre

Pacote criado por Felipe Menino para facilitar as atividades desenvolvidas nas aulas de Matemática Computacional.
