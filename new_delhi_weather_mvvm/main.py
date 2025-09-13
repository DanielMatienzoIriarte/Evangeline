import sys
from PyQt6.QtWidgets import QApplication
from prophet_controller import ProphetController
from view import ProphetView
import pandas as pd
import os


def generate_sample_data(file_path='example_wp.csv'):
    """Generate sample time series data if it doesn't exist."""
    if not os.path.exists(file_path):
        df = pd.DataFrame({
            'ds': pd.to_datetime(pd.date_range(start='2020-01-01', periods=100, freq='D')),
            'y': [10 + i + (i % 7) * 2 + (i % 30) * 0.5 + (i % 365) * 0.1 for i in range(100)]
        })
        df.to_csv(file_path, index=False)
        print(f"Generated sample data at {file_path}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Generate data for the example
    # generate_sample_data()

    # Instantiate the controller and view
    controller = ProphetController()
    view = ProphetView(controller)

    # Connect the controller to the view
    controller.set_view(view)

    # Trigger the forecasting and plotting
    controller.load_data_and_predict('example_wp.csv')

    view.show()
    sys.exit(app.exec())