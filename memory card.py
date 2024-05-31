
from tabnanny import check
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import *
from random  import  shuffle



app = QAppliation([])

window = QWidgets()
window.setWindowTitle('Memory card')

question = QLabel('Какой национальности не существует')
btn_Ok = QPushButton('Отиетить')

layot_1 = QVBoxLayout()

RadioGroupBox = QGroupBox("Варианты ответов") # группа для ответов
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout() # на эту направляющую цепляются др. направлющие
layout_ans2 = QVBoxLayout() # тут будут первые два ответа
layout_ans3 = QVBoxLayout() # тут будут 3 и 4 ответ

layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1) 

line1 = QHBoxLayout() # вопрос
line2 = QHBoxLayout() # варианты
line3 = QHBoxLayout() # кнопка

line1.addWidget(question, alignment=Qt.AlignCenter)
line2.addWidget(RadioGroupBox, alignment=Qt.AlignCenter)
line3.addWidget(btn_Ok, alignment=Qt.AlignCenter)

layout_1.addLayout(line1)
layout_1.addLayout(line2)
layout_1.addLayout(line3)

# заготовка
# панель с результаттом
ansGroupBox = QGroupBox('Результаты теста')
lb_result = QLabel('Правильно или нет')
lb_correct = QLabel('ответ будет тут.')

layaout_res = QVBoxLayout()

layaout_res.addWidget(lb_result, alignment=Qt.AlignLeft)
layaout_res.addWidget(lb_correct, alignment=Qt.AlignCenter)
ansGroupBox.setLayout(layaout_res)


########################################### Это будем переписывать
#line2 = QHBoxLayout() # варианты
#layout_1.addLayout(line2)
#line2.addWidget(ansGroupBox, alignment=Qt.AlignCenter)
#######################################################

def show_question():
    RadioGroupBox.show()
    ansGroupBox.hide()
    btn_Ok.set_text('Следующий вопрос')

def show_result():
    RadioGroupBox.hide()
    ansGroupBox.show()
    btn_Ok.setText('Следующий вопрос')
    


window.setLayout(layout_1)
ask('')
btn_Ok.clicked.cennect(check_answer)
window.show()
app.exec_()
