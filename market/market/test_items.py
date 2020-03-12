import time

"""
pytest -s -v --tb=short --browser_name=chrome --language=es test_items.py
pytest -s -v --language=es
"""

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_sees_add_button(browser):
    browser.get(link)
    buttoncheck = browser.find_element_by_css_selector("button.btn-add-to-basket")
    time.sleep(5)
    assert buttoncheck.is_displayed(), "Button add to basket not displayed"