#km hm dam m dm cm mm

medida=float(input('digite a medida em metros : '))

dm=medida*10
cm=medida*100
mm=medida*1000
dam=medida/10
hm=medida/100
km=medida/1000

print("""
a converção de metros para dm é {:.1f}
a converção de metros para cm é {:.1f}
a converção de metros para mm é {:.1f}
a converção de metros para dam é {:.1f}
a converção de metros para hm é {:.1f}
a converção de metros para km é {:.1f}""".format(dm,cm,mm,dam,hm,km))
