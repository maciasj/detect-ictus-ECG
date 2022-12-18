from oscar_python.client import Client

class OscarManager:
    def __init__(self):
        self.client = Client("oscar-cluster","https://competent-dirac0.im.grycap.net", "oscar", "oscar2022", True)

    def upload_data_file(self, path):
        try:
            storage_service = self.client.create_storage_client("dislib-rf")
            storage_service.upload_file("minio.default", "data/mat/" + path, "dislib-rf/in")
        except Exception as err:
             print("Failed with: ", err)

    def download_result_file(self, path):
        download_path = str(path).split(".")[0] + "-output.log"
        try:
            storage_service = self.client.create_storage_client("dislib-rf")
            storage_service.download_file("minio.default", "data/log", "dislib-rf/out/" + download_path)
        except Exception as err:
             print("Failed with: ", err)
        return download_path


    def get_value(self,log_name):
        with open(log_name, 'r') as f:
            lines= f.readlines()
            value = lines[-5]
            return value
