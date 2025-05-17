from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QGroupBox, QButtonGroup
from random import shuffle, choice

class Question():
    def __init__(self, q, r_a, w_a, w_a1,w_a2):
        self.question = q
        self.rightAnswer = r_a
        self.wrongAnswer = w_a
        self.wrongAnswer1 = w_a1
        self.wrongAnswer2 = w_a2

questions = []
questions.append(Question('Кто я', 'Я', 'Животное', 'Насекомое','Растение'))
questions.append(Question('Из какого мяса традиционно готовитсяначинка для чебуреков', 'Баранина', 'Телятина', 'Свинина', 'Конина'))
questions.append(Question('По какой реке проплыл самый первый пароход', 'Гудзон', 'Сена', 'Рейн', 'Волга'))

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn.setText('Следующий вопрос')
    print('Статистика:\n-Всего вопросов,' ,main_win.total,'\n-Правильных ответов:' ,main_win.score)
    print('Рейтинг:',main_win.score / main_win.total * 100, '%')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn.setChecked(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    RadioGroup.setExclusive(True)

def start_test():
    if btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def ask(q:Question):
    shuffle(rbtns)
    rbtns[0].setText(q.rightAnswer)
    rbtns[1].setText(q.wrongAnswer)
    rbtns[2].setText(q.wrongAnswer1)
    rbtns[3].setText(q.wrongAnswer2)
    question.setText(q.question)
    resultText1.setText(q.rightAnswer)
    show_question()    

def check_answer():
    if rbtns[0].isChecked():
        resultText.setText('Правильно')
        main_win.score += 1
        show_result()
    elif rbtns[1].isChecked() or rbtns[2].isChecked() or rbtns[3].isChecked():
        resultText.setText('Неправильно')
        show_result()

def next_question():
    main_win.total += 1
    rand_q = choice(questions)
    ask(rand_q)


app = QApplication([])
main_win = QWidget()
main_win.score = 0 #верные ответы 
main_win.total = 0 #всего вопросов задано 
main_win.resize(400,400)
main_win.setWindowTitle('Memory Card')

RadioGroupBox = QGroupBox('Варианты ответов')
AnsGroupBox = QGroupBox('Результат')
resultText = QLabel('Правильно/неправильно')
resultText1 = QLabel('Правильный ответ')
question = QLabel('Вопрос.')
rbtn = QRadioButton('1')
rbtn1 = QRadioButton('2')
rbtn2 = QRadioButton('3')
rbtn3 = QRadioButton('4')
btn = QPushButton('Ответить')
rbtns = [rbtn, rbtn1, rbtn2, rbtn3]

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn)
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)

HL1 = QHBoxLayout()
HL2 = QHBoxLayout()
HL3 = QHBoxLayout()
HL4 = QHBoxLayout()
VL1 = QVBoxLayout()
VL2 = QVBoxLayout()
VL3 = QVBoxLayout()
VL4 = QVBoxLayout()

VL1.addWidget(rbtn)
VL1.addWidget(rbtn1)
VL2.addWidget(rbtn2)
VL2.addWidget(rbtn3)
HL1.addLayout(VL1)
HL1.addLayout(VL2)

VL4.addWidget(resultText)
VL4.addWidget(resultText1)

HL2.addWidget(question)
HL3.addWidget(RadioGroupBox)
HL3.addWidget(AnsGroupBox)

HL4.addWidget(btn)
VL3.addLayout(HL2)
VL3.addLayout(HL3)
VL3.addLayout(HL4)



RadioGroupBox.setLayout(HL1)
AnsGroupBox.setLayout(VL4)
main_win.setLayout(VL3)
AnsGroupBox.hide()
next_question()
btn.clicked.connect(start_test)
main_win.show() 
app.exec_()