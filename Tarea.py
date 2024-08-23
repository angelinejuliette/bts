
miembros=[
    {"nombre":"Hoseok",
    "año_nacimiento":1994},
    {"nombre":"TaeHyung",
    "año_nacimiento":1995},
    {"nombre":"Jin",
    "año_nacimiento":1992},
    {"nombre":"YoonGi",
    "año_nacimiento":1993},
    {"nombre":"NamJoon",
    "año_nacimiento":1994},
    {"nombre":"Jimin",
    "año_nacimiento":1995},
    {"nombre":"JungKook",
    "año_nacimiento":1997}]


miembros_ordenados = sorted(miembros, key=lambda x: x['año_nacimiento'])

for miembro in miembros_ordenados:
    print(f"{miembro['nombre']} - {miembro['año_nacimiento']}")