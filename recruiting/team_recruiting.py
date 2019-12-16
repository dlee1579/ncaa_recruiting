from recruiting import *
from recruiting.player import *


class team_recruits(object):
    def __init__(self, url="https://247sports.com/college/georgia-tech/Season/2020-Football/Commits/"):
        self.columns = ["name", "url", "position", "score", "hometown", "offers"]
        self.names = []
        self.urls = []
        self.scores = []
        self.positions = []
        self.hometowns = []
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        r = requests.get(url, headers=self.header)
        self.df = None

        data = r.text
        soup = BeautifulSoup(data)

        for entry in soup.find_all("div", class_="wrapper"):
            name_url = entry.find("a", class_="ri-page__name-link")
            name = name_url.text
            url = "https:" + name_url.get("href")
            score = entry.find("span", class_="score").text
            position = entry.find("div", class_="position").text
            hometown = entry.find("span", class_="meta").text
            if position[0] == " ":
                position = position[1:]

            self.names.append(name)
            self.urls.append(url)
            self.scores.append(score)
            self.positions.append(position)
            self.hometowns.append(hometown)

    def create_table(self):
        self.df = pd.DataFrame(columns=self.columns)
        self.df["name"] = self.names
        self.df["url"] = self.urls
        self.df["score"] = self.scores
        self.df["position"] = self.positions
        self.df["hometown"] = self.hometowns
        return self.df

    def populate_offers(self):
        for i in self.df.index:
            recruit = player()
            recruit.url = self.df.iloc[i].url
            self.df.iloc[i].offers = recruit.get_offers()
            print(self.df.iloc[i])
        return self.df

    def offer_count(self):
        all_offers = []
        df = pd.DataFrame(columns=["Team", "OfferCount"])
        for i in self.df.offers:
            if type(i) != float:
                all_offers += i
        #         all_offers.remove("Georgia Tech")
        all_schools = list(set(all_offers))
        teamlist = []
        offercountlist = []
        for team in all_schools:
            teamlist.append(team)
            offercountlist.append(all_offers.count(team))

        df.Team = teamlist
        df.OfferCount = offercountlist
        return df
