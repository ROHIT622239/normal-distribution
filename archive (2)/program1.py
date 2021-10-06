import csv
import statistics as st 
with open ('StudentsPerformance.csv',newline='')f:
    reader=csv.reader(f)
    filedata=list(reader)

    filedata.pop(0)
    newdata = []
    for i in range(len(filedata)):
        n = filedata[i][1]
    newdata.append(float(n))



mean = st.mean(newdata)
print(mean)


median = st.median(newdata)
print(median)



mode = st.mode(newdata)
print(mode)

sd=st.stded(newdata)
print (sd)