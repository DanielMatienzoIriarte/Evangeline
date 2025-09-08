import pandas as pd
from pandas import DataFrame


class NewDelhiWeather:

    def __init__(self):
        
        super().__init__()

        self.data = pd.read_csv("Resources/Data/DailyDelhiClimateTrain.csv")
        #self._format_data()

    """
    Formats CSV data by splitting date into date, month and year fields.
    
    Args:
    
    returns:
        DataFrame: the formated data
    """
    def _format_data(self) -> DataFrame:
        self.data["date"] = pd.to_datetime(self.data["date"], format = '%Y-%m-%d')
        self.data['year'] = self.data['date'].dt.year
        self.data["month"] = self.data["date"].dt.month
        print(self.data.head())

        return self.data

    """
    returns DataFrame: CSV data
    """
    def get_data(self) -> DataFrame:
        return self.data