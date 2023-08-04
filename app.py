from helpers.config import get_api_settings, get_logger
from helpers.mutations import stagedUploadsCreate, multipart_form, fileCreate
import argparse

def main():
    logger = get_logger()

    parser = argparse.ArgumentParser(description='Uploads a file.')
    parser.add_argument('filename', type=str, help='The json file to upload')

    args = parser.parse_args()

    url, link, headers = get_api_settings()
    staging_variables = {
        "filename": args.filename,
        "httpMethod": "POST",
        "mimeType": "text/json",
        "resource": "FILE",
    }

    res = stagedUploadsCreate(url, headers, staging_variables)
    logger.info(res)
    data = res["data"]["stagedUploadsCreate"]["stagedTargets"][0]
    targets = {param["name"]: param["value"] for param in data["parameters"]}
    targets["url"] = data["url"]
    targets["resourceUrl"] = data["resourceUrl"]

    r = multipart_form(targets, args.filename, f"./{args.filename}")

    if r.status_code == 201:
        logger.info("Form submitted successfully")
    else:
        logger.warning("Form submission failed")

    creation_variables = {
        "alt": "final json",
        "contentType": staging_variables["resource"],
        "originalSource": targets["resourceUrl"],
    }

    final = fileCreate(url, headers, creation_variables)
    logger.info(final)
    logger.info(f"Visit {link}")

if __name__ == '__main__':
    main()
