#!/usr/bin/env python
# -*- coding: utf-8 -*-

import binascii,struct

#Este archivo contiene métodos que son útiles para todas las clases.


def getParametros(argv):
	"""
		Obtiene los parámetros de la línea de comandos
	"""
	if len(argv) <= 1 or len(argv) > 4:
		print "No se especificó un archivo binario"
		sys.exit(0)
	tamanioMemoria = 0
	rutaArchivo = ""
	if argv[1] == "-m":
		try:
			tamanioMemoria = int(argv[2])
			rutaArchivo = argv[3]
		except ValueError:
			print "Error: Ingrese un valor válido de tamaño de memoria principal"
			sys.exit(0)
		except IndexError:
			print "No se especificó un archivo binario"
			sys.exit(0)
	else:
		try:
			rutaArchivo = argv[1]
		except IndexError:
			print "No se especificó un archivo binario"
			sys.exit(0)
	return [tamanioMemoria,rutaArchivo]

def leeArchivoBinario(rutaArchivo):
	"""
		Lee un archivo en modo binario
	"""
	try:
		return open(rutaArchivo,"rb")
	except IOError:
		print "Ocurrió un error al leer el archivo o el archivo no existe"
		sys.exit(0)

def getTotalBytes(rutaArchivo):
	i = 0
	try:
		archivoBinario = open(rutaArchivo,"rb")
		byte = archivoBinario.read(1)
		while byte != "":
			i+=1
			byte = archivoBinario.read(1)
		archivoBinario.close()
		return i
	except IOError:
		print "Ocurrió un error al leer el archivo o el archivo no existe"
		sys.exit(0)

def float_to_hex(f):
	"""
		Convierte un flotante a hexadecimal
	"""
	return hex(struct.unpack('<I', struct.pack('<f', f))[0])
	
def hex_to_float(h):
	"""
		Convierte un hexadecimal a un flotante
	"""
	return struct.unpack('!f', h[2:].decode('hex'))[0]
