# Import Python GPIO library
import RPi.GPIO as GPIO
# Import time library
import time
# Set GPIO pin numbering
GPIO.setmode(GPIO.BCM)

# Name input and output pins
TRIG=23
ECHO=24

# Print message to let the user know measurement is in progress
print "Distance Measurement in Progress"

# Set the two GPIO ports as either inputs or outputs
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

# Ensure that the Trigger pin is set low
GPIO.output(TRIG,False)
 
# The sensor needs a moment
print "Waiting for the sensor to settle"
time.sleep(2)

# Create trigger pulse and set to high
GPIO.output(TRIG, True)

# For 10us
time.sleep(0.00001)

# Set to low again
GPIO.output(TRIG, False)

# Record the last low timestamp for ECHO just before signal is received and the pin goes high
while GPIO.input(ECHO)==0:
 pulse_start = time.time()

# Record the last high timestamp for ECHO
while GPIO.input(ECHO)==1:
 pulse_end=time.time()

# Calculate the difference between the two recorded timestamps to get the duration of pulse and assign that value to pulse_duration
pulse_duration=pulse_end - pulse_start

# Calulate the distance
distance=pulse_duration * 17150

# Round the distance to 2 decimal places
distance=round(distance, 2)

# Print the distance
print "Distance:",distance,"cm"

# Clean the GPIO pins
GPIO.cleanup()