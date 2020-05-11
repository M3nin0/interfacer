# interfacer-descdist

Pacote para facilitar a utilização do [descdist](https://www.rdocumentation.org/packages/fitdistrplus/versions/1.0-14/topics/descdist) em Python

### Instalação

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
    <img src="https://raw.githubusercontent.com/M3nin0/interfacer-descdist/master/image/image.png?token=AEB7NZM4BQC3LXW4BV234EK6YMAT4">
</div>

> Note que pode ser necessário configurar o ambiente R e Python juntos, recomenda-se o Anaconda para gerenciar os pacotes de R e Python

### Sobre

Pacote criado por Felipe Menino para facilitar as atividades desenvolvidas na aula de Matemática Computacional.
