def prime(n):
#nilai awal
    ls = [2,3]

#pengandaian jika n < 3 maka return nilai awal
    if (n < 3):
        return ls[:n]

#pengandaian hingga beroleh bilangan prima
    for i in range(2,n):
        generate = ls[-1]+2
        while any(not(generate%num) for num in ls):
            generate += 2
        ls.append(generate)
    return ls

#kotak input nilai N yang diinginkan
n = int(input('First N prime number:'))

#hasil dari perintah n
print(prime(n))
