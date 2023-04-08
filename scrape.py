# import pandas as pd
# from tqdm import tqdm
import snscraper.modules.twitter as sntwitter


scrapped = sntwitter.TwitterSearchScraper("from:elonmusk").get_items()

print(scrapped)
