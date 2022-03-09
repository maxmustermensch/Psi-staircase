import numpy as np
import PsiMarginal

ntrials = 20  # number of trials
a = np.linspace(0.01, 60, 31)  # threshold/bias grid
b = np.linspace(0.01, 10, 50)  # slope grid
x = np.linspace(0, 45, 19)  # possible stimuli to use
delta = 0.2  # lapse
gamma = np.linspace(0.01, 0.99, 100) # guess


# initialize algorithm
psi = PsiMarginal.Psi(x, Pfunction='Weibull', nTrials=ntrials, threshold=a, slope=b, guessRate=gamma,
                      lapseRate=delta, marginalize=True)

for i in range(0, ntrials):  # run for length of trials
    print ('___________\n\nTrial %d of %d' % (i+1, ntrials))
    print (psi.xCurrent)
    r = int(input("input: "))
    psi.addData(r)  # update Psi with response
    while psi.xCurrent == None:  # wait until next stimuli is calculated
        pass

print ('Estimated parameters of this observer are a=%.2f, b=%.2f and delta=%.2f.' % (psi.eThreshold,
                                                                                         psi.eSlope,
                                                                                         psi.eLapse))
psi.plot(muRef=10, sigmaRef=1, lapseRef=0.2, guessRef=0.5)
