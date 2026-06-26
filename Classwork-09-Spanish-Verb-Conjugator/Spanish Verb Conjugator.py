pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

verbo = input("Ingrese verbo: ")

stem = verbo[:-2]
ending = verbo[-2:]

lista_sufijos = terminaciones[ending]

for i in range(len(pronombres)):
    pronoun = pronombres[i]
    sufijo = lista_sufijos[i]
    print(f"{pronoun} {stem}{sufijo}")


    