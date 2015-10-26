#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib
import csv
import numpy as np
def main():
    fig = plt.figure(1,figsize=(6.7,6.7))
    namesArray=["rsel.csv","cel-rs.csv","2cel-rs.csv","cel.csv","2cel.csv"]
    colorArray=["blue","green","red","black","pink"]
    markers=["o","v","D","s","d"]
    arrayX,arrayY,arrayX1,arrayY1,arrayX2,arrayY2,arrayX3,arrayY3,arrayX4,arrayY4,arr1,arr2,arr3,arr4,arr5=([] for i in range(15))
    arraysXY=[arrayX,arrayY,arrayX1,arrayY1,arrayX2,arrayY2,arrayX3,arrayY3,arrayX4,arrayY4]
    arrayBox=[arr1,arr2,arr3,arr4,arr5]
    i=0
    c=0
    d=0
    f, (ax1, ax2) = plt.subplots(1, 2,sharex=False,sharey=False)
    for nameFile in namesArray:
        with open(nameFile, 'rb') as f:
            reader = csv.reader(f)
            for column in reader:
                #ostatni wiersz dla boxplot
                if(str(column[0])=="199"):
                    for index,x in enumerate(column):

                        y=float(x)*100
                        if ((index!=0) and (index!=1)):
                            arrayBox[d].append(y)
                #wartości srednie dla zwyklego wykresu
                if((str(column[0])!="generation")and(str(column[0])!="199")and(str(column[0])!="198")and(str(column[0])!="197")and(str(column[0])!="196")):
                    sum=0

                    for x in column:
                        sum=sum+float(x)

                    sum=((sum-float(column[0])-float(column[1]))/32)*100
                    bla=int(column[1])/1000
                    arraysXY[i].append(bla)
                    arraysXY[i+1].append(sum)

        #wykres z 5 podwykresami dla kazdego pliku
        ax1.plot(arraysXY[i],arraysXY[i+1],markers[c],ls='-',ms=5,markevery=50,alpha=0.8,label=nameFile,color=colorArray[c])
        ax1.legend(loc='lower right', fontsize="small",fancybox="True",framealpha=0.5)
        ax1.grid(linewidth=0.1)
        ax1.set_xlabel("Rozegranych gier(x1000)")
        ax1.set_ylabel("Odsetek wygranych gier [%]")
        new_tick_locations = np.array([0, 40, 80,120,160,200])
        ax = ax1.twiny()
        ax.plot(arraysXY[i],arraysXY[i+1],markers[c],ls='-',ms=5,markevery=50,alpha=0.9,label=nameFile,color=colorArray[c])
        ax.set_xticklabels(new_tick_locations)
        ax.set_xlabel("Pokolenia")
        i=i+2
        c=c+1
        d=d+1
        # boxplot -- na 5
    ax2.boxplot(arrayBox,notch=True,showmeans=True,bootstrap=10000)
    ax2.grid(linewidth=0.1)
    ax2.set_xticklabels(namesArray,rotation=25);
    plt.savefig('myplot.pdf')
    plt.close()


if __name__=='__main__':
    main()
