from langchain_ollama import OllamaLLM
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
import time

# 1️⃣ Connect to MySQL database
db = SQLDatabase.from_uri("")

# 2️⃣ Load the Ollama LLM model
llm = OllamaLLM(model="tinyllama", temperature=0)


# 4️⃣ Create an AI Query Engine
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, return_direct=True)

# 5️⃣ Run a natural language query
start_time = time.time()
query = """
Return a JSON object with only the MySQL query to retrieve the first 3 customers from the `customers` table.

**Rules:**
1. The response must be **valid JSON**.
2. The JSON **must contain only one key: `sql_query`**.
3. The value of `sql_query` must be a **valid MySQL query**.
4. Do **not** include explanations, comments, or extra text.
5. The response must be **strictly machine-readable JSON**.

Example output:
{
    "sql_query": "SELECT * FROM customers LIMIT 3;"
}
"""

# Run the AI query
response = db_chain.run(query)




print("--- %s seconds ---" % (time.time() - start_time))