# Two lamda functions to convert Root Mean Squared value of the voltage to peak value and vice versa
# Root Mean Squared value of the voltage is also known as the effective value of the voltage, outlets ratings are usually RMS values

V0_RMS = 230 # initial Root Mean Squared value of the voltage 

V_Peak = lambda V0_RMS : V0_RMS*2**0.5 # lambda function to calculate the peak value of the voltage from the RMS value
V0_Peak = V_Peak(V0_RMS) # peak value of the voltage

print(V0_Peak)

V_RMS = lambda V0_Peak : V0_Peak/2**0.5 # lambda function to calculate the RMS value of the voltage from the peak value
V0_RMS = V_RMS(V0_Peak)

print(V0_RMS)