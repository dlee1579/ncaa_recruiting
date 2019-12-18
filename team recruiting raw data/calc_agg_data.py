import pandas as pd
import matplotlib.pyplot as plt
from recruiting import *
# import recruiting

class aggregate_data(object):
	def __init__(self, filename):
		self.team = filename[0:filename.find("commit")-1].title()
		self.offers_df = pd.DataFrame(columns=["Teams", "TotalOffers"])
		self.offers_df_by_opposition = pd.DataFrame(columns=["Team", "OfferCount"])
		self.offers_df_by_state = pd.DataFrame(columns=["State", "StateCount"])
		self.total_teams = 0
		self.total_offers = 0

		all_offers = []


		# what type of aggregate class data would be useful or interesting to see?
		# total number of commits, by position, by hometown/state, sum of all offers, number of all schools competed against, biggest competitors

		self.df = pd.read_csv(filename.lower(), index_col=0)
		self.df.offers = pd.eval(self.df.offers)

		for i in self.df.offers:
			all_offers += i
		print(all_offers)
		print(len(all_offers))

		all_schools = list(set(all_offers))
		try:
			all_schools.remove(self.team)
			all_offers.remove(self.team)
		except ValueError:
			all_schools.remove(self.team.upper())
			all_offers.remove(self.team.upper())

		teamlist = []
		offercountlist = []

		for team in all_schools:
			teamlist.append(team)
			offercountlist.append(all_offers.count(team))

		all_states = list(set(self.df.state))
		statelist = []
		statecountlist = []

		for state in all_states:
			statelist.append(state)
			statecountlist.append(self.df.state.to_list().count(state))

		self.total_teams = len(all_schools)
		self.total_offers = len(all_offers)
		self.offers_df_by_opposition.Team = teamlist
		self.offers_df_by_opposition.OfferCount = offercountlist
		self.offers_df_by_state.State = statelist
		self.offers_df_by_state.StateCount = statecountlist

	def offer_count_total(self):
		# ax = self.offers_df.plot.bar(x="Teams", y="Teams")
		print(self.offers_df.Teams)
		ax = plt.bar(["Total Teams", "Total Offers"], [self.total_teams, self.total_offers])
		ax.set_title("# of Total Offers for {} Commits:".format(self.team))
		# plt.show()
		return ax

	def offer_count_by_opposition(self):
		df = self.offers_df_by_opposition.sort_values(by="OfferCount", ascending=False).head(15)
		title = "Distribution of {} Commits with Offers from:".format(self.team)
		# plt.show()
		return df, title

	def offer_count_by_state(self):
		df = self.offers_df_by_state.sort_values(by="StateCount", ascending=False).head(5)
		title = "Distribution of {} Commits by Home State".format(self.team)
		# plt.show()
		return df, title

	def commit_count_by_position(self):
		df = self.df.groupby("position").count().sort_values(by="name", ascending=False).head()
		title = "Distribution of {} Commits by Position".format(self.team)
		# plt.show()
		return df, title

	def avg_score_by_position(self):
		df = self.df.groupby("position").mean().sort_values(by="score", ascending=False)
		title = "Average Score of {} Commits by Position".format(self.team)
		# plt.show()
		return df, title


if __name__ == "__main__":
	agg = aggregate_data("georgia tech commit data.csv")
	# # agg.graph_offer_count_total()
	# # agg.graph_offer_count_by_state()
	# # agg.graph_avg_score_by_position()
	# # agg.graph_commit_count_by_position()
	plt.figure()

	fontdict = {'fontsize': 8, 'fontweight': 'medium'}
	ax1 = plt.subplot(221)
	df1, title1 = agg.commit_count_by_position()
	# print(agg.df[["name", "position", "state"]].sort_values(by="position"))
	sns.countplot(x="position", data=agg.df, order=agg.df["position"].value_counts().index)
	# ax1.bar(df1.index, df1.name)
	ax1.set_title(title1, fontdict=fontdict)
	#
	ax2 = plt.subplot(222)
	df2, title2 = agg.avg_score_by_position()
	# print(df2.reset_index())
	sns.barplot(x="position", y="score", data=df2.reset_index())
	# ax2.bar(df2.index, df2.score)
	ax2.set_title(title2, fontdict=fontdict)
	ax2.set_ylim([0.8, 1])
	#
	ax3 = plt.subplot(223)
	sns.countplot(x="state", data=agg.df)
	df3, title3 = agg.offer_count_by_state()
	# ax3.bar(df3.State, df3.StateCount)
	ax3.set_title(title3, fontdict=fontdict)
	#
	ax4 = plt.subplot(224)
	df4, title4 = agg.offer_count_by_opposition()
	# print(df4.columns)
	# print(df4.head())
	sns.barplot(x="Team", y="OfferCount", data=df4)
	# plt.show()
	# ax4.bar(df4.Team, df4.OfferCount)
	ax4.set_title(title4, fontdict=fontdict)
	plt.xticks(rotation=90, fontsize=8)
	plt.show()