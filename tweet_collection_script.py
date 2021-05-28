#Code for tweet collection using snscrape

import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools
import time

#list of strings whose tweets need to be scraping
names = list()
names = ["Blue Blindfold", "Blue Blindfold Campaign", "Look Beneath the Surface", "#EndHumanTrafficking", "Blue Heart", "Stop the Traffik", "#STOPTHETRAFFIK", "PACTottawa"]

for word in names:
    tic = time.time()
    df_city = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(word + ' since:2000-01-01 until:2021-05-01').get_items(), 10000))
    toc = time.time()
    print("Time taken for", word,":",toc - tic, "seconds")
    word = word.replace(" ", "")
    save_to = word + ".csv"
    df_city.to_csv(save_to)
    

