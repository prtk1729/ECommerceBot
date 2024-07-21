from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from ecombot.ingest import ingest_data


def generation(vstore):
    retriever = vstore.as_retriever(search_kwargs={"k": 3})

    PRODUCT_BOT_TEMPLATE = """
    Your ecommercebot bot is an expert in product recommendations and customer queries.
    It analyzes product titles and reviews to provide accurate and helpful responses.
    Ensure your answers are relevant to the product context and refrain from off-topic responses.
    Your responses should be concise and informative. In case, user asks for generic queries 
    unrelated to the products, use your own knowledge to answer them.

    CONTEXT:
    {context}

    QUESTION: {question}

    YOUR ANSWER:
    
    """


    prompt = ChatPromptTemplate.from_template(PRODUCT_BOT_TEMPLATE)

    llm = ChatOpenAI()

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain

if __name__=='__main__':
    vstore = ingest_data("Already Ingested to VStore")
    chain  = generation(vstore)
    print(chain.invoke("Suggest me the best bluetooth earphone?"))
    # I would recommend the OnePlus Bullets Wireless Z Bass Edition Bluetooth Headset
    # as it is highly rated for its sound quality, comfort, durability, and battery life.
    
    
    