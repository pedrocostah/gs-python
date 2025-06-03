# SOS Desastres Naturais - Projeto Python (sem bibliotecas externas)

voluntarios = []
mensagens_contato = []

def validar_email(email):
    return "@" in email and "." in email and len(email) >= 6

def validar_telefone(telefone):
    return telefone.isdigit() and len(telefone) >= 8

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

def recursos_e_abrigos_interativo():
    print("\n--- RECURSOS ESSENCIAIS DISPONÍVEIS ---")
    recursos = [
        "Água potável: Distribuição em pontos de apoio e abrigos.",
        "Alimentos não perecíveis: Kits de emergência para famílias afetadas.",
        "Energia elétrica emergencial: Geradores e painéis solares portáteis.",
        "Atendimento médico: Postos móveis de primeiros socorros e equipes de saúde.",
        "Produtos de higiene: Kits de higiene pessoal e limpeza.",
        "Assistência psicológica: Apoio presencial e remoto para afetados.",
        "Comunicação: Pontos de Wi-Fi e telefonia emergencial em abrigos."
    ]
    for recurso in recursos:
        print(f"✔️ {recurso}")

    print("\n--- LISTA DE ABRIGOS TEMPORÁRIOS DISPONÍVEIS ---")
    abrigos = [
        {
            "nome": "Escola Municipal Esperança",
            "endereco": "Rua das Flores, 123, Centro",
            "capacidade": "120 pessoas",
            "status": "Disponível",
            "contato": "(11) 99999-0001"
        },
        {
            "nome": "Ginásio Poliesportivo Vida",
            "endereco": "Avenida das Nações, 456, Bairro Novo",
            "capacidade": "200 pessoas",
            "status": "Quase lotado",
            "contato": "(11) 99999-0002"
        },
        {
            "nome": "Igreja São João",
            "endereco": "Praça da Paz, 789, Vila Verde",
            "capacidade": "80 pessoas",
            "status": "Disponível",
            "contato": "(11) 99999-0003"
        },
        {
            "nome": "Centro Comunitário União",
            "endereco": "Rua do Sol, 321, Jardim Luz",
            "capacidade": "60 pessoas",
            "status": "Lotado",
            "contato": "(11) 99999-0004"
        }
    ]

    for i, abrigo in enumerate(abrigos, 1):
        print(f"{i}. {abrigo['nome']} ({abrigo['status']})")

    opcao = input("Selecione um abrigo para ver mais detalhes (ou digite 0 para voltar): ").strip()

    if opcao.isdigit():
        indice = int(opcao)
        if indice == 0:
            return
        elif 1 <= indice <= len(abrigos):
            a = abrigos[indice - 1]
            print(f"\n🏠 Nome: {a['nome']}")
            print(f"📍 Endereço: {a['endereco']}")
            print(f"👥 Capacidade: {a['capacidade']}")
            print(f"📊 Status: {a['status']}")
            print(f"📞 Contato: {a['contato']}")
        else:
            print("❌ Opção inválida.")
    else:
        print("❌ Entrada inválida. Digite apenas números.")

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
            recursos_e_abrigos_interativo()
        elif opcao == "8":
            chatbot()
        elif opcao == "9":
            quem_somos()
        elif opcao == "0":
            print("✅ Obrigado por usar o SOS Desastres Naturais.")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
