import random

# 产生 1 到 10 的一个整数型随机数
print(random.randint(1, 10))


s = 'snUseRandom'
if s.find('UseRandom') != -1:
    s = s.replace('UseRandom',str(random.randint(1,99999)))

else:
    pass

print(s)

# 随机生成10个字符组成的一个字符串
s = ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a','1','2','3','4','5','6','7','8','9','0'], 10))
print(s)