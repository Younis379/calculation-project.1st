def calc(income, aw, karaba, xwardn, hatucho):
    remaining = income - (aw + karaba + xwardn + hatucho)
    if dol_din == 'dollar':
        print(f"dahati to:{remaining}$")
    elif dol_din == 'dinar':
        print(f"dahati to:{remaining} dinar")


dol_din = input("(dollar) yan (dinar)").lower()
calc(int(input("dahat:")), int(input("aw:")), int(input("karaba:")), int(input("xwardn:")),
     int(input("hatucho:")))
