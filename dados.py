import pandas as pd
questions = [
    ["Onde Anne Frank escreveu seu diário?", "Em um campo de concetração", "No sótão de sua casa", "No anexo secreto em Amsterdã", "Em uma casa de campo na França", 3],
    [" Quando Anne Frank começou a escrever seu diário?", "1935", "1939", "1942", "1944", 3],
    ["Qual foi a razão pela qual Anne Frank e sua família se esconderam?", "Fugir de um regime militar", "Fuga das perseguições nazistas aos judeus", "Buscar um novo começo na América", "Escapar de um ataque aéreo", 2],
    ["Qual é o papel histórico de Dandara no contexto do Quilombo dos Palmares?", " Foi responsável exclusivamente pela produção agrícola do quilombo.", "Atuou como estrategista militar e líder na defesa contra invasores.", "Criou alianças com os portugueses para proteger o quilombo.", "Era apenas a esposa de Zumbi, sem envolvimento político ou militar.", 2],
    ["Por que Dandara é considerada um símbolo de resistência no Brasil?", "Por organizar a fuga de escravizados para os quilombos de forma pacífica.", "Por sua participação ativa nas batalhas e por escolher a morte ao invés da escravidão.", " Por liderar uma revolta vitoriosa contra os portugueses em 1694.", "Por ser a única mulher reconhecida no Quilombo dos Palmares.", 2],
    ["Quais eram as principais contribuições de Dandara dentro do Quilombo dos Palmares?", "Liderança militar, organização da comunidade e defesa da autonomia.", "Representação diplomática do quilombo perante os portugueses.", "Criação de escolas e ensino de estratégias de luta.", "Expansão das terras quilombolas para outras regiões do Brasil.", 1],
    ["Em qual ano Clarice Lispector publicou seu último romance, “A Hora da Estrela?", "1943", "1961", "1977", "1985",3],
    ["Clarice Lispector viveu boa parte da infância e adolescência em qual estado brasileiro?", "São Paulo", "Rio de Janeiro", "Pernabumco", "Minas Gerais", 3],
    ["Clarice Lispector era fascinada por temas filosóficos e biológicos. Em seu conto “O Ovo e a Galinha”, o ovo é considerado um exemplo clássico de qual conceito biológico?", "Fotossíntese", "Ciclo de Vida", "Embriologia", "Metamorfose", 2],
    ["Qual elemento Marie Curie descobriu juntamente com seu marido Pierre Curie, e que lhe rendeu o Prêmio Nobel de Física em 1903?", " Neônio", "Polônio", "Carbono", "Radônio", 2],
    ["Marie Curie foi a primeira mulher a ganhar um Prêmio Nobel. Em que instituição ela realizou grande parte de suas pesquisas sobre radioatividade?", "Universidade de Paris", " Instituto Curie", "Universidade de Varsóvia", "Laboratório de Física Nuclear de Copenhague", 1],
    ["Marie Curie enfrentou desafios devido ao seu gênero em um campo dominado por homens. Qual foi uma das principais barreiras que ela superou para se destacar na ciência? ", "O preconceito racial", "A falta de financiamento para seus estudos", "A dificuldade em ser aceita nas conferências científicas", "O isolamento em seu trabalho de pesquisa", 3],
    ["Angela Davis ganhou notoriedade por seu envolvimento em qual movimento político nos anos 1960?", "Movimento Hippie",  "Movimento Panteras Negras", "Movimento Feminista Branco","Movimento Ambientalista", 2],
    ["Em qual estado dos Estados Unidos Angela Davis nasceu?", "Nova York", "Califórnia", "Alabama","Texas", 3],
    ["Qual é o conceito usado por Angela Davis para criticar o sistema prisional?", "Justiça restaurativa", "Complexo industrial-prisional", "Prisionização seletiva", "Cárcere disciplinar", 2],
]
df = pd.DataFrame(questions,columns=("Perguntas","Opção 1",'Opção 2','Opção 3','Opção 4','Resposta') )
df.to_excel('Questions.xlsx', index=False)
print("Perguntas ensiridas")