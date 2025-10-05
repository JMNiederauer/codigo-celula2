import time # Para adicionar pausas e simular "carregamento" ou reflexão
import os   # Para limpar a tela (opcional, melhora a visualização)

# --- Funções Auxiliares ---
def limpar_tela():
    # Limpa a tela do console para uma melhor experiência
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar(segundos=2):
    # Pausa o jogo por um número de segundos
    time.sleep(segundos)

def digitar_texto(texto, velocidade=0.03):
    # Simula o texto sendo digitado caractere por caractere
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(velocidade)
    print() # Nova linha no final

# --- Variáveis Globais (Estado do Jogo) ---
# Vamos usar um dicionário para guardar o que Pedro já aprendeu
conhecimentos_pedro = {
    "membrana_plasmática_aprendida": False,
    "dna_conectado": False,
    "leucocitos_ativados": False,
    # Adicione mais conforme Pedro avança e aprende
}

# --- Cenas do Jogo ---

def iniciar_jogo():
    limpar_tela()
    digitar_texto("🔐 BEM-VINDO AO JOGO: CÓDIGO CÉLULA – O HACKER P3DR0")
    pausar()
    digitar_texto("Você é P3dr0, um jovem hacker preso em um supercomputador biológico chamado BioMainframe.")
    digitar_texto("Para escapar, você precisará aprender tudo sobre células e estruturas do corpo humano...")
    pausar(3)
    digitar_texto("\nSua missão é coletar informações e reativar os sistemas do BioMainframe, que parece estar em modo de segurança.")
    input("\nPressione ENTER para iniciar sua jornada...\n")
    explorar_membrana_plasmatica()

def explorar_membrana_plasmatica():
    limpar_tela()
    digitar_texto("\n🧩 CAPÍTULO 1 – O Firewall da Célula (Membrana Plasmática)")
    digitar_texto("Você acorda em uma área escura e fria. Telas de energia azul cintilam ao seu redor, formando uma barreira.")
    digitar_texto("Um texto digital flutua: 'Membrana Plasmática - Controle de Acesso'.")

    while not conhecimentos_pedro["membrana_plasmática_aprendida"]:
        digitar_texto("\nO que você deseja fazer?")
        digitar_texto("1. Observar a barreira de perto")
        digitar_texto("2. Tentar forçar a passagem")
        digitar_texto("3. Procurar por alguma informação nas telas")
        
        escolha = input(">>> ").strip()

        if escolha == "1":
            digitar_texto("Você se aproxima da barreira. Pequenas partículas brilhantes atravessam-na em um fluxo constante.")
            digitar_texto("Algumas entram, outras saem. É como um porteiro controlando o tráfego.")
            pausar(3)
            digitar_texto(">> Insight: A Membrana Plasmática permite a passagem seletiva de substâncias.")
            conhecimentos_pedro["membrana_plasmática_aprendida"] = True
            pausar(2)
            digitar_texto("Uma fenda se abre na barreira. Você descobriu como o sistema funciona!")
            digitar_texto("✅ Acesso liberado ao Citoplasma.")
            input("\nPressione ENTER para entrar...")
        elif escolha == "2":
            digitar_texto("Você tenta empurrar a barreira, mas uma descarga elétrica te repele suavemente.")
            digitar_texto("O sistema não vai ceder à força bruta.")
            pausar(2)
        elif escolha == "3":
            digitar_texto("Nas telas, você vê diagramas complexos de moléculas e o que parecem ser 'portões' se abrindo e fechando.")
            digitar_texto("As palavras 'permeabilidade seletiva' piscam rapidamente.")
            pausar(3)
            digitar_texto(">> Insight: A Membrana Plasmática é inteligente! Ela seleciona o que entra e sai.")
            conhecimentos_pedro["membrana_plasmática_aprendida"] = True
            pausar(2)
            digitar_texto("Uma fenda se abre na barreira. Você descobriu como o sistema funciona!")
            digitar_texto("✅ Acesso liberado ao Citoplasma.")
            input("\nPressione ENTER para entrar...")
        else:
            digitar_texto("Comando inválido. Tente novamente.")
            pausar(1)
            
    explorar_citoplasma()

def explorar_citoplasma():
    limpar_tela()
    digitar_texto("\n🧬 CAPÍTULO 2 – O Corredor Principal (Citoplasma)")
    digitar_texto("Você entra em um vasto espaço, iluminado por uma luz difusa. É o Citoplasma, o 'preenchimento' da célula.")
    digitar_texto("Pequenas estruturas flutuam por toda parte, conectadas por filamentos de energia.")
    digitar_texto("Você vê acessos para diferentes áreas:")
    
    while True: # Loop para permitir ao jogador explorar o citoplasma e decidir para onde ir
        digitar_texto("\nPara onde você deseja ir?")
        digitar_texto("1. Explorar a área brilhante com estruturas em espiral (Parece o Núcleo!)")
        digitar_texto("2. Investigar as pequenas 'fábricas' flutuantes (Ribossomos e Retículos?)")
        digitar_texto("3. Observar as cápsulas energéticas que pulsam (Mitocôndrias?)")
        digitar_texto("4. Voltar (Se houvesse um lugar para voltar)") # Podemos remover isso por enquanto
        
        escolha = input(">>> ").strip()

        if escolha == "1":
            explorar_nucleo()
            break # Sai do loop do citoplasma uma vez que a nova cena é acessada
        elif escolha == "2":
            explorar_fabrica_proteinas()
            break
        elif escolha == "3":
            explorar_mitocondria()
            break
        elif escolha == "4":
            digitar_texto("Não há para onde voltar agora. Você precisa avançar!")
            pausar(1)
        else:
            digitar_texto("Comando inválido. Tente novamente.")
            pausar(1)

def explorar_nucleo():
    limpar_tela()
    digitar_texto("\n🧬 CAPÍTULO 4 – A Sala do Código (Núcleo)")
    digitar_texto("Você entra em uma câmara esférica, onde filamentos luminosos se entrelaçam em espirais complexas.")
    digitar_texto("Um painel exibe: 'DNA - Blueprint da Vida'.")
    
    if not conhecimentos_pedro["dna_conectado"]:
        digitar_texto("Há quatro terminais à sua frente, cada um com uma letra: A, T, C, G.")
        digitar_texto("Um prompt aparece: 'Conecte os pares corretos para ativar a sequência genética.'")
        digitar_texto("Você se lembra do que aprendeu em seus estudos sobre códigos...")
        
        tentativas = 0
        while not conhecimentos_pedro["dna_conectado"] and tentativas < 3: # Limita as tentativas
            digitar_texto("\nQuais letras você conecta (ex: AT ou CG)?")
            par1 = input("Primeiro par: ").strip().upper()
            par2 = input("Segundo par: ").strip().upper()
            
            if (par1 == "AT" or par1 == "TA") and (par2 == "CG" or par2 == "GC"):
                digitar_texto("⚡ Conexão estabelecida! Os filamentos de DNA brilham intensamente.")
                digitar_texto("Você sentiu o poder da informação genética fluindo.")
                digitar_texto(">> Insight: O DNA armazena todas as instruções para a vida, usando os pares A-T e C-G.")
                conhecimentos_pedro["dna_conectado"] = True
                pausar(3)
            else:
                digitar_texto("❌ Conexão incorreta. Os filamentos tremem e voltam ao estado inicial.")
                tentativas += 1
                if tentativas == 3:
                    digitar_texto("Falha na conexão... O sistema de segurança do Núcleo está ativo.")
                    digitar_texto("Você precisa voltar e tentar de novo mais tarde. Volte ao Citoplasma.")
                    pausar(3)
                    explorar_citoplasma() # Volta para o citoplasma
                    return # Sai da função do núcleo
                else:
                    digitar_texto(f"Tente novamente. Você tem {3 - tentativas} tentativa(s) restante(s).")
                    pausar(2)
                    
    if conhecimentos_pedro["dna_conectado"]:
        digitar_texto("O Núcleo já está ativado. Você pode explorar outras áreas ou voltar ao Citoplasma.")
        input("\nPressione ENTER para voltar ao Citoplasma...")
        explorar_citoplasma()


def explorar_fabrica_proteinas():
    limpar_tela()
    digitar_texto("\n⚙️ CAPÍTULO 5 – A Fábrica de Proteínas (Ribossomos e Retículo Endoplasmático)")
    digitar_texto("Você adentra uma área agitada, cheia de pequenas máquinas trabalhando. Elas recebem 'códigos' e montam 'blocos'.")
    digitar_texto("Uma tela exibe: 'RNA -> Ribossomo -> Proteína'.")
    digitar_texto(">> Insight: O RNA leva as informações do DNA até os Ribossomos, onde as proteínas são construídas!")
    digitar_texto("Estas proteínas são os 'operários' que fazem tudo funcionar no corpo.")
    
    input("\nPressione ENTER para voltar ao Citoplasma e continuar explorando...")
    explorar_citoplasma()

def explorar_mitocondria():
    limpar_tela()
    digitar_texto("\n🏭 CAPÍTULO 6 – A Usina de Energia (Mitocôndria)")
    digitar_texto("Você entra em uma câmara que pulsa com energia, como um pequeno reator nuclear.")
    digitar_texto("Luzes laranjas e vermelhas indicam calor e atividade constante.")
    digitar_texto("Uma placa luminosa exibe: 'Energia Celular - ATP'.")
    digitar_texto(">> Insight: Esta é a Mitocôndria, a usina de energia que fornece combustível para todas as atividades da célula!")
    
    input("\nPressione ENTER para voltar ao Citoplasma e continuar explorando...")
    explorar_citoplasma()


# --- Iniciar o Jogo ---
iniciar_jogo()