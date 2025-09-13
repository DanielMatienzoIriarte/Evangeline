import pandas as pd
from prophet_model import ProphetModel
from view import ProphetView


class ProphetController:
    def __init__(self):
        self.model = None
        self.view = None

    def load_data_and_predict(self, file_path):
        """
        Loads data, runs the forecast, and tells the view to update.
        """
        try:
            df = pd.read_csv(file_path, parse_dates=['ds'])
            self.model = ProphetModel(df)
            self.model.perform_forecast()

            # Get the Matplotlib Figure from the model
            fig = self.model.get_forecast_figure()

            if fig and self.view:
                self.view.show_plot(fig)

        except Exception as e:
            print(f"Error during forecasting: {e}")

    def set_view(self, view):
        self.view = view