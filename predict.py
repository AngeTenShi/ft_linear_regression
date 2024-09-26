import sys
from train import LinearRegression

def predict(mileage):
	return theta0 + (theta1 * mileage)

if __name__ == "__main__":
	model = LinearRegression("data.csv")
	model.train()
	theta0 = model.get_theta0()
	theta1 = model.get_theta1()
	milage = input("Mileage : ")
	try:
		milage = float(milage)
	except ValueError:
		print("Invalid mileage")
		sys.exit(1)
	print(predict(milage))
