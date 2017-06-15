#!/usr/bin/python
# -*- coding: utf-8 -*

import sys

class ALU(object):
	"""docstring for ALU"""
	def __init__(self,bancoRegistros):
		super(ALU, self).__init__()
		self.bancoRegistros = bancoRegistros

	def add(self,numRegDestinoHex,numRegOp1,numRegOp2):
		"""
			Suma el valor de dos registros y lo almacena en numRegDestinoHex
		"""
		op1 = self.bancoRegistros.get(int(numRegOp1,16))
		op2 = self.bancoRegistros.get(int(numRegOp2,16))
		suma = int(op1,16) + int (op2,16)
		self.bancoRegistros.actualizaRegistro(int(numRegDestinoHex,16),hex(suma)[2:])

	def fadd(self,numRegDestinoHex, numRegOp1, numRegOp2):
		"""
			Suma el valor de dos registros flotantes y lo almacena en numRegDestinoHex
		"""
		op1 = self.bancoRegistros.get(hex_to_float(numRegOp1))
		op1 = self.bancoRegistros.get(hex_to_float(numRegOp1))
		suma = op1 + op2
		self.bancoRegistros.actualizaRegistro(float_to_hex(numRegDestinoHex), hex_to_float(suma))

	def sub(self,numRegDestinoHex,numRegOp1,numRegOp2):
		"""
			Resta el valor de dos registros y lo almacena en numRegDestinoHex
		"""
		op1 = self.bancoRegistros.get(int(numRegOp1,16))
		op2 = self.bancoRegistros.get(int(numRegOp2,16))
		resta = int(op1,16) - int (op2,16)
		self.bancoRegistros.actualizaRegistro(int(numRegDestinoHex,16),hex(resta)[2:])

	def fsub(self, numRegDestinoHex,numRegOp1,numRegOp2):
		"""
			Resta el valor de dos registros flotantes y lo almacena en numRegDestinoHe
		"""
		op1 = self.bancoRegistros.get(hex_to_float(numRegOp1))
		op2 = self.bancoRegistros.get(hex_to_float(numRegOp2))
		resta = op1 - op2
		self.bancoRegistros.actualizaRegistro(hex_to_float(numRegDestinoHex),float_to_hex(resta))

	def mul(self,numRegDestinoHex,numRegOp1,numRegOp2):
		"""
			Multiplica el valor de dos registros y lo almacena en numRegDestinoHex
		"""
		op1 = self.bancoRegistros.get(int(numRegOp1,16))
		op2 = self.bancoRegistros.get(int(numRegOp2,16))
		mult = int(op1,16) * int (op2,16)
		self.bancoRegistros.actualizaRegistro(int(numRegDestinoHex,16),hex(mult)[2:])

	def fmul(self, numRegDestinoHex,numRegOp1,numRegOp2):
		"""
			Multiplica el valor de los registros flotantes y lo almacena en numRegDestinoHex
		"""
		op1 = self.bancoRegistros.get(float_to_hex(numRegOp1))
		op2 = self.bancoRegistros.get(float_to_hex(numRegOp2))
		mult = op1 * op2
		self.bancoRegistros.actualizaRegistro(float_to_hex(numRegDestinoHex), hex_to_float(mult))

	def div(self,numRegDestinoHex,numRegOp1,numRegOp2):
		"""
			Divide el valor de dos registros y lo almacena en numRegDestinoHex
		"""
		op1 = self.bancoRegistros.get(int(numRegOp1,16))
		op2 = self.bancoRegistros.get(int(numRegOp2,16))
		if int(op2,16) == 0:
			print "División entre cero\nCódigo de error: 1"
			sys.exit(0)
		division = int (int(op1,16) / int (op2,16))
		self.bancoRegistros.actualizaRegistro(int(numRegDestinoHex,16),hex(division)[2:])

	def fdiv(self,numRegDestinoHex,numRegOp1,numRegOp2):
		"""
			Divide el valor de dos registros flotantes y lo almacena en numRegDestinoHex
		"""
		op1 = self.bancoRegistros.get(hex_to_float(numRegOp1))
		op2 = self.bancoRegistros.get(hex_to_float(numRegOp2))
		if hex_to_float(op2) == 0.0:
			print "Division entre cero \nCódigo de error: 1"
			sys.exit(0)
		division = op1 / op2
		self.bancoRegistros.actualizaRegistro(float_to_hex(numRegDestinoHex),float_to_hex(division))

	def andM(self,numRegDestinoHex,numRegOp1,numRegOp2):
		"""
			Hace and a nivel de bits de dos registros y lo almacena en numRegDestinoHex
		"""
		op1 = int(self.bancoRegistros.get(int(numRegOp1,16)),16)
		op2 = int(self.bancoRegistros.get(int(numRegOp2,16)),16)
		andR = int(bin(op1)[2:],2) & int(bin(op2)[2:],2)
		self.bancoRegistros.actualizaRegistro(int(numRegDestinoHex,16),hex(andR)[2:])

	def orM(self,numRegDestinoHex,numRegOp1,numRegOp2):
		"""
			Hace or a nivel de bits de dos registros y lo almacena en numRegDestinoHex
		"""
		op1 = int(self.bancoRegistros.get(int(numRegOp1,16)),16)
		op2 = int(self.bancoRegistros.get(int(numRegOp2,16)),16)
		orR = int(bin(op1)[2:],2) | int(bin(op2)[2:],2)
		self.bancoRegistros.actualizaRegistro(int(numRegDestinoHex,16),hex(orR)[2:])

	def xorM(self,numRegDestinoHex,numRegOp1,numRegOp2):
		"""
			Hace xor a nivel de bits de dos registros y lo almacena en numRegDestinoHex
		"""
		op1 = int(self.bancoRegistros.get(int(numRegOp1,16)),16)
		op2 = int(self.bancoRegistros.get(int(numRegOp2,16)),16)
		xorR = int(bin(op1)[2:],2) ^ int(bin(op2)[2:],2)
		self.bancoRegistros.actualizaRegistro(int(numRegDestinoHex,16),hex(xorR)[2:])

	def notM(self, numRegDestinoHex, numRegOp1):
		op1 = int(self.bancoRegistros.get(int(numRegOp1,16)),16)
		notR = not int(bin(op1)[2:],2)
		self.bancoRegistros.actualizaRegistro(int(numRegDestinoHex,16), hex(notR)[2:])


	def lb(self,numRegisDestino, numRegOp1):
		self.bancoRegistros.actualizaRegistro(int(numRegisDestino,16),valor)

	def lw(self, numRegisDestino,numRegOp1):
		op1 = self.bancoRegistros.get(int(numRegOp1,16))
		lwX = numRegOp1
		self.bancoRegistros.actualizaRegistro(int,(numRegisDestino,16), hex(lwX)[2:])

	def sw(self,numRegisDestino,numRegOp1):
		print "Sin hacer aun"

	def li(self,numRegistro, valor):
		"""
			Carga una costante en un registro
		"""
		self.bancoRegistros.actualizaRegistro(int(numRegistro,16),valor)

	def b(self,numRegistroSaltoHex):
		"""
			Realiza un salto incondicional
		"""
		valor = self.bancoRegistros.get(int(numRegistroSaltoHex,16))
		self.bancoRegistros.actualizaRegistro(13,valor)
