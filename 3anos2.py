import tkinter as tk

# =========================
# CONFIGURAÇÕES
# =========================

COR_FUNDO = "#ffd6e7"
COR_BOTAO = "#ff4d6d"
COR_BOTAO_ATIVO = "#c9184a"
COR_TEXTO = "#590d22"
COR_TITULO = "#c9184a"
COR_CERTO = "#4CAF50"
COR_ERRADO = "#e63946"

TEXTO_FINAL = """
Amor, hoje a gente completa 3 anos juntos e eu só tenho a agradecer por tudo que a gente viveu até aqui.

Foram 3 anos de muito amor, parceria, risadas, momentos bons e também momentos difíceis que a gente enfrentou juntos. E acho que é justamente isso que faz o nosso relacionamento ser tão especial pra mim: ter a certeza de que, independentemente da situação, eu tenho você do meu lado.

Obrigado por ser minha companheira, por me apoiar, por cuidar de mim, por ter paciência comigo e por fazer parte de tantos momentos importantes da minha vida.

Sou muito feliz por tudo que construímos nesses 3 anos e por todas as lembranças que já criamos juntos. Parece muito clichê, mas passou muito rápido. Ao mesmo tempo, quando eu lembro de tanta coisa que a gente já viveu, percebo o quanto crescemos e mudamos juntos.

E mesmo depois de todo esse tempo, continuo amando dividir meus dias, minhas preocupações e minhas besteiras com você.

Eu te amo muito.

Obrigado por esses 3 anos, mô. Que esse seja só mais um aniversário entre muitos que ainda vamos comemorar juntos.

Eu te amo demais e sou muito grato por ter você na minha vida.

Feliz 3 anossss ❤️
"""


# =========================
# PERGUNTAS
# =========================

perguntas = [
    {
        "pergunta": "Que dia a gente começou a namorar? ❤️",
        "opcoes": [
            "A) 09/03/2023",
            "B) 03/09/2023",
            "C) 03/09/2024",
            "D) 04/07/2023"
        ],
        "correta": 1
    },

    {
        "pergunta": "O que a gente mais gosta de comer? 😋❤️",
        "opcoes": [
            "A) Doces",
            "B) Legumes",
            "C) Carne",
            "D) Salgadinho"
        ],
        "correta": 0
    },

    {
        "pergunta": "Qual foi o primeiro show que fomos juntos sozinhos? 🎶❤️",
        "opcoes": [
            "A) Matheus e Kauan",
            "B) Luan Santana",
            "C) Bruno Mars",
            "D) Matuê"
        ],
        "correta": 2
    }
]

pergunta_atual = 0
bloqueado = False


# =========================
# FUNÇÕES
# =========================

def responder(indice):
    global pergunta_atual, bloqueado

    if bloqueado:
        return

    bloqueado = True

    correta = perguntas[pergunta_atual]["correta"]
    botao_clicado = botoes[indice]

    if indice == correta:
        botao_clicado.config(
            bg=COR_CERTO,
            text="✓ " + perguntas[pergunta_atual]["opcoes"][indice]
        )

        feedback.config(
            text="Acertou, amor ❤️",
            fg=COR_CERTO
        )

        janela.after(900, proxima_pergunta)

    else:
        botao_clicado.config(
            bg=COR_ERRADO
        )

        feedback.config(
            text="KKKKKK errou 😭 tenta de novo",
            fg=COR_ERRADO
        )

        janela.after(
            700,
            lambda: restaurar_botao(indice)
        )


def restaurar_botao(indice):
    global bloqueado

    botoes[indice].config(
        bg=COR_BOTAO
    )

    feedback.config(text="")

    bloqueado = False


def proxima_pergunta():
    global pergunta_atual, bloqueado

    pergunta_atual += 1
    bloqueado = False

    if pergunta_atual < len(perguntas):
        mostrar_pergunta()
    else:
        mostrar_pergunta_final()


def mostrar_pergunta():
    pergunta = perguntas[pergunta_atual]

    contador.config(
        text=f"Pergunta {pergunta_atual + 1} de 4 ❤️"
    )

    titulo_pergunta.config(
        text=pergunta["pergunta"]
    )

    feedback.config(text="")

    for i in range(4):

        botoes[i].config(
            text=pergunta["opcoes"][i],
            bg=COR_BOTAO,
            state="normal",
            command=lambda i=i: responder(i)
        )

        botoes[i].pack(
            pady=8,
            ipadx=10,
            ipady=8
        )


def mostrar_pergunta_final():

    contador.config(
        text="Pergunta 4 de 4 ❤️"
    )

    titulo_pergunta.config(
        text="Eu te amo muito amor,\nobrigado por esses nossos 3 anos!!!! ❤️"
    )

    feedback.config(text="")

    for botao in botoes:
        botao.pack_forget()

    botao_final.pack(
        pady=30,
        ipadx=25,
        ipady=12
    )


def mostrar_texto_final():

    frame_quiz.pack_forget()

    frame_final.pack(
        fill="both",
        expand=True
    )

    animar_coracoes()


def animar_coracoes():

    coracoes.config(
        text="❤️"
    )

    janela.after(
        300,
        lambda: coracoes.config(
            text="❤️ ❤️ ❤️"
        )
    )

    janela.after(
        600,
        lambda: coracoes.config(
            text="❤️ ❤️ ❤️ ❤️ ❤️"
        )
    )

    janela.after(
        1000,
        iniciar_texto
    )


def iniciar_texto():

    texto_final.config(state="normal")
    texto_final.delete("1.0", tk.END)
    texto_final.config(state="disabled")

    escrever_texto(0)


def escrever_texto(indice):

    if indice < len(TEXTO_FINAL):

        texto_final.config(state="normal")

        texto_final.insert(
            tk.END,
            TEXTO_FINAL[indice]
        )

        texto_final.see(tk.END)

        texto_final.config(state="disabled")

        janela.after(
            12,
            escrever_texto,
            indice + 1
        )


# =========================
# JANELA PRINCIPAL
# =========================

janela = tk.Tk()

janela.title(
    "❤️ Quiz dos nossos 3 anos ❤️"
)

janela.geometry(
    "750x700"
)

janela.configure(
    bg=COR_FUNDO
)

janela.resizable(
    False,
    False
)


# =========================
# TELA DO QUIZ
# =========================

frame_quiz = tk.Frame(
    janela,
    bg=COR_FUNDO
)

frame_quiz.pack(
    fill="both",
    expand=True
)


coracao = tk.Label(
    frame_quiz,
    text="❤️",
    font=("Arial", 60),
    bg=COR_FUNDO
)

coracao.pack(
    pady=(35, 5)
)


titulo_quiz = tk.Label(
    frame_quiz,
    text="Quiz dos nossos 3 anos",
    font=("Arial", 26, "bold"),
    fg=COR_TITULO,
    bg=COR_FUNDO
)

titulo_quiz.pack(
    pady=10
)


contador = tk.Label(
    frame_quiz,
    text="",
    font=("Arial", 12),
    fg="#9d4edd",
    bg=COR_FUNDO
)

contador.pack(
    pady=5
)


titulo_pergunta = tk.Label(
    frame_quiz,
    text="",
    font=("Arial", 18, "bold"),
    fg=COR_TEXTO,
    bg=COR_FUNDO,
    wraplength=650,
    justify="center"
)

titulo_pergunta.pack(
    pady=25
)


# =========================
# BOTÕES
# =========================

botoes = []

for i in range(4):

    botao = tk.Button(
        frame_quiz,
        text="",
        font=("Arial", 14, "bold"),
        width=30,
        bg=COR_BOTAO,
        fg="white",
        activebackground=COR_BOTAO_ATIVO,
        activeforeground="white",
        bd=0,
        cursor="hand2"
    )

    botoes.append(botao)


feedback = tk.Label(
    frame_quiz,
    text="",
    font=("Arial", 14, "bold"),
    bg=COR_FUNDO
)

feedback.pack(
    pady=15
)


# =========================
# ÚLTIMA PERGUNTA
# =========================

botao_final = tk.Button(
    frame_quiz,
    text="A) Ir para o fim do quiz ❤️",
    font=("Arial", 15, "bold"),
    bg=COR_BOTAO,
    fg="white",
    activebackground=COR_BOTAO_ATIVO,
    activeforeground="white",
    bd=0,
    cursor="hand2",
    command=mostrar_texto_final
)


# =========================
# TELA FINAL
# =========================

frame_final = tk.Frame(
    janela,
    bg=COR_FUNDO
)


coracoes = tk.Label(
    frame_final,
    text="",
    font=("Arial", 32),
    bg=COR_FUNDO
)

coracoes.pack(
    pady=(20, 5)
)


titulo_final = tk.Label(
    frame_final,
    text="Feliz 3 anossss ❤️",
    font=("Arial", 27, "bold"),
    fg=COR_TITULO,
    bg=COR_FUNDO
)

titulo_final.pack(
    pady=(5, 15)
)


texto_final = tk.Text(
    frame_final,
    wrap="word",
    font=("Arial", 13),
    bg="#fff0f5",
    fg=COR_TEXTO,
    bd=0,
    padx=30,
    pady=25,
    spacing1=5,
    spacing3=8
)

texto_final.pack(
    padx=40,
    pady=(0, 30),
    fill="both",
    expand=True
)

texto_final.config(
    state="disabled"
)


# =========================
# COMEÇAR
# =========================

mostrar_pergunta()

janela.mainloop()