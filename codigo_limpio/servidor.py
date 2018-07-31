import tkinter as tk
import socket 
import threading
# - automatas
# - ia2
# redes 2
# arquitectura
# electiva
# taller grado
# - grafos
# - metodos
# 
class Servidor(threading.Thread):

	encendido = True

	def __init__(self, master=None, nombre_hilo):
		self.encendido = True
		self.nombre_hilo = nombre_hilo
		threading.Thread.__init__(self, name=nombre_hilo, target=Servidor.run)
		self.window = tk.Frame(master)
		self.window.pack()

	def run(self):
		self.execute()

	def execute(self):
		self.mi_servidor = socket.socket()
		self.mi_servidor.bind( ('localhost',8507) )
		self.mi_servidor.listen(5)

		while self.encendido:
			try:
				conexion, addr = self.mi_servidor.accept()
				print("nueva conexion establecida")
				print(addr)
				respuesta = conexion.recv(1024).decode()
				print(respuesta)
				conexion.send(str.encode("hola, te saludo desde el servidor"))
				conexion.close()
			except:
				break

	def close(self):
		print("gato intenta parar")
		self.encendido = False

root = tk.Tk()
s = Servidor(master=root, "Mi servidor")
s.start()
root.mainloop()
