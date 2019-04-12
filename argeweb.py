# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
from time import sleep
import datetime
from random import randint
import os,time
import re



#for https://www.argeweb.nl/argecs/
def domain_register_argeweb(domain):
	#id,password
	argeweb_id = '3128297'
	argeweb_pwd = 'Rz7Oo5p%&(sY'

	chromeOptions = webdriver.ChromeOptions()

	#linux运行chrome所需
	chromeOptions.set_headless()
	chromeOptions.add_argument('--disable-gpu')
	chromeOptions.add_argument('--no-sandbox')
	
	start = time.time()
	browser = webdriver.Chrome(chrome_options=chromeOptions)#windows下运行chrome_options=None即可
	#print('login reday...')
	browser.get('https://www.argeweb.nl/argecs/index.php')
	sleep(randint(3,5))
	browser.find_element_by_css_selector('a.cc-cookie-accept').click()
	#'''
	#browser.execute_script('document.getElementsByClassName("cc-cookies")[0].style.display="None";')
	#browser.execute_script('document.getElementsByClassName("ccdiv")[0].style.position="relative";')
	print('get %s success.' % domain)
	sleep(randint(8,12))
	login_id = browser.find_element_by_name('debiteurnummer')
	login_id.send_keys(argeweb_id)#账号
	login_pwd = browser.find_element_by_name('password')
	login_pwd.send_keys(argeweb_pwd)#密码
	login_pwd.submit()
	sleep(randint(3,5))
	print('login success...')
	#'''
	while True:
		try:
			browser.get('https://www.argeweb.nl/bestellen/?functie=whois&category=&domain=' + domain)
			sleep(randint(3,5))
			if (browser.find_elements_by_css_selector("td.whois-action")[0].text == 'Registreren'):
				print(domain + ' 可以注册.')
				browser.find_elements_by_css_selector('button.btn-registreren')[0].click()
				sleep(randint(8,12))
				browser.find_elements_by_css_selector('a.btn-whois-shoppingcart')[0].click()
				sleep(randint(3,5))
				browser.find_element_by_css_selector('input.inputbox').click()
				sleep(randint(3,5))
				the_price=browser.find_element_by_id('domein_prijs_per['+domain+']').text
				#print(the_price)
				if ('0,50' in the_price) or ('2,95' in the_price):
					browser.find_element_by_css_selector('input.inputbox').click()
					sleep(randint(3,5))
					browser.find_element_by_name('terms').click()
					sleep(randint(3,5))
					browser.find_element_by_css_selector('input.CS_link_button').click()
					print('%s done.' % domain)
					sleep(randint(3,5))
					browser.quit()
					end = time.time()
					print('%s Sec done. - %s' % (end - start, domain))
					return domain + ' SUCCESS'
				else:
					browser.quit()
					return '价格不正确 | ' + the_price
			else:
				browser.quit()
				return 'argeweb被占用'
		except:
			print('sth goes wrong...')
		else:
			break

def get_domains():
	if os.path.exists('domains.txt'):
		with open('domains.txt','r+',encoding='utf-8') as f:
			lines = f.readlines()
			if lines != []:
				domains = [re.search(r'([a-zA-Z0-9-]+\..+?)\s', i).group(1) for i in lines] 
				#print(domains)
				dt = [re.search(r'(\d{4}.*\d{2})|(\n)', i).group(0) for i in lines]
				#print(dt)
				return dict(zip(domains,dt))

def now_time():
	return datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H')

def delete_success_domain():
	if os.path.exists('available_domains.txt'):
		with open('available_domains.txt','r',encoding='utf-8') as f:
			domains = f.readlines()
			if domains != []:
				a = [i.strip('\n') for i in domains]
				with open('available_domains.txt','w',encoding='utf-8') as f:
					rv = [i+'\n' for i in a if i not in L]
					#rv.reverse()
					f.writelines(rv)


def delete_failed_domain():
	pass

if __name__=='__main__':
	d = get_domains()
	while d != {}:
		for domain in list(d.keys()):
			if d[domain] == '\n':
				domain_register_argeweb(domain)
				del d[domain]
			elif d[domain][0:-6] == now_time():
				domain_register_argeweb(domain)
				del d[domain]
			sleep(1)
		sleep(1)
