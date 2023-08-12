
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Web_Scrap\dataset\On-Theaters-Rotten-Tomatoes-11-08-2023.csv")

#GRÁFICA 1---------------------------------------------------
criticas=[]
for item in df['Critics Score']:
    if item!="Sin calificación":
        criticas.append(item)

criticas=[int(num) for num in criticas]
indicescrit = list(range(len(criticas)))

mediacricticas=np.mean(criticas)

plt.bar(indicescrit,criticas)
plt.xlabel('Movie Index')
plt.ylabel('Score')
plt.title('Critics Scores')
plt.annotate(f'Average Score: {round(mediacricticas,2)}', xy=(-3.20,100.5))
plt.show()


#GRÁFICA 2---------------------------------------------------
audiencia=[]
for item in df['Audience Score']:
    if item!="Sin calificación":
        audiencia.append(item)

audiencia=[int(num) for num in audiencia]
indicesaud = list(range(len(audiencia)))

mediaaud=np.mean(audiencia)

plt.bar(indicesaud,audiencia)
plt.xlabel('Movie Index')
plt.ylabel('Score')
plt.title('Audience Scores')
plt.annotate(f'Average Score: {round(mediaaud,2)}', xy=(-3.20,100.5))
plt.show()



#GRÁFICA 3---------------------------------------------------
#Sacar media de diferencia
scores_criticas=[]
scores_audience=[]

for index, row in df.iterrows():
    critics_score = row['Critics Score']
    audience_score = row['Audience Score']
    
    if critics_score != "Sin calificación" and audience_score != "Sin calificación":
        scores_criticas.append(critics_score)
        scores_audience.append(audience_score)
    else:
        pass

#pasar a enteros
scores_criticas=[int(num) for num in scores_criticas]
scores_audience=[int(num) for num in scores_audience]


diferencias=[]
for i in range (len(scores_criticas)):
    r=(scores_audience[i])-(scores_criticas[i])
    diferencias.append(r)
    diferencias=[abs(numero) for numero in diferencias]

media_total=np.mean(diferencias)

#crear gráfico
indices = list(range(len(scores_criticas)))
plt.plot(indices, scores_criticas, label='Critics', marker='o', color='red')
plt.plot(indices, scores_audience, label='Audience', marker='o',color='green')
plt.xlabel('Movie Index')
plt.ylabel('Score')
plt.title('Critics vs Audience Scores')
plt.legend()

plt.annotate(f'Average Difference: {round(media_total,2)}', xy =(15, 35))
plt.show()
