import sqlite3
import os
from pathlib import Path

def initialize_database_from_root(db_name="databank.db", folder_name="data"):
    """
    Initializes an SQLite database file using a path relative to the 
    directory where this Python script is located (i.e., the project root).
    """
    project_root = Path(__file__).resolve().parent.resolve().parent
    data_folder_path = project_root / folder_name
    db_path = data_folder_path / db_name
    print(data_folder_path)
    data_folder_path.mkdir(exist_ok=True)
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            create_table_sql = """
            CREATE TABLE IF NOT EXISTS table1 (
                website_name TEXT,
                words TEXT,
                sentiment_p_n INTEGER,
                sentiment_value INTEGER
            );
            """
            cursor.execute(create_table_sql)
            conn.commit()
        print(f"✅ Successfully initialized database at: {db_path}")
        print("✅ Table 'table1' created with the specified schema.")
    except sqlite3.Error as e:
        print(f"❌ An error occurred during database initialization: {e}")
    except NameError:
        print("❌ Error: __file__ is not defined. You may be running this code in an interactive environment (like an IDE console or Jupyter Notebook). This method only works when run as a script.")
initialize_database_from_root()
def putdata_to_databank()