import pandas as pd
from langchain_core.documents import Document # AstraDB and langchain 
#require this format -> COnvert to this Document format


def create_documents(list_of_dicts):
    '''
        Returns a list of Document-objects
    '''
    ret = []
    for le in list_of_dicts:    
        metadata = {"product_name": le["product_name"]}
        page_content = le["review"]
        ret.append( Document( page_content=page_content, metadata=metadata ) )
    return ret


def data_converter():
    df = pd.read_csv("../data/flipkart_product_review.csv")
    # print( df.head() )
    data = df[ ["product_title", "review"] ]

    list_of_dict = []
    for index, row in data.iterrows():
        obj = {
                "product_name": row["product_title"],
                "review": row["review"] 
              }
        list_of_dict.append(obj)

    docs = create_documents(list_of_dict)
    return docs



if __name__ == "__main__":
    docs = data_converter()
    print( docs )
