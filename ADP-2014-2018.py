#!/usr/bin/env python
# coding: utf-8

# # Escolas sem água, energia e esgoto no Brasil: 2014 a 2018

#Importando bibliotecas que serão usadas.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
low_memory=False
pd.options.display.max_columns = 80
pd.options.display.max_rows = 90


#Abrindo o arquivos CSV e produzindo os dataframes.
df2018 = pd.read_csv('ESCOLAS2018.CSV', delimiter = '|', encoding='iso-8859-1', usecols=['TP_SITUACAO_FUNCIONAMENTO', 'IN_AGUA_INEXISTENTE', 'IN_ESGOTO_INEXISTENTE', 'IN_ENERGIA_INEXISTENTE', 'NO_ENTIDADE'])
df2017 = pd.read_csv('ESCOLAS2017.CSV', delimiter = '|', encoding='iso-8859-1', usecols=['TP_SITUACAO_FUNCIONAMENTO', 'IN_AGUA_INEXISTENTE', 'IN_ESGOTO_INEXISTENTE', 'IN_ENERGIA_INEXISTENTE', 'NO_ENTIDADE'])
df2016 = pd.read_csv('ESCOLAS2016.CSV', delimiter = '|', encoding='iso-8859-1', usecols=['TP_SITUACAO_FUNCIONAMENTO', 'IN_AGUA_INEXISTENTE', 'IN_ESGOTO_INEXISTENTE', 'IN_ENERGIA_INEXISTENTE', 'NO_ENTIDADE'])
df2015 = pd.read_csv('ESCOLAS2015.CSV', delimiter = '|', encoding='iso-8859-1', usecols=['TP_SITUACAO_FUNCIONAMENTO', 'IN_AGUA_INEXISTENTE', 'IN_ESGOTO_INEXISTENTE', 'IN_ENERGIA_INEXISTENTE', 'NO_ENTIDADE'])
df2014 = pd.read_csv('ESCOLAS2014.CSV', delimiter = '|', encoding='iso-8859-1', usecols=['DESC_SITUACAO_FUNCIONAMENTO', 'ID_AGUA_INEXISTENTE','ID_ESGOTO_INEXISTENTE', 'ID_ENERGIA_INEXISTENTE', 'NO_ENTIDADE'])

#Declarando váriaveis para produzir o gráfico.
A2018 = df2018.query('TP_SITUACAO_FUNCIONAMENTO == 1 and IN_AGUA_INEXISTENTE == 1 and IN_ESGOTO_INEXISTENTE == 1 and IN_ENERGIA_INEXISTENTE == 1')['NO_ENTIDADE'].count()
A2017 = df2017.query('TP_SITUACAO_FUNCIONAMENTO == 1 and IN_AGUA_INEXISTENTE == 1 and IN_ESGOTO_INEXISTENTE == 1 and IN_ENERGIA_INEXISTENTE == 1')['NO_ENTIDADE'].count()
A2016 = df2016.query('TP_SITUACAO_FUNCIONAMENTO == 1 and IN_AGUA_INEXISTENTE == 1 and IN_ESGOTO_INEXISTENTE == 1 and IN_ENERGIA_INEXISTENTE == 1')['NO_ENTIDADE'].count()
A2015 = df2015.query('TP_SITUACAO_FUNCIONAMENTO == 1 and IN_AGUA_INEXISTENTE == 1 and IN_ESGOTO_INEXISTENTE == 1 and IN_ENERGIA_INEXISTENTE == 1')['NO_ENTIDADE'].count()
A2014 = df2014.query('DESC_SITUACAO_FUNCIONAMENTO == 1 and ID_AGUA_INEXISTENTE == 1 and ID_ESGOTO_INEXISTENTE == 1 and ID_ENERGIA_INEXISTENTE == 1')['NO_ENTIDADE'].count()

#Imprimindo o número de escolas sem água, energia e esgoto no Brasil.
print(f"O número de escolas sem água, energia e esgoto no Brasil em 2018 foi de {A2018} escolas.")
print(f"O número de escolas sem água, energia e esgoto no Brasil em 2017 foi de {A2017} escolas.")
print(f"O número de escolas sem água, energia e esgoto no Brasil em 2016 foi de {A2016} escolas.")
print(f"O número de escolas sem água, energia e esgoto no Brasil em 2015 foi de {A2015} escolas.")
print(f"O número de escolas sem água, energia e esgoto no Brasil em 2014 foi de {A2014} escolas.")

#Produzindo o gráfico.
figura = plt.figure()
eixo = figura.add_axes([1,1,1,2])
plt.title('Escolas sem água, energia e esgoto no Brasil no decorrer de 2014 até 2019')
plt.xlabel('Anos')
plt.ylabel('Escolas')
anos = ['2014', '2015', '2016', '2017', '2018']
escolas = (1149, 1057, 907, 873, 810)
eixo.plot(anos,escolas)
plt.show()

