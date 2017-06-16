#!/usr/bin/python
# -*- coding: utf-8 -*-

import binascii, sys


class MemoriaPrincipal(object):
	"""
		Modela la memoria principal con un tamaño dado por el usuario.
		Si el tamaño <= 0 se inicia en 2048 bytes.
	"""

	def __init__(self, tamanioInicial):
		super(MemoriaPrincipal, self).__init__()
		self.tamanioInicial = (tamanioInicial,2048)[tamanioInicial <= 0]
		self.memoria = []
		self.ultima_posicion_inicio = 0
		self.espacios_vacios = 0
		for x in xrange(0,tamanioInicial):
			self.memoria.append(None)
			self.espacios_vacios+=1
			
	def insertaEnMemoria(self,byte):
		if self.espacios_vacios <= 0:
			print "Memoria Agotada\nCódigo de error: 3"
			sys.exit(0)
		self.memoria[self.ultima_posicion_inicio] = byte
		self.ultima_posicion_inicio+=1
		self.espacios_vacios-=1;

	def insertaEnIndice(self,byte,indice):		
		if self.espacios_vacios <= 0 or indice > self.tamanioInicial:
			print "Memoria Agotada\nCódigo de error: 3"
			sys.exit(0)
		self.memoria[indice] = byte
		self.espacios_vacios-=1;

	def getUltimoIndice(self):
		return self.tamanioInicial - 1

	def imprimeMemoria(self):
			print self.memoria

	def imprimeMemoriaArchivo(self):
		str = ""
		for x in xrange(0,self.tamanioInicial):
			str += self.memoria[x] + "\n" if self.memoria[x] != None else "None\n"
		f = open("memoria.txt","w")
		f.write(str)
		f.close()

	def get(inicio,fin):
		if(fin > inicio):
			sys.exit(0)
		return self.memoria[inicio:fin]

	def getFromIndex(self,i):
		if i > self.tamanioInicial:
			sys.exit(0)
		return self.memoria[i]

	def cargaInstrucciones(self,archivoBinario):
		byte = binascii.hexlify(archivoBinario.read(1))
		while byte != "":
			self.insertaEnMemoria("0x" + byte);
			byte = binascii.hexlify(archivoBinario.read(1))

	def getConstantes(self, i):
		"""
			Lee las constantes hasta encontrar un caracter nulo \0 o '00'
		"""
		if i > self.tamanioInicial or i < 0:			
			sys.exit(0)
		constante = ""
		byte = ""
		while byte != '0x00':
			byte = self.memoria[i]
			constante += byte[2:]
			i+=1
		return constante

#end class MemoriaPrincipal