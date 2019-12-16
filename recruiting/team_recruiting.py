from recruiting import *
from recruiting.player import *


class team_recruits(object):
    def __init__(self, url="https://247sports.com/college/georgia-tech/Season/2020-Football/Commits/"):
        self.team_name = ""
        columns = ["name", "url", "position", "score", "hometown", "offers"]
        names = []
        urls = []
        scores = []
        positions = []
        hometowns = []
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        r = requests.get(url, headers=header)
        self.df = pd.DataFrame(columns=columns)

        data = r.text
        soup = BeautifulSoup(data, features="html.parser")

        self.team_name = soup.find("a", class_="plldwn_team tltp_click tltp_bm").text
        while self.team_name.endswith(" "):
            self.team_name = self.team_name[0:len(self.team_name)-1]

        for entry in soup.find_all("div", class_="wrapper"):
            name_url = entry.find("a", class_="ri-page__name-link")
            name = name_url.text
            url = "https:" + name_url.get("href")
            score = entry.find("span", class_="score").text
            position = entry.find("div", class_="position").text
            hometown = entry.find("span", class_="meta").text
            if position[0] == " ":
                position = position[1:]

            names.append(name)
            urls.append(url)
            scores.append(score)
            positions.append(position)
            hometowns.append(hometown)

        self.df["name"] = names
        self.df["url"] = urls
        self.df["score"] = scores
        self.df["position"] = positions
        self.df["hometown"] = hometowns

    def populate_offers(self):
        os.chdir("../team recruiting raw data")
        team_data_file = "{} commit data.csv".format(self.team_name.lower())
        if team_data_file in os.listdir():
            print("Bypassing offer data collection because csv file already exists.")
            team_data = pd.read_csv(team_data_file)
            team_data.drop(columns=team_data.columns[0], inplace=True)
            team_data["offers"] = pd.eval(team_data["offers"])
            self.df = team_data
            return self.df
        else:
            for i in self.df.index:
                recruit = player()
                recruit.url = self.df.iloc[i].url
                self.df.iloc[i].offers = recruit.get_offers()
                print(self.df.iloc[i])
            return self.df

    def count_offers(self):
        all_offers = []
        df = pd.DataFrame(columns=["Team", "OfferCount"])
        for i in self.df.offers:
            print(i)
            if type(i) != float:
                all_offers += i
        #         all_offers.remove("Georgia Tech")
        all_schools = list(set(all_offers))
        all_schools.remove(self.team_name)
        all_offers.remove(self.team_name)
        teamlist = []
        offercountlist = []
        for team in all_schools:
            teamlist.append(team)
            offercountlist.append(all_offers.count(team))

        df.Team = teamlist
        df.OfferCount = offercountlist
        return df
