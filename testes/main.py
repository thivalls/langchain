# pip install langchain-groq => precisa instalar
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from pydantic import Field, BaseModel
from typing import Optional
from langchain_core.runnables import RunnableLambda
# from langchain_groq import ChatGroq

load_dotenv()

class GratherSoccerChampion(BaseModel):
    is_soccer_about: bool = Field(description="Is question about futebol? Fill with boolean value")
    name: Optional[str] = Field(description="Fill with the name of the first team from response or the main team from response. It can be the most important team or bigger one")

# question_of_user = "Qual o nome do maior tenista brasileiro?"
question_of_user = "quantos anos tem o futebol"

initial_prompt = """
    Você é um especialista em futebol brasileiro e deve responder apenas se o assunto for sobre futebol\n
    {format_instructions}
    {question_of_user}
"""

my_parser = PydanticOutputParser(pydantic_object=GratherSoccerChampion)

model = ChatOpenAI(model = "gpt-4o", temperature = 0.5)

rota_prompt_template = ChatPromptTemplate([("system", initial_prompt),],
                                          partial_variables={"format_instructions": my_parser.get_format_instructions()}
                                          )

chain = rota_prompt_template | model | my_parser

result = chain.invoke({"question_of_user" : question_of_user})

print(result)

if(result.is_soccer_about):
    if not result.name:
        print("it is about soccer but it is not about teams")
    else:
        print(f"o time é: {result.name}")
else:
    print("it is not about soccer")