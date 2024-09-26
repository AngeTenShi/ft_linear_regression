from train import LinearRegression
def mae(model): # mean absolute error
	mae = 0
	expected = [model.dataset[i].split(',')[1] for i in range(model.m)]
	mean_price = sum([float(x) for x in expected]) / model.m
	for i in range(model.m):
		mileage, price = model.standardized_dataset[i].split(',')
		mileage = float(mileage)
		price = float(price)
		mae += abs(model.estimate_price(mileage) - price)
	mae /= model.m
	mae /= mean_price
	return (mae)

if __name__ == "__main__":
	model = LinearRegression("data.csv")
	model.train()
	print(str(mae(model)) + "%")
