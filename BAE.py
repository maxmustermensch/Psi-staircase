import numpy as np
import PsiMarginal

ntrials = 5  # number of trials
a = np.linspace(0.01, 60, 31)  # threshold/bias grid
b = np.linspace(0.01, 10, 50)  # slope grid
x = np.linspace(0, 45, 19)  # possible stimuli to use
delta = 0.2  # lapse grid
gamma = np.linspace(0.01, 0.99, 100)  # guess rate equal to lapse

# parameters used to simulate observer
a_Gen = 12
b_Gen = 2
delta_Gen = 0.2
gamma_Gen = 0.3


# initialize algorithm
psi = PsiMarginal.Psi(x, Pfunction='Weibull', nTrials=ntrials, threshold=a, slope=b, guessRate=gamma,
                      lapseRate=delta, marginalize=True)

# parameters to generate first response
generativeParams = np.array(([a_Gen, b_Gen, delta_Gen, gamma_Gen, psi.xCurrent])).T
# [1,4] appose to [0,4] is required for likelihood function, so add an additional dim.
generativeParams = np.expand_dims(generativeParams, 0)

print ('Simulating an observer with a=%.2f, b=%.2f and delta=%.2f.' % (a_Gen, b_Gen, delta_Gen))
for i in range(0, ntrials):  # run for length of trials
    print (psi.xCurrent)
    # r = PsiMarginal.GenerateData(generativeParams, psyfun='Weibull')  # generate simulated response
    r = int(input("input: "))
    psi.addData(r)  # update Psi with response
    print ('Trial %d of %d' % (i, ntrials))
    while psi.xCurrent == None:  # wait until next stimuli is calculated
        pass

    generativeParams[0, 4] = psi.xCurrent  # set new stimuli to present
print ('Estimated parameters of this observer are a=%.2f, b=%.2f and delta=%.2f.' % (psi.eThreshold,
                                                                                         psi.eSlope,
                                                                                         psi.eLapse))
psi.plot(muRef=a_Gen, sigmaRef=b_Gen, lapseRef=delta_Gen, guessRef=gamma_Gen)
