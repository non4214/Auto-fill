from selenium import webdriver
import time
import sys

driver = webdriver.Chrome("C:/Users/ADMIN/Desktop/google/chromedriver.exe")
url = "https://docs.google.com/forms/d/e/1FAIpQLSfrlCBLWyl05xQPgihq69qKU3HqmLc5C2InPMwDXsFYBktTLA/viewform?usp=sf_link"

driver.get(url)

def fill_from(firstname, lastname ,gemder ,age):
    inputs = driver.find_elements_by_class_name("quantumWizTextinputInput")
    radiobuttons = driver.find_elements_by_class_name("appsMaterialWizToggleFladiogroupEl")
    submit=browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")
    textboxes[0].send_keys("exemail@gmail.com")
    time.sleep(10)

    inputs_array = [
        firstname, lastname,age
        ]

    for i in range(len(inputs)):
            inputs[i].clear()
            inputs[i].send_keys(inputs_array[i])

fill_from("ณัฐชนน","วะลับ","ชาย","22")
radio_buttons[2].click()
submit.click()