"""
Button server.
Run a server listening for button presses. When discovered, communicate the press out to the 
(local) server.
"""
import sys
import socket
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)


HOST = 'localhost' 
PORT = 8000 
SIZE = 1024 


def doButtonPressed(button):
	# * "side:A,button:B,press:C", where A=1 or 2; B=1 or 2; C=single or double
	# * "reset". In this case, we expect the scorecard to reset itself.

	print 'Sending: ' + button
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.connect((HOST,PORT))
	s.send(button + '\r\n')
	data = s.recv(SIZE)
	s.close()

def main():
	print "Starting loop..."

	bA1pressed = False
	bA2pressed = False
	bB1pressed = False
	bB2pressed = False

	while True:
		if (GPIO.input(12) == GPIO.LOW):
			if bA1pressed == False:
				doButtonPressed('side:A,button:1,press:single')
				bA1pressed = True
		elif (GPIO.input(16) == GPIO.LOW):
			if bA2pressed == False:
				doButtonPressed('side:A,button:2,press:single')
				bA2pressed = True
		elif (GPIO.input(17) == GPIO.LOW):
			if bB1pressed == False:
				doButtonPressed('side:B,button:1,press:single')
				bB1pressed = True
		elif (GPIO.input(26) == GPIO.LOW):
			if bB2pressed == False:
				doButtonPressed('side:B,button:2,press:single')
				bB2pressed = True
		else:
			bA1pressed = False
			bA2pressed = False
			bB1pressed = False
			bB2pressed = False
		time.sleep(0.05)

if __name__ == '__main__':
    main()