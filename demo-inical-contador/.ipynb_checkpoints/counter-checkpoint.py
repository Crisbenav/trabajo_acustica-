#CREA UNA APLICACIÓN QUE POSEE UN CONTADOR 

import flet 
from flet import IconButton, Page, Row, TextField, icons # 

def main (page:Page): # función que tenga un parametro 'page'
    page.title ='Flet Counter' # titulo de la pagina 
    page.vertical_alignment = 'center' # alinación vertical (todos los elemnetos quedan al centro)

    txt_number = TextField(value='0',text_align='right',width=100) # creación de campo de texto 

    def minus_click(event): # captura los clicks 
        txt_number.value=int(txt_number.value)-1 #
        page.update()

    def plus_click(event):
        txt_number.value=int(txt_number.value)+1
        page.update()
# agrega distintos elemnetos
    page.add( 
        Row
            [
               IconButton(icons.REMOVE,
               on_click=minus_click),
               txt_number,
               IconButton(icons.ADD,on_click=plus_click) 
            ],
            alignment='center'
        )
    )
# Spara visualizar en desktop 
flet.app(target=main)




