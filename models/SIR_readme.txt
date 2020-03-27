SIR disease model

N : fixed population
S : number of susceptible people
I : number of infected people
R : number of removed or recovered people(includes people who are dead but not taken into account for small death rates)
trans : Transmission rate
recov : Recovery rate

N = S(t) + I(t) + R(t)
recov = 1/no.of days required for an infected person to recover #recov = 1/10 to 1/14 for SARS-Cov2
Ro = trans/recov
trans = Ro * recov

S' = (-trans*S*I)/N
I' = (trans*S*I)/N - recov*I
R' = recov*I


