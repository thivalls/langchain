# pip install langchain-groq => precisa instalar
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
# from langchain_groq import ChatGroq

load_dotenv()

pergunta = "como posso criar uma lista o mais perfomatica possivel?"

prompt = PromptTemplate(
    input_variables=["especialidade", "area", "linguagem", "pergunta"],
    template="""
        Você é um {especialidade}, na area de {area} e trabalha com a linguagem {linguagem}\n 
        Pergunta: \n
        {pergunta}
    """
)

# Para gerar o texto com uma variável:
prompt = prompt.format(especialidade="engenheiro de software", area="desenvolvimento de software", linguagem="python", pergunta=pergunta)
print(prompt)

model = ChatOpenAI(model = "gpt-4o", temperature = 0.1)
# model = ChatGroq(model = "llama-3.1-8b-instant", temperature = 0.1)

# O CHatModel é um componente LangChain então ele possui o protocolo invoke()

resposta = model.invoke(prompt)

# print("--------RESPOSTA AIMessage:---------")
# print(resposta)
# print("-------------------------------------")

print("--------RESPOSTA Somente Texto:------")
print(resposta.content)
print("-------------------------------------")
