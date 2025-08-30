from ftplib import FTP

ftp_host = "ftp.dlptest.com"
ftp_user = "dlpuser"
ftp_pass = "rNrKYTX9g7z3RgJRmxWuGHbeu"

try:
    with FTP(ftp_host, ftp_user, ftp_pass) as ftp:
        print(f"Connected to {ftp_host}")

        filename_to_upload = "upload_test.txt"
        with open(filename_to_upload, "w") as f:
            f.write("This is a test file for FTP.")
        
        with open(filename_to_upload, "rb") as f:
            ftp.storbinary(f"STOR {filename_to_upload}", f)
        print(f"\nUploaded '{filename_to_upload}'.")

        print("\nListing directory contents:")
        ftp.dir()

        filename_to_download = "downloaded_test.txt"
        with open(filename_to_download, "wb") as f:
            ftp.retrbinary(f"RETR {filename_to_upload}", f.write)
        print(f"\nDownloaded file as '{filename_to_download}'.")

except Exception as e:
    print(f"FTP operation failed: {e}")
