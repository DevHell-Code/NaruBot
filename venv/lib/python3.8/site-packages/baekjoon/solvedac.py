import requests
from bs4 import BeautifulSoup

def download(url, file_name):
    with open(file_name, "wb") as file:   # open in binary mode
        response = requests.get(url)               # get request
        file.write(response.content) 

def tierfinder(word):
    if word.find('tier/1.svg') != -1:
        return "브론즈 5"
    elif word.find('tier/2.svg') != -1:
        return "브론즈 4"
    elif word.find('tier/3.svg') != -1:
        return "브론즈 3"
    elif word.find('tier/4.svg') != -1:
        return "브론즈 2"
    elif word.find('tier/5.svg') != -1:
        return "브론즈 1"
    elif word.find('tier/6.svg') != -1:
        return "실버 5"
    elif word.find('tier/7.svg') != -1:
        return "실버 4"
    elif word.find('tier/8.svg') != -1:
        return "실버 3"
    elif word.find('tier/9.svg') != -1:
        return "실버 2"
    elif word.find('tier/10.svg') != -1:
        return "실버 1"
    elif word.find('tier/11.svg') != -1:
        return "골드 5"
    elif word.find('tier/12.svg') != -1:
        return "골드 4"
    elif word.find('tier/13.svg') != -1:
        return "골드 3"
    elif word.find('tier/14.svg') != -1:
        return "골드 2"
    elif word.find('tier/15.svg') != -1:
        return "골드 1"
    elif word.find('tier/16.svg') != -1:
        return "플래티넘 5"
    elif word.find('tier/17.svg') != -1:
        return "플래티넘 4"
    elif word.find('tier/18.svg') != -1:
        return "플래티넘 3"
    elif word.find('tier/19.svg') != -1:
        return "플래티넘 2"
    elif word.find('tier/20.svg') != -1:
        return "플래티넘 1"
    elif word.find('tier/21.svg') != -1:
        return "다이아몬드 5"
    elif word.find('tier/22.svg') != -1:
        return "다이아몬드 4"
    elif word.find('tier/23.svg') != -1:
        return "다이아몬드 3"
    elif word.find('tier/24.svg') != -1:
        return "다이아몬드 2"
    elif word.find('tier/25.svg') != -1:
        return "다이아몬드 1"
    elif word.find('tier/26.svg') != -1:
        return "루비 5"
    elif word.find('tier/27.svg') != -1:
        return "루비 4"
    elif word.find('tier/28.svg') != -1:
        return "루비 3"
    elif word.find('tier/29.svg') != -1:
        return "루비 2"
    elif word.find('tier/30.svg') != -1:
        return "루비 1"
    elif word.find('tier/31.svg') != -1:
        return "마스터"
    else:
        return "언랭크"

def get_tier(user_name):
    url = 'https://www.acmicpc.net/user/' + user_name
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rank = soup.find('img' , {'class' : 'solvedac-tier'})
    return tierfinder(rank['src'])

def get_ac_rating(user_name):
    url = 'https://solved.ac/profile/' + user_name
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rating = soup.select_one("#u-result-6").text
    return rating

def get_exp(user_name):
    url = 'https://solved.ac/profile/' + user_name
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    exp = soup.select_one("#__next > div.ProfileHeaderCard__ProfileHeaderCardWrapper-sc-1ds1sbv-0.fhLOCV > div.ProfileHeaderCardstyles__ProfileHeaderCardTop-wboshd-0.iothCP > div > div > div:nth-child(4) > div.ProfileHeaderCardstyles__UserNumberContainer-wboshd-4.jOszzV > span:nth-child(1) > b").text
    return exp

def get_rank(user_name):
    url = 'https://solved.ac/profile/' + user_name
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rank = soup.select_one("#__next > div.ProfileHeaderCard__ProfileHeaderCardWrapper-sc-1ds1sbv-0.fhLOCV > div.ProfileHeaderCardstyles__ProfileHeaderCardTop-wboshd-0.iothCP > div > div > div:nth-child(4) > div.ProfileHeaderCardstyles__UserNumberContainer-wboshd-4.jOszzV > span:nth-child(2) > b").text
    return rank

def get_rival_amount(user_name):
    url = 'https://solved.ac/profile/' + user_name
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rival_amount = soup.select_one("#__next > div.ProfileHeaderCard__ProfileHeaderCardWrapper-sc-1ds1sbv-0.fhLOCV > div.ProfileHeaderCardstyles__ProfileHeaderCardTop-wboshd-0.iothCP > div > div > div:nth-child(4) > div.ProfileHeaderCardstyles__UserNumberContainer-wboshd-4.jOszzV > span:nth-child(5) > b").text
    return rival_amount

