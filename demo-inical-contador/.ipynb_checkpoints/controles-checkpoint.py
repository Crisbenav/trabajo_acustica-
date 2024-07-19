import flet 
from flet import Page, Text 

def main(page: Page): 
    t = Text(value='Hola, Mundo', color='green')
    page.controls.append(t)
    page.update()

flet.app(target=main) 