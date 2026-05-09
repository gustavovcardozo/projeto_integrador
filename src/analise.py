#📥 IMPORTAÇÃO DA PLANILHA .CSV

import pandas as pd

df = pd.read_csv('habitos_estudantes_tratada.csv')

print(df.head())


#🔥 BURNOUT

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('habitos_estudantes_tratada.csv')

categorias = pd.cut(
    df['burnout_level'],
    bins=[0, 4, 7, 10],
    labels=['Baixo', 'Médio', 'Alto']
)

contagem = categorias.value_counts()

plt.figure(figsize=(8,8))

plt.pie(
    contagem,
    labels=contagem.index,
    autopct='%1.1f%%'
)

plt.title('Distribuição de Burnout')

plt.savefig('burnout_pizza.png')

plt.show()


#😴 SONO X FOCO

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('habitos_estudantes_tratada.csv')

categorias = pd.cut(
    df['sleep_hours'],
    bins=[0, 5, 8, 12],
    labels=['Pouco Sono', 'Sono Normal', 'Muito Sono']
)

contagem = categorias.value_counts()

plt.figure(figsize=(8,8))

plt.pie(
    contagem,
    labels=contagem.index,
    autopct='%1.1f%%'
)

plt.title('Distribuição das Horas de Sono')

plt.savefig('sono_foco_pizza.png')

plt.show()


#🧠 SAÚDE MENTAL

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('habitos_estudantes_tratada.csv')

categorias = pd.cut(
    df['mental_health_score'],
    bins=[0, 4, 7, 10],
    labels=['Baixa', 'Média', 'Alta']
)

contagem = categorias.value_counts()

plt.figure(figsize=(8,8))

plt.pie(
    contagem,
    labels=contagem.index,
    autopct='%1.1f%%'
)

plt.title('Distribuição da Saúde Mental')

plt.savefig('saude_mental_pizza.png')

plt.show()


#📱 USO DE REDES SOCIAIS

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('habitos_estudantes_tratada.csv')

categorias = pd.cut(
    df['social_media_hours'],
    bins=[0, 2, 5, 10],
    labels=['Baixo Uso', 'Uso Moderado', 'Uso Alto']
)

contagem = categorias.value_counts()

plt.figure(figsize=(8,8))

plt.pie(
    contagem,
    labels=contagem.index,
    autopct='%1.1f%%'
)

plt.title('Uso de Redes Sociais')

plt.savefig('redes_sociais_pizza.png')

plt.show()


#📚 HORAS DE ESTUDO

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('habitos_estudantes_tratada.csv')

categorias = pd.cut(
    df['study_hours'],
    bins=[0, 2, 5, 10],
    labels=['Pouco Estudo', 'Estudo Moderado', 'Muito Estudo']
)

contagem = categorias.value_counts()

plt.figure(figsize=(8,8))

plt.pie(
    contagem,
    labels=contagem.index,
    autopct='%1.1f%%'
)

plt.title('Distribuição das Horas de Estudo')

plt.savefig('estudo_pizza.png')

plt.show()


#📊 CORRELAÇÃO

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('habitos_estudantes_tratada.csv')

correlacao = df.corr(numeric_only=True)['exam_score']

correlacao = correlacao.drop('exam_score')

correlacao = correlacao.sort_values()

plt.figure(figsize=(10,6))

correlacao.plot(kind='barh')

plt.title('Fatores que Influenciam a Nota Final')

plt.xlabel('Correlação')

plt.savefig('correlacao_barras.png')

plt.show()
