import xlrd
import xlwt
print('xlwt',xlwt.__VERSION__)
def write_excel(data):
  wb = xlwt.Workbook(encoding='utf-8',style_compression=0)
  ws = wb.add_sheet('考勤统计',cell_overwrite_ok=True)

  for row,rowItem in enumerate(data):
    print(data)
    for col,colItem in enumerate(rowItem):
      ws.write(row, col, colItem)
  wb.save('result/result.xls')

def read_excel():
    # 打开文件
    workBook = xlrd.open_workbook('data/total.xls');

    # 1.获取sheet的名字
    # 1.1 获取所有sheet的名字(list类型)
    allSheetNames = workBook.sheet_names();

    # 1.2 按索引号获取sheet的名字（string类型）
    sheet1Name = workBook.sheet_names()[0];

    # 2. 获取sheet内容
    ## 2.1 法1：按索引号获取sheet内容
    sheet1_content1 = workBook.sheet_by_index(0); # sheet索引从0开始
    ## 2.2 法2：按sheet名字获取sheet内容
    sheet1_content2 = workBook.sheet_by_name('Sheet1');

    # 3. sheet的名称，行数，列数
    print('originData',sheet1_content1.ncols,sheet1_content1.nrows)
    result =[]
    row = 1
    while (row < sheet1_content1.nrows):
      count = 1
      user = []
      work=[]
      rest = []
      headStr = ''
      headStr = sheet1_content1.cell_value(row,0)
      while (count < sheet1_content1.ncols):
        timeArr = []
        timeArr.append(sheet1_content1.col_values(count,0,1)[0])
        timeArr.append(sheet1_content1.cell_value(row,count))
        # timeArr = sheet1_content1.col_values(count)
        if count% 2 == 0:
          time = timeArr[0].split('-')  
          work.append([int(time[0]),timeArr[1]])
        else:
          time = timeArr[0].split('-')  
          rest.append([int(time[0]),timeArr[1]])
        count = count+1
      useSleep =[]
      key = 0
      print(work,rest)
      for child in work:
        # print(key,useSleep,child,rest[key])
        resTime = rest[key][1]
        if len(useSleep) < 3:
          useSleep.append(child[1])
          start = 0
          while (resTime!=0):
            if useSleep[start] < resTime:
              resTime = resTime - useSleep[start]
              useSleep[start] = 0
            else:
              useSleep[start] = useSleep[start] - resTime
            start = start +1
            if start==len(useSleep):
              resTime = 0
        elif len(useSleep) >=3 :
          start = 0
          while (start != len(useSleep)):
            if useSleep[start] < resTime:
              resTime = resTime - useSleep[start]
              useSleep[start] = 0
            else:
              useSleep[start] = useSleep[start] - resTime
              resTime=0
            start = start +1
          useSleep = useSleep[1:]
          useSleep.append(child[1])
          if useSleep[2] < resTime:
            if key == len(rest) -1 :
              useSleep[2] = useSleep[2] - resTime
              resTime = 0
            else:
              resTime = resTime - useSleep[2]
              useSleep[2] = 0
          else:
            useSleep[2] = useSleep[2] - resTime
        key =key +1
      print(useSleep)
      useSleep.insert(0,headStr)
      result.append(useSleep)
      row  = row +1
    print(result)
    write_excel(result)



if __name__ == '__main__':
    read_excel();