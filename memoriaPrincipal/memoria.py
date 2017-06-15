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

	def imprimeMemoria(self):
			print self.memoria

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
			self.insertaEnMemoria(byte);
			byte = binascii.hexlify(archivoBinario.read(1))


#end class MemoriaPrincipal