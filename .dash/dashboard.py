import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea

# Configura a página para se ajustar ao tamanho da tela
st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

#titulo do dashboard
st.title("Dashboard de Vendas por Curso")

#carrega os dados
df = pd.read_csv(r"C:\Users\layss\OneDrive\Cursos\Desafio-Data-Science\dados.csv", sep=",")

#realiza o calculo do total de vendas em R$ adiciona a coluna na tabela
df["Total R$"] = df["Quantidade de Vendas"] * df ["Preço Unitário"]

#cria as colunas para o layout
col1, col2, col3 = st.columns(3)
col4, col5 = st.columns(2)

with col1:
    #calcula o valor total da receita
    total_receita = df["Total R$"].sum()
    st.metric(label="Valor Total da Receita", value=f"R${total_receita:,.2f}")

    #calcula a quantidade total de cursos vendidos
    quant_total = df["Quantidade de Vendas"].sum()
    st.metric(label="Quantidade Total Vendido", value=f"{quant_total}")

with col2:
    #calcula as estatisticas das colunas com conteudos numericos
    filtro_estatisticas = ["mean", "std", "min", "50%", "max"]
    df_estatisticas = df[["Quantidade de Vendas", "Preço Unitário", "Total R$"]].describe().loc[filtro_estatisticas]
    df_estatisticas = df_estatisticas.rename(index={"mean": "Média", "std": "Desvio Padrão", "min": "Mínimo", "50%": "Mediana", "max": "Máximo"})
    
    st.subheader("Estatísticas")
    st.write(df_estatisticas)

with col3:
    #curso mais vendido
    vendas_por_curso = df.groupby("Nome do Curso")["Quantidade de Vendas"].sum()
    id_mais_vendido = vendas_por_curso.idxmax()
    qntd_mais_vendido = vendas_por_curso.max()
    st.markdown(f"<h3 style='font-size: 20px;'>Curso Mais Vendido: {id_mais_vendido} com {qntd_mais_vendido} vendas</h3>", unsafe_allow_html=True)

#grafico de vendas por curso (quantidade)
top5_cursos = df.groupby("Nome do Curso")["Quantidade de Vendas"].sum().nlargest(5).reset_index()
outros_cursos = df.groupby("Nome do Curso")["Quantidade de Vendas"].sum().nsmallest(df["Nome do Curso"].nunique() - 5).sum()
top5_cursos.loc[len(top5_cursos)] = ["Outros", outros_cursos]
fig2, ax = plt.subplots()
ax.pie(top5_cursos["Quantidade de Vendas"], labels=top5_cursos["Nome do Curso"], colors=["pink", "magenta", "mediumpurple", "cyan", "deepskyblue", "blue"])
ax.axis("equal")
ax.set_title("Vendas por Curso")
col3.pyplot(fig2, use_container_width=True)

#grafico de vendas por dia
fig1, ax = plt.subplots(figsize=(15, 5))
df.plot(kind="bar", x="Data", y="Total R$", ax=ax, color="royalblue")
ax.set_xlabel("Data")
ax.set_ylabel("Total R$")
ax.set_title("Vendas por Dia R$")
col4.pyplot(fig1, use_container_width=True)

with col5:
    #grafico quantidade por dia
    fig01, ax = plt.subplots(figsize=(11.5, 5))
    sea.scatterplot(data=df, x="Data", y="Quantidade de Vendas", color="royalblue")
    plt.xlabel("Data")
    plt.ylabel("Quantidade de Vendas")
    plt.title("Quantidade Total de Vendas por Dia")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt.gcf(), use_container_width=True)

#exibe a tabela de dados das vendas
st.dataframe(df, use_container_width=True)