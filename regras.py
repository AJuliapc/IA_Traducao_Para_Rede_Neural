import csv

with open("regras.csv", mode="w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["A,B -> C"])
    writer.writerow(["~B,C -> D"])
    writer.writerow(["A,~C -> ~D"])
    writer.writerow(["D -> B"])
    writer.writerow(["~A,~D -> ~C"])

print("Arquivo 'regras.csv' gerado com sucesso!")
