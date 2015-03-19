from splinter.browser import Browser

browser = Browser('firefox')
browser.visit('https://www.twitter.com')


def do_login_if_need(self, username, password):
    if self.browser.is_element_present_by_css('div.menu_login_container'):
        self.browser.fill('XXXXXX', username)
        self.browser.fill('XXXXXXX', password)
        self.browser.find_by_css('div.menu_login_container input[type="submit"]').first.click()
        assert self.browser.is_element_present_by_css('li#navAccount')



	
if __name__ == "__main__":
    print main 
    