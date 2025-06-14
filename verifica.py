import csv


def verifica_regra(premissas, conclusao, entrada, saida, variaveis):
    # Avalia a premissa
    premissa_ok = True
    for p in premissas:
        negado = p.startswith('~')
        var = p.replace('~', '')
        idx = variaveis.index(var)
        valor = entrada[idx]
        if (not negado and valor != 1) or (negado and valor != -1):
            premissa_ok = False
            break

    # Se premissa for verdadeira, testa a conclusão
    if premissa_ok:
        negado = conclusao.startswith('~')
        var = conclusao.replace('~', '')
        idx = variaveis.index(var)
        valor = saida[idx]
        if (not negado and valor == 1) or (negado and valor == -1):
            return True  # Regra satisfeita
        else:
            return False  # Premissa ok, mas conclusão não
    else:
        return None  # Premissa falsa, não avalia


def main():
    with open("saida_resultado.csv") as f:
        reader = csv.reader(f)
        linhas = list(reader)

    headers = linhas[0]
    n = len(headers) // 2
    variaveis = headers[:n]

    dados = []
    for linha in linhas[1:]:
        entrada = list(map(int, linha[:n]))
        saida = list(map(int, linha[n:]))
        dados.append((entrada, saida))

    regras = [
        (["A", "B"], "C"),
        (["~B", "C"], "D"),
        (["A", "~C"], "~D"),
        (["D"], "B"),
        (["~A", "~D"], "~C")
    ]

    for idx, (entrada, saida) in enumerate(dados):
        print(f"\n🧠 Linha {idx + 1}: Entrada={entrada}, Saída={saida}")
        for premissas, conclusao in regras:
            resultado = verifica_regra(premissas, conclusao, entrada, saida, variaveis)
            if resultado is True:
                print(f"✅ Regra {premissas} → {conclusao} satisfeita")
            elif resultado is False:
                print(f"❌ Regra {premissas} → {conclusao} VIOLADA")
            else:
                print(f"➖ Regra {premissas} → {conclusao} não se aplica")

if __name__ == "__main__":
    main()
