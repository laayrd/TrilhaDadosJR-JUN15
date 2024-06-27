# Dashboard de Vendas Por Curso
Este projeto é um dashboard interativo desenvolvido com Streamlit para visualizar e analisar as vendas de cursos.
Disponivel para vizualização em ('https://laayrd-desafiods--dashdashboard-upfa7x.streamlit.app/')

## Visão Geral
O dashboard permite visualizar:
- O valor total da receita
- A quantidade total de cursos vendidos
- Estatísticas descritivas das vendas
- O curso mais vendido
- Gráficos de vendas por curso e por dia

## Tecnologias Utilizadas
- Python
- Streamlit
- Pandas
- Matplotlib
- Seaborn

## Instalação
1. Clone o repositório:
    ```sh
    git clone https://github.com/laayrd/DesafioDS.git
    cd DesafioDS
    ```
2. Baixe o arquivo `requirements.txt` que contém as bibliotecas.
3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Uso
1. Baixe o arquivo de dados (`dados.csv`), copie e altere o caminho do 'df' na linha 13 código.
2. Execute o aplicativo Streamlit:
    ```
    streamlit run desafioDS.py
    ```
3. Abra seu navegador e vá para `http://localhost:8501` para ver o dashboard.

## Estrutura do Código
O código principal do aplicativo está no arquivo `dashboard.py`. Aqui está uma visão geral do que cada parte do código faz:
- **Configuração da página**: Ajusta o layout da página para ser responsivo.
    ```python
    st.set_page_config(page_title="Dashboard de Vendas", layout="wide")
    ```
- **Carregamento dos dados**: Lê os dados do arquivo CSV.
    ```python
    df = pd.read_csv(r"C:\Users\layss\OneDrive\Cursos\Desafio-Data-Science\dados.csv", sep=",")
    ```
- **Cálculo do total de vendas**: Adiciona uma coluna com o total de vendas em R$.
    ```python
    df["Total R$"] = df["Quantidade de Vendas"] * df ["Preço Unitário"]
    ```
- **Criação do layout**: Define as colunas e insere as métricas, estatísticas e gráficos.
    ```python
    col1, col2, col3 = st.columns(3)
    col4, col5 = st.columns(2)
    ```
- **Métricas e estatísticas**: Calcula e exibe o valor total da receita, a quantidade total vendida, e as estatísticas descritivas.
    ```python
    total_receita = df["Total R$"].sum()
    st.metric(label="Valor Total da Receita", value=f"R${total_receita:,.2f}")

    quant_total = df["Quantidade de Vendas"].sum()
    st.metric(label="Quantidade Total Vendido", value=f"{quant_total}")
    ```
- **Gráficos**: Cria gráficos para visualização das vendas por curso e por dia.
    ```python
    fig2, ax = plt.subplots()
    ax.pie(top5_cursos["Quantidade de Vendas"], labels=top5_cursos["Nome do Curso"], colors=["pink", "magenta", "mediumpurple", "cyan", "deepskyblue", "blue"])
    col3.pyplot(fig2, use_container_width=True)
    ```
## Contribuição
Contribuições são bem-vindas! Por favor, abra uma issue para discutir o que você gostaria de mudar ou melhorar.

## Contato
Para mais informações, entre em contato pelo email: [layssa21.alves@gmail.com]
