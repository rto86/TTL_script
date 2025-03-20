import subprocess

def obtener_ttl(ip):
    try:
        # Ejecuta el comando ping de manera segura
        resultado = subprocess.check_output(["ping", "-n", "1", ip], universal_newlines=True)
        # Busca el valor de TTL en la respuesta del ping
        for linea in resultado.splitlines():
            if "TTL=" in linea:
                ttl = linea.split("TTL=")[-1].split()[0]
                return int(ttl)
        print("No se encontró TTL en la respuesta.")
        return None
    except subprocess.CalledProcessError:
        print("Error al hacer ping a la IP. Verifica que la dirección es válida.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None

def identificar_sistema(ttl):
    if ttl is None:
        print("No se pudo determinar el TTL.")
    elif 0 <= ttl <= 64:
        print("Sistema operativo: Linux")
    elif 65 <= ttl <= 128:
        print("Sistema operativo: Windows")
    elif 129 <= ttl <= 255:
        print("Sistema operativo: Solaris, AIX, Cisco, etc.")
    else:
        print("No se pudo determinar el sistema operativo.")

# Solicita la IP al usuario y procesa el TTL
ip = input("Ingresa la dirección IP: ").strip()
ttl = obtener_ttl(ip)
if ttl is not None:
    print(f"TTL detectado: {ttl}")
identificar_sistema(ttl)
