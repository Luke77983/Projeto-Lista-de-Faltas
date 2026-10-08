import customtkinter

janela = customtkinter.CTk()
janela.title("Lista de Faltas")

janela._set_appearance_mode("dark")
janela.minsize(width=500, height=400)

janela.geometry("700x400")

abas = customtkinter.CTkTabview(janela,width=400,bg_color="black", fg_color="#504D4D", corner_radius=20, border_width=1, border_color="blue", segmented_button_fg_color="blue", segmented_button_selected_color="blue", segmented_button_unselected_hover_color="gray")
abas.pack()
abas.add("Código")
abas.add("Produtos")
abas.add("Valor")
abas.tab("Código").grid_columnconfigure(0,weight=1)
abas.tab("Produtos").grid_columnconfigure(0, weight=1)
abas.tab("Valor").grid_columnconfigure(0, weight=1)

texto = customtkinter.CTkLabel(abas.tab("Código"), text=" 001\n 002\n 003\n", text_color="white" )
texto.pack()

nomes = customtkinter.CTkLabel(abas.tab("Produtos"), text="Esmerilhadeira\n Tomada\n Alicate\n", text_color="white")
nomes.pack()


valores = customtkinter.CTkLabel(abas.tab("Valor"), text="R$299,99\n R$8,00\n R$29,99\n", text_color="white")
valores.pack()

caixa_texto = customtkinter.CTkTextbox(janela, width=300,height=350, fg_color="#504D4D", text_color="white", scrollbar_button_color="gray", bg_color="#504D4D", scrollbar_button_hover_color="blue", border_color="blue", border_width=1, corner_radius=15)
caixa_texto.pack()

caixa_texto.insert("0.0", "Título do seu Texto\n\n" + "Oi, meu nome é Goku\n\n" * 20)

janela.mainloop()