from pandas import read_csv
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import lime
import lime.lime_tabular

# Carregando os dados
filename = 'Group1_BancoTCE_24h_FUP_Impulsividade_050823_type02.csv'
names = ['age', 'Angiotensin 1-7', 'Angiotensin 2', 'Cathepsin D', 'Copeptin', 'GRO', 'IFN alpha 2', 'IL-4',
         'MDC', 'MCP-1', 'MCP3', 'MMP9', 'MPO', 'Neuropilin-1', 'PAI-1', 'PDGF-AB-BB', 'RAGE', 'sCD40L', 'sex',
         'sVCAM-1', 'VEGF-A', 'BIS attentional', 'BIS motor', 'BIS nonplanning', 'BIS total', 'BIS 2F inhibitorycontrol',
         'BIS 2F nonplanning']

# Carregar os dados do arquivo CSV para um DataFrame
dataframe = read_csv(filename, names=names)
array = dataframe.values  # Converter DataFrame para uma matriz numpy

names2 = names[0:21]  # Selecionar apenas os nomes dos atributos

# Função para calcular a importância das features usando LIME
def calculate_feature_importance_with_lime(X, y, names2, title_figure):
    explainer = lime.lime_tabular.LimeTabularExplainer(X, mode="regression")
    v_import = np.zeros(X.shape[1])  # Inicializar vetor de importância
    
    simulations = 10  # Definir o número de simulações
    
    # Realizar simulações para obter a média da importância das features
    for ite in range(0, simulations):
        model = RandomForestRegressor(random_state=ite)  # Criar o modelo RandomForestRegressor
        model.fit(X, y)  # Treinar o modelo
        print(f'Score-r2 for {title_figure}: {model.score(X, y):.3f}')  # Avaliar o modelo
        importance = model.feature_importances_  # Obter a importância das features
        
        # Acumular a importância das features em cada iteração
        for ii in range(len(importance)):
            v_import[ii] = v_import[ii] + (importance[ii] / simulations)
    
    # Iterar sobre cada instância dos dados
    for i in range(len(X)):
        exp = explainer.explain_instance(X[i], model.predict)
        feature_importance = exp.as_list()
        
        # Mostrar as importâncias das features para cada instância
        for feat in feature_importance:
            feature_idx = feat[0]
            feature_score = feat[1]
            
            # Verificar se o valor do índice da feature é uma string e tentar extrair o valor numérico
            if isinstance(feature_idx, str):
                # Extrair apenas o valor numérico da string
                num_value = ''.join(filter(str.isdigit, feature_idx))
                
                try:
                    feature_idx = int(num_value)
                except ValueError:
                    pass
            
            if isinstance(feature_idx, int) and feature_idx < len(v_import):
                v_import[feature_idx] += feature_score / len(X)
    
    return v_import  # Retornar a média da importância das features

# Loop para testar cada variável-alvo
for variable_prediction in range(21, 27):  # Testar cada variável-alvo
    y = array[:, variable_prediction]  # Selecionar a variável-alvo atual
    
    X = array[:, 0:21]  # Selecionar os 21 atributos como variáveis preditoras
    
    title_figure = names[variable_prediction]  # Nome da variável-alvo atual
    
    # Calcular a importância das features para a variável-alvo atual
    feature_importance = calculate_feature_importance_with_lime(X, y, names2, title_figure)
    
    # Plotar os resultados da importância das features
    ax = plt.subplot()  # Criar um subplot para o gráfico
    pos = np.arange(len(names2))  # Posições para as barras no gráfico
    ax.barh(pos, feature_importance, color='blue', edgecolor='black')  # Gráfico de barras horizontais
    plt.yticks(pos, names2)  # Rótulos para as barras
    plt.xlabel("Mean of feature importance")  # Rótulo do eixo x
    plt.title(title_figure)  # Título do gráfico
    
    plt.show()  # Mostrar o gráfico
    
    # Análise dos resultados da importância das features
    for i, v in enumerate(feature_importance):
        print(f'Feature {i}: {names2[i]}, Score: {v:.3f}')  # Mostrar a importância de cada feature
    
    valor_medio = np.mean(feature_importance)  # Calcular o valor médio da importância das features
    valor_desvio_padrao = np.std(feature_importance)  # Calcular o desvio padrão da importância das features
    print(f'Desvio padrão = {valor_desvio_padrao:.3f}')  # Mostrar o desvio padrão
    print(f'Valor médio = {valor_medio:.3f}')  # Mostrar o valor médio
    
    print('\nAtributos com score >= valor médio:')  # Mostrar as features com importância maior ou igual à média
    for i, v in enumerate(feature_importance):
        if v >= valor_medio:
            print(f'Feature {i}: {names2[i]}, Score: {v:.3f}')
