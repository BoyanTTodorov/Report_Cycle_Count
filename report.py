import pandas as pd
import sqlite3
#ModuleNotFoundError: No module named 'matplotlib.backends.backend_pdf
import matplotlib.backends.backend_pdf
import matplotlib.pyplot as plt 

class Report:
    def __init__(self) -> None:
        self.path = r"S:\Warehouse dept\Inventory control\Reporting and dashboards\Cycle_Count\CycleCounting\DATABASE\cycle_couting.db"
        self.all_warehouses = {'MKI':[203552], 'JTS1':[135524], 'JTS2':[204451]}
        self.all_warehouses_counted = {}
        self.conn = sqlite3.connect(self.path)
        self.mki = pd.read_sql('SELECT * FROM MKI', self.conn)
        self.jts1 = pd.read_sql('SELECT * FROM JTS1', self.conn)
        self.jts2 = pd.read_sql('SELECT * FROM JTS2', self.conn)       

    def agregate_storage_type(self, df, size, my_title,location):
        result = pd.DataFrame()
        result['Total'] = df.Type.value_counts()
        result['Counted'] = df.groupby('Type')['Counted'].sum()
        result['NotCounted'] = result.Total - result.Counted
        plt.style.use("ggplot")
        ax = result.plot.bar( stacked=False, figsize=(size, 6), rot=0, xlabel='Type', ylabel='Counted', title = my_title)
        ax.set_yticks([])
        for c in ax.containers:
            labels = [v.get_height() if v.get_height() > 0 else '' for v in c]
            ax.bar_label(c, labels=labels, label_type='center')
        plt.savefig(location, format="pdf",bbox_inches="tight")
        plt.show()
