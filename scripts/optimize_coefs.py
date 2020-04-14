from bass.optimization import optimize_region

regions = ["Provence-Alpes-Côte d'Azur", 'Auvergne-Rhône-Alpes',
           'Occitanie', 'Nouvelle-Aquitaine', 'Pays de la Loire', 'Grand Est',
           'Hauts-de-France', 'Bretagne', 'Bourgogne-Franche-Comté',
           'Centre-Val de Loire', 'Île-de-France', 'Normandie']

for region in regions:
    opt = optimize_region(region)
    print(region, opt)
