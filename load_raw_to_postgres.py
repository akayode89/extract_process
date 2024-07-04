def load_postgres(src_path,password,host,database):
    import pandas as pd
    import re
    import os
    from sqlalchemy import create_engine


    os.chdir(src_path)

    files = os.listdir()

    engine = create_engine(f"postgresql+psycopg2://postgres:{password}@localhost:{host}/{database}")

    for file in files:
        try:
            df = pd.read_csv(file)
            df.to_sql(f"{file[:-4]}", \
                engine, \
                schema = 'raw', \
                if_exists = 'replace', \
                index = False)
            print(f'Load process successful for {file}')
        except:
            print(f'Load process failed for {file}')

if __name__ == "__main__":
    # Example usage
    src_path = 'C:\\Users\\ajkay\\OneDrive\\Desktop\\Data\\tgt'
    password = 'password1234'
    host = '5433'
    database = 'formular1'

    load_postgres(src_path,password,host,database)