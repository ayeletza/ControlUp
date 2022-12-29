
# Imports:
import csv
import datetime as dt
from ReadFile import LinksFile
from Constants import HIGHEST_PRICE_TTL, LOWEST_PRICE_TTL, AVG_PRICE_TTL
from Backend import DB
from SearchTheNet import STN


def read_file(filename):
    '''
    A function to read a csv file from a given path.
    :param filename: filename to read.
    :return: None.
    '''
    with open(filename) as f:
        csv_file = csv.reader(f)
        for row in csv_file:
            url = row[0]
            yield url


def main():
    '''
    The main function of the code.
    This function reads the file that contains the urls from the cloud,
    makes the calculations that are needed and keeps the new data in DB.
    :return: None.
    '''
    lf = LinksFile()
    file_data = lf.read_file()
    # lf.download_file()

    db = DB()
    stn = STN()

    # rf = read_file(FILE_PATH)
    rf = file_data

    for url in rf:
        ts = dt.datetime.now()
        stn.web_opener(url)
        prices = stn.get_prices()
        hp = prices[HIGHEST_PRICE_TTL]
        lp = prices[LOWEST_PRICE_TTL]
        ap = prices[AVG_PRICE_TTL]
        db.add_entry(ts, url, hp, lp, ap)

    # lf.delete_file(FILE_PATH)
    for entry in db.get_all_data():
        print(entry)

    db.close_session()


if __name__ == '__main__':
    main()



