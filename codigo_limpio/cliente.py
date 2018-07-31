import socket 
import tkinter as tk

class Cliente(tk.Frame):
	
	def __init__(self, master=None):
		self.send_text = ""
		self.count = 0
		super().__init__(master)
		self.pack()
		self.componentes()

	def componentes(self):
		self.message = tk.Label(self, text="Mensaje Recibido:")
		self.message.pack(padx=25, pady=10)

		self.cuenta = tk.Label(self, text=str(self.count))
		self.cuenta.pack(padx=25, pady=10)

		self.mess_send = tk.Entry(self, textvar=self.send_text)
		self.mess_send.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

		self.contador = tk.Button(self)
		self.contador["text"] = "Contar"
		self.contador["command"] = self.handler_cliente
		self.contador.pack(side="top", padx=100, pady=5)

		self.cliente = tk.Button(self)
		self.cliente["text"] = "Enviar Mensaje"
		self.cliente["command"] = self.handler_cliente
		self.cliente.pack(side="top", padx=100, pady=5)

	def handler_cliente(self):
		try:
			mi_socket  = socket.socket()
			mi_socket.connect( ('localhost', 8507) )
			saludo = "hola desde el cliente"
			# mi_socket.send(str.encode(self.mess_send.get()))
			mi_socket.send(str.encode("c"))
			respuesta = mi_socket.recv(1024).decode()
			print(respuesta)
			if respuesta == "c":
				self.contar()
			self.message['text'] = respuesta;
			
			mi_socket.close()
		except:
			self.message['text'] = "ERROR EN LA CONEXION!!!!";
	
	def contar(self):
		self.count = self.count + 1
		self.cuenta['text'] = str(self.count);


root = tk.Tk()
client = Cliente(master=root)
client.mainloop() 

