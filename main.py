#objetivo: criar 3 funções usadas em estatística
#1 - Média aritmética
#2 - Desvio padrão
#3 - Valores máximo e mínimo

import tkinter as tk
import tkinter.ttk as tkk
import statistics as st

class estatistica():



    def __init__(self):
        self.vetor=[]

        tela= tk.Tk()
        tela.title("Estatística")
        tela.geometry("400x400")
        tela.resizable(width=False,height=False)

        #CONSTRUÇÃO DO LABEL ENTRADA DE VALORES
        lbEntradaValores=tk.Label(tela,text="Entre com os valores", font="Arial, 10")
        lbEntradaValores.place(x=30,y=30)
        # CONSTRUÇÃO DO CAMPO DE ENTRADA DE VALORES
        self.cxEntradaValores=tk.Entry(tela,justify="center")
        self.cxEntradaValores.place(x=30,y=50)
        # CONSTRUÇÃO DO BOTÃO OK
        btOk=tk.Button(tela,text="Ok",relief="raised", bg="light blue",command=self.inserirValores)
        btOk.place(x=70,y=72)

        # CONSTRUÇÃO DO LABEL LISTA DOS VALORES DIGITADOS
        lbValoresDigitados = tk.Label(tela, text="Valores", font="Arial, 10")
        lbValoresDigitados.place(x=60, y=120)
        #CONSTRUÇÃO DA LISTA
        self.lista= tk.Listbox(tela)
        self.lista.place(x=30,y=150)

        #PRIMEIRO SEPARADOR
        sep1=tkk.Separator(tela, orient="vertical")
        sep1.place(x=180,y=0,width=5,height=400)

        #CONSTRUÇÃO LABEL ESCOLHA A FUNÇÃO
        lbEscolhaFuncao=tk.Label(tela,text="Escolha a função",font="Arial, 10")
        lbEscolhaFuncao.place(x=220,y=30)

        # CONSTRUÇÃO DOS RADIO BUTTONS
        self.var=tk.IntVar()
        self.btRadio1=tk.Radiobutton(tela, text="Média",variable=self.var,value=0)
        self.btRadio1.place(x=220,y=55)
        self.btRadio2 = tk.Radiobutton(tela, text="Desvio padrão",variable=self.var,value=1)
        self.btRadio2.place(x=220, y=75)
        self.btRadio3 = tk.Radiobutton(tela, text="Máximo e mínimo",variable=self.var,value=2)
        self.btRadio3.place(x=220, y=95)

        # SEGUNDO SEPARADOR
        sep2 = tkk.Separator(tela, orient="horizontal")
        sep2.place(x=181, y=140, width=220, height=5)

        #CONSTRUÇÃO DO LABEL RESULTADO
        lbResultado= tk.Label(tela, text="Resultado", font="Arial, 10")
        lbResultado.place(x=240, y=150)
        # CONSTRUÇÃO DO LABEL VALOR FUNÇÃO MÉDIA
        lbValorMedia = tk.Label(tela, text="Média : ", font="Arial, 10")
        lbValorMedia.place(x=255, y=180)
        # CONSTRUÇÃO DO LABEL VALOR FUNÇÃO DP
        lbValorDP = tk.Label(tela, text="Desvio padrão : ", font="Arial, 10")
        lbValorDP.place(x=210, y=200)
        # CONSTRUÇÃO DO LABEL VALOR FUNÇÃO MAX MIN
        lbValorMAxMin = tk.Label(tela, text="Máximo e Mínimo : ", font="Arial, 10")
        lbValorMAxMin.place(x=188, y=220)

        # CONSTRUÇÃO DO LABEL VALOR FUNCOES

        self.lbValorMedia1 = tk.Label(tela, text="--", font="Arial, 10")
        self.lbValorMedia1.place(x=330, y=180)
        self.lbValorDP1 = tk.Label(tela, text="--", font="Arial, 10")
        self.lbValorDP1.place(x=330, y=200)
        self.lbValorMAxMin1 = tk.Label(tela, text="--", font="Arial, 10")
        self.lbValorMAxMin1.place(x=330, y=220)
        self.lbValorMAxMin2 = tk.Label(tela, text="--", font="Arial, 10")
        self.lbValorMAxMin2.place(x=370, y=220)

        # TERCEIRO SEPARADOR
        sep3 = tkk.Separator(tela, orient="horizontal")
        sep3.place(x=181, y=250, width=220, height=5)

        #CRIAÇÃO BOTÃO CALCULAR
        btCalcular=tk.Button(tela, text="Calcular",font="Arial, 12", relief="raised",bg="light blue", width=10,command=self.seletora)
        btCalcular.place(x=230,y=300)


        tela.mainloop()






        #FIM DA CONSTRUÇÃO DA TELA

    def inserirValores(self):

        self.lista.insert(0,float(self.cxEntradaValores.get()))
        self.vetor.append(self.lista.get(0))
        print(self.vetor)


    def media(self):
        media=round(st.mean(self.vetor),2)
        self.lbValorMedia1.config(text=str(media))
        print(media)
    def desvioPadrao(self):
        dp=round(st.stdev(self.vetor),2)
        self.lbValorDP1.config(text=str(dp))
        print(dp)
    def minimoMaximo(self):
        min = self.vetor[0]
        max = self.vetor[0]
        for i in range(len(self.vetor)):
            #achando o minimo
            if self.vetor[i]<min:
                min=self.vetor[i]
            #achando o máximo
            if self.vetor[i]>max:
                max=self.vetor[i]
        self.lbValorMAxMin1.config(text=str(max))
        self.lbValorMAxMin2.config(text=str(min))
        print(min)
        print(max)

    def seletora(self):

        if self.btRadio1.getvar(name=str(self.var))==0:
            self.media()
        if self.btRadio2.getvar(name=str(self.var))==1:
            self.desvioPadrao()
        if self.btRadio3.getvar(name=str(self.var))==2:
            self.minimoMaximo()




Est=estatistica()




