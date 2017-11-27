 Python program to display 
# the examination schedule.
# (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

a=exam_st_date[0]
b=exam_st_date[1]
c=exam_st_date[2]

a= str(a)
b= str(b)
c= str(c)

date = a + ' / '+ b+ ' / '+c
print(date)

