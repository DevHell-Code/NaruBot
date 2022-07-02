import requests
from bs4 import BeautifulSoup

def get_solvedac_rank(user_name):
    url = 'https://www.acmicpc.net/user/' + user_name
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rank = soup.find('img' , {'class' : 'solvedac-tier'})
    return rank
def get_boj_status_message(user_name):
    url = 'https://www.acmicpc.net/user/' + user_name
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    status = soup.find('blockquote' , {'class' : 'no-mathjax'}).text
    return status
def get_boj_rank(user_name):
    url = 'https://www.acmicpc.net/user/' + user_name
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    bojrank = soup.select_one("#statics > tbody > tr:nth-child(1) > td").text
    return bojrank
def get_correct_q(user_name):
    url = 'https://www.acmicpc.net/user/' + user_name
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    correct_q = soup.select_one("#u-solved").text
    return correct_q
