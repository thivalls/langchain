from langchain.prompts import PromptTemplate

# USING CLASS + FORMAT to bind data
prompt_template_1 = PromptTemplate(
    input_variables=["especialidade", "area", "linguagem", "pergunta"],
    template="""
        Você é um {especialidade}, na area de {area} e trabalha com a linguagem {linguagem}\n 
        Pergunta: \n
        {pergunta}
    """
)
prompt_template_1 = prompt_template_1.format(especialidade="engenheiro de software", area="desenvolvimento de software", linguagem="python", pergunta=pergunta)
print(prompt_template_1)

# USING FROM TEMPLATE METHOD
prompt_template_2 = PromptTemplate.from_template("""Você é um {especialidade}, na area de {area} e trabalha com a linguagem {linguagem}\n 
        Pergunta: \n
        {pergunta}
    """)
print(prompt_template_2.invoke({"especialidade" : "engenheiro de software", "area":"desenvolvimento de software", "linguagem":"python", "pergunta":pergunta}))