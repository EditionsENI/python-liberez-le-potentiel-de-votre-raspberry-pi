l_prix = {"pomme": 2, "banane": 2.5, "tomate": 3.15}

l_achat = {"pomme": 5, "tomate": 1}

budget_maxi = 15

prix_tot = 0

for elt in l_achat:
    prix_kg = l_prix[elt]
    quant_achat = l_achat[elt]
    prix_tot += prix_kg * quant_achat

if prix_tot < budget_maxi and prix_tot < 0.95 * budget_maxi:
    print("Coût achat compatible budget")

elif prix_tot < budget_maxi and prix_tot > 0.95 * budget_maxi:
    print("Coût critique : 95% du budget")

else:
    print("Hors Budget")

print("Le coût total est : ", prix_tot)
