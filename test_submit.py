import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from pytest import fixture


def test_clicker1():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.implicitly_wait(5)
    url = 'https://ultimateqa.com/complicated-page/'
    chrome.get(url=url)

    loc_name_field = (By.XPATH, '//input[@id="et_pb_contact_name_0"]')
    name_field = chrome.find_element(loc_name_field[0], loc_name_field[1])

    loc_email_field = (By.XPATH, '//input[@id="et_pb_contact_email_0"]')
    email_field = chrome.find_element(loc_email_field[0], loc_email_field[1])

    loc_message_field = (By.XPATH, '//textarea[@id="et_pb_contact_message_0"]')
    message_field = chrome.find_element(loc_message_field[0], loc_message_field[1])

    # Решение КАПЧИ
    loc_task_captcha = (By.XPATH, '//textarea[@id="et_pb_contact_message_0"]/../../div//span')
    result_task_captcha = chrome.find_element(loc_task_captcha[0], loc_task_captcha[1]).text
    captcha_answer = eval(result_task_captcha)
    loc_answer_captcha = (By.XPATH, '//textarea[@id="et_pb_contact_message_0"]/../../div//input['
                                    '@name="et_pb_contact_captcha_0"]')
    answer_captcha_field = chrome.find_element(loc_answer_captcha[0], loc_answer_captcha[1])
    input_data = {'name': "Nikita", 'email': 'nikita@mail.ru', 'wrong_email': 'nikita@mail', 'message': 'Hello world',
                  'captcha': f'{captcha_answer}'}

    name_field.send_keys(f"{input_data.get('name')}")
    email_field.send_keys(f"{input_data.get('email')}")
    message_field.send_keys(f"{input_data.get('message')}")
    answer_captcha_field.send_keys(f"{input_data.get('captcha')}")
    time.sleep(5)
    loc_submit_but = (By.XPATH, '//*[@id="et_pb_contact_form_0"]//button[@type="submit"]')
    submit_but = chrome.find_element(loc_submit_but[0], loc_submit_but[1])
    submit_but.click()
    loc_success = (By.XPATH, '//*[@id="et_pb_contact_form_0"]//div[@class="et-pb-contact-message"]/p')
    success_message = chrome.find_element(loc_success[0], loc_success[1])
    result = success_message.text
    assert result == 'Thanks for contacting us'
    chrome.refresh()


def test_clicker2():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.implicitly_wait(5)
    url = 'https://ultimateqa.com/complicated-page/'
    chrome.get(url=url)

    loc_name_field = (By.XPATH, '//input[@id="et_pb_contact_name_0"]')
    name_field = chrome.find_element(loc_name_field[0], loc_name_field[1])

    loc_email_field = (By.XPATH, '//input[@id="et_pb_contact_email_0"]')
    email_field = chrome.find_element(loc_email_field[0], loc_email_field[1])

    loc_message_field = (By.XPATH, '//textarea[@id="et_pb_contact_message_0"]')
    message_field = chrome.find_element(loc_message_field[0], loc_message_field[1])

    # Решение КАПЧИ
    loc_task_captcha = (By.XPATH, '//textarea[@id="et_pb_contact_message_0"]/../../div//span')
    result_task_captcha = chrome.find_element(loc_task_captcha[0], loc_task_captcha[1]).text
    captcha_answer = eval(result_task_captcha)
    loc_answer_captcha = (By.XPATH, '//textarea[@id="et_pb_contact_message_0"]/../../div//input['
                                    '@name="et_pb_contact_captcha_0"]')
    answer_captcha_field = chrome.find_element(loc_answer_captcha[0], loc_answer_captcha[1])
    input_data = {'name': "Nikita", 'email': 'nikita@mail.ru', 'wrong_email': 'nikita@mail', 'message': 'Hello world',
                  'captcha': f'{captcha_answer}'}
    loc_name_field = (By.XPATH, '//input[@id="et_pb_contact_name_0"]')
    name_field = chrome.find_element(loc_name_field[0], loc_name_field[1])
    name_field.send_keys(f"{input_data.get('name')}")
    loc_submit_but = (By.XPATH, '//*[@id="et_pb_contact_form_0"]//button[@type="submit"]')
    submit_but = chrome.find_element(loc_submit_but[0], loc_submit_but[1])
    submit_but.click()
    alert_message = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_form_0"]/div[@class="et-pb-contact-message"]')
    text_alert_message = alert_message.text
    assert text_alert_message != 'Thanks for contacting us'
    chrome.refresh()


def test_clicker3():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.implicitly_wait(5)
    url = 'https://ultimateqa.com/complicated-page/'
    chrome.get(url=url)

    loc_name_field = (By.XPATH, '//input[@id="et_pb_contact_name_0"]')
    name_field = chrome.find_element(loc_name_field[0], loc_name_field[1])

    loc_email_field = (By.XPATH, '//input[@id="et_pb_contact_email_0"]')
    email_field = chrome.find_element(loc_email_field[0], loc_email_field[1])

    loc_message_field = (By.XPATH, '//textarea[@id="et_pb_contact_message_0"]')
    message_field = chrome.find_element(loc_message_field[0], loc_message_field[1])

    # Решение КАПЧИ
    loc_task_captcha = (By.XPATH, '//textarea[@id="et_pb_contact_message_0"]/../../div//span')
    result_task_captcha = chrome.find_element(loc_task_captcha[0], loc_task_captcha[1]).text
    captcha_answer = eval(result_task_captcha)
    loc_answer_captcha = (By.XPATH, '//textarea[@id="et_pb_contact_message_0"]/../../div//input['
                                    '@name="et_pb_contact_captcha_0"]')
    answer_captcha_field = chrome.find_element(loc_answer_captcha[0], loc_answer_captcha[1])
    loc_message_field = (By.XPATH, '//textarea[@id="et_pb_contact_message_0"]')

    input_data = {'name': "Nikita", 'email': 'nikita@mail.ru', 'wrong_email': 'nikita@mail', 'message': 'Hello world',
                  'captcha': f'{captcha_answer}'}
    message_field = chrome.find_element(loc_message_field[0], loc_message_field[1])
    message_field.send_keys(f"{input_data.get('message')}")
    loc_submit_but = (By.XPATH, '//*[@id="et_pb_contact_form_0"]//button[@type="submit"]')
    submit_but = chrome.find_element(loc_submit_but[0], loc_submit_but[1])
    submit_but.click()
    alert_message = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_form_0"]/div[@class="et-pb-contact-message"]')
    text_alert_message = alert_message.text
    assert text_alert_message != 'Thanks for contacting us'

    chrome.close()
