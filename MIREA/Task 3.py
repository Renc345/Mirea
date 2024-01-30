n = int(input())
for i1 in ['', '', '+']:
    for i2 in ['', '-', '+']:
        for i3 in ['', '-', '+']:
            for i4 in ['', '-', '+']:
                for i5 in ['', '-', '+']:
                    for i6 in ['', '-', '+']:
                        for i7 in ['', '-', '+']:
                            for i8 in ['', '-', '+']:
                                s = '1' + i8 + '2' + i7 + '3' + i6 + '4' + i5 + '5' + i4 + '6' + i3 + '7' + i2 + '8' + i1 + '9'
                                if eval(s) == n:
                                    print(s)
                                    exit()
print('Нет решения')
