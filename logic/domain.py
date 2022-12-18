from time import sleep
from logic.our_oscar import OscarManager
import logic.our_fitbit as our_fitbit
import scipy.io
import pandas as pd

class Domain:
    def __init__(self):
        self.om = OscarManager()

    def process_electro(self):
        # gets the name of the csv gotten, saves the csv to data/csv
        csv_file = our_fitbit.get_fitbit_csv();
        print(csv_file) #########

        # gets the name of the mat_file gotten after converting
        # the csv to mat and saves it to data/mat
        mat_file = self.convert_to_mat(csv_file)

        # uploads the mat_file from data/mat to the cluster
        # and runs the inference service
        self.om.upload_data_file(mat_file);
        sleep(15)

        # downloads the result of the inference
        # and saves it to data/log as CLIENT_ID + %Y%m%d%H%M%S format
        log_file = self.om.download_result_file(mat_file);

        # gets the result from the log file
        result = self.om.get_value("data/log/" + log_file)
        print("-------------------")
        print(result)
        print("-------------------")
        return result

    def convert_to_mat(self, csv_file):
        df = pd.read_csv("data/csv/" + csv_file)
        mat_file = csv_file.replace(".csv", ".mat")
        # convert data frame to dictionary
        data = df.to_dict()
        # save it to a file
        scipy.io.savemat("data/mat/" + mat_file, data)
        print("mat_file: " + mat_file)
        return mat_file

if __name__ == '__main__':
    dom = Domain()
    result = dom.process_electro();
    print(result)
    
