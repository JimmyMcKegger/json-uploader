import requests
import json
from typing import Any


def stagedUploadsCreate(url: str, headers: dict, input: Any) -> dict:
    """Create staged uploads on the shop.

    :param url: The URL where the request is sent.
    :param headers: The headers used for authentication.
    :param input: The body of the request.
    :return: The response from the server as a dictionary.
    """

    query = """
    mutation stagedUploadsCreate($input: [StagedUploadInput!]!) {
        stagedUploadsCreate(input: $input) {
            userErrors {
                field
                message
            }
            stagedTargets {
                url
                resourceUrl
                parameters {
                    name
                    value
                }
            }
        }
    }
    """

    variables = {"input": input}

    # Format the payload
    payload = {"query": query, "variables": variables}

    res = requests.post(url, headers=headers, data=json.dumps(payload))
    return res.json()


def multipart_form(targets: dict, file: str, path: str) -> dict:
    """
    Posts multipart form to upload the file.

    :param targets: The targets used for the multipart form.
    :param file: The file to be uploaded.
    :param path: The path of the file to be uploaded.
    :return: The status code from the server response.
    """
    url = targets["url"]

    payload = {
        "acl": targets["acl"],
        "success_action_status": targets["success_action_status"],
        "x-goog-algorithm": targets["x-goog-algorithm"],
        "x-goog-date": targets["x-goog-date"],
        "x-goog-credential": targets["x-goog-credential"],
        "policy": targets["policy"],
        "x-goog-signature": targets["x-goog-signature"],
        "key": targets["key"],
        "Content-Type": targets["Content-Type"],
    }
    with open(path, "rb") as f:
        myfile = {"file": (file, f, "application/json")}
        response = requests.request(
            "POST", url, data=payload, files=myfile, allow_redirects=False
        )

    return response


def fileCreate(url: str, headers: dict, input: dict) -> dict:
    """
    Creates a file in Shopify with the Admin API.

    :param url: The URL where the request is sent.
    :param headers: The headers used for authentication.
    :param input: The body of the request.
    :return: The response from the server as a dictionary.
    """

    query = """
    mutation fileCreate($files: [FileCreateInput!]!) {
        fileCreate(files: $files) {
            files {
                ... on GenericFile {
                    id
                    alt
                    url
                    createdAt
                    fileStatus
                    fileErrors {
                        code
                        details
                        message
                    }
                }
            }
            userErrors {
                field
                message
            }
        }
    }
    """
    variables = {"files": input}
    payload = {"query": query, "variables": variables}
    res = requests.post(url, headers=headers, json=payload)

    return res.json()
