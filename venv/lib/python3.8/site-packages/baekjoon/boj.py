import requests
from bs4 import BeautifulSoup



def get_status_message(user_name):
    url = 'https://www.acmicpc.net/user/' + user_name
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    status = soup.find('blockquote' , {'class' : 'no-mathjax'}).text
    return status
def get_rank(user_name):
    url = 'https://www.acmicpc.net/user/' + user_name
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    bojrank = soup.select_one("#statics > tbody > tr:nth-child(1) > td").text
    return bojrank

def get_correct_qs(user_name):
    url = 'https://www.acmicpc.net/user/' + user_name
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    correct_qs = soup.select_one("body > div.wrapper > div.container.content > div.row > div:nth-child(2) > div > div.col-md-9 > div:nth-child(1) > div.panel-body").text
    return correct_qs

def get_correct_q(user_name):
    url = 'https://www.acmicpc.net/user/' + user_name
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    correct_q = soup.select_one("#u-solved").text
    return correct_q

def get_unsolved_qs(user_name):
    url = 'https://www.acmicpc.net/user/' + user_name
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    wrong_qs = soup.select_one("body > div.wrapper > div.container.content > div.row > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div.panel-body").text
    return wrong_qs

def get_unsolved_q(user_name):
    url = 'https://www.acmicpc.net/user/' + user_name
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    wrong_q = soup.select_one("#u-failed").text
    return wrong_q

def get_submit_time(user_name):
    url = 'https://www.acmicpc.net/user/' + user_name
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    submit_time = soup.select_one("#statics > tbody > tr:nth-child(4) > td > a").text
    return submit_time

