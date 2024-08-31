from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QGroupBox, QLineEdit, QButtonGroup
from random import shuffle, randint


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory card')
#122222222222222222222222
question = QLabel('Какой национальности не существует?')
answer_button = QPushButton()
answer_button.setText('Ответить')

rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Смурфы')
rbtn3 = QRadioButton('Чулымцы')
rbtn4 = QRadioButton('Алеуты')

Main_Vline = QVBoxLayout()

text_line = QHBoxLayout()
text_line.addWidget(question)



btngroup_line = QHBoxLayout()

button_line = QHBoxLayout()
button_line.addWidget(answer_button, stretch= 3)

btns_vline1 = QVBoxLayout()
btns_vline2 = QVBoxLayout()

btns_vline1.addWidget(rbtn1)
btns_vline1.addWidget(rbtn2)
btns_vline2.addWidget(rbtn3)
btns_vline2.addWidget(rbtn4)

btngroup_line.addLayout(btns_vline1)
btngroup_line.addLayout(btns_vline2)

ButtonsGroupBox =   QGroupBox('Варианты ответа:')
ButtonsGroupBox.setLayout(btngroup_line)

btngroup_line = QHBoxLayout()
btngroup_line.addWidget(ButtonsGroupBox)


Main_Vline.addLayout(text_line)
Main_Vline.addLayout(btngroup_line)
Main_Vline.addLayout(button_line)

Main_Vline.setSpacing(20)

ButtonsGroupBox.show()


answer_label = QLabel('')
true_answer = QLabel('')
answer_layout = QHBoxLayout()
answer_layout.addWidget(answer_label)
answer_layout.addWidget(true_answer)




answer_group = QGroupBox('Результат теста')
answer_group.setLayout(answer_layout)

btngroup_line.addWidget(ButtonsGroupBox)
btngroup_line.addWidget(answer_group)
ButtonsGroupBox.show()
answer_group.hide()

def show_result():
    ButtonsGroupBox.hide()
    answer_group.show()
    answer_button.setText('Следующий вопрос')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

def show_questions():
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)
    ButtonsGroupBox.show()
    answer_group.hide()
    answer_button.setText('Ответить')


buttons = [rbtn1, rbtn2, rbtn3, rbtn4]

class Question():
    def __init__(self, question1, right_answer, wrong1, wrong2, wrong3):
        self.question1 = question1
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3




questions = []
questions.append(Question('выберите число 1', '1', '2', '3','4'))
questions.append(Question('выберите число 2', '2', '1', '3','4'))
questions.append(Question('выберите число 3', '3', '2', '1','4'))
questions.append(Question('выберите число 4', '4', '2', '1','3'))


main_win.count_questions = 0
main_win.score = 0

def ask(q):
    shuffle(buttons)
    buttons[0].setText(q.right_answer)
    buttons[1].setText(q.wrong1)
    buttons[2].setText(q.wrong2)
    buttons[3].setText(q.wrong3)

    question.setText(q.question1)
    true_answer.setText(q.right_answer)
    show_questions()

def check_answer():
    if buttons[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
    else:
        if buttons[1].isChecked() or buttons[2].isChecked() or buttons[3].isChecked():
            show_correct('Неправильно')

def show_correct(input1):
    answer_label.setText(input1)
    show_result()
   
def next_question():
    main_win.count_questions +=1
    ask(questions[randint(0, len(questions)-1)])

def click_ok():
    if answer_button.text() == 'Ответить':
        check_answer()
    else:
        if main_win.count_questions < 3:
            next_question()
        else:
            messbox = QMessageBox()
            messbox.setText(f'Правильные ответы: {main_win.score} из {main_win.count_questions}')
            messbox.exec_()
            

ask(questions[randint(0, len(questions)-1)])
answer_button.clicked.connect(click_ok)


main_win.resize(350, 250)
main_win.setLayout(Main_Vline)
main_win.show()
app.exec_()
