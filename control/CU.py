#!/usr/bin/python
# -*- coding: utf-8 -*


import sys
sys.path.append("..")
from util import util

class ControlUnit(object):
	"""docstring for ControlUnit"""

	def __init__(self,memoria,registros,alu):
		super(ControlUnit, self).__init__()
		self.memoria = memoria
		self.registros = registros
		self.alu = alu
	#end __init__

	def decodifica(self):
		ciclos = 0
		self.registros.setStackPointer(self.memoria.getUltimoIndice());
		while True:
			contadorPrograma =self.registros.getContadorPrograma()
			byte = self.memoria.getFromIndex(contadorPrograma)
			if byte == None:
				print ciclos
				break;
			#add
			if byte == "00":
				params = self.getParamsReg4(contadorPrograma)
				self.alu.add(params[0],params[1],params[2])
				ciclos += 3
			#sub
			elif byte == "01":
				params = self.getParamsReg4(contadorPrograma)
				self.alu.sub(params[0],params[1],params[2])
				ciclos += 4
			#mul
			elif byte == "02":
				params = self.getParamsReg4(contadorPrograma)
				self.alu.mul(params[0],params[1],params[2])
				ciclos += 10
			#div
			elif byte == "03":
				params = self.getParamsReg4(contadorPrograma)
				self.alu.div(params[0],params[1],params[2])
				ciclos += 11
			#fadd
			elif byte == "04":
				params = self.getParamsReg4(contadorPrograma)
				self.alu.fadd(params[0],params[1],params[2])
				ciclos += 4
			#fsub
			elif byte == "05":
				params = self.getParamsReg4(contadorPrograma)
				self.alu.fsub(params[0],params[1],params[2])
				ciclos +=5
			#fmul
			elif byte == "06":
				params = self.getParamsReg4(contadorPrograma)
				self.alu.fmul(params[0],params[1],params[2])
				ciclos += 9
			#fdiv
			elif byte == "07":
				params = self.getParamsReg4(contadorPrograma)
				self.alu.fdiv(params[0],params[1],params[2])
				ciclos += 10
			#and
			elif byte == "08":
				params = self.getParamsReg4(contadorPrograma)
				self.alu.andM(params[0],params[1],params[2])
				ciclos += 1
			#or
			elif byte == "09":
				params = self.getParamsReg4(contadorPrograma)
				self.alu.orM(params[0],params[1],params[2])
				ciclos += 1
			#xor
			elif byte == "0a":
				params = self.getParamsReg4(contadorPrograma)
				self.alu.xorM(params[0],params[1],params[2])
				ciclos += 1
			#not
			elif byte == "0b":
				params = self.getParamsReg3(contadorPrograma)
				self.alu.notM(params[0], params[1])
				ciclos += 1
			#lb
			elif byte == "0c":
				#Obtenemos el valor del registro
				params = self.getParamsReg3(contadorPrograma)
				self.alu.lb(params[0], params[1])
				ciclos += 500
			#lw
			elif byte == "0d":
				#Obtener registro de la memoria
				registroMemoria = self.memoria.getFromIndex(contadorPrograma + 2)
				registroDestino = self.getFromIndex(contadorPrograma +1)

				self.alu.lw(registroMemoria, registroDestino)

			#sb
			elif byte == "0e":
				print "sb"
				ciclos += 700
			#sw
			elif byte == "0f":
				print "sw"
				ciclos += 2100
			#li
			elif byte == "10":
				#Obtener el registro destino del siguiente byte
				registroDestino = self.memoria.getFromIndex(contadorPrograma+1)
				#Obtener la constante a guardar de los siguientes 4 bytes
				valor = self.memoria.getFromIndex(contadorPrograma+2) + self.memoria.getFromIndex(contadorPrograma+3) + self.memoria.getFromIndex(contadorPrograma+4) + self.memoria.getFromIndex(contadorPrograma+5)
				#Ejecutar li
				self.alu.li(registroDestino,valor)
				#Actualizar el contador de programa
				self.registros.setContadorPrograma(contadorPrograma+6)
				ciclos += 1500
			#b
			elif byte == "11":
				#Obtener el registro que tiene la dirección del salto
				registroSalto = self.memoria.getFromIndex(contadorPrograma + 3)
				#Ejecutar b
				self.alu.b(registroSalto)
				ciclos += 1
			#beqz
			elif byte == "12":
				print "beqz"
				ciclos += 4
			#bltz
			elif byte == "13":
				print "bltz"
				ciclos += 5
			#syscall
			elif byte == "14":
				self.alu.syscall(ciclos)
				self.registros.setContadorPrograma(contadorPrograma+4)
				ciclos += 50
			else:
				print "Código de operación inválido\nCódigo de error: 5"
		#end while
	#end decodifica

	def getParamsReg4(self, contadorPrograma):
		regDestino = self.memoria.getFromIndex(contadorPrograma+1)
		regOp1 = self.memoria.getFromIndex(contadorPrograma+2)
		regOp2 = self.memoria.getFromIndex(contadorPrograma+3)
		self.registros.setContadorPrograma(contadorPrograma+4)
		return [regDestino,regOp1,regOp2]

	def getParamsReg3(self, contadorPrograma):
		regDestino = self.memoria.getFromIndex(contadorPrograma +1)
		regOp1 = self.memoria.getFromIndex(contadorPrograma+2)
		self.registros.setContadorPrograma(contadorPrograma+3)
		return [regDestino,regOp1]
