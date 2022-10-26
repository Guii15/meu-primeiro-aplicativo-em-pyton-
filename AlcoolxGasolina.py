alcool = float(input("digete o valor do alcool"))
gasolina = float(input("digete o valor da gasolina"))
formula = alcool/gasolina

print("resultado do calculo: ", formula)
if formula <= 0.70:
    print("compensa alcool")
else:
    print("compensa gasolina")