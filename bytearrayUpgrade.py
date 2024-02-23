int = [1, 2, 3, 4]
bytArr = bytearray(int)

for byte in bytArr:
	print(bytArr[byte-1])
	bytArr[byte-1] = bytArr[byte-1] + 1

for bytes in bytArr:
	print(bytArr[byte-1])