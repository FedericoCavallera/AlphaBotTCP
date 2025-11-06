import RPi.GPIO as GPIO
import time

#Classe modificata sui metodi forward, backward, left, right
#Aggiunto il reset del dutycycle
class AlphaBot(object):
	
	def __init__(self,in1=12,in2=13,ena=6,in3=20,in4=21, sL=19, sR=16,enb=26):
		self.IN1 = in1
		self.IN2 = in2
		self.IN3 = in3
		self.IN4 = in4
		self.ENA = ena
		self.ENB = enb
		self.DR = sR
		self.DL = sL

		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(self.IN1,GPIO.OUT)
		GPIO.setup(self.IN2,GPIO.OUT)
		GPIO.setup(self.IN3,GPIO.OUT)
		GPIO.setup(self.IN4,GPIO.OUT)
		GPIO.setup(self.ENA,GPIO.OUT)
		GPIO.setup(self.ENB,GPIO.OUT)
		GPIO.setup(self.DR, GPIO.IN, GPIO.PUD_UP)
		GPIO.setup(self.DL, GPIO.IN, GPIO.PUD_UP)
		self.PWMA = GPIO.PWM(self.ENA,500)
		self.PWMB = GPIO.PWM(self.ENB,500)
		self.PWMA.start(50)
		self.PWMB.start(50)

	def forward(self):
		self.setPWMB(50)
		self.setPWMA(50)
		print("Avanti")
		GPIO.output(self.IN1,GPIO.HIGH)
		GPIO.output(self.IN2,GPIO.LOW)
		GPIO.output(self.IN3,GPIO.LOW)
		GPIO.output(self.IN4,GPIO.HIGH)

	def stop(self):
		self.setPWMB(50)
		self.setPWMA(50)
		print("Stop")
		GPIO.output(self.IN1,GPIO.LOW)
		GPIO.output(self.IN2,GPIO.LOW)
		GPIO.output(self.IN3,GPIO.LOW)
		GPIO.output(self.IN4,GPIO.LOW)

	def backward(self):
		self.setPWMB(50)
		self.setPWMA(50)
		print("Indietro")
		GPIO.output(self.IN1,GPIO.LOW)
		GPIO.output(self.IN2,GPIO.HIGH)
		GPIO.output(self.IN3,GPIO.HIGH)
		GPIO.output(self.IN4,GPIO.LOW)

	def left(self):
		self.setPWMB(50)
		self.setPWMA(50)
		print("Sinistra")
		GPIO.output(self.IN1,GPIO.LOW)
		GPIO.output(self.IN2,GPIO.LOW)
		GPIO.output(self.IN3,GPIO.LOW)
		GPIO.output(self.IN4,GPIO.HIGH)

	def right(self):
		self.setPWMB(50)
		self.setPWMA(50)
		print("Destra")
		GPIO.output(self.IN1,GPIO.HIGH)
		GPIO.output(self.IN2,GPIO.LOW)
		GPIO.output(self.IN3,GPIO.LOW)
		GPIO.output(self.IN4,GPIO.LOW)
  
	def square(self):
		for i in range(4):
			self.forward()
			time.sleep(1.2)
			self.stop()

			self.right()
			time.sleep(0.33)
			self.stop()

		

	def circle(self):
		for i in range(14):
			self.forward()
			time.sleep(0.1)
			self.stop()
   
			self.right()
			time.sleep(0.1)
			self.stop()

	def setPWMA(self,value):
		self.PWMA.ChangeDutyCycle(value)

	def setPWMB(self,value):
		self.PWMB.ChangeDutyCycle(value)	
		
	def ex():
		print("Exit")
  
	def readRight(self):
		return GPIO.input(self.DR)

	def readLeft(self):
		return GPIO.input(self.DL)
  
	def setMotor(self, left, right):
		if((right >= 0) and (right <= 100)):
			GPIO.output(self.IN1,GPIO.HIGH)
			GPIO.output(self.IN2,GPIO.LOW)
			self.PWMA.ChangeDutyCycle(right)
		elif((right < 0) and (right >= -100)):
			GPIO.output(self.IN1,GPIO.LOW)
			GPIO.output(self.IN2,GPIO.HIGH)
			self.PWMA.ChangeDutyCycle(0 - right)
		if((left >= 0) and (left <= 100)):
			GPIO.output(self.IN3,GPIO.HIGH)
			GPIO.output(self.IN4,GPIO.LOW)
			self.PWMB.ChangeDutyCycle(left)
		elif((left < 0) and (left >= -100)):
			GPIO.output(self.IN3,GPIO.LOW)
			GPIO.output(self.IN4,GPIO.HIGH)
			self.PWMB.ChangeDutyCycle(0 - left)
   
