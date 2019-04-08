import RPi.GPIO as GPIO
import time
import maestro

class rcCar():

	class USArray():
		def __init__(self):
			self.USleftOut = 27
			self.USleftIn = 22

			self.USfrontOut = 23
			self.USfrontIn = 24

			self.USrightOut = 10
			self.USrightIn = 9
		def initialize(self):
			GPIO.setup(self.USleftOut, GPIO.OUT)
			GPIO.setup(self.USfrontOut, GPIO.OUT)
			GPIO.setup(self.USrightOut, GPIO.OUT)

                	GPIO.setup(self.USleftIn, GPIO.IN)
			GPIO.setup(self.USfrontIn, GPIO.IN)
			GPIO.setup(self.USrightIn, GPIO.IN)

	def __init__(self):
		#Pines Ruedas Motrices:
		self._forwardEngine1 = 2
		self._forwardEngine2 = 3

		self._backwardEngine1 = 4
		self._backwardEngine2 = 17

		#Pin servomotor encargado de la direccion:
		self._steeringServo = 2 #pin 2 of pololu

		#Infrared

		##Distance consts:
		self._a = 6787.0
		self._b = 3.0
		self._c = 4.0
		##Pines:
		self._forwardIR = 0
		self._backwardIR = 5
		##Object Pololu:
		self._pololu = maestro.Controller() #create object of Controller class

		#Ultrasounds
                self._USarray = self.USArray() # create an object that contains parameters of three US sensors
		self._soundVelocity = 343 # sound velocity in m/s

		#Configuramos pines
		self._initialize()

		#Object to move the servo to 50 pulses per second
		#self._servo = GPIO.PWM(self._steeringServo, 50)

	def __del__(self):
		self.move(0, 0)
		time.sleep(1)


	def move(self, motionstate, turndegrees):
		'''
		Controls car movement
		@type motionstate: int
		@type turnstate: int

		@param motionstate:
		-1: go backward
		0: stop
		1: go forward

		@param turnstate: 45-135
		'''

		error = False
		minDegrees = 45
		maxDegrees = 135

		if(motionstate == -1):
			self._goBackward()
		elif(motionstate == 0):
			self.stop()
		elif(motionstate == 1):
			self._goForward()
		else:
			error = True
		if(turndegrees >= minDegrees and turndegrees <= maxDegrees):
			self._turnFrontWheels(turndegrees)
		else:
			error = True
		if(error):
			self._wheelsException()

	def stop(self):
		'''
		Does robot stop
		'''

		GPIO.output(self._forwardEngine1, 0)
                GPIO.output(self._forwardEngine2, 0)
                GPIO.output(self._backwardEngine1, 0)
                GPIO.output(self._backwardEngine2, 0)

	def readIR(self):
		'''
		returns distance values of forward and backward infrared sensors
		'''
		return self._distIR(self._forwardIR), self._distIR(self._backwardIR)

	def readUS(self):
		'''
		returns distance values of three ultrasounds sensor
		'''
		leftDist = self._distUS(self._USarray.USleftIn, self._USarray.USleftOut)
		frontDist = self._distUS(self._USarray.USfrontIn, self._USarray.USfrontOut)
		rightDist = self._distUS(self._USarray.USrightIn, self._USarray.USrightOut)

		return leftDist, frontDist, rightDist

	#PRIVATE METHODS

	def _initialize(self):
                '''
                Initialize the robot setup
                '''

                GPIO.setmode(GPIO.BCM)
                GPIO.setwarnings(False)
                GPIO.setup(self._steeringServo, GPIO.OUT)
                GPIO.setup(self._forwardEngine1, GPIO.OUT)
                GPIO.setup(self._forwardEngine2, GPIO.OUT)
                GPIO.setup(self._backwardEngine1, GPIO.OUT)
                GPIO.setup(self._backwardEngine2, GPIO.OUT)
		GPIO.setup(self._forwardIR, GPIO.IN)
		self._USarray.initialize()
                print "RC Car Initialized"

	def _goForward(self):
                '''
                Does robot go forward
                '''

                GPIO.output(self._forwardEngine1, 1)
                GPIO.output(self._forwardEngine2, 1)
                GPIO.output(self._backwardEngine1, 0)
                GPIO.output(self._backwardEngine2, 0)

        def _goBackward(self):
                '''
                Does robot go backward
                '''

                GPIO.output(self._forwardEngine1, 0)
                GPIO.output(self._forwardEngine2, 0)
                GPIO.output(self._backwardEngine1, 1)
                GPIO.output(self._backwardEngine2, 1)

        def _turnFrontWheels(self, degrees):
                '''
                Does front wheels turn right or left
                @type degrees: int
                @param degrees: 45-135
                '''
		minDegrees = 45
		maxDegrees = 135

		minComm = 5000
		maxComm = 6600
		if(degrees == 90):
			command = 5800
		else:
			command = self._map(degrees, minDegrees, maxDegrees, minComm, maxComm)
		self._pololu.setTarget(self._steeringServo, int(command))
		time.sleep(0.003)

	def _distIR(self, pin):
		'''
		return the distance of IR sensor (in meters) whose pin is specified
		@param pin: pin of IR sensor
		@type pin: int
		'''
		out = self._pololu.getPosition(pin)
		try:
			dist = ((self._a / (float(out) - self._b)) - self._c) / 100.0 #Distance in meters
			return dist
		except ZeroDivisionError:
			print"distIR[ZeroDivisionError] division by zero"

	def _distUS(self, input, output):
		'''
		returns the distance of US sensor (in meters) whose pins are specified
		@type input: int
		@type output: int

		@param input: input pin
		@param output: output pin
		'''
		GPIO.output(output, 0)
		time.sleep(0.0001)
		GPIO.output(output, 1)
		time.sleep(0.0001)
		GPIO.output(output, 0)
		start = time.time()
		while(GPIO.input(input) == 0):
			start = time.time()
		while(GPIO.input(input) == 1):
			stop = time.time()
		elapsed = stop - start

		return (elapsed * self._soundVelocity) / 2

	def _map(self, value, rmin1, rmax1, rmin2, rmax2):
		r1 = rmax1 - rmin1
		r2 = rmax2 - rmin2
		percent = (value - rmin1) * 100.0 / float(r1)
		res = percent * float(r2) / 100.0
		return rmin2 + res

	##Exceptions

	def _wheelsException(self):
		print "Usage Error[wheelsException]: only -1, 0 or 1 and 45-135 are allowed"
