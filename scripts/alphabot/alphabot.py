import RPi.GPIO as GPIO
import time

class AlphaBot(object):
	
	def __init__(self,in1=21,in2=22,ena=33,in3=24,in4=26,enb=32):
		self.IN1 = in1
		self.IN2 = in2
		self.IN3 = in3
		self.IN4 = in4
		self.ENA = ena
		self.ENB = enb

		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		GPIO.setup(self.IN1,GPIO.OUT)
		GPIO.setup(self.IN2,GPIO.OUT)
		GPIO.setup(self.IN3,GPIO.OUT)
		GPIO.setup(self.IN4,GPIO.OUT)
		GPIO.setup(self.ENA,GPIO.OUT)
		GPIO.setup(self.ENB,GPIO.OUT)
		#self.forward()
                GPIO.output(self.ENA, True)
                GPIO.output(self.ENB, True)
		self.PWMA = GPIO.PWM(self.ENA,50)
		self.PWMB = GPIO.PWM(self.ENB,50)
		self.PWMA.start(0)
		self.PWMB.start(0)

	def forward(self):
                GPIO.output(self.ENA, True)
                GPIO.output(self.ENB, True)
		GPIO.output(self.IN1,GPIO.HIGH)
		GPIO.output(self.IN2,GPIO.LOW)
		GPIO.output(self.IN3,GPIO.LOW)
		GPIO.output(self.IN4,GPIO.HIGH)
                print("F")
                #GPIO.cleanup()

	def stop(self):
                GPIO.output(self.ENA, False)
                GPIO.output(self.ENB, False)
		GPIO.output(self.IN1,GPIO.LOW)
		GPIO.output(self.IN2,GPIO.LOW)
		GPIO.output(self.IN3,GPIO.LOW)
		GPIO.output(self.IN4,GPIO.LOW)
                GPIO.cleanup()


	def backward(self):
                GPIO.output(self.ENA, True)
                GPIO.output(self.ENB, True)
		GPIO.output(self.IN1,GPIO.LOW)
		GPIO.output(self.IN2,GPIO.HIGH)
		GPIO.output(self.IN3,GPIO.HIGH)
		GPIO.output(self.IN4,GPIO.LOW)
                #GPIO.cleanup()

	def left(self):
                GPIO.output(self.ENA, True)
                GPIO.output(self.ENB, True)
		GPIO.output(self.IN1,GPIO.LOW)
		GPIO.output(self.IN2,GPIO.HIGH)
		GPIO.output(self.IN3,GPIO.LOW)
		GPIO.output(self.IN4,GPIO.HIGH)
                #GPIO.cleanup()

	def right(self):
                GPIO.output(self.ENA, True)
                GPIO.output(self.ENB, True)
		GPIO.output(self.IN1,GPIO.HIGH)
		GPIO.output(self.IN2,GPIO.LOW)
		GPIO.output(self.IN3,GPIO.HIGH)
		GPIO.output(self.IN4,GPIO.LOW)
                #GPIO.cleanup()
		
	def setPWMA(self,value):
		self.PWMA.ChangeDutyCycle(value)

	def setPWMB(self,value):
		self.PWMB.ChangeDutyCycle(value)	
		
	def setMotor(self, left, right):
		if((left >= 0) and (left <= 100)):
			GPIO.output(self.IN1,GPIO.HIGH)
			GPIO.output(self.IN2,GPIO.LOW)
			self.PWMA.ChangeDutyCycle(left)
		elif((left < 0) and (left >= -100)):
			GPIO.output(self.IN1,GPIO.LOW)
			GPIO.output(self.IN2,GPIO.HIGH)
			self.PWMA.ChangeDutyCycle(0 - left)
		if((right >= 0) and (right <= 100)):
			GPIO.output(self.IN3,GPIO.LOW)
			GPIO.output(self.IN4,GPIO.HIGH)
			self.PWMB.ChangeDutyCycle(right)
		elif((right < 0) and (right >= -100)):
			GPIO.output(self.IN3,GPIO.HIGH)
			GPIO.output(self.IN4,GPIO.LOW)
			self.PWMB.ChangeDutyCycle(0 - right)
                if((left == 0) and (right == 0)):
                        GPIO.output(self.IN1,GPIO.LOW)
		        GPIO.output(self.IN2,GPIO.LOW)
		        GPIO.output(self.IN3,GPIO.LOW)
		        GPIO.output(self.IN4,GPIO.LOW)
                        self.PWMA.ChangeDutyCycle(0)
                        self.PWMB.ChangeDutyCycle(0)
