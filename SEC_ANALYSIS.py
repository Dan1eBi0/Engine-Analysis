#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[1]:


def gera_lista (tempo, vel, data_hora):
    p = []
    t = []
    i = 0 
    w = 0
    for i in tempo:
        if data_hora in str(i):
            t.append(i)
            p.append(vel[w])
        w = w+1
    return (t, p)


# In[3]:


def gera_grafico (tempo, vel):
    
    min_vel = min(vel)
    max_vel = max(vel)
    
    lim_max_vel = [max_vel]*len(tempo)
    lim_min_vel = [min_vel]*len(tempo)
    
    frequencia_max = vel.count(max(vel))
    frequencia_min = vel.count(min(vel))
    
    fig, ax = plt.subplots()
    ax.set_ylim(min_vel - 5, max_vel + 5)
    ax.plot(tempo, lim_max_vel, color = 'red')
    ax.plot(tempo, lim_min_vel, color = 'red')
    ax.plot(tempo, vel)

    ax.set(xlabel='Tempo', ylabel='Velocidade',
       title='Velocidade do Motor')
    ax.grid()

    #fig.savefig("test21.png")
    #plt.show()

    return plt


# In[ ]:


def gera_listas_conjunto (dataFrame):
    
    df_s1 = dataFrame[dataFrame['Set']==1]
    df_s2 = dataFrame[dataFrame['Set']==2]
    df_s3 = dataFrame[dataFrame['Set']==3]
    df_s4 = dataFrame[dataFrame['Set']==4]
    
    p2_1 = df_s1['BasicVariables/SEC_Velocidade_P2_PV'].tolist()
    p2_2 = df_s2['BasicVariables/SEC_Velocidade_P2_PV'].tolist()
    p2_3 = df_s3['BasicVariables/SEC_Velocidade_P2_PV'].tolist()
    p2_4 = df_s4['BasicVariables/SEC_Velocidade_P2_PV'].tolist()

    t2_1 = df_s1['BasicVariables/SEC_Velocidade_P2_PV_Timestamp'].tolist()
    t2_2 = df_s2['BasicVariables/SEC_Velocidade_P2_PV_Timestamp'].tolist()
    t2_3 = df_s3['BasicVariables/SEC_Velocidade_P2_PV_Timestamp'].tolist()
    t2_4 = df_s4['BasicVariables/SEC_Velocidade_P2_PV_Timestamp'].tolist()
    
    p3_1 = df_s1['BasicVariables/SEC_Velocidade_P3_PV'].tolist()
    p3_2 = df_s2['BasicVariables/SEC_Velocidade_P3_PV'].tolist()
    p3_3 = df_s3['BasicVariables/SEC_Velocidade_P3_PV'].tolist()
    p3_4 = df_s4['BasicVariables/SEC_Velocidade_P3_PV'].tolist()

    t3_1 = df_s1['BasicVariables/SEC_Velocidade_P2_PV_Timestamp'].tolist()
    t3_2 = df_s2['BasicVariables/SEC_Velocidade_P2_PV_Timestamp'].tolist()
    t3_3 = df_s3['BasicVariables/SEC_Velocidade_P2_PV_Timestamp'].tolist()
    t3_4 = df_s4['BasicVariables/SEC_Velocidade_P2_PV_Timestamp'].tolist()
    
    p4_1 = df_s1['BasicVariables/SEC_Velocidade_P4_PV'].tolist()
    p4_2 = df_s2['BasicVariables/SEC_Velocidade_P4_PV'].tolist()
    p4_3 = df_s3['BasicVariables/SEC_Velocidade_P4_PV'].tolist()
    p4_4 = df_s4['BasicVariables/SEC_Velocidade_P4_PV'].tolist()

    t4_1 = df_s1['BasicVariables/SEC_Velocidade_P2_PV_Timestamp'].tolist()
    t4_2 = df_s2['BasicVariables/SEC_Velocidade_P2_PV_Timestamp'].tolist()
    t4_3 = df_s3['BasicVariables/SEC_Velocidade_P2_PV_Timestamp'].tolist()
    t4_4 = df_s4['BasicVariables/SEC_Velocidade_P2_PV_Timestamp'].tolist()
    
    p5_1 = df_s1['BasicVariables/SEC_Velocidade_P5_PV'].tolist()
    p5_2 = df_s2['BasicVariables/SEC_Velocidade_P5_PV'].tolist()
    p5_3 = df_s3['BasicVariables/SEC_Velocidade_P5_PV'].tolist()
    p5_4 = df_s4['BasicVariables/SEC_Velocidade_P5_PV'].tolist()

    t5_1 = df_s1['BasicVariables/SEC_Velocidade_P2_PV_Timestamp'].tolist()
    t5_2 = df_s2['BasicVariables/SEC_Velocidade_P2_PV_Timestamp'].tolist()
    t5_3 = df_s3['BasicVariables/SEC_Velocidade_P2_PV_Timestamp'].tolist()
    t5_4 = df_s4['BasicVariables/SEC_Velocidade_P2_PV_Timestamp'].tolist()

    return (t2_1,p2_1,t3_1,p3_1,t4_1,p4_1,t5_1,p5_1,t2_2,p2_2,t3_2,p3_2,t4_2,p4_2,t5_2,p5_2,t2_3,p2_3,t3_3,p3_3,t4_3,p4_3,t5_3,p5_3,t2_4,p2_4,t3_4,p3_4,t4_4,p4_4,t5_4,p5_4)


# In[ ]:


def gera_grafico_multiplo (tempo1, vel1,tempo2, vel2,tempo3, vel3,tempo4, vel4):
    
    fig, axs = plt.subplots(2, 2)
    
    min_vel1 = min(vel1)
    max_vel1 = max(vel1)
    lim_max_vel1 = [max_vel1]*len(tempo1)
    lim_min_vel1 = [min_vel1]*len(tempo1)
    
    min_vel2 = min(vel2)
    max_vel2 = max(vel2)
    lim_max_vel2 = [max_vel2]*len(tempo2)
    lim_min_vel2 = [min_vel2]*len(tempo2)
    
    min_vel3 = min(vel3)
    max_vel3 = max(vel3)
    lim_max_vel3 = [max_vel3]*len(tempo3)
    lim_min_vel3 = [min_vel3]*len(tempo3)
    
    min_vel4 = min(vel4)
    max_vel4 = max(vel4)
    lim_max_vel4 = [max_vel4]*len(tempo4)
    lim_min_vel4 = [min_vel4]*len(tempo4)
    
    
    axs[0, 0].set_ylim(min_vel1 - 5, max_vel1 + 5)
    axs[0, 0].plot(tempo1, lim_max_vel1, color = 'red')
    axs[0, 0].plot(tempo1, lim_min_vel1, color = 'red')
    axs[0, 0].plot(tempo1, vel1)
    axs[0, 0].set_title("P2 Conjunto 1")
    axs[0,0].grid()
    
    axs[1, 0].set_ylim(min_vel2 - 5, max_vel2 + 5)
    axs[1, 0].plot(tempo2, lim_max_vel2, color = 'red')
    axs[1, 0].plot(tempo2, lim_min_vel2, color = 'red')
    axs[1, 0].plot(tempo2, vel2)
    axs[1, 0].set_title("P2 Conjunto 2")
    #axs[1, 0].sharex(tempo1, vel1)
    axs[1,0].grid()
    
    axs[0, 1].set_ylim(min_vel3 - 5, max_vel3 + 5)
    axs[0, 1].plot(tempo3, lim_max_vel3, color = 'red')
    axs[0, 1].plot(tempo3, lim_min_vel3, color = 'red')
    axs[0, 1].plot(tempo3, vel3)
    axs[0, 1].set_title("P2 Conjunto 3")
    axs[0,1].grid()
    
    axs[1, 1].set_ylim(min_vel4 - 5, max_vel4 + 5)
    axs[1, 1].plot(tempo4, lim_max_vel4, color = 'red')
    axs[1, 1].plot(tempo4, lim_min_vel4, color = 'red')
    axs[1, 1].plot(tempo4, vel4)
    axs[1, 1].set_title("P2 Conjunto 4")
    axs[1,1].grid()
    
    fig.tight_layout()
    
    return plt


# In[ ]:


def calcula_frequencia(vel):

    frequencia_max = vel.count(max(vel))
    frequencia_min = vel.count(min(vel))
  
    return frequencia_min,frequencia_max


# In[ ]:


def calcula_frequencia_round(vel):
    
    vel_round =  [round(y) for y in vel]
    maximo = max(vel_round)
    minimo = min(vel_round)
    frequencia_max = vel_round.count(maximo)
    frequencia_min = vel_round.count(minimo)
  
    return frequencia_min,frequencia_max


# In[ ]:


def calcula_variacao_set_point(vel,setPoint):
    
    result = [((y-setPoint)/setPoint)*100 for y in vel]
    maximo = max(result)
    minimo = min(result)
    
    
    return (minimo,maximo,result)


# In[ ]:


def gera_grafico_multiplo_2 (tempo1, vel1,tempo2, vel2,tempo3, vel3):
    
    fig, axs = plt.subplots(2, 2)
    
    min_vel1 = min(vel1)
    max_vel1 = max(vel1)
    lim_max_vel1 = [max_vel1]*len(tempo1)
    lim_min_vel1 = [min_vel1]*len(tempo1)
    
    min_vel2 = min(vel2)
    max_vel2 = max(vel2)
    lim_max_vel2 = [max_vel2]*len(tempo2)
    lim_min_vel2 = [min_vel2]*len(tempo2)
    
    min_vel3 = min(vel3)
    max_vel3 = max(vel3)
    lim_max_vel3 = [max_vel3]*len(tempo3)
    lim_min_vel3 = [min_vel3]*len(tempo3)
    
    
    
    axs[0, 0].set_ylim(min_vel1 - 5, max_vel1 + 5)
    axs[0, 0].plot(tempo1, lim_max_vel1, color = 'red')
    axs[0, 0].plot(tempo1, lim_min_vel1, color = 'red')
    axs[0, 0].plot(tempo1, vel1)
    axs[0, 0].set_title("P2 Conjunto 1")
    axs[0,0].grid()
    
    axs[1, 0].set_ylim(min_vel2 - 5, max_vel2 + 5)
    axs[1, 0].plot(tempo2, lim_max_vel2, color = 'red')
    axs[1, 0].plot(tempo2, lim_min_vel2, color = 'red')
    axs[1, 0].plot(tempo2, vel2)
    axs[1, 0].set_title("P2 Conjunto 2")
    #axs[1, 0].sharex(tempo1, vel1)
    axs[1,0].grid()
    
    axs[0, 1].set_ylim(min_vel3 - 5, max_vel3 + 5)
    axs[0, 1].plot(tempo3, lim_max_vel3, color = 'red')
    axs[0, 1].plot(tempo3, lim_min_vel3, color = 'red')
    axs[0, 1].plot(tempo3, vel3)
    axs[0, 1].set_title("P2 Conjunto 3")
    axs[0,1].grid()
    
    '''axs[1, 1].set_ylim(min_vel4 - 5, max_vel4 + 5)
    axs[1, 1].plot(tempo4, lim_max_vel4, color = 'red')
    axs[1, 1].plot(tempo4, lim_min_vel4, color = 'red')
    axs[1, 1].plot(tempo4, vel4)
    axs[1, 1].set_title("P2 Conjunto 4")
    axs[1,1].grid()'''
    
    fig.tight_layout()
    
    return plt

