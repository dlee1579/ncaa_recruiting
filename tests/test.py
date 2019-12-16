from recruiting import *
import recruiting.team_recruiting as tr
import recruiting.player as player
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # gt19 = tr.team_recruits()
    # df = gt19.create_table()
    # df = gt19.populate_offers()
    # print(df)

    # print(recruiting.__dict__)
    # print(requests)
    # team = tr.team_recruits(url="https://247sports.com/college/texas/Season/2020-Football/Commits/")
    team = tr.team_recruits()
    # print(team.team_name)
    df = team.populate_offers()
    # df.to_csv("{} commit data.csv".format(team.team_name.lower()))
    #
    # print(df)
    # print(team.count_offers().sort_values(by="OfferCount", ascending=False))
    ax = team.count_offers().sort_values(by="OfferCount", ascending=False).head(15).plot.bar(x='Team', y='OfferCount', rot=90)
    plt.title("# of {} Commits with Offers from:".format(team.team_name))
    plt.show()