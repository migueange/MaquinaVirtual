#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
from util import util
from memoriaPrincipal import memoria
from registros import registros
from control import ALU, CU
from maquina import maquinaVirtual


def main():
	#Leer archivos y parámetros de la línea de comandos
	parametros = util.getParametros(sys.argv)	
	archivoBinario = util.leeArchivoBinario(parametros[1]);	
	#Crear componentes de la máquina
	#Crear memoria 
	memoriaPrincipal = memoria.MemoriaPrincipal(parametros[0])	
	#Cargar programa en memoria
	memoriaPrincipal.cargaInstrucciones(archivoBinario)
	archivoBinario.close()
	#Crear registros
	bancoRegistros = registros.BancoRegistros()
	alu = ALU.ALU(bancoRegistros,memoriaPrincipal)
	cu = CU.ControlUnit(memoriaPrincipal,bancoRegistros,alu)
	#Crear máquina virtual
	maquina = maquinaVirtual.MaquinaVirtual(memoriaPrincipal,bancoRegistros,alu,cu,archivoBinario,parametros[1])
	maquina.ejecuta()
#end main



if __name__ == "__main__":
	main()