import cowsay
import cliente


while True:
    msg = cliente.obtener_mensaje()
    if msg == None:
        continue

    msg_formateado = f"{msg["usuario"]}:{msg["texto"]}"
    cowsay.tux(msg_formateado)