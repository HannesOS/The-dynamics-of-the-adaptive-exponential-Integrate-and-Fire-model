all_parameter_sets = []

#Paper Parameters
all_parameter_sets.append({
    'name' : 'no spike',
    'C' : 281,          #pF
    'g_L' : 30,        #nS
    'E_L' : -70.6,      #mV
    'V_T' : -50.4,      #mV
    'delta_T' : 2 ,      #mV
    'a' : 4,            #nS
    'tau_w': 144,       #ms
    'b': 80.5,        #pA
    'V_reset' : -70.6,  #mV
    'V_thresh' : 20,    #mV
    'I' : 500,         #pA
    'none' : 0         #placeholder
})

#Paper Parameters (accelerated firing)
all_parameter_sets.append({
    'name' : 'accelerated firing',
    'C' : 281,          #pF
    'g_L' : 30,        #nS
    'E_L' : -70.6,      #mV
    'V_T' : -50.4,      #mV
    'delta_T' : 2 ,      #mV
    'a' : 4,            #nS
    'tau_w': 144,       #ms
    'b': 80.5,        #pA
    'V_reset' : -70.6,  #mV
    'V_thresh' : 20,    #mV
    'I' : 700,         #pA
    'none' : 0         #placeholder
})


# Initial Bursting
all_parameter_sets.append({
    'name' : 'initial bursting',
    'C' : 281,          #pF
    'g_L' : 30,        #nS
    'E_L' : -70.6,      #mV
    'V_T' : -50.4,      #mV
    'delta_T' : 2 ,      #mV
    'a' : 4,            #nS
    'tau_w': 144,       #ms
    'b': 80.5,        #pA
    'V_reset' : -49.5,  #mV
    'V_thresh' : 20,    #mV
    'I' : 900,         #pA
    'none' : 0         #placeholder
})

#Continued Bursting
all_parameter_sets.append({
    'name' : 'continued bursting',
    'C' : 281,          #pF
    'g_L' : 30,        #nS
    'E_L' : -70.6,      #mV
    'V_T' : -50.4,      #mV
    'delta_T' : 2 ,      #mV
    'a' : 4,            #nS
    'tau_w': 144,       #ms
    'b': 80.5,        #pA
    'V_reset' : -47,  #mV
    'V_thresh' : 20,    #mV
    'I' : 700,         #pA
    'none' : 0         #placeholder
})

#Regular spiking
all_parameter_sets.append({
    'name' : 'regular spiking',
    'C' : 281,          #pF
    'g_L' : 30,        #nS
    'E_L' : -70.6,      #mV
    'V_T' : -50.4,      #mV
    'delta_T' : 2 ,      #mV
    'a' : 4,            #nS
    'tau_w': 144,       #ms
    'b': 80.5,        #pA
    'V_reset' : -70.6,  #mV
    'V_thresh' : 20,    #mV
    'I' : 750,         #pA
    'none' : 0         #placeholder
})

#Just one spike
all_parameter_sets.append({
    'name' : 'just one spike',
    'C' : 281,          #pF
    'g_L' : 30,        #nS
    'E_L' : -70.6,      #mV
    'V_T' : -50.4,      #mV
    'delta_T' : 2 ,      #mV
    'a' : 4,            #nS
    'tau_w': 144,       #ms
    'b': 80.5,        #pA
    'V_reset' : -70.6,  #mV
    'V_thresh' : 20,    #mV
    'I' : 600,         #pA
    'none' : 0         #placeholder
})

#Chaos
all_parameter_sets.append({
    'name' : 'chaos',
    'C' : 281,          #pF
    'g_L' : 30,        #nS
    'E_L' : -70.6,      #mV
    'V_T' : -50.4,      #mV
    'delta_T' : 2 ,      #mV
    'a' : 4,            #nS
    'tau_w': 40,       #ms
    'b': 80.5,        #pA
    'V_reset' : -47.9,  #mV
    'V_thresh' : 20,    #mV
    'I' : 800,         #pA
    'none' : 0         #placeholder
})

#Chaos2
all_parameter_sets.append({
    'name' : 'chaos2',
    'C' : 281,          #pF
    'g_L' : 30,        #nS
    'E_L' : -70.6,      #mV
    'V_T' : -50.4,      #mV
    'delta_T' : 2 ,      #mV
    'a' : 4,            #nS
    'tau_w': 40,       #ms
    'b': 80.5,        #pA
    'V_reset' : -47.9,  #mV
    'V_thresh' : 20,    #mV
    'I' : 800,         #pA
    'none' : 0         #placeholder
})


def get_params(name):
    for parameter_set in all_parameter_sets:
        if parameter_set['name'] == str(name).lower():
            return parameter_set

    raise Exception(f'The parameter set for {name} could not be found.')