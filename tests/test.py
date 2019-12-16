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
    ut20 = tr.team_recruits(url="https://247sports.com/college/texas/Season/2020-Football/Commits/")
    df = ut20.create_table()
    df = ut20.populate_offers()
    df.to_csv("commit data.csv")

    ax = ut20.offer_count().sort_values(by="OfferCount", ascending=False).head(15).plot.bar(x='Team', y='OfferCount',
                                                                                          rot=90)
    plt.title("# of Texas Commits with Offers from:")
    plt.show()