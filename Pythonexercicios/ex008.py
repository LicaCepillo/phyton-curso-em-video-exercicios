num = float(input('Digite uma medida em metros : '))
cm = num*100
mm = num*1000
dm = num/10
hm = num/100
km = num/1000
print('{} metros, corresponde: \n {:.0f} cm , \n {:.0f} mm , \n {} dm , \n {} hm, \n {} km .'.format(num, cm, mm, dm, hm, km))
