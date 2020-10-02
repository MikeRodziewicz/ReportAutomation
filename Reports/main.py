import os
from FileManagement.file_management import (
    current_date, main_folder_creation, folder_creation, copy_template, dst, templates_repo)
# from DataManipulation.data_manipulation import DataFrameProd, Daily_Report

#
# def main():
main_folder_creation()
folder_creation(dst)
copy_template(templates_repo, dst)
#     df1 = DataFrameProd().df_creation()
#     stps = DataFrameProd().stp_mapping()
#     base = Daily_Report(df1, stps).make_daily_base()
#     write_daily_report(Daily_Report(df1, stps).make_daily_call(base))
#     write_daily_report_maker(Daily_Report(df1, stps).make_daily_dsr_one(
#         base), Daily_Report(df1, stps).make_daily_dsr_two(base))
#
#
# if __name__ == '__main__':
#     main()
