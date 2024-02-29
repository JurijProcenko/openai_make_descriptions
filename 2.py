import pandas as pd


data = pd.read_csv(
    "1000 descriptions.csv",
    encoding="utf-8",
)
print(data)


# data = {
#     "Name": ["Alice", "Bob"],
#     "Age": [30, 25],
#     "City": ["New York", "San Francisco"],
# }

# df = pd.DataFrame(data)
# df.to_csv("output.csv", index=False)
