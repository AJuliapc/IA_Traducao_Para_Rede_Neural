import csv
import torch
import torch.nn as nn


def parse_rule(line):
    line = line.replace(" ", "").replace('"', '')
    antecedent, consequent = line.split("->")
    inputs = antecedent.split(",")
    return inputs, consequent


def build_vocab(rules):
    symbols = set()
    for inputs, output in rules:
        for i in inputs:
            symbols.add(i.replace("~", ""))
        symbols.add(output.replace("~", ""))
    return sorted(symbols)


def rule_to_weight(inputs, output, vocab):
    weights = torch.zeros(len(vocab))
    bias = -len(inputs) + 0.5
    for symbol in inputs:
        idx = vocab.index(symbol.replace("~", ""))
        weights[idx] = -1.0 if "~" in symbol else 1.0
    out_idx = vocab.index(output.replace("~", ""))
    out_sign = -1.0 if "~" in output else 1.0
    return weights, bias, out_idx, out_sign


class CILPNet(nn.Module):
    def __init__(self, size, rules):
        super().__init__()
        self.size = size
        self.rules = rules
        self.weights = torch.zeros((len(rules), size))
        self.biases = torch.zeros(len(rules))
        self.out_map = []
        for i, (w, b, out_idx, out_sign) in enumerate(rules):
            self.weights[i] = w
            self.biases[i] = b
            self.out_map.append((i, out_idx, out_sign))

    def forward(self, x, max_iters=20, verbose=False):
        current = x.clone()

        for step in range(max_iters):
            hidden = torch.sign(torch.matmul(self.weights, current) + self.biases)
            hidden = torch.clamp(hidden, min=0)
            out = current.clone()

            for hid_idx, out_idx, sign in self.out_map:
                if hidden[hid_idx] > 0:
                    out[out_idx] = 1.0 * sign

            if verbose:
                print(f"Step {step + 1}: {out.tolist()}")

            if torch.equal(out, current):
                break

            current = out

        return current


def run_cilp(regras_csv, entradas_csv, saida_csv, verbose=False):
    with open(regras_csv, newline='') as f:
        reader = csv.reader(f)
        rules = [parse_rule(row[0]) for row in reader if row]

    vocab = build_vocab(rules)
    rule_weights = [rule_to_weight(i, o, vocab) for i, o in rules]

    model = CILPNet(len(vocab), rule_weights)

    with open(entradas_csv, newline='') as f:
        reader = csv.reader(f)
        headers = next(reader)
        linhas = [list(map(int, row)) for row in reader]

    with open(saida_csv, mode="w", newline='') as f_out:
        writer = csv.writer(f_out)
        writer.writerow(headers + vocab)

        for linha in linhas:
            x = torch.tensor(linha, dtype=torch.float)
            output = model(x, verbose=verbose)
            output_logic = [int(y.item()) for y in output]
            writer.writerow(linha + output_logic)

    print(f"Resultados salvos em '{saida_csv}'.")


if __name__ == "__main__":
    run_cilp("regras.csv", "entradas_logicas.csv", "saida_resultado.csv", verbose=False)
