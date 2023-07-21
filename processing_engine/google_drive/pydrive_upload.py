import pydrive

def get_google_drive_zip_file_url(subdirectory, zip_file_name):
    """Gets the URL for a zip file in a subdirectory on Google Drive.

    Args:
        subdirectory (str): The name of the subdirectory.
        zip_file_name (str): The name of the zip file.

    Returns:
        str: The URL for the zip file.
    """

    drive = pydrive.auth.GoogleDrive()
    with drive.auth.authorize():
        file_id = "1_{}".format(zip_file_name)
        file = drive.CreateFile({"id": file_id})
        return file.alternate_link

def main():
    """Gets the URL for a zip file in a subdirectory on Google Drive and puts that URL in the prompt "Run OCR on each file in the zip file at '{Google Drive zip file url}'".
    """

    subdirectory = "my_subdirectory"
    zip_file_name = "my_zip_file.zip"
    url = get_google_drive_zip_file_url(subdirectory, zip_file_name)
    prompt = "Run OCR on each file in the zip file at '{}'".format(url)
    print(prompt)

if __name__ == "__main__":
    main()