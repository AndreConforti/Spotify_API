from playwright.sync_api import sync_playwright
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup as bs4
from datetime import datetime, date
import os


def principal():
    with sync_playwright() as p:
        ## open browser and go to page
        browser = p.chromium.launch(
            timeout=5*60*1000,  # 5 min
            headless=False
        )
        page = browser.new_page()

        ## setting fixed viewport
        page.set_viewport_size({"width": 1080, "height": 1980})
        page.goto("https://accounts.spotify.com/pt-BR/login?continue=https%3A%2F%2Fopen.spotify.com%2F")
        sleep(5)

        ## login
        page.get_by_label("Endereço de e-mail ou nome de usuário").fill('gcm.martins.leme@gmail.com')
        page.get_by_label("Senha").fill('namaguederaz10')
        page.get_by_text("Entrar").click()
        sleep(5)

        page.goto("https://developer.spotify.com/console/get-recently-played/?limit=&after=&before=")
        sleep(5)

        # ## select id
        # page.get_by_text("Nenhuma").click()
        # page.locator("span", has_text="6 - CD").click()
        # page.get_by_text("Selecionar").click()



def main():
    principal()

main()