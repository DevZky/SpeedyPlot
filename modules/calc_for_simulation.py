# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:34:43 2018

@author: franzky
"""
import xlsxwriter
import datetime

#from matplotlib.widgets import CheckButtons
#from matplotlib.font_manager import FontProperties

workbook = xlsxwriter.Workbook('calculations_{}.xlsx'.format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
worksheet = workbook.add_worksheet()
excellist = [["File", "Type", "Min","Mean","Max"]]


def calculation(dataframes):
    for ndf in range(0,10,2):
        df = dataframes[ndf]

        lzt=[]
        szt=[]
        cyc= []
        negTime = 0
        posTime= 0
        
        #detect flanks
        s = df[1]["Compressor"].diff()
        
        #plot for camparison
        #plt.figure(df[0])
        #df[1]["Compressor"].plot()
        #s[s!=0].plot(marker="o", linewidth = 0)
        
#        # get two lists with flanktimes -1 neg. flanks, +1 positive flanks
#        [mat.append(s.groupby(s).groups.get(x)._data.tolist()) for x in [-1,1]]
#        
#        # calculate SZT or LZT
#        for e in range(min(len(mat[0]),len(mat[1]))):
#                res.append(abs(mat[0][e]-mat[1][e]))
        
        # calculate SZT and LZT 
        for e in s[s!=0].iteritems():
            if e[1]== -1:
                if negTime!=0:
                    cyc.append(e[0]-negTime)
                negTime=e[0]
                if posTime!=0:
                    lzt.append(negTime-posTime)
            if e[1]==1:
                if posTime!=0:
                    cyc.append(e[0]-posTime)
                posTime = e[0]
                if negTime!=0:
                    szt.append(posTime-negTime)
            
        RED = [x[0]/x[1] for x in zip(lzt,[sum(x) for x in zip(szt, lzt)])]
        
        try:
            tsr_LZ = df[1]["TSR"][df[1]["Compressor"]==1]
            tsr_LZ_end = df[1]["TSR"][df[1]["Compressor"].diff(periods=-1)==1]
        except:
            pass
        
        tnd_LZ = df[1]["TND"][df[1]["Compressor"]==1]
        
        thd_LZ = df[1]["THD"][df[1]["Compressor"]==1]
        
        
        # Umweg über Liste
        #pDiffs = df[1]["P"].diff()
        #pel_LZ_end = [df[1]["P"].iloc[df[1].index.get_loc(i)-1] for i in list(pDiffs[pDiffs<-20].index)]
        
        pel_LZ_end = df[1]["P"][df[1]["P"].diff(periods= - 1)>20]
        
        thd_LZ_end = df[1]["THD"][df[1]["Compressor"].diff(periods=-1)==1]
        
        tnd_LZ_end = df[1]["TND"][df[1]["Compressor"].diff(periods=-1)==1]
        
        fcs_LZ_start = df[1]["FgCompSensor"][df[1]["Compressor"].diff()==1]
        
        fcs_LZ_end = df[1]["FgCompSensor"][df[1]["Compressor"].diff(periods=-1)==1]
        
        ccs_LZ_start  = df[1]["CCompSensor"][df[1]["Compressor"].diff()==1]
        
        ccs_LZ_end = df[1]["CCompSensor"][df[1]["Compressor"].diff(periods=-1)==1]
        
        cces_LZ_start = df[1]["CCompEvapSensor"][df[1]["Compressor"].diff()==1]
        
        cces_LZ_end = df[1]["CCompEvapSensor"][df[1]["Compressor"].diff(periods=-1)==1]

        pel_LZ = df[1]["P"][df[1]["P"]>40.0]
        
        pel_SZ = df[1]["P"][df[1]["P"]<5.0]    
        
        tkf = df[1]["TKF oben"].add(df[1]["TKF mitte"]).add(df[1]["TKF unten"])/3
        
        tkf_LZ = tkf[df[1]["Compressor"]==1]
        
        tkf_LZ_end = tkf[df[1]["Compressor"].diff(periods=-1)==1]
        
        tkf_LZ_start = tkf[df[1]["Compressor"].diff()==1]
        
        try:
            tvf = df[1]["TKLF o"].add(df[1]["TKLF m"]).add(df[1]["TKLF u"])/3
        except:
            tvf = df[1]["P"]*0
        
        tvf_LZ = tvf[df[1]["Compressor"]==1]
    
        tvf_LZ_end =  tvf[df[1]["Compressor"].diff(periods=-1)==1]
    
        tvf_LZ_start = tvf[df[1]["Compressor"].diff()==1]

        try:
            tovfm_LZ = df[1]["TOVFm"][df[1]["Compressor"]==1]
            tovfm_LZ_end = df[1]["TOVFm"][df[1]["Compressor"].diff(periods=-1)==1]
        except:
            tovfm_LZ = df[1]["P"]*0
            tovfm_LZ_end = df[1]["P"]*0
        
        
        
        
        
        cycletime = sum(szt)/len(szt) + sum(lzt)/len(lzt)
        ean =  (pel_LZ.mean()*sum(lzt)/len(lzt) + pel_SZ.mean()*sum(szt)/len(szt))/cycletime/1000*24
        
        try:
            df[1]["TR"] = df[1]["TR 1"].add(df[1]["TR 2"])/2
        except:
            pass
        
        
        # save in excelfile to check the plausibility of the calculated values
        
        #lists
        excellist.append([df[0],"SZT" , min(szt),sum(szt)/len(szt), max(szt)])
        excellist.append([df[0],"LZT" , min(lzt),sum(lzt)/len(lzt), max(lzt)])
        excellist.append([df[0],"RED", min(RED), sum(RED)/len(RED), max(RED)])
        excellist.append([df[0],"CycleTime", min(cyc), sum(cyc)/len(cyc), max(cyc)])
        
        #dataframes
        excellist.append([df[0],"TSR_LZ", tsr_LZ.min(), tsr_LZ.mean(), tsr_LZ.max()])
        excellist.append([df[0],"TND_LZ", tnd_LZ.min(), tnd_LZ.mean(), tnd_LZ.max()])
        excellist.append([df[0],"THD_LZ", thd_LZ.min(), thd_LZ.mean(), thd_LZ.max()])
        excellist.append([df[0],"Pel_LZ", pel_LZ.min(), pel_LZ.mean(), pel_LZ.max()])
        excellist.append([df[0],"Pel_LZ_end", pel_LZ_end.min(), pel_LZ_end.mean(), pel_LZ_end.max()])
        excellist.append([df[0],"THD_LZ_end", thd_LZ_end.min(), thd_LZ_end.mean(), thd_LZ_end.max()])
        excellist.append([df[0],"TND_LZ_end", tnd_LZ_end.min(), tnd_LZ_end.mean(), tnd_LZ_end.max()])
        excellist.append([df[0],"TSR_LZ_end", tsr_LZ_end.min(), tsr_LZ_end.mean(), tsr_LZ_end.max()])
        
        excellist.append([df[0],"FgCompSensor_start", fcs_LZ_start.min(), fcs_LZ_start.mean(), fcs_LZ_start.max()])
        excellist.append([df[0],"FgCompSensor_end", fcs_LZ_end.min(), fcs_LZ_end.mean(), fcs_LZ_end.max()])
        
        excellist.append([df[0],"CCompSensor_start", ccs_LZ_start.min(), ccs_LZ_start.mean(), ccs_LZ_start.max()]) 
        excellist.append([df[0],"CCompSensor_end", ccs_LZ_end.min(), ccs_LZ_end.mean(), ccs_LZ_end.max()])
        
        excellist.append([df[0],"CCompEvapSensor_start", cces_LZ_start.min(), cces_LZ_start.mean(), cces_LZ_start.max()]) 
        excellist.append([df[0],"CCompEvapSensor_end", cces_LZ_end.min(), cces_LZ_end.mean(), cces_LZ_end.max()])

        
        # print to console for copy-paste to modelica model
        print("{}\n".format(df[0])+
                "TR_m={:.4f},\n".format(df[1]["TR"].mean())+
              "dTK_H={:.4f},\n".format(tkf_LZ_start.mean()-tkf_LZ_end.mean())+
              "dVF_H={:.4f},\n".format(tvf_LZ_start.mean()-tvf_LZ_end.mean())+
              f"EAN_m={ean:.4f},\n"+ 
              "RED_m={:.4f},\n".format(sum(RED)/len(RED))+
              "LZT_m={:.4f},\n".format(sum(lzt)/len(lzt))+
              "SZT_m={:.4f},\n".format(sum(szt)/len(szt))+
              "Pel(meanLZ_m={:.4f},endLZ_m={:.4f}),\n".format(pel_LZ.mean(),pel_LZ_end.mean())+
              "THD(meanLZ_m={:.4f},endLZ_m={:.4f}),\n".format(thd_LZ.mean(),thd_LZ_end.mean())+
              "TND(meanLZ_m={:.4f},endLZ_m={:.4f}),\n".format(tnd_LZ.mean(),tnd_LZ_end.mean())+
              "TOVFm(meanLZ_m={:.4f},endLZ_m={:.4f}),\n".format(tovfm_LZ.mean(),tovfm_LZ_end.mean())+
              f"TKF(mean_m={tkf.mean():.4f}),\n"+ 
              f"TVF(mean_m={tvf.mean():.4f}),\n"+ 
              "TSR(meanLZ_m={:.4f},endLZ_m={:.4f}),\n".format(tsr_LZ.mean(),tsr_LZ_end.mean())
                )
            
            
            
    # after calculation: for every measurement --> write data from excellist to .xlsx file        
    for row, data in enumerate(excellist):
        worksheet.write_row(row,0, data)
        
    workbook.close()


if __name__=="__main__":    
    pass