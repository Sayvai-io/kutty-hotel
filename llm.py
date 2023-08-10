# Server class for the project

# from langchain.llms import OpenLLM
import os
import openai
import os
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
from langchain.vectorstores import Pinecone
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory



with open("openai_api_key.txt", "r") as f:
    api_key = f.read()

os.environ["OPENAI_API_KEY"] = api_key


class Server:
    "server class for the project"
    defalut_params = {
        "pine-cone_key": "da26b242-4825-43e9-b5dd-6a94047d2860",
        "pine-cone_env": "northamerica-northeast1-gcp",
        "index_name": "index-1"
    }

    def __init__(self):
        self.model_name: str = "gpt-3.5-turbo"
        self.model_id: str = "google/flan-t5-large"
        self.temperature: float = 0.94
        self.repetition_penalty: float = 1.2
        self.directory: str = "docs/"
        self.docs = None
        self.index = None
        self.chain = None
        self.chunk_size: int = 1000
        self.chunk_overlap: int = 100
        self.memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

    # @staticmethod
    def load_docs(self):
        loader = DirectoryLoader(self.directory)
        self.docs = loader.load()

    # @staticmethod
    def split_docs(self):
        self.load_docs()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        self.docs = text_splitter.split_documents(self.docs)

    # @staticmethod
    def load_pinecone(self):
        pinecone.init(
            api_key=self.defalut_params["pine-cone_key"],  # find at app.pinecone.io
            environment=self.defalut_params["pine-cone_env"]  # next to api key in console
        )
        #   self.split_docs()
        embeddings = OpenAIEmbeddings()
        self.index = Pinecone.from_existing_index(self.defalut_params["index_name"], embeddings,
                                                  namespace="pearl-hotel")
        print(self.index)

    # @staticmethod
    def get_similiar_docs(self, query, k=2, score=False):
        try:
            if len(query)!=0:
                if score:
                    similar_docs = self.index.similarity_search_with_score(query, k=k)
                else:
                    similar_docs = self.index.similarity_search(query, k=k)
                return similar_docs
        except  ValueError:
            return None
        
            

    def get_answer(self, query):
        similar_docs = self.get_similiar_docs(query)
        prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(
               """"
               You are talking to kutty. You are a hotel bot. 
               ###Instruction###
               You should provide information only about food. You should always be polite. If you don't know the answer,don't try to make up an answer.
               Answer that you'll ask the chef and get back.

               ###Menu###
                Appetizers:

                    Spring Rolls - ₹400
                    Dumplings Sampler - ₹550
                    Hot and Sour Soup - ₹350
                    Crispy Wontons - ₹300
                    Scallion Pancakes - ₹250
                    Sesame Cold Noodles - ₹400
                    Salt and Pepper Calamari - ₹600
                    Crab Rangoon - ₹450

                    Soups:

                    Wonton Soup - ₹450
                    Egg Drop Soup - ₹300
                    Hot and Sour Soup - ₹350
                    Miso Soup - ₹250
                    Corn and Crab Soup - ₹400
                    Lemon Coriander Soup - ₹300
                    Seafood Tom Yum Soup - ₹500
                    Vegetable Tofu Noodle Soup - ₹350
                    Chinese Herbal Chicken Soup - ₹450

                    Main Courses:

                    General Tso's Chicken - ₹800
                    Kung Pao Shrimp - ₹950
                    Beef with Broccoli - ₹850
                    Mapo Tofu - ₹600
                    Sweet and Sour Pork - ₹700
                    Vegetable Chow Mein - ₹550
                    Cashew Chicken - ₹750
                    Black Bean Sauce Tofu - ₹550
                    Orange Glazed Beef - ₹900
                    Sesame Tofu Stir-Fry - ₹600
                    Spicy Garlic Eggplant - ₹650
                    Honey Walnut Shrimp - ₹850

                    Specialties:

                    Peking Duck (Half) - ₹2000
                    Peking Duck (Full) - ₹3500
                    Mongolian Beef - ₹1200
                    Szechuan Eggplant - ₹600
                    Crispy Honey Chicken - ₹850
                    Cantonese Steamed Fish - ₹1100
                    Five Spice Spare Ribs - ₹950
                    Dragon and Phoenix - ₹1200
                    Lotus Leaf Rice - ₹800
                    Crispy Sesame Tofu - ₹750
                    Tea-Smoked Duck - ₹1400
                    Stir-Fried Clams with Black Bean Sauce - ₹1100

                    Side Dishes:

                    Steamed Jasmine Rice - ₹50
                    Vegetable Fried Rice - ₹300
                    Egg Fried Rice - ₹250
                    Stir-Fried Noodles - ₹350
                    Garlic Bok Choy - ₹200
                    Szechuan Cucumber Salad - ₹250
                    Hot and Spicy Tofu - ₹300
                    Sesame Green Beans - ₹250
                    Scallion Pancakes - ₹250
                    Crispy Wonton Strips - ₹150

                    Drinks:

                    Jasmine Green Tea - ₹150
                    Lychee Cooler - ₹200
                    Fortune Iced Tea - ₹150
                    Ginger Honey Lemonade - ₹180
                    Chinese Herbal Tea - ₹180
                    Coconut Water - ₹120
                    Mango Lassi - ₹220
                    Chinese Plum Juice - ₹170
                    Green Apple Sparkler - ₹190
                    Hot Ginger Tea - ₹160

                    Desserts:

                    Fortune Cookies (Complimentary)
                    Mango Sticky Rice - ₹300
                    Red Bean Paste Pancakes - ₹250
                    Sesame Balls - ₹200
                    Almond Tofu Pudding - ₹220
                    Fried Ice Cream - ₹280
                    Coconut Jelly - ₹180
                    Osmanthus Jelly - ₹200
                    Black Sesame Soup - ₹250
                    Fruit Platter - ₹350
               """
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{input}")
        ])
        llm = ChatOpenAI(temperature=0)
        conversation = ConversationChain(memory=self.memory, prompt=prompt, llm=llm)
        return conversation.predict(input = str(similar_docs) +" "+ query)


        
