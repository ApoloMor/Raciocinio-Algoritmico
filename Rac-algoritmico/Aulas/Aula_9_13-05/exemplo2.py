
def pa(a, r, n):
    if n ==1:
        return a
    return r + pa(a, r, n-1)
a = int(input('Digite o termo inicial da PA: '))
r = int(input('Digite a razão da PA: '))
n = int(input('Digite o numero do termoque deseja obter desta PA: '))
an = pa(a, r, n)
print(f'O {n}° termo da pa é: {an}')