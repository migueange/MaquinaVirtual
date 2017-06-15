#!/usr/bin/python
# -*- coding: utf-8 -*-


class MaquinaVirtual(object):
	"""
		Modela una máquina virtual con una 
	"""
	def __init__(self, memoria, bancoRegistros, alu, cu, archivoBinario, rutaArchivo):
		super(MaquinaVirtual, self).__init__()
		self.memoria = memoria
		self.bancoRegistros = bancoRegistros
		self.alu = alu
		self.cu = cu
		self.archivoBinario = archivoBinario
		self.rutaArchivo = rutaArchivo


	def ejecuta	(self):
		self.cu.decodifica()
		
