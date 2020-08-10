import numpy as np

R=np.matrix([[-1,-1,-1,-1,0,-1],[-1,-1,-1,0,-1,100],[-1,-1,-1,0,-1,-1],[-1,0,-1,-1,0,-1],[0,-1,-1,0,-1,100],[-1,0,-1,-1,0,100]])

Q=np.matrix(np.zeros([6,6]))

gamma=0.8

initial_state=1

def available_action(state):
    current_state=R[state]
    av_act=np.where(current_state>=0)[1]
    return av_act

def next_action(ava_action):
    next_act=int(np.random.choice(ava_action,1))
    return next_act

def update_matrix(current,gamma,action):
    c=0
    A= available_action(action)
    for i in range(len(A)):
        if Q[action,A[i]]>=c:
            c=Q[action,A[i]]
        else:
            c=c
    Q[current,action]=R[current,action]+gamma*c


for i in range(5000):
    current=np.random.randint(0,6)
    available_act=available_action(current)
    action=next_action(available_act)
    update_matrix(current,gamma,action)

print(Q/np.max(Q)*100)

current_step=2
steps=[current_step]

while current_step != 5:
    next_step=np.where(Q[current_step,]==np.max(Q[current_step,]))[1]
    if next_step.shape[0]>1:
        next_step=int(np.random.choice(next_step,size=1))
    else:
        next_step=int(next_step)
    steps.append(next_step)
    current_step=next_step

print(steps)