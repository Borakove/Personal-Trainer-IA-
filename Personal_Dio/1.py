#Mapeamento 
class PersonalTrainerIA:
    def __init__(self):
        self.user_data = {}

    def collect_user_data(self):
        print("Bem-vindo ao Personal Trainer IA!")
        self.user_data['nome'] = input("Qual o seu nome? ")
        self.user_data['idade'] = int(input("Qual a sua idade? "))
        self.user_data['altura'] = float(input("Qual a sua altura (em metros)? "))
        self.user_data['peso'] = float(input("Qual o seu peso (em kg)? "))
        self.user_data['objetivo'] = input("Qual o seu objetivo (hipertrofia, emagrecimento, resistência)? ").lower()
        self.user_data['frequencia_treino'] = int(input("Quantos dias por semana você pode treinar? "))
        self.user_data['tempo_treino'] = int(input("Quanto tempo você tem para cada treino (em minutos)? "))
        self.user_data['nivel_atividade'] = input("Qual o seu nível de atividade atual (iniciante, intermediário, avançado)? ").lower()

    def show_user_data(self):
        print(f"\nInformações do usuário:")
        for key, value in self.user_data.items():
            print(f"{key.capitalize()}: {value}")

#Gerador de plano de treino
    def gerar_plano_treino(self):
        print("\nGerando plano de treino personalizado...\n")
        objetivo = self.user_data['objetivo']
        nivel = self.user_data['nivel_atividade']
        dias = self.user_data['frequencia_treino']
        tempo = self.user_data['tempo_treino']

        if objetivo == 'hipertrofia':
            if nivel == 'iniciante':
                treino = f"Treino de {dias} dias por semana, focado em exercícios básicos como supino, agachamento e levantamento terra. Cada sessão terá cerca de {tempo} minutos com ênfase em 3 séries de 8-12 repetições."
            elif nivel == 'intermediário':
                treino = f"Treino de {dias} dias, com divisão por grupos musculares (peito, costas, pernas). Exercícios compostos e isolados com 4 séries de 6-10 repetições."
            else:
                treino = f"Treino de {dias} dias com rotina avançada, incorporando técnicas como drop-sets e superséries, com exercícios focados na progressão de carga e variação de estímulos."
        
        elif objetivo == 'emagrecimento':
            treino = f"Treino de {dias} dias por semana, focado em alta intensidade e intervalos (HIIT), combinado com exercícios de força para aumentar o metabolismo. Duração de {tempo} minutos com ênfase em 4-5 exercícios compostos e movimentos multiarticulares."
        
        elif objetivo == 'resistência':
            treino = f"Treino de {dias} dias focado em resistência muscular, com circuitos de exercícios e baixa carga. Cada sessão terá {tempo} minutos com alta repetição (15-20 repetições) e curto descanso entre séries."
        
        else:
            treino = "Objetivo não reconhecido. Por favor, escolha entre hipertrofia, emagrecimento ou resistência."

        print(treino)

#Gerador de plano alimentar 
    def gerar_plano_alimentar(self):
        print("\nGerando plano alimentar personalizado...\n")
        objetivo = self.user_data['objetivo']
        peso = self.user_data['peso']
        
        if objetivo == 'hipertrofia':
            calorias = peso * 35  # Calorias para hipertrofia
            plano = f"Para hipertrofia, sua ingestão calórica recomendada é de cerca de {calorias} calorias por dia, com ênfase em proteínas (2g por kg de peso), carboidratos de qualidade e gorduras boas."
        
        elif objetivo == 'emagrecimento':
            calorias = peso * 25  # Calorias para emagrecimento
            plano = f"Para emagrecimento, sua ingestão calórica recomendada é de cerca de {calorias} calorias por dia, com um déficit de 300-500 calorias. Priorize proteínas, vegetais e carboidratos de baixo índice glicêmico."
        
        elif objetivo == 'resistência':
            calorias = peso * 30  # Calorias para resistência
            plano = f"Para resistência, você deve consumir cerca de {calorias} calorias por dia, com foco em carboidratos complexos e proteínas para sustentar o alto volume de treino."
        
        else:
            plano = "Objetivo não reconhecido para gerar plano alimentar."

        print(plano)

#Execução 
if __name__ == "__main__":
    personal_trainer = PersonalTrainerIA()
    personal_trainer.collect_user_data()
    personal_trainer.show_user_data()

    personal_trainer.gerar_plano_treino()
    personal_trainer.gerar_plano_alimentar()
