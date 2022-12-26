

def calc(income):
    xadamat = income // 17
    karabay_aw_u_molida = income // 85 + income // 17
    xwardn_hatucho = income // 8.5 + income // 5.6
    rem = income - (xadamat + xwardn_hatucho + karabay_aw_u_molida)
    print(f"your income is {rem}$")
    print(f"xadamat:{xadamat}$, karabay aw u molida:{karabay_aw_u_molida}$, xwardn u hatucho:{xwardn_hatucho}$")


calc(int(input(">")))
