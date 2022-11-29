import cmath
pi = cmath.pi

def twiddler(N):

    twiddle_holder = []
    for k in range(N):
        twiddle_holder.append(cmath.exp((-2j*pi*k)/N))

    return twiddle_holder

def ifft(freq_cmplx):

    length = len(freq_cmplx)
    w = twiddler(length)

    # Base cases
    if length == 1:
        return freq_cmplx

    if length == 2:
        a = freq_cmplx[0] + freq_cmplx[1]
        b = freq_cmplx[0] - freq_cmplx[1]
        return [a/2, b/2]

    # Splitting into Xns into quarters
    quarter = int(length/4)
    X0 = [freq_cmplx[i] for i in range(quarter)]
    X1 = [freq_cmplx[i+(quarter)] for i in range(quarter)]
    X2 = [freq_cmplx[i+(2*quarter)] for i in range(quarter)]
    X3 = [freq_cmplx[i+(3*quarter)] for i in range(quarter)]

    # Xns have 2 different set of es
    fft_e_1h = []
    fft_e_2h = []

    sum_odd = []
    diff_odd = []

    # Extracting each es sum_odds and diff_odds from Xns through systems of eqs.
    for x in range(len(X0)):
        fft_e_1h.append((X0[x] + X2[x])/2)
        sum_odd.append((X0[x] - X2[x])/2)
        diff_odd.append((X1[x] - X3[x])/-2j)
        fft_e_2h.append((X3[x] + X1[x])/2)
    
    # merging the 2 different es
    fft_e = fft_e_1h + fft_e_2h

    fft_a = []
    fft_b = []

    # Extracting a and b from sum_odds and diff_odds through system of eqs.
    for odd in range(len(sum_odd)):

        fft_a.append((sum_odd[odd] + diff_odd[odd])/(2*w[odd]))
        fft_b.append((sum_odd[odd] - diff_odd[odd])/(2*w[3*odd]))
    
    # Recursing through the extracted es as and bs
    e = ifft(fft_e)
    a = ifft(fft_a)
    b = ifft(fft_b)

    ifft_output = []
    
    # Sorting bit-reversed output
    for i in range(len(a)):
        ifft_output.append(e.pop(0))
        ifft_output.append(a.pop(0))
        ifft_output.append(e.pop(0))
        ifft_output.append(b.pop(0))

    return ifft_output

# Input Handling
fd_signals = int(input()) # number of frequency signals to ifft
print(fd_signals)

for fd_signal in range(fd_signals):

    signal = input() # signal input 
    signal = signal.split() # make it an array

    final = int(signal.pop(0)) # final = output size
    n_points = int(signal.pop(0)) # n_points = N element of 2^n
    signal = [complex(point) for point in signal] # complexify

    time_domain = ifft(signal)

    # Output Handling
    time_domain = [round(i.real) for i in time_domain]
    print(final, end = '')
    output = ''
    for i in range(final):
        output += ' ' + str(time_domain[i])

    print(output)




        


    
    
    


