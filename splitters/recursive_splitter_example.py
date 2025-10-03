from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter

text = """
A inteligência artificial (IA) tem se tornado uma das áreas mais transformadoras da tecnologia, impactando setores que vão desde a saúde até as finanças. Seu principal objetivo é criar sistemas capazes de aprender, raciocinar e tomar decisões de forma semelhante aos seres humanos, mas com maior velocidade e precisão. Isso é possível graças a técnicas como aprendizado de máquina, redes neurais e processamento de linguagem natural.
Nos últimos anos, a evolução da IA tem acelerado de forma significativa, impulsionada pelo aumento da capacidade computacional e pela disponibilidade de grandes volumes de dados. Ferramentas de IA já estão presentes no cotidiano, como assistentes virtuais, tradutores automáticos e sistemas de recomendação em plataformas digitais. Além disso, no campo corporativo, ela ajuda empresas a otimizar processos, reduzir custos e melhorar a experiência do cliente.
Apesar dos avanços, a IA também levanta desafios importantes, como questões éticas, privacidade de dados e o impacto no mercado de trabalho. É fundamental estabelecer regulamentos claros e práticas responsáveis para garantir que seu uso traga benefícios coletivos sem comprometer direitos individuais. O futuro da IA aponta para um equilíbrio entre inovação e responsabilidade, onde a tecnologia pode ampliar o potencial humano e contribuir para soluções mais inteligentes e inclusivas.
"""

original_text = Document(page_content=text)

# print(original_text.page_content)

docs = [original_text]

# print(docs)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=40,
    chunk_overlap=10,
    length_function=len,
    separators=[""],
)

spliched_docs = text_splitter.split_documents(docs)

i = 0
for doc in spliched_docs:
    print("--" * 20)
    print(f"chunk: {i}")
    print("--" * 20)
    print(doc.page_content)
    print("--" * 20)
    i += 1
