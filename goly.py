import numpy as np
import random as rand


class Goly:
	def __init__(self, alto=3, ancho=3, prob=-1, tabla=""):
		self.alto = alto
		self.ancho = ancho
		self.tabla = np.zeros((alto, ancho), dtype=bool) if tabla == "" else tabla

		for line in range(0, len(self.tabla)):
			for column in range(0, len(self.tabla[line])):
				if rand.random() <= prob:
					self.tabla[line][column] = True

	def __str__(self):
		msg = ""
		msg += "+" + "-"*(3 * len(self.tabla)) + "+\n"
		for line in self.tabla:
			msg += "|"
			for column in line:
				msg += " * " if column else "   "
			msg += "|\n"
		msg += "+" + "-" * (3 * len(self.tabla)) + "+\n"
		return msg

	def isViva(self, fil, col):
		return self.tabla[fil][col]

	def isGameDead(self):
		dead = True
		for line in self.tabla:
			for column in line:
				if column:
					dead = False
		return dead

	def getTotalVecinos(self, fil, col):
		tot_vec = 0
		# Posiciones:
		# | 1 | 2 | 3 |
		# | 4 |   | 6 |
		# | 7 | 8 | 9 |

		# Posición 1
		if fil != 0 and col != 0:
			tot_vec += 1 if self.isViva(fil - 1, col - 1) else 0
		elif fil != 0:
			tot_vec += 1 if self.isViva(fil - 1, self.ancho - 1) else 0
		elif col != 0:
			tot_vec += 1 if self.isViva(self.alto - 1, col - 1) else 0
		else:
			tot_vec += 1 if self.isViva(self.alto - 1, self.ancho - 1) else 0

		# Posición 2
		if fil != 0:
			tot_vec += 1 if self.isViva(fil - 1, col) else 0
		else:
			tot_vec += 1 if self.isViva(self.alto - 1, col) else 0

		# Posición 3
		if fil != 0 and col != self.ancho - 1:
			tot_vec += 1 if self.isViva(fil - 1, col + 1) else 0
		elif fil != 0:
			tot_vec += 1 if self.isViva(fil - 1, 0) else 0
		elif col != self.ancho - 1:
			tot_vec += 1 if self.isViva(self.alto - 1, col + 1) else 0
		else:
			tot_vec += 1 if self.isViva(self.alto - 1, 0) else 0

		# Posición 4
		if col != 0:
			tot_vec += 1 if self.isViva(fil, col - 1) else 0
		else:
			tot_vec += 1 if self.isViva(fil, self.ancho - 1) else 0

		# Posición 6
		if col != self.ancho - 1:
			tot_vec += 1 if self.isViva(fil, col + 1) else 0
		else:
			tot_vec += 1 if self.isViva(fil, 0) else 0

		# Posición 7
		if col != 0 and fil != self.alto - 1:
			tot_vec += 1 if self.isViva(fil + 1, col - 1) else 0
		elif col != 0:
			tot_vec += 1 if self.isViva(0, col - 1) else 0
		elif fil != self.alto - 1:
			tot_vec += 1 if self.isViva(fil + 1, self.ancho - 1) else 0
		else:
			tot_vec += 1 if self.isViva(0, self.ancho - 1) else 0

		# Posición 8
		if fil != self.alto - 1:
			tot_vec += 1 if self.isViva(fil + 1, col) else 0
		else:
			tot_vec += 1 if self.isViva(0, col) else 0

		# Posición 9
		if fil != self.alto - 1 and col != self.ancho - 1:
			tot_vec += 1 if self.isViva(fil + 1, col + 1) else 0
		elif col != self.ancho - 1:
			tot_vec += 1 if self.isViva(0, col + 1) else 0
		elif fil != self.alto - 1:
			tot_vec += 1 if self.isViva(fil + 1, 0) else 0
		else:
			tot_vec += 1 if self.isViva(0, 0) else 0
		
		return tot_vec

	def comprobarCambios(self):
		tmp_table = []
		for line in range(0, len(self.tabla)):
			tmp_table.append([])
			for column in range(0, len(self.tabla[line])):
				vec = self.getTotalVecinos(line, column)
				if vec < 2 or vec > 3:
					tmp_table[line].append(False)  # muere
				elif vec == 3:
					tmp_table[line].append(True)  # nace
				else:
					tmp_table[line].append(self.tabla[line][column])  # permanece
		self.tabla = tmp_table[:]
