from FileManagement.file_management import Date_Stamps
import pandas as pd


class DataFrameProd():

    location = '/home/mike/github/ReportAutomation/Reports/DataImport'

    def df_creation(self):
        csv_item = pd.DataFrame(pd.read_csv(
            f'{self.location}/data.csv', header=0, skip_blank_lines=True))
        csv_item['Created'] = pd.to_datetime(csv_item['Created'].str[:11])
        return csv_item

    def stp_mapping(self):
        sip_writer = pd.read_excel(f'{self.location}/STP_MAP.xlsx')
        with_stp = pd.DataFrame(sip_writer[['Assignment Group', 'STP']])
        return with_stp


df1 = DataFrameProd().df_creation()
print(df1.columns)


class Daily_Report(Date_Stamps):

    def __init__(self, input, stp):
        super().__init__()
        self.input = input
        self.stp = stp

    def make_daily_base(self):
        daily_base = pd.DataFrame(
            self.input[['Ticket', 'Created', 'Score', 'Comment', 'Factor', 'Assignment Group']])
        data_frame = pd.merge(daily_base, self.stp, on='Assignment Group', how='left')
        return data_frame

    def make_daily_call(self, data_frame):
        daily_rpt = pd.DataFrame(
            data_frame[['Ticket', 'Created', 'Score', 'Comment', 'Factor', 'Assignment Group']])
        report = pd.merge(daily_rpt, self.stp, on='Assignment Group', how='left')
        filt = (report['Created'] >= str(self.count_in_weekend()))
        report = report.loc[filt]
        filt_2 = (report['Created'] < str(self.get_today()))
        report = report.loc[filt_2]
        return report

    def make_daily_dsr_one(self, data_frame):
        report = pd.DataFrame(data_frame[['Created', 'Score', 'STP']])
        filt = (report['Created'] >= str(self.count_in_weekend()))
        report = report.loc[filt]
        filt_2 = (report['Created'] < str(self.get_today()))
        report = report.loc[filt_2]
        report = pd.DataFrame(report[['Score', 'STP']])
        return report

    def make_daily_dsr_two(self, data_frame):
        report = pd.DataFrame(data_frame[['Created', 'Score', 'STP']])
        filt = (report['Created'] >= str(self.get_start_month()))
        report = report.loc[filt]
        filt_2 = (report['Created'] < str(self.get_today()))
        report = report.loc[filt_2]
        report = pd.DataFrame(report[['Score', 'STP']])
        return report
