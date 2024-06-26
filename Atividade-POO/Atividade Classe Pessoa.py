class Pessoa:
    def __init__(self, nome, ano_nascimento, altura, peso, genero, cpf, cep, numero, email):
        self.nome = nome
        self.ano_nascimento = ano_nascimento
        self.altura = altura
        self.peso = peso
        self.genero = genero
        self.cpf = cpf
        self.cep = cep
        self.numero = numero
        self.email = email

    def calcular_idade(self, ano_atual):
        return ano_atual - self.ano_nascimento

    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.calcular_idade(2023)}\nAltura: {self.altura} cm\nPeso: {self.peso} Kg\nGênero: {self.genero}\nCPF: {self.cpf}\nCEP: {self.cep}\nNúmero: {self.numero}\nE-mail: {self.email}"


def cadastrar_usuario():
    print(".___________________________________.")
    print("| Bem-vindo ao cadastro de usuário! |")
    print("|___________________________________|")
    print(" ")
    print("Iremos iniciar com um questionário, ok?")

    print("PART 1/3")
    nome = input("Let's go! Qual o seu nome?")
    ano_nascimento = int(input("Qual ano você nasceu?"))
    calculo_idade = 2023 - ano_nascimento

    if calculo_idade >= 18:
        print("PART 2/3 - Descrições adicionais.")
        altura = float(input("Altura (em cm): "))
        peso = float(input("Peso (em Kg): "))
        genero = input("Gênero (Feminino/Masculino): ")
        cpf = input("CPF: ")
        cep = input("CEP: ")

        print("PART 3/3 - CONTATO")
        numero = input("Número: ")
        email = input("E-mail: ")

        return Pessoa(nome, ano_nascimento, altura, peso, genero, cpf, cep, numero, email)
    else:
        print("Parece que você ainda não atingiu a idade mínima...")
        return None


def main():
    pessoa = cadastrar_usuario()
    if pessoa:
        print("\n._________________________________.")
        print("|      MODELAÇÃO DEFINITIVA       |")
        print("|_________________________________|")
        print(pessoa)
        print("|_______________________________")
    else:
        print("Cadastro não realizado.")

#GPT
if __name__ == "__main__":
    main()


def verificar_condicoes(acao):
    if acao == "falar":
        print("Não pode dormir ou comer.")
    elif acao == "andar":
        print("Não pode dormir.")
    elif acao == "dormir":
        print("Não pode falar, andar ou comer.")
    elif acao == "comer":
        print("Não pode falar ou dormir.")
    else:
        print("Ação inválida.")

# Exemplos de uso:
verificar_condicoes("falar")
verificar_condicoes("andar")
verificar_condicoes("dormir")
verificar_condicoes("comer")
verificar_condicoes("correr")  # Exemplo de ação inválida
