from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import *

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
#se arma el camino de la base de datos
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de
# la entidad estudiante (clase Estudiante)

estudiantes = session.query(Estudiante).all()
#print(estudiantes)
#for e in estudiantes:
#    print(f"{e.id}-{e.apellido}")

# print("--------------------------------------")
# Obtener todos los registros de la clase Modulo
#modulos = session.query(Modulo).all()
#print(modulos)

print("--------------------------------------")
#Obtener todos los registros de la clase Matricula
#En esta consulta se obtiene el listado de todas las matrículas mediante un recorrido de for
matriculas = session.query(Matricula).all()
for m in matriculas:
    print(f"{m.estudiante.nombre}-{m.estudiante.apellido}")
# nombre y apellido del estudiante de cada matrícula

print(matriculas)