from recruiting import *
import recruiting.team_recruiting as tr
import recruiting.player as player
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # teams_df = pd.read_csv("teams_list.csv")
    # teams_list = teams_df["Teams"]
    # for team_class in teams_list:
    #     print("Collecting data for {}".format(team_class))
    #     team = tr.team_recruits(team_class)
    #     df = team.populate_offers()
        # df.to_csv("{} commit data.csv".format(team.team_name.lower()))
    # ax = team.count_offers().sort_values(by="OfferCount", ascending=False).head(15).plot.bar(x='Team', y='OfferCount', rot=90)
    # plt.title("# of {} Commits with Offers from:".format(team.team_name))
    # plt.show()

    team = tr.team_recruits("georgia tech")
    df = team.populate_offers()
    ax = team.count_offers().sort_values(by="OfferCount", ascending=False).head(15).plot.bar(x='Team', y='OfferCount', rot=90)
    plt.title("# of {} Commits with Offers from:".format(team.team_name))
    plt.show()