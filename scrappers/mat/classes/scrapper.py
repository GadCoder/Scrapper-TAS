import os
import requests

from dotenv import load_dotenv

from scrappers.mat.classes.auth_handler import AuthHandler


load_dotenv()

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DNI = os.getenv("DNI")

TOKEN = "eyJhbGciOiJIUzUxMiJ9.eyJhdXRob3JpdGllcyI6Ilt7XCJhY2Npb25lc0FzaWduYWRhc1wiOlwiMTAxXCIsXCJhdXRob3JpdHlcIjpcIkNPTl9DQU1CSUFSX0xPQ0FMXCJ9LHtcImFjY2lvbmVzQXNpZ25hZGFzXCI6XCIyMDFcIixcImF1dGhvcml0eVwiOlwiQ09OX01VTFRJX1RBQkxBXCJ9LHtcImFjY2lvbmVzQXNpZ25hZGFzXCI6XCIxMDEsMTAyLDEwNCwxMDUsMTA2XCIsXCJhdXRob3JpdHlcIjpcIkNPTl9QRVJTT05BXCJ9LHtcImFjY2lvbmVzQXNpZ25hZGFzXCI6XCIxMDFcIixcImF1dGhvcml0eVwiOlwiQ09OX1BFUlNPTkFTXCJ9LHtcImFjY2lvbmVzQXNpZ25hZGFzXCI6XCIxMDFcIixcImF1dGhvcml0eVwiOlwiQ09OX1NFR1VJTUlFTlRPX05PVElGSUNBQ0lPTlwifSx7XCJhY2Npb25lc0FzaWduYWRhc1wiOlwiMTAxLDEwMiwxMDMsMzAxXCIsXCJhdXRob3JpdHlcIjpcIkNPTl9TRUdVSU1JRU5UT19UUkFNSVRFXCJ9LHtcImFjY2lvbmVzQXNpZ25hZGFzXCI6XCIyMDFcIixcImF1dGhvcml0eVwiOlwiQ09OX1RSQU1JVEVTXCJ9LHtcImFjY2lvbmVzQXNpZ25hZGFzXCI6XCIyMDFcIixcImF1dGhvcml0eVwiOlwiQ09OX1RSQU1JVEVTX1NFR1VJTUlFTlRPXCJ9LHtcImFjY2lvbmVzQXNpZ25hZGFzXCI6XCIyMDFcIixcImF1dGhvcml0eVwiOlwiQ09OX1RSQU1JVEVTX1NFR1VJTUlFTlRPX1ZFUklGSUNBXCJ9LHtcImFjY2lvbmVzQXNpZ25hZGFzXCI6XCIxMDNcIixcImF1dGhvcml0eVwiOlwiTUFOX0NST05PR1JBTUFfVklHRU5URVwifSx7XCJhY2Npb25lc0FzaWduYWRhc1wiOlwiMTAyLDEwNSwxMDZcIixcImF1dGhvcml0eVwiOlwiTUFOX0VTQ0VOQVJJT19SRVFVSVNJVE9fVk9VQ0hFUlwifSx7XCJhY2Npb25lc0FzaWduYWRhc1wiOlwiMTAzXCIsXCJhdXRob3JpdHlcIjpcIk1BTl9HRU5FUkFSX0RPQ1VNRU5UT1wifSx7XCJhY2Npb25lc0FzaWduYWRhc1wiOlwiMTAzXCIsXCJhdXRob3JpdHlcIjpcIk1BTl9HRU5FUkFSX0RPQ19MT0NBTFwifSx7XCJhY2Npb25lc0FzaWduYWRhc1wiOlwiMTA0XCIsXCJhdXRob3JpdHlcIjpcIk1BTl9HRU5FUkFSX0RPQ19WQVJcIn0se1wiYWNjaW9uZXNBc2lnbmFkYXNcIjpcIjEwMSwxMDIsMTAzXCIsXCJhdXRob3JpdHlcIjpcIk1BTl9MT0NBTFwifSx7XCJhY2Npb25lc0FzaWduYWRhc1wiOlwiMTAxLDEwMiwxMDMsMTA0LDIwMSwzMDEsNDAxXCIsXCJhdXRob3JpdHlcIjpcIk1BTl9MT0dfTk9USUZJQ0FDSU9OXCJ9LHtcImFjY2lvbmVzQXNpZ25hZGFzXCI6XCIxMDJcIixcImF1dGhvcml0eVwiOlwiTUFOX01VTFRJVEFCX0RFVFwifSx7XCJhY2Npb25lc0FzaWduYWRhc1wiOlwiMzAxXCIsXCJhdXRob3JpdHlcIjpcIk1BTl9QRVJTT05BX0lOVEVSTk9cIn0se1wiYWNjaW9uZXNBc2lnbmFkYXNcIjpcIjEwNFwiLFwiYXV0aG9yaXR5XCI6XCJNQU5fUkVRVUlTSVRPXCJ9LHtcImFjY2lvbmVzQXNpZ25hZGFzXCI6XCIxMDIsMzAyXCIsXCJhdXRob3JpdHlcIjpcIk1BTl9TT0xJQ0lUVURfVFJBTUlURV9SRVFVSVNJVE9cIn0se1wiYWNjaW9uZXNBc2lnbmFkYXNcIjpcIjIwMFwiLFwiYXV0aG9yaXR5XCI6XCJNQU5fVElQT1NfVFJBTUlURVwifSx7XCJhY2Npb25lc0FzaWduYWRhc1wiOlwiMTA0LDEwNSwxMDhcIixcImF1dGhvcml0eVwiOlwiTUFOX1RJUE9fVFJBTUlURVwifSx7XCJhY2Npb25lc0FzaWduYWRhc1wiOlwiMTA0LDEwNVwiLFwiYXV0aG9yaXR5XCI6XCJNQU5fVElQT19UUkFNSVRFX0xPQ0FMXCJ9LHtcImFjY2lvbmVzQXNpZ25hZGFzXCI6XCIxMDEsMTAyXCIsXCJhdXRob3JpdHlcIjpcIlBST19BTkVYT1wifSx7XCJhY2Npb25lc0FzaWduYWRhc1wiOlwiMTAxXCIsXCJhdXRob3JpdHlcIjpcIlBST19FWFBFRElFTlRFXCJ9LHtcImFjY2lvbmVzQXNpZ25hZGFzXCI6XCIxMDEsMTAzXCIsXCJhdXRob3JpdHlcIjpcIlBST19HRU5fRE9DVU1FTlRPXCJ9LHtcImFjY2lvbmVzQXNpZ25hZGFzXCI6XCIzMDEsMzAyXCIsXCJhdXRob3JpdHlcIjpcIlBST19QRVJTT05BX1JFR0lTVFJPXCJ9LHtcImFjY2lvbmVzQXNpZ25hZGFzXCI6XCIxMDFcIixcImF1dGhvcml0eVwiOlwiUFJPX1JFR19TT0xJQ0lUVURfVFJBTUlURVwifSx7XCJhY2Npb25lc0FzaWduYWRhc1wiOlwiMTAzLDEwOSwxMTAsMTExLDExNSwxMTYsMTE5LDEyMCwxMjEsMTIyLDEyMyw1MDEsNTAyLDUwNCw1MDVcIixcImF1dGhvcml0eVwiOlwiUFJPX1NPTElDSVRVRF9UUkFNSVRFXCJ9LHtcImFjY2lvbmVzQXNpZ25hZGFzXCI6XCIxMDEsMTAzLDEwNFwiLFwiYXV0aG9yaXR5XCI6XCJQUk9fVFJBTUlURVwifSx7XCJhY2Npb25lc0FzaWduYWRhc1wiOlwiMTAwXCIsXCJhdXRob3JpdHlcIjpcIlVJX0RFVEFMTEVTX1NPTElDSVRVRFwifSx7XCJhY2Npb25lc0FzaWduYWRhc1wiOlwiMTAwXCIsXCJhdXRob3JpdHlcIjpcIlVJX0hJU1RPUklBTF9OT1RJRklDQUNJT05cIn0se1wiYWNjaW9uZXNBc2lnbmFkYXNcIjpcIjEwMCwyMDAsMjAxLDIwMiwzMDAsNDAwXCIsXCJhdXRob3JpdHlcIjpcIlVJX01JU19UUkFNSVRFU1wifSx7XCJhY2Npb25lc0FzaWduYWRhc1wiOlwiMTAwLDIwMCwyMDEsMjAyLDMwMCw0MDBcIixcImF1dGhvcml0eVwiOlwiVUlfUEVSRklMXCJ9LHtcImFjY2lvbmVzQXNpZ25hZGFzXCI6XCIxMDBcIixcImF1dGhvcml0eVwiOlwiVUlfUkVBTElaQVJfU09MSUNJVFVERVNcIn0se1wiYWNjaW9uZXNBc2lnbmFkYXNcIjpcIjEwMCwyMDAsMjAxLDIwMiwzMDAsNDAwXCIsXCJhdXRob3JpdHlcIjpcIlVJX1RSQU1JVEVcIn0se1wiYWNjaW9uZXNBc2lnbmFkYXNcIjpcIjEwMCwyMDAsMjAxLDIwMiwzMDAsNDAwXCIsXCJhdXRob3JpdHlcIjpcIlVJX1RSQU1JVEVTX0VOX0xJTkVBXCJ9XSIsInBmbCI6W3siaWRTaXN0ZW1hIjoiMSIsInNpZ2xhU2lzdGVtYSI6Ik1BVCIsImlkUGVyZmlsIjoxLCJub21icmVQZXJmaWwiOiJFc3R1ZGlhbnRlIC0gRG9jZW50ZXMifV0sImNkZyI6IjIwMjAwMDkzIiwibHNjZGciOiIyMDIwMDA5MywiLCJzdWIiOiJnZXJtYW4uYW1wdWVybyIsImp0aSI6Ijc3NTA1MzU2IiwiaWF0IjoxNzMzNTE4NDkxLCJleHAiOjE3MzM1Mjg0OTF9.Mj6kQeVSpdiuVuDVr9PJjo0GfnpApLI8_KdeIJbdbNTLVuOfBuV4yOr0t7myjppLFPVZFuh3KZRHwTC57lz6eQ"


class Scrapper:
    def __init__(self):
        self.auth_token: str = None
        self.auth_handler: AuthHandler = AuthHandler()
        self.results: list = []

        # self.get_auth_token()

    def get_auth_token(self):
        print("Getting token")
        self.auth_token = self.auth_handler.get_auth_token(user=USER, password=PASSWORD)

    def get_results(self):
        url = f"https://servicioonline.unmsm.edu.pe/sgdfd/mat/backend/tipos-tramite/local/20/numero-documento/{DNI}"
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Referer": "https://tramiteonline.unmsm.edu.pe/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Authorization": "Bearer " + TOKEN,
        }
        request = requests.get(url, headers=headers)
        if request.status_code != 200:
            print("ERROR getting results")
            return
        for result in request.json():
            name = result["nombre"]
            description = result["descripcion"]
            url = f"https://tramiteonline.unmsm.edu.pe/sgdfd/mat/tipo-tramite/{result['nombreUrl']}/?local=20"
            status = result["nombreEstado"]
            print(f"Saving: {name}")
            self.results.append(
                {"name": name, "description": description, "url": url, "status": status}
            )
