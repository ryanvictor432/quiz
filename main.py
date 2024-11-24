import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

df = pd.read_excel("Questions.xlsx")
questions = df.values.tolist()

score=0
current_question=0

def check_answer(answer):
    global score, current_question

    # Verifica se a resposta está correta antes de atualizar
    if answer == correct_answer.get():
        score += 1

    current_question += 1

    if current_question < len(questions):
        display_question()
    else:
        show_result()

def display_question():
    question, option1, option2, option3, option4, answer = questions[current_question]
    correct_answer.set(answer)  # Atualiza a resposta correta da pergunta atual
    question_label.config(text=question)
    option1_btn.config(text=option1, state=tk.NORMAL, command=lambda: check_answer(1))
    option2_btn.config(text=option2, state=tk.NORMAL, command=lambda: check_answer(2))
    option3_btn.config(text=option3, state=tk.NORMAL, command=lambda: check_answer(3))
    option4_btn.config(text=option4, state=tk.NORMAL, command=lambda: check_answer(4))

def show_result():
    messagebox.showinfo("Finalizado.",f"Parabens! Você chegou ao final.\n\nPontuação final: {score}/{len(questions)}")
    option1_btn.config(state=tk.NORMAL)
    option2_btn.config(state=tk.NORMAL)
    option3_btn.config(state=tk.NORMAL)
    option4_btn.config(state=tk. NORMAL)
    play_again_btn.pack()

def play_again():
    global score, current_question
    score = 0
    current_question = 0  # Volta para a primeira pergunta
    option1_btn.config(state=tk.NORMAL)
    option2_btn.config(state=tk.NORMAL)
    option3_btn.config(state=tk.NORMAL)
    option4_btn.config(state=tk.NORMAL)
    play_again_btn.pack_forget()
    display_question()  # Recarrega a primeira pergunta




janela= tk. Tk()
janela.title('quiz')
janela.geometry ("400x540")
background_color = "#ECECEC"
text_color= "#333333"
button_color = "4CAF50"
button_text_color = "#FFFFFF"
janela.config(bg=background_color)
janela.option_add('Font','Arial')

app_icon = PhotoImage(file='quiz 00.png')
app_label = tk.Label(janela,image=app_icon, bg=background_color)
app_label.pack(pady=10)
question_label = tk.Label(janela, text='',wraplength=400, bg= background_color, fg=text_color, font=('Arial', 12, "bold"))
question_label.pack(pady=20)

correct_answer= tk.IntVar()
option1_btn=tk.Button(janela,text="", width=70, bg=button_text_color,state=tk.DISABLED,font=('Arial',10,"bold"))
option1_btn.pack(pady=10)

option2_btn=tk.Button(janela,text="", width=70, bg=button_text_color,state=tk.DISABLED,font=('Arial',10,"bold"))
option2_btn.pack(pady=10)

option3_btn=tk.Button(janela,text="", width=70, bg=button_text_color,state=tk.DISABLED,font=('Arial',10,"bold"))
option3_btn.pack(pady=10)

option4_btn=tk.Button(janela,text="", width=70, bg=button_text_color,state=tk.DISABLED,font=('Arial',10,"bold"))
option4_btn.pack(pady=10)

play_again_btn=tk.Button(janela,command=play_again,text="Jogar de novo", width=50, bg=button_text_color,font=('Arial',10,"bold"))
play_again_btn.pack(pady=10)

display_question()









janela.mainloop()