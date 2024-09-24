import requests


def fileUrlQuery(url: str, headers: dict, file_id: str) -> str:
    """
    Queries a file in Shopify with the Admin API returns it's CDN url

    :param url: The URL where the request is sent.
    :param headers: The headers used for authentication.
    :param query: The query to be sent.
    :return: The response from the server as a dictionary.
    """
    query = """
        query fileQuery($file: ID!) {
            node(id: $file){
                    id
                    ...on GenericFile{
                    alt
                    createdAt
                    updatedAt
                    mimeType
                    originalFileSize
                    fileStatus
                    fileErrors{
                        message
                    }
                    url
                    }
                }
            }
    """
    variables = {"file": file_id}
    payload = {"query": query, "variables": variables}
    res = requests.post(url, headers=headers, json=payload)
    print(res.json())
    res_url = res.json()["data"]["node"]["url"]
    print(res_url)

    return res_url
