import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_basket(browser):
    browser.get(link)
    element_text = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket").text
    if element_text == "Añadir al carrito":
        assert element_text == "Añadir al carrito","Should be a button 'Añadir al carrito'"
    else:
        assert element_text == "Ajouter au panier","Should be a button 'Ajouter au panier'"
