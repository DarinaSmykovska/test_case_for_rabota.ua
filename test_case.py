from selenium import webdriver

# input there your login and password for rabota.ua
login = ''
password = ''
driver = webdriver.Chrome(executable_path='chromedriver.exe')


driver.get('https://rabota.ua/')
driver.implicitly_wait(2)
driver.find_element_by_class_name('f-header-menu-list-link-with-border').click()
driver.find_element_by_id('ctl00_Sidebar_login_txbLogin').send_keys(login)
driver.find_element_by_id('ctl00_Sidebar_login_txbPassword').send_keys(password)
driver.find_element_by_id('ctl00_Sidebar_login_lnkLogin').click()


try:
	driver.find_element_by_class_name('f-signin-error')
	print('Failed to log in')	

except Exception:
	print('Successfully logged in')