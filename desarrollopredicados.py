# UNIVERSO

universo = [
    "David", "Fabian", "Erick",
    "Ana", "Carlos", "Maria",
    "Laura", "Roberto", "Miguel",
    "Programacion", "Programacion_2",
    "Redes", "Bases_de_Datos", "Ingles",
    "Sistemas_Computacionales", "Administracion",
    "A101", "B202", "C303"
]
# PREDICADOS DE LA ACTIVIDAD ANTERIOR

estudiantes = {
    "David", "Fabian", "Erick",
    "Ana", "Carlos", "Maria"
}

profesores = {
    "Laura", "Roberto", "Miguel"
}

materias = {
    "Programacion",
    "Programacion_2",
    "Redes",
    "Bases_de_Datos",
    "Ingles"
}

carreras = {
    "Sistemas_Computacionales",
    "Administracion"
}

salones = {
    "A101", "B202", "C303"
}


# Relaciones de la actividad anterior

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

# PREDICADOS

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

# DATOS PARA LAS REGLAS

# Alumnos inscritos en Programacion
# Se usan tres alumnos diferentes, como en el ejemplo de clase.

inscritos = {
    ("David", "Programacion"),
    ("Fabian", "Programacion"),
    ("Erick", "Programacion")
}


# Calificaciones

calificaciones = {
    ("Carlos", "Ingles"): 65,
    ("Ana", "Programacion"): 60
}


# Materias seriadas

seriadas = {
    ("Programacion", "Programacion_2")
}


# Entrada a la universidad con carro

entran_con_carro = {
    "Ana"
}

credenciales = {
    "Ana"
}

gafetes = set()


# Alumnos que no realizaron su inscripción
# durante el periodo correspondiente

no_inscritos_periodo = {
    "Carlos"
}

# REGLA 1
# MATERIA ACTIVA

def materia_activa(y):
    alumnos = [
        x for x, materia_inscrita in inscritos
        if materia_inscrita == y
    ]

    return (
        len(alumnos) >= 3
        and alumnos[0] != alumnos[1]
        and alumnos[0] != alumnos[2]
        and alumnos[1] != alumnos[2]
    )

# REGLA 2
# NO APRUEBA UNA MATERIA

def no_aprueba(x, y):
    return (
        estudiante(x)
        and (x, y) in calificaciones
        and calificaciones[(x, y)] < 70
    )

# REGLA 3
# MATERIA SERIADA

def no_puede_cursar_siguiente(x, y, z):
    return (
        estudiante(x)
        and (y, z) in seriadas
        and (x, y) in calificaciones
        and calificaciones[(x, y)] < 70
    )

# REGLA 4
# ENTRADA CON CARRO

def puede_entrar_con_carro(x):
    return (
        estudiante(x)
        and x in entran_con_carro
        and (x in credenciales or x in gafetes)
    )

# REGLA 5
# CARGA ACADEMICA

def no_puede_tomar_carga(x):
    return (
        estudiante(x)
        and x in no_inscritos_periodo
    )

# CONSULTAS POSITIVAS

print("==========================================")
print("     REGLAS - CONTEXTO UNIVERSIDAD")
print("==========================================")


print("\nConsulta 1:")
print("materia_activa(Programacion)")
print("Resultado:", materia_activa("Programacion"))


print("\nConsulta 2:")
print("no_aprueba(Carlos, Ingles)")
print("Resultado:", no_aprueba("Carlos", "Ingles"))


print("\nConsulta 3:")
print("no_puede_cursar_siguiente(Ana, Programacion, Programacion_2)")
print(
    "Resultado:",
    no_puede_cursar_siguiente(
        "Ana",
        "Programacion",
        "Programacion_2"
    )
)


print("\nConsulta 4:")
print("puede_entrar_con_carro(Ana)")
print("Resultado:", puede_entrar_con_carro("Ana"))


print("\nConsulta 5:")
print("no_puede_tomar_carga(Carlos)")
print("Resultado:", no_puede_tomar_carga("Carlos"))
