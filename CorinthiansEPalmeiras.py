import pandas as pd

# Carregar os dados
df = pd.read_csv("historicoCorinthiansPalmeiras.csv", sep=';')

# Inicializar contadores
tot_vitoria_c = 0
tot_vitoria_p = 0
tot_empate = 0

# Contadores para as características
tot_boa_c = 0
tot_media_c = 0
tot_ruim_c = 0
tot_boa_p = 0
tot_media_p = 0
tot_ruim_p = 0

# Contar os resultados
for index, row in df.iterrows():
    if row['Resultado'] == 'Vitória do Corinthians':
        tot_vitoria_c += 1
        if row['FormaCorinthians'] == 'Boa':
            tot_boa_c += 1
        elif row['FormaCorinthians'] == 'Média':
            tot_media_c += 1
        else:
            tot_ruim_c += 1
            
    elif row['Resultado'] == 'Vitória do Palmeiras':
        tot_vitoria_p += 1
        if row['FormaPalmeiras'] == 'Boa':
            tot_boa_p += 1
        elif row['FormaPalmeiras'] == 'Média':
            tot_media_p += 1
        else:
            tot_ruim_p += 1
            
    else:
        tot_empate += 1

# Calcular probabilidades
total_jogos = len(df)
probabilidade_vitoria_c = (tot_vitoria_c / total_jogos) * 100
probabilidade_vitoria_p = (tot_vitoria_p / total_jogos) * 100
probabilidade_empate = (tot_empate / total_jogos) * 100

# Identificando a regra
regra = ""
if tot_boa_c >= tot_media_c and tot_boa_c >= tot_ruim_c:
    regra = "Se FormaCorinthians é Boa, então Vitória do Corinthians"
elif tot_boa_p >= tot_media_p and tot_boa_p >= tot_ruim_p:
    regra = "Se FormaPalmeiras é Boa, então Vitória do Palmeiras"
else:
    regra = "Empate pode ser esperado"

# Resultados
print("Probabilidades:")
print(f"Vitória do Corinthians: {probabilidade_vitoria_c:.2f}%")
print(f"Vitória do Palmeiras: {probabilidade_vitoria_p:.2f}%")
print(f"Empate: {probabilidade_empate:.2f}%")
print("\nRegra Identificada:")
print(regra)


