# 1. Läs filen
with open("service_loggar.txt", "r") as fil:
    rader = fil.readlines()

# 2. Funktioner
def sammanfatta(loggar):
    resultat = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for log in loggar:
        if "INFO" in log:
            resultat["INFO"] += 1
        elif "WARNING" in log:
            resultat["WARNING"] += 1
        elif "ERROR" in log:
            resultat["ERROR"] += 1
    return resultat

def hämta_errors(loggar):
    error_lista = []
    for log in loggar:
        if "ERROR" in log:
            error_lista.append(log)
    return error_lista

# 3. Kör och läs resultatet
print("=== Sammanfattning ===")
print(sammanfatta(rader))

print("=== Error-rader ===")
for error in hämta_errors(rader):
    print(error)

#NU VINNER VI MOT AIK