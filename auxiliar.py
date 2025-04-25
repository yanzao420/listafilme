from collections import Counter
import json

def carregar_filmes_json(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        return json.load(f)



def coletar_preferencias():
    print("Digite 1 filmes que você gosta:")
    preferencias = []
    for i in range(1):
        filme = input("- Filme: ").strip()
        preferencias.append(filme)
    return preferencias

def encontrar_generos_preferidos(preferencias, filmes):
    generos = []
    for filme in preferencias:
        for item in filmes:
            if item["titulo"].lower() == filme.lower():
                generos.append(item["genero"])
    return generos

def recomendar_filmes(generos_preferidos, filmes, preferencias):
    contagem = Counter(generos_preferidos)
    genero_mais_comum = contagem.most_common(1)[0][0]
    recomendacoes = []

    for item in filmes:
        if item["genero"] == genero_mais_comum and item["titulo"] not in preferencias:
            recomendacoes.append(item["titulo"])
            
    return recomendacoes