import sys
import matplotlib.pyplot as plt

class LinearRegression:
	def __init__(self, dataset, learningRate = 0.1, iterations = 10000):
		self.theta0 = 0
		self.theta1 = 0
		self.filename = dataset
		self.m = 0
		self.learningRate = learningRate
		self.iterations = iterations
		self.open_dataset()
		self.standardize_dataset()

	def get_theta0(self):
		return self.theta0

	def get_theta1(self):
		return self.theta1
	
	def open_dataset(self):
		with open(self.filename, 'r') as file:
			self.dataset = file.readlines()[1:]
			self.dataset = [x.strip() for x in self.dataset]
			self.m = len(self.dataset)
		if (self.m == 0):
			print("Dataset is empty")
			sys.exit(1)

	def standardize_dataset(self):
		mileages = [float(x.split(',')[0]) for x in self.dataset]
		prices = [float(x.split(',')[1]) for x in self.dataset]

		min_mileage = min(mileages)
		max_mileage = max(mileages)
		min_price = min(prices)
		max_price = max(prices)

		self.standardized_dataset = []
		for i in range(self.m):
			mileage, price = self.dataset[i].split(',')
			mileage = float(mileage)
			price = float(price)
			standardized_mileage = (mileage - min_mileage) / (max_mileage - min_mileage) # formula is x - min(x) / max(x) - min(x) feature scaling
			standardized_price = (price - min_price) / (max_price - min_price)
			self.standardized_dataset.append(f"{standardized_mileage},{standardized_price}")

	def estimate_price(self, km):
		return self.theta0 + (self.theta1 * km)

	def set_learningRate(self, learningRate):
		self.learningRate = learningRate

	def train(self):
		for _ in range(self.iterations):
			sum_error0 = 0
			sum_error1 = 0
			for i in range(self.m):
				mileage,price = self.standardized_dataset[i].split(',')
				mileage = float(mileage)
				price = float(price)
				error = self.estimate_price(mileage) - price
				sum_error0 += error
				sum_error1 += error * mileage
			self.theta0 -= self.learningRate * (1/self.m) * sum_error0
			self.theta1 -= self.learningRate * (1/self.m) * sum_error1

	def plot_regression(self):
		mileage = [float(x.split(',')[0]) for x in self.standardized_dataset]
		price = [float(x.split(',')[1]) for x in self.standardized_dataset]
		plt.scatter(mileage, price, color="blue", label="Données réelles")
		regression_line = [self.estimate_price(x) for x in mileage]
		plt.plot(mileage, regression_line, color="red", label="Régression linéaire")

		# Labels
		plt.xlabel("Kilométrage")
		plt.ylabel("Prix")
		plt.legend()
		plt.show()

if __name__ == "__main__":
	if (len(sys.argv) != 2):
		print("Usage : python(3) train.py <dataset>")
		sys.exit(1)
	dataset_name = sys.argv[1]
	trainer = LinearRegression(dataset_name, 0.1, 10000)
	trainer.train()
	trainer.plot_regression()
