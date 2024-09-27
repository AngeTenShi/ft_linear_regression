from train import LinearRegression

def calculate_r2(y_real, y_predicted):
	mean_y_real = sum(y_real) / len(y_real)
	ss_total = sum((yi - mean_y_real) ** 2 for yi in y_real)
	ss_residual = sum((yi - y_pred) ** 2 for yi, y_pred in zip(y_real, y_predicted))
	r2 = 1 - (ss_residual / ss_total)
	return r2

def calculate_mse(y_real, y_predicted):
	mse = sum((yi - y_pred) ** 2 for yi, y_pred in zip(y_real, y_predicted)) / len(y_real)
	return mse

def calculate_mae(y_real, y_predicted):
	mae = sum(abs(yi - y_pred) for yi, y_pred in zip(y_real, y_predicted)) / len(y_real)
	return mae

if __name__ == "__main__":
	model = LinearRegression("data.csv")
	model.train()
	mileage_dataset = [float(x.split(',')[0]) for x in model.standardized_dataset]
	real_price = [float(x.split(',')[1]) for x in model.standardized_dataset]
	price_estimations = [model.estimate_price(x) for x in mileage_dataset]
	print("R2 (1 is best):", calculate_r2(real_price, price_estimations))
	print("MSE (0 is best):", calculate_mse(real_price, price_estimations))
	print("MAE (0 is best):", calculate_mae(real_price, price_estimations))
	model.plot_regression()
