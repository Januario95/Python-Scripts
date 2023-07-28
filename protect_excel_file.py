# pip install pywin32


from win32com.client.gencache import EnsureDispatch
    
app = EnsureDispatch("Excel.Application")
excel_file = app.Workbooks.Open('Book1.xlsx')
app.DisplayAlerts = False
excel_file.Visible = False
excel_file.SaveAs('Book1.xlsx', Password = 'Jaci1995')
excel_file.Close()
app.Quit()
    

