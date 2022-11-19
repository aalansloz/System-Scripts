from pathlib import Path
from os import listdir,scandir,walk

#we move the file that is within the path to move to the prior folder

#path_to_move="C:\\Users\\laptop\\Downloads\\JDOWNLOADER"
path_to_move="/mnt/610fa500-e003-430f-b5f8-a5f40b9b8f46/Jdownloader/"
path_to_move=r'{}'.format(path_to_move)
for carpeta in listdir(path_to_move):
	try:
		print(carpeta)
		a=f"{path_to_move}//{carpeta}"
		b=listdir(a)
		Path(f"{a}//{b[0]}").rename(f"{path_to_move}//{b[0]}")
		a=""
	except:
		print("File not found")

	#i remove the previous folder that should now be empty
	os.rmdir(path_to_move)
#faltaria modulo que borre las carpetas luego
