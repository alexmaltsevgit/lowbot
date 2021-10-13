def get_horses_links(browser):
    selector = "a.horsename[href]"
    horses_links = browser.find_elements_by_css_selector(selector)
    hrefs = map(lambda link: link.get_attribute('href'), horses_links)

    return list(hrefs)
