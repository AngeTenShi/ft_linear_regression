import sys
import os

def predict(mileage, theta0, theta1):
	return theta0 + (theta1 * mileage)

if __name__ == "__main__":
	milage = input("Mileage : ")
	try:
		milage = float(milage)
	except ValueError:
		print("Invalid mileage")
		sys.exit(1)
	theta0 = 0
	theta1 = 0
	if (os.path.isfile("theta_values.txt")):
		file = open("theta_values.txt", "r")
		theta0, theta1 = file.readlines()[0].split(',')
	print(predict(milage, float(theta0), float(theta1)))
