import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_should_see_add_basket_button(browser):
    browser.get(link)
    #time.sleep(30)
    button_name = browser.find_element_by_css_selector("#add_to_basket_form")
    assert button_name.is_displayed(), \
        'Кнопка добавить в корзину не найдена'
    
