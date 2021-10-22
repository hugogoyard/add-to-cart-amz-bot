from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from colorama import Fore, Back, Style, init
import time

init(autoreset=True)

url = 'https://www.amazon.fr/PlayStation-Digital-Manette-DualSense-Couleur/dp/B08H98GVK8/ref=sr_1_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=ps5+digital&qid=1633869712&qsid=260-3594671-7176730&s=videogames&sr=1-1&sres=B08H98GVK8%2CB094J12PPX%2CB094VKN192%2CB08PTXSKHS%2CB091D8MDF3%2CB097XXCVKC%2CB0924452L1%2CB093QZ7YD3%2CB094DH53S7%2CB091CKVF4S%2CB09F2HMG7P%2CB091CLJY3V%2CB099HZHR84%2CB0953MWP8L%2CB098JQLW48%2CB09248RKD6'
url = 'https://www.amazon.fr/PlayStation-officielle-DualSense-rechargeable-Compatible/dp/B08H99BPJN?ref_=ast_sto_dp&th=1&psc=1'
res = False
essai = 0

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(executable_path='chromedriver.exe', options=options)

def acceptCookies():
    try:
        cookiesBtn = browser.find_element_by_id('sp-cc-accept')
        cookiesBtn.click()
        print(Fore.GREEN + '✔ ' + Fore.RESET + 'The bot has successfully accepted cookies')
    except:
        print(Fore.YELLOW + 'No cookies has been found')

print('Launching program (' + Fore.BLUE + 'trial: #' + str(essai) + Fore.RESET+')')
while(res == False):
    if essai == 0:
        browser.get(url)
        acceptCookies()
    else:
        print('New Try (' + Fore.BLUE + 'trial: #' + str(essai) + Fore.RESET+')')
        browser.get(url)
    try:
        productPrice = browser.find_element_by_id('priceblock_ourprice')
        res = True
        try:
            addToCartBtn = browser.find_element_by_id('add-to-cart-button')
        except:
            print(Fore.RED + "✘ " + Fore.RESET + 'The bot didnt find the add to cart button')
    except:
        res = False
        print(Fore.RED + '✘ ' + Fore.RESET + 'The product seems unavailable')
        t=30
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            time.sleep(1)
            t -= 1
            print('The bot will try to reload the page in ' + Fore.RED + str(timer) + Fore.RESET, end='\r')
            if(t == 0):
                print('The bot will try to reload the page in ' + Fore.RED + str(timer) + Fore.RESET)
    essai += 1
else:
    print(Fore.GREEN + '✔ ' + Fore.RESET + 'The product seems available')
    addToCartBtn.click()
    time.sleep(5)
    closeRightPanel = browser.find_element_by_id('attach-popover-lgtbox').click()
    time.sleep(5)
    goToCartBtn = browser.find_element_by_id('nav-cart').click()
    print(Fore.GREEN + "✔ " + Fore.RESET + 'Product successfully added to your cart.')
