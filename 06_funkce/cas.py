import time

# unix time (epoch time)

"""
print("teď budu čekat 2s")
time.sleep(2)
print("konec")
"""
"""
while True:
    print(time.time())
    time.sleep(1)
"""

print(time.time())  # aktuální čas v unix formátu
print(time.ctime(8527))  # převod času unix -> běžný
cas = time.localtime()  #  vrátí (něco jako) seznam s časovými údaji
print(cas.tm_hour,":",cas.tm_min)  # aktuální čas (hodiny a minuty)
novyCas = (2017, 2, 3, 4, 17, 19, 0, 0, 0)
#(year, month, day, hour, minute, second, weekday, day of the year, daylight saving)
print(time.mktime(novyCas))  # převod času běžný -> unix

#  kolik sekund jsem na světě?

narozeni = (2003, 12, 1, 0, 0, 0, 0, 0, 0)
narozeniUnix = time.mktime(narozeni)
print(time.time() - narozeniUnix)