#!/usr/bin/python
# -*- coding: utf-8 -*

class BancoRegistros(object):
	"""Modela los 14 registros de la máquina"""
	
	def __init__(self):
		super(BancoRegistros, self).__init__()		
		self.registros = []
		for x in xrange(0,14):
			self.registros.append('00')

	def imprimeRegistros(self):
		print self.registros


	def actualizaRegistro(self,numRegistro,valorHex):
		if numRegistro < 0 or numRegistro > 13:			
			print "No existe el registro %d\nCódigo de error: 4" % numRegistro
			sys.exit(0)
		self.registros[numRegistro] = valorHex

	def get(self,numRegistro):
		if numRegistro < 0 or numRegistro > 13:
			print "No existe el registro %d\nCódigo de error: 4" % numRegistro
			sys.exit(0)
		return self.registros[numRegistro]		

	def getContadorPrograma(self):
		"""
			Regrese un entero con la dirección de memoria
		"""		
		return int(self.registros[12],16)

	def setContadorPrograma(self,direccion):
		"""
			Recibe una dirección en decimal y la guarda en el 
			contador de programa en hexadecimal
		"""
		self.registros[12] = hex(direccion)[2:]

	def setStackPointer(self,direccion):
		"""
			Recibe una dirección en decimal y la guarda en el 
			stack pointer en hexadecimal
		"""
		self.registros[13] = hex(direccion)[2:]
