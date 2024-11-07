import os
import subprocess

nstar = [3, 4, 5, 6, 7, 7, 8]
varepsilon = [0.4, 0.5, 0.6, 0.7, 0.7, 0.8, 0.8]
halftheta = [17.347, 20.159, 22.735, 25.1, 23.877, 27.276, 26.225]
L = [1.408, 1.41, 1.41, 1.408, 1.432, 1.405, 1.426]
ii = 1
for i, j, k, l in zip(nstar, varepsilon, halftheta, L):
    with open('star.txt', 'w') as fp:
        fp.write(str(i) + '\n')
        fp.write(str(j) + '\n')
        fp.write('0.05356' + '\n')
        fp.write('0.003975' + '\n')
        fp.write('0.008' + '\n')
        fp.write('0.265' + '\n')
        fp.write(str(k) + '\n')
        fp.write(str(l) + '\n')
        fp.write('1770' + '\n')
        fp.write('0.0667857' + '\n')
        fp.write('22.3' + '\n')
        fp.write('3150' + '\n')
        fp.write('1.19' + '\n')
        fp.write('8.0' + '\n')
        fp.write('0.33' + '\n')
    os.system('bat.bat')
    os.rename('p.dat', 'wp'+str(ii)+'dat')
    ii = ii + 1
