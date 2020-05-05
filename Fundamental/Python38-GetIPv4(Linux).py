import subprocess as sp

try:
	op = sp.check_output("""ifconfig wlp6s0|grep "inet "|awk -F'[: ]+' '{ print $4 }'""",shell=True)
	
	sendtext = op.decode().split()[0]
	print (sendtext)
except Exception as e:
	print (str(e))