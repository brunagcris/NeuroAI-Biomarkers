# NeuroAI-Biomarkers  

Um projeto de pesquisa que utiliza técnicas de Inteligência Artificial, como o algoritmo de Floresta Aleatória, para identificar a relevância de biomarcadores em comportamentos impulsivos. O objetivo é aplicar aprendizado de máquina para melhorar o entendimento das relações entre fatores biológicos e impulsividade, contribuindo para diagnósticos e tratamentos mais eficazes.

## Objetivo  

Identificar biomarcadores associados à impulsividade em pacientes com TCE usando aprendizado de máquina, permitindo diagnósticos mais precisos e tratamentos personalizados.  

### Objetivos específicos  

- Criar modelos baseados em Florestas Aleatórias.
- Interpretar os resultados dos modelos para identificar padrões.
- Quantificar a relevância dos biomarcadores nos comportamentos impulsivos.  

---

## Metodologia  

Os dados clínicos de 21 pacientes com TCE foram analisados. Eles incluíram:  

- **Biomarcadores**: 21 substâncias no sangue que ajudam a compreender a resposta do corpo ao trauma.  
- **Medidas de Impulsividade**: Escalas BIS Attentional e BIS Motor, que avaliam aspectos diferentes da impulsividade.  

### Etapas  

1. **Carregamento e preparação dos dados**: Manipulação de um dataset em CSV.  
2. **Treinamento do modelo**: Uso do `RandomForestRegressor` para prever associações entre biomarcadores e impulsividade.  

---

## Resultados  

### Principais descobertas:  

Os biomarcadores mais relevantes para as dimensões de impulsividade incluem:

#### BIS Attentional  

![BIS attentional](https://github.com/user-attachments/assets/b8ab0c28-3dac-4cb4-8f58-0c17861550c1)

- **Copeptin**: Relacionado ao estresse.  
- **Idade**: Fator de variação na impulsividade.  
- **Neuropilin-1**: Ligada à regeneração celular.  

#### BIS Motor  

![BIS motor](https://github.com/user-attachments/assets/72a8d87e-eff8-4f92-bf3b-4cc908ff1180)

- **RAGE**: Associada à inflamação.  
- **IL-4**: Citocina anti-inflamatória.  
- **Idade**: Relevante para o tipo de impulsividade.
- 
Esses resultados destacam como processos biológicos influenciam diferentes dimensões da impulsividade.

---

## Tecnologias Utilizadas  

- **Python**: Linguagem para desenvolvimento do projeto.  
- **Scikit-learn**: Biblioteca de aprendizado de máquina para construir e interpretar modelos.  
- **Pandas/Numpy**: Manipulação e análise de dados.  
- **Matplotlib**: Visualização de resultados.  

---

## Conclusão  

O uso de Florestas Aleatórias demonstrou ser uma abordagem eficaz para identificar biomarcadores relevantes no TCE. Os resultados contribuem para um diagnóstico mais preciso e tratamentos personalizados, promovendo melhorias na qualidade de vida dos pacientes.

---

## Como executar  

1. **Clone o repositório**:  

   ```bash
   git clone https://github.com/seu-usuario/NeuroAI-Biomarkers.git
   cd NeuroAI-Biomarkers
