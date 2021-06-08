m = float(input('Metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('{0}m correspondem à {1:.2f}km.'.format(m, km))
print('{0}m correspondem à {1:.2f}hm.'.format(m, hm))
print('{0}m correspondem à {1:.2f}dam.'.format(m, dam))
print('{0}m correspondem à {1:.2f}dm.'.format(m, dm))
print('{0}m correspondem à {1:.2f}cm.'.format(m, cm))
print('{0}m correspondem à {1:.2f}mm.'.format(m, mm))


