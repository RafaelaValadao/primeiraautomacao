from playwright.sync_api import Playwright, sync_playwright, expect
import re

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

     """Mudar o URL para alterar ambiente"""
    page.goto("https://gestao.pontotel.com.br/#/cognito/login")
    page.get_by_role("textbox").click()

    """Mudar o lar21 para alterar a compmann - """
    page.get_by_role("textbox").fill("lar21@bancodaycovalsa.com.br")
    page.get_by_role("textbox").press("Enter")

    """ Mudar a senha de acordo com a senha da compmann """
    page.locator("input[type=\"password\"]").fill("coracaojunino")
    page.locator("input[type=\"password\"]").press("Enter")


    page.locator("a").filter(has_text=re.compile(r"^folha$")).click()
    page.get_by_role("link", name="Folhas de ponto").click()
    page.locator("#Ponto-0-0-0").click()
    page.get_by_text("empregados", exact=True).click()
    page.get_by_placeholder("empregados - nenhum selecionado").click()

    """ Mudar o "func" para o nome do Colaborador a ser selecionado > em seguida o sistema vai clicar nele (garantir que ele seja o 1º da lista)"""
    page.get_by_placeholder("empregados - nenhum selecionado").fill("func")
    page.get_by_title("FUNCIONARIO TESTE IFP").dblclick()

    """ A numeração na casa 1 equivale a linha (de 0 a 31). Nas seguintes casas, dita o tipo de ponto """
    """ 1 = entrada | 2 = pausa | 3 = retorno | = 4 = saida """
    """ No exemplo abaixo, executamos o script na 4a linha da folha do colaborador, e alternamos o tipo de ponto """

    page.locator("#Ponto-3-0-0").click()
    page.locator("#Ponto-3-0-0").fill("08:00")
    page.get_by_role("button", name="2 - Esqueceu de bater ponto").click()
    page.wait_for_timeout(2000)
    page.locator("#Ponto-3-1-0").fill("12:00")
    page.get_by_role("button", name="2 - Esqueceu de bater ponto").click()
    page.wait_for_timeout(2000)
    page.locator("#Ponto-3-2-0").fill("13:00")
    page.get_by_role("button", name="2 - Esqueceu de bater ponto").click()
    page.wait_for_timeout(2000)
    page.locator("#Ponto-3-3-0").fill("17:00")
    page.get_by_role("button", name="2 - Esqueceu de bater ponto").click()
    page.wait_for_timeout(2000)

    """ A numeração na casa 1 equivale a linha (de 0 a 31). Nas seguintes casas, dita o tipo de ponto """
    """ 1 = entrada | 2 = pausa | 3 = retorno | = 4 = saida """
    """ No exemplo abaixo, executamos o script na 5a linha da folha do colaborador, e alternamos o tipo de ponto """
    page.locator("#Ponto-4-0-0").fill("08:00")
    page.get_by_role("button", name="2 - Esqueceu de bater ponto").click()
    page.locator("#Ponto-4-1-0").fill("12:00")
    page.get_by_role("button", name="2 - Esqueceu de bater ponto").click()
    page.locator("#Ponto-4-2-0").fill("13:00")
    page.get_by_role("button", name="2 - Esqueceu de bater ponto").click()
    page.locator("#Ponto-4-3-0").fill("17:00")
    page.get_by_role("button", name="2 - Esqueceu de bater ponto").click()

    """ A numeração na casa 1 equivale a linha (de 0 a 31). Nas seguintes casas, dita o tipo de ponto """
    """ 1 = entrada | 2 = pausa | 3 = retorno | = 4 = saida """
    """ No exemplo abaixo, executamos o script na 4a linha da folha do colaborador, e alternamos o tipo de ponto """
    entrada = page.locator("#Ponto-3-0-0")
    entrada.press("Delete")
    page.wait_for_timeout(5000)
    pausa = page.locator("#Ponto-3-1-0")
    pausa.press("Delete")
    page.wait_for_timeout(5000)
    retorno = page.locator("#Ponto-3-2-0")
    retorno.press("Delete")
    page.wait_for_timeout(5000)
    saida = page.locator("#Ponto-3-3-0")
    saida.press("Delete")
    page.wait_for_timeout(5000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
