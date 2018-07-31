import tkinter as tk
from datetime import datetime
import threading
import socket
# from servidor import Servidor

class MainMenu(tk.Frame):

	def __init__(self, master=None):
		super().__init__(master)
		self.send_text = ""
		self.count = 0
		self.pack()
		self.encendido = True;
		self.createComponents()

	def createComponents(self):
		self.label = tk.Label(self, text=str(self.count))
		self.label.pack(padx=30, pady=30)

		self.mess_send = tk.Entry(self, textvar=self.send_text)
		self.mess_send.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

		self.contador = tk.Button(self)
		self.contador["text"] = "Contar"
		self.contador["command"] = self.empezar_conteo
		self.contador.pack(side="top", padx=100, pady=5)

		self.cliente = tk.Button(self)
		self.cliente["text"] = "Iniciar Servidor"
		self.cliente["command"] = self.handler_cliente
		self.cliente.pack(side="top", padx=100, pady=5)

		self.servidor = tk.Button(self)
		self.servidor["text"] = "Cerrar Servidor"
		self.servidor["command"] = self.cerrar_servidor
		# self.servidor.visible = False
		self.servidor.pack(side="top", padx=100, pady=5)
		self.servidor.configure(state=tk.DISABLED)

	def empezar_conteo(self):
		self.count = self.count + 1
		self.label["text"] = str(self.count)

	def handler_cliente(self):
		# print("gato")
		# self.server = Servidor("Mi servidor")
		# self.server.start()
		self.servidor.configure(state=tk.NORMAL)
		hilo = threading.Thread(target=self.iniciar_servidor)
		hilo.start()

	def iniciar_servidor(self):
		self.mi_servidor = socket.socket()
		self.mi_servidor.bind( ('localhost',8507) )
		self.mi_servidor.listen(5)

		while self.encendido:
			try:
				conexion, addr = self.mi_servidor.accept()
				# print("nueva conexion establecida")
				print(addr)
				respuesta = conexion.recv(1024).decode()
				if respuesta == "c":
					self.empezar_conteo()
				print(respuesta)
				# self.label["text"] = respuesta
				conexion.send(str.encode(self.mess_send.get()))
				conexion.close()
				# print("muere el servidor")
			except:
				break

	def cerrar_servidor(self):	
		self.encendido = False
		self.servidor.configure(state=tk.DISABLED)

	def contar():
		while True:
			time.sleep(1)
			# count++
			self.label["text"] = str(self.count)

root = tk.Tk()
menu = MainMenu(master=root)
menu.mainloop()