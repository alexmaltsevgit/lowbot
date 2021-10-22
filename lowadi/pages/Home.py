import os

import lowadi


class Home(lowadi.Page):
    url = "https://www.lowadi.com/"
    selectors = {
        "css": {
            "accept_cookie_btn": ".grid-cell.even.last.pr--1",
            "open_login_form_btn": "#header-login-label",
            "username_field": "#login",
            "password_field": "#password",
            "login_form_submit_btn": "#authentificationSubmit"
        }
    }

    def login(self):
        if self.site.cookies.exist():
            self.__login_by_cookies()
        else:
            self.__login_manually()

    def __login_by_cookies(self):
        self.site.cookies.load()
        self.site.refresh()

    def __login_manually(self):
        username = os.getenv("LOWADI_USERNAME")
        password = os.getenv("LOWADI_PASSWORD")

        self.site.click_on_many([
            Home.selectors['css']['accept_cookie_btn'],
            Home.selectors['css']['open_login_form_btn'],
        ])

        self.site.fill_many_fields({
            Home.selectors['css']['username_field']: username,
            Home.selectors['css']['password_field']: password
        })

        submit = Home.selectors['css']['login_form_submit_btn']
        self.site.click_on(submit)

        self.site.cookies.save()
