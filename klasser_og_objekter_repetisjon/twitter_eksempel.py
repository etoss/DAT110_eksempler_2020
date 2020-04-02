import datetime


class Bruker:
    neste_id = 1

    def __init__(self, brukernavn, passord):
        self.brukernavn = brukernavn
        self.passord = passord
        self.id = Bruker.neste_id
        Bruker.neste_id += 1
        self.tweets = []

    def hent_tweets(self):
        return self.tweets

    def hent_fem_siste_tweets(self):
        if len(self.tweets) <= 5:
            return self.tweets
        return self.tweets[len(self.tweets)-5:]

    def __str__(self):
        return f"{self.id}: {self.brukernavn}"

class Tweet:
    neste_id = 1

    def __init__(self, tittel, tekst, dato, forfatter: Bruker):
        self.tittel = tittel
        self.tekst = tekst
        self.dato = dato
        self.forfatter = forfatter
        if self not in forfatter.tweets:
            forfatter.tweets.append(self)
        self.id = Tweet.neste_id
        Tweet.neste_id += 1
        self.likes = []

    def __str__(self):
        return f"{self.id}: {self.tittel} \n{self.tekst}\n\n"


def lag_test_data():
    brukeren = Bruker("Arne Einarsen", "dfgre24")
    brukere = {}
    brukere[brukeren.id] = brukeren
    brukeren = Bruker("Ida Hansen", "45.sdgsd")
    brukere[brukeren.id] = brukeren
    brukeren = Bruker("Nils Ås", "435dfgh!")
    brukere[brukeren.id] = brukeren
    tweets = {}
    ny_tweet = Tweet("Tittel", "Tester systemet", datetime.date(2020, 3, 20), brukere[1])
    tweets[ny_tweet.id] = ny_tweet
    ny_tweet = Tweet("System", "Systemtest", datetime.date(2020, 3, 21), brukere[1])
    tweets[ny_tweet.id] = ny_tweet
    ny_tweet = Tweet("Noe", "Noe", datetime.date(2020, 3, 22), brukere[2])
    tweets[ny_tweet.id] = ny_tweet
    return brukere, tweets


class System:
    def __init__(self):
        self.brukere = {}
        self.tweets = {}
        self.innlogget_bruker = None

    def sett_inn_test_data(self):
        self.brukere, self.tweets = lag_test_data()

    def lag_bruker(self, brukernavn, passord):
        brukeren = Bruker(brukernavn, passord)
        self.brukere[brukeren.id] = brukeren

    def logg_inn(self, bruker_id):
        self.innlogget_bruker = self.brukere[bruker_id]

    def brukerliste(self):
        return self.brukere

    def tweets_for_bruker(self, bruker_id=None):
        if bruker_id is None:
            bruker = self.innlogget_bruker
        else:
            bruker = self.brukere[bruker_id]
        tweets = bruker.hent_tweets()
        return tweets

    def alle_tweets_med_brukerinfo(self):
        tweet_utskrift_liste = []
        for tweet_id in self.tweets:
            tweet = self.tweets[tweet_id]
            streng = f"{tweet_id}: {tweet.tittel}\n{tweet.tekst}\n{tweet.forfatter}\n\n"
            tweet_utskrift_liste.append(streng)
        return tweet_utskrift_liste

    def lag_tweet(self, tittel, tekst):
        ny_tweet = Tweet(tittel, tekst, datetime.datetime.now(), self.innlogget_bruker)
        self.tweets[ny_tweet.id] = ny_tweet


class Grensesnitt:
    def __init__(self, system):
        self.system = system

    def skriv_inn_ny_bruker(self):
        print("Skriv inn ny bruker: ")
        navn = input("Skriv inn brukernavn: ")
        passord = input("Skriv inn passord")
        self.system.lag_bruker(navn, passord)

    def skriv_brukerliste(self):
        brukerliste = self.system.brukerliste()
        print("Brukere: ")
        for nokkel in brukerliste:
            print(brukerliste[nokkel])

    def logg_inn_bruker(self):
        self.skriv_brukerliste()
        bruker_id = int(input("Logg inn hvilken bruker? "))
        self.system.logg_inn(bruker_id)

    def tweets_for_innlogget_bruker(self):
        print("Tweets for innlogget bruker: ")
        tweets = self.system.tweets_for_bruker()
        for tweet in tweets:
            print(tweet)

    def skriv_alle_tweets(self):
        tweetliste = self.system.alle_tweets_med_brukerinfo()
        for linje in tweetliste:
            print(linje)

    def skriv_tweet(self):
        print(f"Skriv inn tweet for {self.system.innlogget_bruker}")
        tittel = input("Tittel")
        print("Skriv inn teksten. Avslutt med tom linje")
        linja = input("> ")
        tekst = linja + "\n"
        while linja != "":
            linja = input("> ")
            if linja == "":
                break
            tekst += linja + "\n"
        self.system.lag_tweet(tittel, tekst)


    def meny(self):
        avslutter = False
        while not avslutter:
            print("Velg hva du vil gjøre:")
            print("1: Skriv ut brukerliste")
            print("2: Skriv inn ny bruker")
            print("3: Logg inn bruker")
            print("4: Skriv ut tweets for bruker")
            print("5: Skriv ut alle tweets")
            print("6: Skriv inn tweet for innlogget bruker")
            print("a: avslutt")
            valg = input("Velg: ")
            if valg == "1":
                self.skriv_brukerliste()
            if valg == "2":
                self.skriv_inn_ny_bruker()
            if valg == "3":
                self.logg_inn_bruker()
            if valg == "4":
                self.tweets_for_innlogget_bruker()
            if valg == "5":
                self.skriv_alle_tweets()
            if valg == "6":
                self.skriv_tweet()
            if valg == "a":
                avslutter = True


if __name__ == "__main__":
    systemet = System()
    systemet.sett_inn_test_data()
    grensesnitt = Grensesnitt(systemet)
    grensesnitt.meny()
