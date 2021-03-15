#%%
def ADC(n, V_in, V_ref):
    v = 0
    bits = [-1] * n
    for i in range(1, n + 1):
        print(f"Step {i}: MSB{'-'+str(i-1) if (i-1)!=0 else ''} : (Bit {n-i})")
        if (v + V_ref / (2 ** i)) <= V_in:
            v += V_ref / (2 ** i)
            bits[i - 1] = 1
            print("v<=V_in \n>>> " + f"{v}<={V_in}")
            print(f"so MSB{'-'+str(i-1) if (i-1)!=0 else ''} = 1")
            print(bits)
        else:
            bits[i - 1] = 0
            print("v>V_in \n>>> " + f"{v+V_ref/(2**i)}>{V_in}")
            print(f"so MSB{'-'+str(i-1) if (i-1)!=0 else ''} = 0")
            print(bits)
        
        print('-'*50)
    


#%%
vi = 0.6
vr = 1
n = 10

ADC(n, vi, vr)

print(f'ans:{bin(int(vi/vr*2**n))}')
# %%

# %%
