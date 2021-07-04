import openpyxl

def get_value_excel(filename, cellname):
    wb = openpyxl.load_workbook(filename)
    Sheet1 = wb['Sheet1']
    wb.close()
    return Sheet1[cellname].value
    
def update_value_excel(filename, cellname, value):
    wb = openpyxl.load_workbook(filename)
    Sheet1 = wb['Sheet1']
    Sheet1[cellname].value = value
    wb.close()
    wb.save(filename)

''' demo 1
filename = 'file.xlsx'
cellname = 'C1'
x = get_value_excel(filename, cellname)
print('x=', x)
'''

''' demo 2
filename = 'file.xlsx'
cellname = 'C1'
value = '0879545777'
update_value_excel(filename, cellname, value)
'''

col_acc = 'A'
col_pass = 'B'
filename = 'file.xlsx'
for i in range(3,18):
    cell_name = '%s%s'%(col_acc,i)
    cell_pass = '%s%s'%(col_pass,i)
    #print(cell_name,cell_pass)
    #input('aaaaa')
    account = get_value_excel(filename, cell_name)
    password = get_value_excel(filename, cell_pass)
    print('account',account)
    print('password',password)
    input('kết quả:')