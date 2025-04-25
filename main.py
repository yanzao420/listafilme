import json
from collections import Counter
from auxiliar import carregar_filmes_json, coletar_preferencias, encontrar_generos_preferidos, recomendar_filmes


def main():
    print("=== Recomendador de Filmes ===\n")

    filmes = carregar_filmes_json("lista.json")

    preferencias = coletar_preferencias()

    generos_preferidos = encontrar_generos_preferidos(preferencias, filmes)

    if not generos_preferidos:
        print("\nNenhum dos filmes informados está na base de dados.")
        return

    recomendacoes = recomendar_filmes(generos_preferidos, filmes, preferencias)

    print("\n🎥 Recomendações de filmes para você:")
    if recomendacoes:
        for filme in recomendacoes:
            print(f"- {filme}")
    else:
        print("Nenhuma recomendação encontrada com base nos seus gostos.")


if __name__ == "__main__":
    main()
