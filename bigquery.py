from google.cloud import bigquery
from google.oauth2 import service_account
from conf import service_account_file

bq_client = bigquery.client.Client(
    project='project_name',
    credentials=service_account.Credentials.from_service_account_file(
        service_account_file))

def exampleQuery():
    query = """
    SELECT * FROM `project_name.dataset_name.table_name`
    """

    result = bq_client.query(query).to_dataframe()
    return result