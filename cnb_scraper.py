import csv
import datetime

import requests
from bs4 import BeautifulSoup


def hlavni():
    data = ["1.1.2022", "1.2.2022"]
    meny = ["EUR", "GBP", "USD"]
    # TODO najdi kurz pro vybrana data a meny - najdi_kurz()
    # TODO uloz hodnoty do CSV - tabulka_do_csv()


def najdi_kurz(datum: str, meny: list) -> list:
    """TODO Najdi tabulku kurzu pro dane datum a vrat hodnoty pro zvolene meny."""
    url = "https://www.cnb.cz/cs/platebni-styk/sluzby-pro-klienty/kurzovni-listek-cnb/index.html"


def zpracuj_odpoved_serveru(url: str) -> BeautifulSoup:
    """TODO Odesli pozadavek na prislusnou adresu 'url' a vracenou odpoved parsuj pomoci 'BeautifulSoup'."""
    pass


def najdi_radky_tabulky(soup):
    """TODO V zadanem objektu 'soup' vyhledej html tabulku men a vrat vsechny jeji radky.
    :return: bs4.element.ResultSet
    """
    pass


def preved_na_tabulku(vsechny_tr: list, datum: str) -> list:
    """TODO Najdi v seznam <tr> tagu hodnoty bunek <td>
    a naskladej je do tabulky (list listu)"""
    tabulka_kurzy = []
    return tabulka_kurzy


def tabulka_do_csv(tabulka: list, soubor: str):
    """Uloz tabulku men s datem do CSV souboru"""
    sloupce = ["Datum", "Měna", "Země", "Množství",
               "Deviza nákup", "Deviza prodej",
               "Valuta nákup", "Valuta prodej"]
    with open(soubor, "w", encoding="utf-8", newline="") as csv_s:
        zapisovac = csv.writer(csv_s, dialect="excel")
        zapisovac.writerow(sloupce)
        zapisovac.writerows(tabulka)


def kontrola_data(datum: str):
    # TODO Proved kontrolu data pomoci knihovny datetime
    # https://stackoverflow.com/a/9988288
    format_data = "%d.%m.%Y"
    try:
        pass
    except ValueError:
        print("Špatný formát data, správný tvar je DD.MM.YYYY")
        exit()
    else:
        return True


if __name__ == "__main__":
    hlavni()

# TODO Navic - stahovani kurzu z daneho rozsahu dni
# https://stackoverflow.com/questions/993358/creating-a-range-of-dates-in-python
