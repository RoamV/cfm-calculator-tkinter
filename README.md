# cfm-calculator-tkinter
Costume calculator tkinter (Length, Width Qty) to (Mm,m3,Cfm,inch)

function:

Milimetre= (int(Length)*int(Width))/10**6

Inch= (int(Length)+int(Width))/50

Cubic Feet per Minute (CFM) =(int(Length)*int(Width)/10**6/0.09*600)

m^3 (metre cubic) =(int(Qty)*((Length+60)*(Width+60)*60)/10**9)
