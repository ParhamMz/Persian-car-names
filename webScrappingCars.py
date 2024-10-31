
from bs4 import BeautifulSoup
import requests as req


def find_cars():
    site_info = req.get("https://www.khodrobank.com/cars").text
    soup = BeautifulSoup(site_info, "lxml")
    cars = soup.find_all("div", class_="brand_item_name_fa")
    res = []

    for brand in cars:
        site_info = req.get("https://www.khodrobank.com/cars/"+ brand.text).text
        soup = BeautifulSoup(site_info, "lxml")
        car_names = soup.find_all("h5", class_="carspecs__title fa")
        for name in car_names:
            res.append(name.text)
    with open("carsList.txt", "w", encoding="utf-8") as my_file:
        my_file.write(str(res))



find_cars()
