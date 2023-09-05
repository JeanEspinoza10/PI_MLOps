from datetime import datetime

def convertir_fecha(fecha_str):
    # Convierte una fecha en formato "Posted November 5, 2011" en un objeto datetime
    partes = fecha_str.split(" ")
    mes = partes[1]
    dia = int(partes[2][:-1])
    año = int(partes[3].strip("."))  # Elimina el punto al final del año
    fecha_dt = datetime.strptime(f"{año}-{mes}-{dia}", "%Y-%B-%d")
    return fecha_dt.date()


