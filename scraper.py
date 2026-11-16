import requests
from bs4 import BeautifulSoup
import csv

date = input("Please Enter A Date In MM/DD/YYYY : ")
page = requests.get(f"https://www.yallakora.com/Match-Center/?date={date}")

def main(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    matches = soup.find_all("div", {"class": "liItem"})

    results = []

    for match in matches:
        teamA = match.find("div", {"class": "teamA"}).find("p").text
        teamB = match.find("div", {"class": "teamB"}).find("p").text
        scores = match.find_all("span", {"class": "score"})
        time = match.find("span", {"class": "time"}).text

        results.append([teamA, scores[0].text, scores[1].text, teamB, time])

    with open("matches.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["Team A", "Score A", "Score B", "Team B", "Time"])
        writer.writerows(results)

    print("Done!")

main(page)
