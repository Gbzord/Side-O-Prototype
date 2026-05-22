# SIDE-O: Framework de Complexidade-Entropia

Sistema Inteligente para Diagnóstico de Emissões Offshore via Dinâmica Não-Linear

---

## 📋 Descrição

O SIDE-O é um framework interativo desenvolvido em Python e Streamlit para análise e diagnóstico de séries temporais de sensores de gás (CH₄) em ambientes offshore. Utiliza conceitos de Física Estatística, Teoria da Informação e Dinâmica Não-Linear para detectar transições de fase e anomalias (ex: vazamentos) em sinais ruidosos.

---

## ⚛️ Fundamentação Científica

O SIDE-O fundamenta-se em:
- **Teoria da Informação**
- **Física Estatística**
- **Dinâmica Não-Linear**
- **Método de Bandt-Pompe**
- **Plano Complexidade-Entropia**
- **Sistemas Complexos**

Fluxo:  
**Sensor → Série Temporal → Bandt-Pompe → H×C → Classificação → Alerta**  

**TRL Atual:** 3-4

---

## 🚀 Funcionalidades

- Upload ou carregamento automático de séries temporais (.csv)
- Visualização do sinal bruto do sensor
- Processamento matemático com janelas deslizantes
- Cálculo e plotagem do Plano de Causalidade Complexidade-Entropia (H × C)
- Diagnóstico automático de anomalias e emissão de alertas preventivos

---

## 📁 Estrutura do Projeto

```
Streamlit/
│
├── app.py                  # Aplicação principal Streamlit
├── engine.py               # Funções de processamento matemático e diagnóstico
├── gerar_dataset.py        # Script para gerar dataset simulado
├── sensor_gas_dataset.csv  # Dataset de exemplo gerado/simulado
├── requirements.txt        # Dependências do projeto
└── README.md               # Este arquivo
```

---

## ⚙️ Instalação e Execução

1. **Clone o repositório ou baixe os arquivos.**

2. **(Opcional) Crie um ambiente virtual:**
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Gere o dataset de exemplo (caso não exista):**
   ```powershell
   python gerar_dataset.py
   ```

5. **Execute o aplicativo Streamlit:**
   ```powershell
   streamlit run app.py
   ```

6. **Acesse o app no navegador:**  
   Normalmente em [http://localhost:8501](http://localhost:8501)

---

## 🗂️ Como Usar

- **Modo Automático:**  
  O app carrega automaticamente o arquivo `sensor_gas_dataset.csv` se estiver presente na pasta do projeto.

- **Modo Manual:**  
  Faça upload de um arquivo `.csv` com duas colunas: tempo e concentração de CH₄.

- **Visualização:**  
  O app exibe o gráfico do sinal bruto, o plano de complexidade-entropia e o diagnóstico automático.

---

## 🧪 Geração de Dataset Simulado

O script `gerar_dataset.py` cria um arquivo `sensor_gas_dataset.csv` com uma transição de fase simulada (mudança de regime no sinal, representando um possível vazamento).

---

## 📦 Requisitos

- Python 3.8+
- streamlit
- pandas
- numpy
- plotly
- matplotlib

Instale todos via `requirements.txt`.

---

## 📝 Exemplo de Dataset

```csv
Tempo_segundos,Concentracao_CH4_ppm
0.0,0.5496714153011233
0.1,0.4861735698828815
...
```

---

## 🗺️ Roadmap

- [x] Prova de conceito dinâmica
- [ ] Integração com dados Sentinel-5P
- [ ] Correção atmosférica
- [ ] Inferência espacial
- [ ] Deploy orbital

---

## 👨‍💻 Autores

- Gabriel Christino

---

## 📄 Licença

Este projeto é livre para fins acadêmicos e de pesquisa. Consulte o autor para usos
