import pandas as pd

purchase_amounts = pd.Series([20, 35, 50, 20, 35, 50, 20, 35, 50, 100])

mean_purchase_amount = purchase_amounts.mean()
print("Mean (average) purchase amount:", mean_purchase_amount)

mode_purchase_amount = purchase_amounts.mode()
print("Mode of the purchase amounts:", mode_purchase_amount)
