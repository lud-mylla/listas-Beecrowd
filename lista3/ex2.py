print("Digite sua nota do primeiro bimestre: ")

n1 = float(input())
n1_formatado =f" {n1:2f}"

print("Digite sua nota do segundo bimestre: ")

n2 = float(input())
n2_formatado =f" {n2:2f}"

media = (n1 * 3.5 + n2 * 7.5) / 11
print(f"Média = {media:.5f}")

