import os, pandas as pd

if __name__ == "__main__":
	filelist = [file for file in os.listdir() if ".csv" in file]

	for file in filelist:
		print(file)
		df = pd.read_csv(file, index_col=0)
		if "state" not in df.columns:
			df["state"] = df.apply(lambda row: row.hometown[row.hometown.find(", ")+2:row.hometown.find(",")+4], axis=1)
			df.to_csv(file)
	print("Updated commit state data for {}".format(file))

