universo = [
    "Ana", "Carlos", "Maria", "Laura", "Roberto", "Miguel",
    "Programacion", "Redes", "Bases_de_Datos", "Ingles",
    "Sistemas_Computacionales", "Administracion", "A101", "B202", "C303"
]

estudiantes = {"Ana", "Carlos", "Maria"}
profesores = {"Laura", "Roberto", "Miguel"}
materias = {"Programacion", "Redes", "Bases_de_Datos", "Ingles"}
carreras = {"Sistemas_Computacionales", "Administracion"}
salones = {"A101", "B202", "C303"}

cursan = {
    ("Ana", "Programacion"),
    ("Carlos", "Redes"),
    ("Maria", "Bases_de_Datos")
}

imparten = {
    ("Laura", "Programacion"),
    ("Roberto", "Redes"),
    ("Miguel", "Bases_de_Datos")
}

# 7 predicados seleccionados
def estudiante(x):
    return x in estudiantes

def profesor(x):
    return x in profesores

def materia(x):
    return x in materias

def carrera(x):
    return x in carreras

def salon(x):
    return x in salones

def cursa(x, y):
    return (x, y) in cursan

def imparte(x, y):
    return (x, y) in imparten

# Consultas: una positiva y una negativa por predicado
consultas = [
    ("estudiante(Ana)", estudiante("Ana")),
    ("estudiante(Laura)", estudiante("Laura")),
    ("profesor(Laura)", profesor("Laura")),
    ("profesor(Ana)", profesor("Ana")),
    ("materia(Redes)", materia("Redes")),
    ("materia(Ana)", materia("Ana")),
    ("carrera(Sistemas_Computacionales)", carrera("Sistemas_Computacionales")),
    ("carrera(Programacion)", carrera("Programacion")),
    ("salon(A101)", salon("A101")),
    ("salon(Ana)", salon("Ana")),
    ("cursa(Ana, Programacion)", cursa("Ana", "Programacion")),
    ("cursa(Ana, Redes)", cursa("Ana", "Redes")),
    ("imparte(Laura, Programacion)", imparte("Laura", "Programacion")),
    ("imparte(Ana, Programacion)", imparte("Ana", "Programacion"))
]

print("=== ACTIVIDAD DE PREDICADOS - UNIVERSIDAD ===")
print("\nUNIVERSO:")
for elemento in universo:
    print("-", elemento)

print("\nRESULTADOS DE LAS CONSULTAS:")
for consulta, resultado in consultas:
    print(f"{consulta} -> {resultado}")