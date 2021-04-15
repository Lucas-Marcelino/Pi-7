import cv2 			# Biblioteca OpenCV
import numpy as nu 	# Biblioteca carrega a imagem que usar função imread
					#

img = cv2.imread('OpenCV_Logo.png', cv2.IMREAD_COLOR) 
# IMREAD_COLOR é uma constante, asssim como IMREAD_GRAYSCALE
# Poderia trocar por 1 ou 0, respectivamente
# Se não colocar a imagem junto do arquivo python, tem que colocar o caminho do arquivo da imagem

cv2.namedWindow('Teste opencv')	# Cria uma janela
cv2.imshow('Teste opencv', img)	# Mostra a janela criada(1º parâmetro) e atribuí a imagem img (2º parâmetro)
cv2.waitKey() 					# Após criar janela com img, aguarda alguma tecla para break
								# waitKey('milisegundos')