from selenium.webdriver.common.by import By
#Ссылочка для вебравки
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

#сама функция(тест)
def test_check_cart_button_exists(browser):
    #запихуеваем в браузер ссылку
    browser.get(link)

    #проверка наличия кнопки добавления в корзину btn-add-to-basket
    find_basket = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    find_basket = find_basket.text
    #тригер если кнопка есть
    assert find_basket is None, f"Всё четко"