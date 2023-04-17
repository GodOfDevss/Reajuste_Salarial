print('Reajuste Salarial')

sa = float(input('Digite o Salario:'))

if sa < 500:
    ns = sa * 1.15
else:
    if sa <= 1000:
        ns = sa * 1.10
    else:
        ns = sa * 1.08
print(ns)
