from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda

chain_1 = RunnablePassthrough()

def get_len(some_str: str) -> int:
    return len(some_str["input"])

def add_string(input_data: str) -> str:
    return input_data["input"] + " " + "conseguiu"

runnable_get_len = RunnableLambda(get_len)

chain_3 = RunnablePassthrough.assign(num_caract=runnable_get_len)

chain_4 = RunnableLambda(add_string)

runnable_passa_pra_frente = RunnablePassthrough()
runnable_parallel_result = RunnableParallel(
    transformar_entrada = chain_4,
    passe_para_frente = runnable_passa_pra_frente
)

runnable_pass = RunnablePassthrough()

chain = chain_1 | chain_3 | runnable_parallel_result | runnable_pass
 
print(chain.invoke({"input": "Parabéns Você"}))
