# AutomacaoEmissoesdeNotasFiscais
- Automação de processo de emissão de notas ficais de vários clientes de uma só vez.
- Desafio: A depender do número de clientes de uma determinada empresa é necessário emitir incontáveis notas fiscais o que pode ser um trabalho manual muito repetitivo e que perfeitamente, pode ser facilitado com um projeto python de Automação Web. Este foi meu desafio. 

-Pontapé Incial: Reprodução do processo manual para depois entender quais ferramentas, bibliotecas python seriam necessárias para resolver o desafio. A partir dessa reprodução um step by step foi criado para que dele pudesse ser traçada a lógica de programação, conforme a seguir:

#Passo 1: Entrar no navegador

#Passo2: Preencher login e senha

#Passo3: Preencher os campos do sistema
    #Campo 1: Nome/Razão Social
    #Campo 2: Endereço
    #Campo 3: Bairro
    #Campo 4: Município
    #Campo 5: CEP
    #Campo 6: UF
    #Campo 7: CNPJ/CPF
    #Campo 8: Incrição estadual
    #Campo 9: Descrição do produto/serviço
    #Campo 10: Quantidade
    #Campo 11: Valor Unitário
    #Campo 12: Valor Total
    
#Passo 4: Clicar no botão de Emitir Nota

#Passo 5: Recarregar o navegador e limpar o formulário
    
- Considerações Finais: Se tratando de uma Automação Web a principal ferramenta utilizada foi o Selenium. A biblioteca Pandas foi utilizada para ler a tabela que simulava uma lista de clientes, os quais deveriam ser emitidas notas fiscais, de uma determinada empresa. Trata-se de um projeto pequeno em que todo o código está centralizado na pasta: AutomacaoEmissoesdeNotasFiscais.py.
