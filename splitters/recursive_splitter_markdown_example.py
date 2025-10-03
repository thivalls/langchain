from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter, MarkdownHeaderTextSplitter

text = """
### O que é Inteligência Artificial  
A inteligência artificial (IA) é um ramo da tecnologia que busca criar sistemas capazes de simular a inteligência humana. Por meio de algoritmos e modelos avançados, a IA consegue aprender com dados, identificar padrões e tomar decisões, muitas vezes superando a capacidade humana em velocidade e precisão. Esse campo tem sido a base de inovações que já estão presentes no dia a dia de milhões de pessoas.  

### Avanços e Aplicações  
Nos últimos anos, a IA evoluiu de forma acelerada, impulsionada pelo poder computacional e pela abundância de informações digitais. Hoje, ela está presente em assistentes virtuais, sistemas de recomendação em plataformas de streaming e até mesmo em diagnósticos médicos auxiliados por algoritmos. No ambiente empresarial, a IA tem sido aplicada para otimizar processos, reduzir custos e aumentar a eficiência em diferentes setores.  

### Desafios e Futuro  
Apesar do seu enorme potencial, a IA também traz desafios que precisam ser enfrentados, como a preservação da privacidade, a transparência dos algoritmos e o impacto sobre empregos tradicionais. É essencial estabelecer um uso ético e responsável dessa tecnologia, garantindo que seus benefícios sejam distribuídos de forma justa. O futuro da IA dependerá da capacidade da sociedade em equilibrar inovação com responsabilidade social.  
"""

original_text = Document(page_content=text)

# print(original_text.page_content)

docs = [original_text]

# print(docs)

text_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=[
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]
)

spliched_docs = text_splitter.split_text(text)

i = 0
for doc in spliched_docs:
    print("--" * 20)
    print(f"chunk: {i}")
    print("--" * 20)
    print(doc.page_content)
    print("--" * 20)
    i += 1
