def throws():
	return 5/0
try:
	throws()
except ZeroDivisionError:
	print ("division by Zero!")
except Exception:
	print("Caught an Exception")
finally:
	print("In finally block for cleanup")