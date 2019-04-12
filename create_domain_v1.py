import requests
import re
import time
import datetime
from send_email import send_email
from argeweb import domain_register_argeweb

'''
2019-2-14
因godaddy无法查询fr,故调整直接每小时33分钟去尝试注册一次

argeweb注册nl,be
internetbs注册fr,需要birthday和注册信息里countrycode(法国为FR,意大利为IT)
'''

#当前目录下创建一个文本，存放需要抢注的域名
domains_txt = 'domains_neo.txt'
#access_token 可以在个人账户里找到
access_token = 'MmQwMjQxZTZiNjI0YWJhMGQ4MjJmOWZkYWJjZDFiMTZhMDRkMjNkMzMwOTUwNjdkYTE1MzA2NzgxZjZkN2UxMQ'
vps = '138.68.138.213' #vps
proxies = {
'https' : 'https://127.0.0.1:1080',
'http' : 'http://127.0.0.1:1080'
}
#create .fr
def create_fr(domain):
	proxies = {
	'https' : 'https://127.0.0.1:1080',
	'http' : 'http://127.0.0.1:1080'
	}
	#个人internetbs账户下api
	apikey = 'E4B5H7V9G9H7M4J3G0' #ApiKey
	apipwd = 'sbm201111' #API passwprd
	clone_domain = 'olewski.fr' #clone a domain
	#520crusher@gmail.com
	#E4B5H7V9G9H7M4J3G0
	#olewski.fr	
	params = {
	'ApiKey' : apikey,
	'Password' : apipwd,
	'Domain' : domain,
	'CloneContactsFromDomain' : clone_domain,
	'registrant_dotfrcontactentitybirthdate' : '1992-11-11', #birthday
	'admin_dotfrcontactentitybirthdate' : '1992-11-11',
	'registrant_dotfrcontactentitybirthplacecountrycode' : 'IT', #countrycode
	'admin_dotfrcontactentitybirthplacecountrycode' : 'IT'
	}
	url = 'https://api.internet.bs/Domain/Create'
	#url = 'https://api.internet.bs/Domain/Check?ApiKey=K6T0E8H9A0Y5S5O6K9&Password=sbm201111&Domain=' + domain
	r = requests.get(url, params=params, proxies=None)
	#print(r.text)
	return r.text

'''
#create .it
def create_it(domain):
	#nnlovework@gmail.com
	apikey = 'T3L9K1Q5U8B4I6D6P8S8'
	apipwd = 'sbm201111'
	clone_domain = 'garciacornici.it'	
	params = {
	'ApiKey' : apikey,
	'Password' : apipwd,
	'Domain' : domain,
	'CloneContactsFromDomain' : clone_domain,
	'registrant_dotitterm1' : 'YES',
	'registrant_dotitterm2' : 'YES',
	'registrant_dotitterm3' : 'YES',
	'registrant_dotitterm4' : 'YES',
	'registrant_clientip' : vps
	#138.68.138.213
	#149.28.75.248
	}
	url = 'https://api.internet.bs/Domain/Create'
	#url = 'https://api.internet.bs/Domain/Check?ApiKey=K6T0E8H9A0Y5S5O6K9&Password=sbm201111&Domain=' + domain
	r = requests.get(url, params=params, proxies=None)
	#print(r.text)
	return r.text


#create .be
def create_be(domain):
	#boy1990girl@gmail.com
	apikey = 'D2Q7Y1X7Z0H1L2R5Q5M3'
	apipwd = 'sbm201111'
	clone_domain = 'pizzatongeren-etna.be'	
	params = {
	'ApiKey' : apikey,
	'Password' : apipwd,
	'Domain' : domain,
	'CloneContactsFromDomain' : clone_domain
	}
	url = 'https://api.internet.bs/Domain/Create'
	#url = 'https://api.internet.bs/Domain/Check?ApiKey=K6T0E8H9A0Y5S5O6K9&Password=sbm201111&Domain=' + domain
	r = requests.get(url, params=params, proxies=None)
	#print(r.text)
	return r.text

# neostrada.com whois
def check_neo(domain):
	headers = {
	'Content-Type' : 'application/json',
	'Authorization' : 'Bearer ' + access_token
	}

	params = {
	'domain' : domain
	}

	api_url = 'https://api.neostrada.com/api/whois'
	r = requests.post(api_url, json=params, headers=headers, proxies=proxies)
	r_json = r.json()
	print(r_json)
	return r_json['extension_id'], r_json['available']


# neostrada.com register domain
def register_neo(domain, extension_id):

	headers = {
	'Accept' : 'application/json',
	'Authorization' : 'Bearer ' + access_token
	}
	params = {
	'domain' : domain,
	'extension_id' : extension_id,
	'year' : 1
	}
	api_url = 'https://api.neostrada.com/api/orders/add/'
	r = requests.post(api_url, headers=headers, json=params, proxies=None)
	#print(r.json()['message'])
	return r.json()['message']
'''

#godaddy
def check_godaddy(domain):
	api_key = 'e4CDquLzemu5_RqUzd65RbhGnEpc3XDwitr' # Key
	#api_key = 'dLiYHJeLFe6V_5NmDEwzoTsqQCdu1u9AwQr' # Key
	api_secret = 'RqVZ7zG3QDf1BcJLxXBgT4' # Secret
	#api_secret = '5NmH5LcF96U4Nwo8mveaG6' # Secret
	proxies = {
	'https' : 'https://127.0.0.1:1080',
	'http' : 'http://127.0.0.1:1080'
	}
	headers = {
	'accept' : 'application/json',
	'Content-Type': 'application/json',
	'Authorization' : 'sso-key ' + api_key + ':' + api_secret
	}
	api_url = 'https://api.godaddy.com/v1/domains/available'
	r = requests.post(api_url, headers=headers, json=[domain], proxies=None)
	#print(r.json())
	return r.json()['domains'][0]['available']
'''
def check_internetbs(domain):
	#nnlovework@gmail.com
	apikey = 'T3L9K1Q5U8B4I6D6P8S8'
	apipwd = 'sbm201111'
	params = {
	'ApiKey' : apikey,
	'Password' : apipwd,
	'Domain' : domain	
	}
	url = 'https://api.internet.bs/Domain/Check'
	r = requests.get(url, params=params, proxies=proxies)
	print(r.text)
	return r.text
'''

if __name__ == '__main__':
	print('Program is running...')
	'''
	rs = check_neo('fermelabrador.fr')
	#rs = check_godaddy('jsosnduidsnbdks.com')
	#rs = create_domain('laubergedejacques.fr')
	print(rs)
	'''
	while True:
		with open(domains_txt, 'r', encoding='utf-8') as f:
			text = f.read()
		domains = re.findall(r'[a-zA-Z0-9\-]*\.[a-z]*', text)

		while domains != []:
			fr_count = len([i for i in domains if '.fr' in i])
			for domain in domains:
				#print(domain)
				if ('.fr' in domain):
					if (datetime.datetime.now().minute == 33):
						create_fr_rs = create_fr(domain)
						if 'SUCCESS' in create_fr_rs:
							print( domain + ' 注册成功')
							send_email(domain + ' | '+domain.split('.')[1].upper()+' DOMAIN', domain + ' created')
							domains = [i for i in domains if i not in domain]
							with open(domains_txt, 'w', encoding='utf-8') as f:
								text = text.replace(domain, '')
								f.write(text)
							time.sleep((60 - fr_count * 10) // fr_count)
						else:
							time.sleep(60 // fr_count)
				else:
					while True:
						try:
							#rs = check_neo(domain)
							rs = check_godaddy(domain)
						except:
							time.sleep(1)
							print('check again...')
						else:
							#if rs[1] == 210:
							if rs == True:
								print(time.strftime("%Y-%m-%d %H:%M:%S") + '    ' +domain+ ' 可以注册')
								'''
								if '.fr' in domain:
									create_fr = create_fr(domain)
									if 'SUCCESS' in create_fr:
										print( domain + ' 注册成功')
										time.sleep(1)
										send_email(domain + ' | '+domain.split('.')[1].upper()+' DOMAIN', domain + ' created')
								'''
								if ('.be' in domain) or ('.nl' in domain):
									create_benl = domain_register_argeweb(domain)#arge
									#create_be = create_be(domain)#internetBS注册be
									if 'SUCCESS' in create_benl:
										print( domain + ' 注册成功')
										time.sleep(1)
										send_email(domain + ' | '+domain.split('.')[1].upper()+' DOMAIN', domain + ' created')																
									elif '被占用' in create_benl:
										time.sleep(1)
										send_email(domain + ' | '+domain.split('.')[1].upper()+' DOMAIN', create_benl)
									elif '价格' in create_benl:
										time.sleep(1)
										send_email(domain + ' | '+domain.split('.')[1].upper()+' DOMAIN', create_benl)
									elif register_neo(domain, rs[0]) == 'Order placed':#neo
										print( domain + ' 注册成功')
										time.sleep(1)
										send_email(domain + ' | '+domain.split('.')[1].upper()+' DOMAIN', domain + ' created')
								domains = [i for i in domains if i not in domain]
								with open(domains_txt, 'w', encoding='utf-8') as f:
									text = text.replace(domain, '')
									f.write(text)
							break
				time.sleep(1)
			break
		time.sleep(1)
		
	

		