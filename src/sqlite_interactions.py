import sqlite3
import os
from pathlib import Path
import pandas as pd
def initialize_database_from_root(db_name="databank.db", folder_name="data"):
    """
    Initializes an SQLite database file using a path relative to the 
    directory where this Python script is located (i.e., the project root).
    """
    project_root = Path(__file__).resolve().parent.resolve().parent
    data_folder_path = project_root / folder_name
    db_path = data_folder_path / db_name
    # print(data_folder_path)
    data_folder_path.mkdir(exist_ok=True)
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            create_table_sql = """
            CREATE TABLE IF NOT EXISTS table1 (
                website_name TEXT,
                words TEXT,
                sentiment_p_n TEXT,
                sentiment_value INTEGER
            );
            """
            cursor.execute(create_table_sql)
            conn.commit()
        # print(f" Successfully initialized database at: {db_path}")
        # print(" Table 'table1' created with the specified schema.")
    except sqlite3.Error as e:
        print(f"didnt work{e}")
initialize_database_from_root()

def putdata_to_databank(websitename,word_array,sentiment_p_n,sentiment_value):
    """
    websitename = string, other are arrays"""
    data_length=len(word_array)
    df1={
        "website_name":[websitename for _ in range(data_length)],
        "words":word_array,
        "sentiment_p_n":sentiment_p_n,
        "sentiment_value":sentiment_value
    }
    df=pd.DataFrame(df1)
    print(df)
    project_root = Path(__file__).resolve().parent.resolve().parent
    data_folder_path = project_root / "data"
    db_path = data_folder_path / "databank.db"
    conn = sqlite3.connect(db_path)
    try:
        df.to_sql("table1", conn, if_exists='append', index=False)
        print(f"pushed rows to table1 sucessfully")
    except Exception as e:
        print(f"did not push")
    finally:
        conn.close()

def retrieve_data_by_website(websitename):
    project_root = Path(__file__).resolve().parent.resolve().parent
    data_folder_path = project_root / "data"
    db_path = data_folder_path / "databank.db"
    conn = sqlite3.connect(db_path)
    sql_query = f"""
        SELECT * FROM table1 WHERE website_name = '{websitename}'
        """
    df_retrieved = pd.read_sql(
            sql_query, 
            conn
        )
    print(df_retrieved)

     
