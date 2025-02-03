#exercice 1
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
week_days=days[:5]
end_days=days[5:]

week_days_v2=[]
for i in range(5):
    week_days_v2.append(days[i])

end_days_v2=[]
for i in range(5,7):
    end_days_v2.append(days[i])

print(days[6])
print(days[-1])
print(days[::-1])

#exercice 2
print(list(range(0,21*9,9)))

#exercice 3
print(len(list(range(2,10001,2))))