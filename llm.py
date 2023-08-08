# Server class for the project

# from langchain.llms import OpenLLM

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
                                                  namespace="Proposal-investors")
        print(self.index)

    # @staticmethod
    def get_similiar_docs(self, query, k=2, score=False):
        if score:
            similar_docs = self.index.similarity_search_with_score(query, k=k)
        else:
            similar_docs = self.index.similarity_search(query, k=k)
        return similar_docs

    def get_answer(self, query):
        similar_docs = self.get_similiar_docs(query)
        prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(
               """"
               """
            ),
            MessagesPlaceholder(variable_name="history"),
            HumanMessagePromptTemplate.from_template("{similar_docs} + {query}")
        ])
        llm = ChatOpenAI(temperature=0)
        memory = ConversationBufferMemory(return_messages=True)
        conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)
        return conversation.predict(query)
        