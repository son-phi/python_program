# PY04013 - TÍNH TOÁN LƯỢNG MƯA




class RainfallStation:
    def __init__(self,id, name, duration, rainfall_amount ) -> None:
        self.id = str(id)
        self.name = str(name)
        self.duration = int(duration)
        self.amt = rainfall_amount
        self.average_hourly_rainfall = round(self.amt/ (self.duration/60),2)
        pass
    
    def update(self,dur,amt):
        self.duration += dur
        self.amt += amt
        return 
    
    
dict_station = {}
t = int(input())

for x in range(t):
    name = input()
    start = input()
    end = input()
    amt = int(input())
    duration = 60 - int(start[-2:]) + int(end[-2:]) + int(end[:2]) - int(start[:2]) -1
    
    id = "T0{}".format(len(dict_station)+1) 
    st1 = RainfallStation(id, name, duration, amt)
    if name not in dict_station.keys() :
        dict_station[name] = st1
    else:
        st2 = dict_station[name]
        st2.update(duration, amt)
        dict_station[name] = st2


print(len(dict_station))
# print(dict_station)
for s in dict_station.values() :
    # s = RainfallStation(st[0],st[1],st[2],st[3])
    print( "{} {} {:.2f}".format(s.id, s.name,s.average_hourly_rainfall))
    print( s.duration , s.amt)
    # print(st[2],st[3])

