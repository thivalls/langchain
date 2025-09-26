# documentação: https://python.langchain.com/docs/concepts/output_parsers/

# Realizando as importações:
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# Contextualização - Exemplo da aula anterior.

# Carregamento das variáveis de ambiente presentes em .env
load_dotenv()

### Exemplo 1

prompt_template = ChatPromptTemplate([("user", "Escreva um poema em {lingua} sobre o tema: {assunto}")])

# Criando o componente de langchain que iterage com os LLMs
model = ChatOpenAI(model="gpt-4o")

ouput_parser = StrOutputParser()

# PART 2: Criando a chain
chain1 = prompt_template | model | ouput_parser

# PART 3: Invoke da chain passando as variáveis.
resposta1 = chain1.invoke({"lingua": "pt-br", "assunto":"frutas"})

print(type(resposta1)) # aqui será criada uma AIMessage
print("--"*50)
print(resposta1) # Aqui estamos acessando o conteudo da mensagem via content.
print("--"*50)
