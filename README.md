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
    df = pd.read_csv(r".dash/dados.csv", sep=",")
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
- **Métricas e estatísticas**: Calcula e exibe o valor total da receita e a quantidade total vendida.
    ```python
    total_receita = df["Total R$"].sum()
    st.metric(label="Valor Total da Receita", value=f"R${total_receita:,.2f}")

    quant_total = df["Quantidade de Vendas"].sum()
    st.metric(label="Quantidade Total Vendido", value=f"{quant_total}")
    ```
- **Estatísticas**: Calcula e filtra as as estatísticas descritivas e calculo do curso mais vendido.
    ```python
    filtro_estatisticas = ["mean", "std", "min", "50%", "max"]
    df_estatisticas = df[["Quantidade de Vendas", "Preço Unitário", "Total R$"]].describe().loc[filtro_estatisticas]
    df_estatisticas = df_estatisticas.rename(index={"mean": "Média", "std": "Desvio Padrão", "min": "Mínimo", "50%": "Mediana", "max": "Máximo"})
    
    st.subheader("Estatísticas")
    st.write(df_estatisticas)

    vendas_por_curso = df.groupby("Nome do Curso")["Quantidade de Vendas"].sum()
    id_mais_vendido = vendas_por_curso.idxmax()
    qntd_mais_vendido = vendas_por_curso.max()
    st.markdown(f"<h3 style='font-size: 20px;'>Curso Mais Vendido: {id_mais_vendido} com {qntd_mais_vendido} vendas</h3>", unsafe_allow_html=True)
    ```
- **Gráficos**: Cria gráficos para visualização das vendas por curso, vendas por dia e quantidade por dia, respectivamente.
    ```python
    top5_cursos = df.groupby("Nome do Curso")["Quantidade de Vendas"].sum().nlargest(5).reset_index()
    outros_cursos = df.groupby("Nome do Curso")["Quantidade de Vendas"].sum().nsmallest(df["Nome do Curso"].nunique() - 5).sum()
    top5_cursos.loc[len(top5_cursos)] = ["Outros", outros_cursos]
    fig2, ax = plt.subplots()
    ax.pie(top5_cursos["Quantidade de Vendas"], labels=top5_cursos["Nome do Curso"], colors=["pink", "magenta", "mediumpurple", "cyan", "deepskyblue", "blue"])
    ax.axis("equal")
    ax.set_title("Vendas por Curso")
    col3.pyplot(fig2, use_container_width=True)

    fig1, ax = plt.subplots(figsize=(15, 5))
    df.plot(kind="bar", x="Data", y="Total R$", ax=ax, color="royalblue")
    ax.set_xlabel("Data")
    ax.set_ylabel("Total R$")
    ax.set_title("Vendas por Dia R$")
    col4.pyplot(fig1, use_container_width=True)

    fig01, ax = plt.subplots(figsize=(11.5, 5))
    sea.scatterplot(data=df, x="Data", y="Quantidade de Vendas", color="royalblue")
    plt.xlabel("Data")
    plt.ylabel("Quantidade de Vendas")
    plt.title("Quantidade Total de Vendas por Dia")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt.gcf(), use_container_width=True)
    ```
## Contribuição
Contribuições são bem-vindas! Por favor, abra uma issue para discutir o que você gostaria de mudar ou melhorar.

## Contato
Para mais informações, entre em contato pelo email: [layssa21.alves@gmail.com]
