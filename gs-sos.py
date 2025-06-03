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
    print("\n--- DOAÇÃO EM DINHEIRO VIA PIX ---")
    print("Contribua com a nossa causa via PIX. Sua doação será destinada diretamente às vítimas de desastres naturais.")
    print("Chave PIX: 123.456.789.00")
    print("Faça seu PIX agora mesmo e ajude quem precisa.")
    print("Não há valores mínimos ou máximos. Cada contribuição conta!")

    print("\n--- DOAÇÃO DE MANTIMENTOS E ROUPAS ---")
    print("Doe mantimentos e roupas usadas em bom estado para quem precisa.")

    print("\n📍 Pontos de Coleta:")
    print("Centro de Coleta 1: Rua das Flores, 123 - Centro")
    print("Centro de Coleta 2: Av. Brasil, 456 - Bairro Alto")
    print("Centro de Coleta 3: Rua Vitória, 789 - Zona Norte")

def como_pedir_socorro():
    print("\n=== COMO PEDIR AJUDA EM CASO DE EMERGÊNCIA ===")
    print("\n🆘 Em Caso de Emergência, Aja Rapidamente")
    print("Se você estiver em uma situação de risco, siga as orientações abaixo para pedir ajuda imediatamente.")

    print("\n📞 Contatos de Emergência Globais")
    print("• Emergências Gerais: 112 (UE, Canadá, Austrália, etc.)")
    print("• EUA/Canadá: 911")
    print("• Brasil: 190 (Polícia), 192 (SAMU), 193 (Bombeiros)")
    print("• Defesa Civil: 199 (Brasil), 112 (UE)")
    print("• Emergências Médicas Globais: 112")
    print("• Emergências Ambientais: 121 (alguns países)")

    print("\n📌 Dicas para Pedir Socorro")
    print("• Seja claro: tipo de emergência, local, nome.")
    print("• Mantenha a calma e fale devagar.")
    print("• Use apps oficiais com localização.")
    print("• Em desastres, siga rotas seguras e fontes confiáveis.")

    print("\n⚠️ Emergências Comuns e Ações:")
    print("• Incêndios: Saia rápido e ligue 193. Evite elevador.")
    print("• Acidentes: Chame 192, sinalize, não mova vítimas.")
    print("• Desastres: Procure áreas altas e siga instruções da Defesa Civil.")

    print("\n🌐 ONGs Mundiais")
    print("• Cruz Vermelha Internacional - www.ifrc.org")
    print("• Médicos Sem Fronteiras - www.msf.org / www.msf.org/contact-us")

def monitoramento_tempo_real():
    print("\n--- MONITORAMENTO EM TEMPO REAL ---")
    print("🌊 Enchente - Irã")
    print("🔥 Incêndio Florestal - Camarões")
    print("🌍 Tremor de Terra - Argentina")

def faq():
    print("\n=== FAQ - PERGUNTAS FREQUENTES ===")

    perguntas_respostas = [
        ("Como a plataforma ajuda durante eventos extremos?",
         "Nossa plataforma oferece monitoramento em tempo real das áreas afetadas, um sistema de doações e voluntariado, um chatbot inteligente para orientação, contato de emergência e informações sobre recursos e abrigos disponíveis na região."),
        ("Como funciona o chatbot integrado?",
         "O chatbot utiliza inteligência artificial para oferecer orientações sobre prevenção, primeiros socorros e informações específicas para cada tipo de desastre, auxiliando a população antes, durante e após os eventos extremos. Basta clicar no ícone de diálogo na parte inferior à direita da página."),
        ("Como são gerenciados os abrigos e recursos?",
         "A plataforma permite que autoridades, equipes de resgate e vítimas visualizem em tempo real a disponibilidade de abrigos, recursos essenciais e status das operações, facilitando a tomada de decisões rápidas e eficazes."),
        ("Como posso ajudar as vítimas?",
         "Você pode doar qualquer quantia em dinheiro via PIX, mantimentos como roupas e alimentos não perecíveis ou se voluntariar ajudando abrigos e equipes de triagem."),
        ("Quais tipos de eventos extremos são monitorados?",
         "A plataforma monitora diversos eventos, incluindo chuvas intensas, tremores de terra, incêndios florestais e enchentes, utilizando dados de satélites e sensores IoT."),
        ("O que fazer em casos de emergência?",
         "Na página inicial, clique em 'Pedir socorro'; a página contará com diversos telefones de emergência e algumas dicas do que fazer nesses casos.")
    ]

    for pergunta, resposta in perguntas_respostas:
        print(f"\n❓ {pergunta}")
        print(f"➡️  {resposta}")

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
        {"nome": "Escola Municipal Esperança", "endereco": "Rua das Flores, 123, Centro", "capacidade": "120 pessoas", "status": "Disponível", "contato": "(11) 99999-0001"},
        {"nome": "Ginásio Poliesportivo Vida", "endereco": "Av. das Nações, 456, Bairro Novo", "capacidade": "200 pessoas", "status": "Quase lotado", "contato": "(11) 99999-0002"},
        {"nome": "Igreja São João", "endereco": "Praça da Paz, 789, Vila Verde", "capacidade": "80 pessoas", "status": "Disponível", "contato": "(11) 99999-0003"},
        {"nome": "Centro Comunitário União", "endereco": "Rua do Sol, 321, Jardim Luz", "capacidade": "60 pessoas", "status": "Lotado", "contato": "(11) 99999-0004"}
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
        print(f"\n👤 {nome}\n🎓 RM: {rm}\n🔗 LinkedIn: {linkedin}\n💻 GitHub: {github}")

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
