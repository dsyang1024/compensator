# -*- coding: utf-8 -*-
from datetime import date

PIC = 'DK'
stations = ['OUT','ILA','ILB','CEN','F63','BARO']
newlist = [['2023_03_04_ACRE_OUT_COMP.csv', '2023_03_26_ACRE_OUT_COMP.csv', '2023_03_31_ACRE_OUT_COMP.csv'], ['2023_03_26_ACRE_ILA_COMP.csv', '2023_03_31_ACRE_ILA_COMP.csv', '2023_04_08_ACRE_ILA_COMP.csv'], ['2023_03_04_ACRE_ILB_COMP.csv', '2023_03_26_ACRE_ILB_COMP.csv', '2023_03_31_ACRE_ILB_COMP.csv'], ['2023_03_04_ACRE_CEN_COMP.csv', '2023_03_26_ACRE_CEN_COMP.csv', '2023_03_31_ACRE_CEN_COMP.csv'], ['2023_03_26_ACRE_F63_COMP.csv', '2023_03_31_ACRE_F63_COMP.csv'], ['2023_02_25_ACRE_BARO.csv', '2023_03_04_ACRE_BARO.csv', '2023_03_26_ACRE_BARO.csv', '2023_03_31_ACRE_BARO.csv', '2023_04_08_ACRE_BARO.csv', '2023_04_16_ACRE_BARO.csv']]

def receipt(PIC,stations,newlist):
    """
    refer: https://www.educative.io/answers/how-to-write-text-on-an-image-in-python

    Returns
    -------
    None.

    """
    
    from PIL import Image, ImageDraw, ImageFont
    img = Image.open("Receipt_Picture.png")
    draw = ImageDraw.Draw(img)
    today = str(date.today())
    
    txt = PIC+'        '+today
    draw.text((40, 80), txt, fill =(0, 0, 0))
    
    yaxis = 80
    
    for i in range(len(stations)):
        yaxis = yaxis+15
        txt = stations[i]
        draw.text((40, yaxis), txt, fill =(0, 0, 0))
        for r in newlist[i]:
            yaxis = yaxis+10
            txt = r
            draw.text((40, yaxis), txt, fill =(0, 0, 0))
    img.save('receipt/'+today+'_'+PIC+'.png')
    img.show()
    
receipt(PIC,stations,newlist)