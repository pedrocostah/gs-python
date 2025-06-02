# Dados em memória
voluntarios = []
mensagens_contato = []

# Validações manuais
def validar_email(email):
    return "@" in email and "." in email and len(email) >= 6

def validar_telefone(telefone):
    return telefone.isdigit() and len(telefone) >= 8

# Funcionalidades
def cadastrar_voluntario():
    print("\n--- Cadastro de Voluntário ---")
    nome = input("Nome completo: ").strip()
    email = input("E-mail: ").strip()
    telefone = input("Telefone: ").strip()
    senha = input("Crie uma senha: ").strip()

    if not nome or not validar_email(email) or not validar_telefone(telefone) or not senha:
        print("Erro: dados inválidos.")
        return

    for v in voluntarios:
        if v["email"] == email or v["telefone"] == telefone:
            print("Erro: e-mail ou telefone já cadastrado.")
            return

    voluntarios.append({"nome": nome, "email": email, "telefone": telefone, "senha": senha})
    print("✅ Cadastro feito com sucesso!")

def enviar_contato():
    print("\n--- Contato ---")
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    mensagem = input("Mensagem: ").strip()

    if not nome or not validar_email(email) or not mensagem:
        print("Erro: dados inválidos.")
        return

    mensagens_contato.append({"nome": nome, "email": email, "mensagem": mensagem})
    print("✅ Mensagem enviada com sucesso!")

def informacoes_doacao():
    print("\n--- DOAÇÕES ---")
    print("Chave PIX: sos@ajuda.org")
    print("Locais de coleta: Escola Central, Praça da Liberdade, Ginásio Municipal")

def como_pedir_socorro():
    print("\n--- EMERGÊNCIA ---")
    print("193 - Bombeiros | 192 - SAMU | 190 - Polícia")
    print("Cruz Vermelha: contato@cruzvermelha.org")
    print("ONU: +1-202-555-0111")

def monitoramento_tempo_real():
    print("\n--- MONITORAMENTO ---")
    print("🌊 Enchente - São Paulo/SP")
    print("🔥 Incêndio Florestal - Amazônia")
    print("🌍 Tremor de Terra - Turquia")

def faq():
    print("\n--- FAQ ---")
    perguntas = [
        ("O que é o SOS Desastres Naturais?", "Uma plataforma de apoio durante desastres."),
        ("Como faço doações?", "Através de PIX ou postos de coleta."),
        ("Meus dados estão seguros?", "Sim, não divulgamos suas informações."),
        ("Posso ser voluntário mesmo morando longe?", "Sim, basta se cadastrar.")
    ]
    for p, r in perguntas:
        print(f"\n❓ {p}\n➡️  {r}")

def recursos_e_abrigos():
    print("\n--- RECURSOS E ABRIGOS ---")
    abrigos = [
        ("Abrigo Central", "1123456789", "Rua das Flores, 123", "Disponível"),
        ("Abrigo Zona Leste", "1198765432", "Av. Esperança, 456", "Quase cheio"),
        ("Abrigo Municipal", "1133332222", "Praça União, 789", "Lotado")
    ]
    for nome, tel, end, status in abrigos:
        print(f"\n🏠 {nome}\n📞 {tel}\n📍 {end}\n📊 {status}")

def chatbot():
    print("\n--- CHATBOT ---")
    print("🤖 Converse com nosso assistente virtual:")
    print("🔗 https://t.me/SOSDesastresChatbot")

def quem_somos():
    print("\n--- QUEM SOMOS ---")
    membros = [
        ("Pedro Henrique Costa", "RM559932", "https://linkedin.com/in/pedrocostahch", "https://github.com/pedrocostah"),
        ("Júlia Menezes", "RM565568", "https://linkedin.com/in/julia-menezesf", "https://github.com/juliamenezesf")
    ]
    for nome, rm, linkedin, github in membros:
        print(f"\n👤 {nome}\n🎓 {rm}\n🔗 LinkedIn: {linkedin}\n💻 GitHub: {github}")

# Menu principal
def menu():
    while True:
        print("\n=== SOS DESASTRES NATURAIS ===")
        print("1 - Fazer uma doação")
        print("2 - Como pedir socorro")
        print("3 - Seja um voluntário")
        print("4 - Monitoramento em tempo real")
        print("5 - Enviar mensagem de contato")
        print("6 - FAQ - Perguntas Frequentes")
        print("7 - Recursos e Abrigos")
        print("8 - Chatbot Inteligente (Telegram)")
        print("9 - Quem Somos")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            informacoes_doacao()
        elif opcao == "2":
            como_pedir_socorro()
        elif opcao == "3":
            cadastrar_voluntario()
        elif opcao == "4":
            monitoramento_tempo_real()
        elif opcao == "5":
            enviar_contato()
        elif opcao == "6":
            faq()
        elif opcao == "7":
            recursos_e_abrigos()
        elif opcao == "8":
            chatbot()
        elif opcao == "9":
            quem_somos()
        elif opcao == "0":
            print("✅ Obrigado por usar o SOS Desastres Naturais.")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

# Execução
if __name__ == "__main__":
    menu()
