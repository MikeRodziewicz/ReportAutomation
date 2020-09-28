import os
import pandas as pd
from datetime import date, timedelta
from openpyxl import load_workbook
import shutil


def search_string():
    wb = load_workbook(f"{location}/data.xlsx")
    ws_inc = wb['INC']
    ws_wo = wb['WO']
    with open(f"{dst}/INC.txt", 'w') as inc_txt:
        for row in ws_inc.rows:
            for cell in row:
                inc_txt.write(f"""'Service Request ID' = "{cell.value}" OR """)

        inc_txt.seek(0, 2)
        inc_txt.seek(inc_txt.tell() - 3, 0)
        inc_txt.truncate()

    with open(f"{dst}/WO.txt", 'w') as wo_txt:
        for row in ws_wo.rows:
            for cell in row:
                wo_txt.write(f"""'Associated Request ID' = "{cell.value}" OR """)

        wo_txt.seek(0, 2)
        wo_txt.seek(wo_txt.tell() - 3, 0)
        wo_txt.truncate()
