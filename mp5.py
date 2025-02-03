from random import*
interact={0:(2,4),1:(0,4),2:(1,3),3:(1,4),4:(0,2)}
sign_list=["rock","paper","scissors","lezard","spock"]
score_comp=0
score_plr=0
while score_comp<3 and score_plr<3:
    plr_sign=""
    while plr_sign not in ["0","1","2","3","4"]:
        plr_sign=input("Please choose a sign (0: rock, 1:paper, 2: scissors, 3: lezard, 4: spock)")
    plr_sign=int(plr_sign)
    comp_sign=randint(0,4)
    if plr_sign==comp_sign:
        result="draw"
    elif comp_sign in interact[plr_sign]:
        result="victory"
        score_plr+=1
    else:
        result="defeat"
        score_comp+=1
    print(f"Sign player => {sign_list[plr_sign]} / {sign_list[comp_sign]} <= sign computer")
    print(f"{result} (score player {score_plr} / {score_comp} score computer)")
if score_plr==3:
    print("**********You won the game**********")
else:
    print("**********You lost the game**********")