from art import text2art

def edit_new_file():
	inp = input("Enter a dir to file or c?dir to create: ")
	try:
		while True:
			cnts = 0
			lines = []
			if "b?" in inp:
				inp = inp.split("b?")[1]
				with open(inp, "rb") as file:
					print("\n")
					liness = file.readlines()
					cnt = 1
					print("File created\n")
					for line in liness:
						print(f"{cnt}: {line}")
						cnt += 1
					cnts = cnt
			elif "c?" in inp:
				inp = inp.split("c?")[1]
				with open(inp, "w+") as file:
					file.write("# New file")
					print("\n")
					cnt = 1
					liness = ["# New file"]
					for line in liness:
						print(f"{cnt}: {line}")
						cnt += 1
					cnts = cnt
			else:
				with open(inp, "r") as file:
					print("\n")
					liness = file.readlines()
					cnt = 1
					for line in liness:
						print(f"{cnt}: {line}")
						cnt += 1
					cnts = cnt
			lines = liness
			print("\n")
			inps = input("Enter a number of line or E to exit, S to save: ")
			if inps == "E":
				raise Exception("Exit")
			elif inps == "S":
				saveable = ""
				for line in lines:
					saveable += line + "\n"
				if "b?" in inp:
					with open(inp, "wb") as file:
						file.write(saveable)
				else:
					with open(inp, "w") as file:
						file.write(saveable)
				print("Saved!")
			try:
				inps = int(inps)
				if inps == 0 or inps > cnts:
					print("Invalid number of line!")
			except:
				raise Exception("Invalid command!")
	except Exception as e:
		if type(e) == IsADirectoryError: raise Exception("Is a folder!")
		elif type(e) == FileNotFoundError: raise Exception("Invalid directory!")
		elif type(e) == UnicodeDecodeError: raise Exception("File not supported! Try open in bin mode - b?dir")
		else: raise Exception(f"Error occuried - {e}")

def recent_files():
	pass

while True:
	print(text2art("PY;VI"))
	print("\n")
	print("1. Edit a file \n2. Recent files")
	print("\n")
	inp = input("root@pyvi: ")
	try:
		inp = int(inp)
		print("\n")
		if inp == 1: edit_new_file()
		elif inp == 2: recent_files()
		else: raise Exception("Unknown command!")
	except Exception as e:
		print("\n")
		print(f"Error occuried - {e}")
	print("\n")