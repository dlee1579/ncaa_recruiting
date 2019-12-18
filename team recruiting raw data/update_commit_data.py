import os, pandas as pd
import recruiting.team_recruiting as tr

if __name__ == "__main__":
	filelist = [file for file in os.listdir() if ".csv" in file]
	teamlist = ["alabama", "arizona state", "auburn"]
	# for file in filelist[0:3]:
	# 	print(file)
	# 	df = pd.read_csv(file, index_col=0)
		# if "state" not in df.columns:
		# 	df["state"] = df.apply(lambda row: row.hometown[row.hometown.find(", ")+2:row.hometown.find(",")+4], axis=1)
		# 	df.to_csv(file)

	for teamname in teamlist:
		team = tr.team_recruits(team_name=teamname)
		team.populate_offers()
		print("Updated commit state data for {}".format(teamname))
	# file = "georgia tech commit data.csv"
	# gt20 = tr.team_recruits()
	# gt20.populate_offers()
	# print("Updated commit state data for {}".format(file))

