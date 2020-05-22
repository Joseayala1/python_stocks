import csv
with open('myData.csv','w') as f:
    # stocks=['Creal','Cuervo','Cultiba','Cydsasa']
    nombre="nombre_empresa.csv"
    y=open(nombre,"r")
    reader=csv.reader(y)
    lista=[]
    for data in reader:
        lista.append(data[0])
    y.close() 
    for stk in lista:
        myfile=open("Datos históricos "+stk+".csv","r")
        reader1= csv.reader(myfile)
        headers=next(reader1,None)   
        # print(headers)
        count=0
        for x in reader1:
            # fecha, cierrre, apertura, volumen
            f.write(stk+","+x[0]+","+x[1]+","+x[2]+","+x[5]+"\n")
            count=count+1
        print (count)
        myfile.close()
f.close()
