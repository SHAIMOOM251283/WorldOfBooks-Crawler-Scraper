import os
import pandas as pd
import plotly.graph_objects as go

class DataVisualization:

    def __init__(self):
        self.folder_path = r"replace_with_file_path\data"
        self.file_names = []
        self.item_counts = []

    def process_files(self):
        for file in os.listdir(self.folder_path):
            if file.endswith(".csv"):
                # Append file name without extension
                self.file_names.append(os.path.splitext(file)[0])
        
                # Read CSV file and count the number of rows (items)
                file_path = os.path.join(self.folder_path, file)
                df = pd.read_csv(file_path)
                self.item_counts.append(len(df))

    def calculate_total_items(self):
        self.total_items = sum(self.item_counts)

    def create_bar_chart(self):
        fig = go.Figure([go.Bar(x=self.file_names, y=self.item_counts)])

        # Add title and labels
        fig.update_layout(
            title=f"Number of Items in Each Category (Total Items: {self.total_items})",
            xaxis_title="Categories",
            yaxis_title="Number of Items",
        )

        # Display the total number of items as annotation
        fig.add_annotation(
            xref="paper", yref="paper",
            x=0.5, y=-0.2,
            font=dict(size=14)
        )

        # Show the plot
        fig.show()

    def run(self):
        self.process_files()
        self.calculate_total_items()
        self.create_bar_chart()

if __name__ == '__main__':
    visualize = DataVisualization()
    visualize.run()