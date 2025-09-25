from langchain_core.runnables import RunnableLambda, RunnablePassthrough, RunnableParallel

def concat_bla(prompt: str) -> str:
    return prompt + " " + "bla"

runnable_1 = RunnableLambda(concat_bla)

def concat_bling(prompt: str) -> str:
    return prompt + " " + "bling"

runnable_2 = RunnableLambda(concat_bling)

def concat_xuxa(prompt: str) -> str:
    return prompt + " " + "xuxa"

runnable_3 = RunnableLambda(concat_xuxa)

runnable_pass = RunnablePassthrough()

start_prompt = runnable_pass.invoke("valls")

# calling parallel as dict format (is it possible in the middle of chain not in start of chain)
# chain = runnable_pass | runnable_1 | {
#     "result_2" : runnable_2,
#     "result_3" : runnable_3
# } | RunnablePassthrough.assign(oala=lambda x: "oaaaaala")

# on start of chain only RunnableParallel() is allowed (ps)

chain = runnable_pass | runnable_1 | RunnableParallel(
    result_2=runnable_2,
    result_3=runnable_3
) | RunnablePassthrough.assign(oala=lambda x: "oaaaaala")

print(chain.invoke(runnable_pass.invoke("Iniciando")))