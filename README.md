# Web scraper kurzu měn ČNB

Ahoj, zase nestíhám a potřeboval bych pomoct s projektem - chceme zjistit vývoj ceny cizích měn podle kurzu ČNB. Problém je, že tahle data jsou k dispozici jen ve formě tabulky na webu 

> https://www.cnb.cz/cs/platebni-styk/sluzby-pro-klienty/kurzovni-listek-cnb/index.html

V prohlížeči lze měnit datum platnosti kurzů pomocí nabídky **Datum** a tlačítkem **Odeslat**.
To přidá na konec adresy `?date=14.12.2022` = požadavek na server ([query string](https://en.wikipedia.org/wiki/Query_string)).

Také potřebujeme hodnoty jen pro určité měny, takže by se hodilo nějaké filtrování.

Potřebuješ z webu dostat HTML pomocí knihovny [requests](https://requests.readthedocs.io/en/latest/) a z HTML dostat hodnoty pomocí [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/). Pro jejich instalaci použij `requirements.txt`

Pak už stačí jen dostat hodnoty do formy tabulky (seznam seznamů), ty už pak můžeš uložit funkcí `tabulka_do_csv()`

Kdybys ti zbyl nějaký čas, můžeš zkusit automatické generování tabulek pro zadaný rozsah dní.

> Díky
> Ondra
