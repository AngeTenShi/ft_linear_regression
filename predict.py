import sys
import os

def unstandardize(price):
	if (os.path.isfile("min_max_price.txt")):
		min_max = open("min_max_price.txt", "r").readlines()
		min, max = min_max[0].split(',')
		min = float(min)
		max = float(max)
		return (price * (max - min) + min)
	else:
		return (price)

def standardize_mileage(mileage):
	if (os.path.isfile("min_max_mileage.txt")):
		min_max = open("min_max_mileage.txt", "r").readlines()
		min, max = min_max[0].split(',')
		min = float(min)
		max = float(max)
		return (mileage - min) / (max - min)
	else:
		return (mileage)

def predict(mileage, theta0, theta1):
	return theta0 + (theta1 * mileage)

if __name__ == "__main__":
	milage = input("Mileage : ")
	try:
		mileage = float(milage)
	except ValueError:
		print("Invalid mileage")
		sys.exit(1)
	theta0 = 0
	theta1 = 0
	if (os.path.isfile("theta_values.txt")):
		file = open("theta_values.txt", "r")
		theta0, theta1 = file.readlines()[0].split(',')
	if (mileage < 0  or mileage > 350000):
		print("Invalid mileage")
		sys.exit(1)
	print(unstandardize(predict(standardize_mileage(mileage), float(theta0), float(theta1))))
