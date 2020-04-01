def format_duration(seconds):
    res=""
    s = [" second", " minute", " hour", " day", " year"]
    if seconds == 0: res = "now";
    time =[seconds,0,0,0,0]
    x= [60,60,24,365]
    unit = []
    for i in range(time.__len__()):
        if time.__len__()-1!=i :
            time[i+1] = time[i]//x[i]
            time[i] = time[i]%x[i]
        if time[i] > 0:
            if time[i] > 1:
                y = "s";
            else:
                y = "";
            unit.insert(0,(str(time[i]) + s[i] + y))

    i = len(unit) - 1;
    while i >= 0:
        res = unit[i] + res;
        if i == len(unit) - 1 and len(unit) > 1:
            res = ' and ' + res;
        elif i <= len(unit) - 2 and i > 0:
            res = ", " + res;
        i -= 1;
    return res
  
print(format_duration(99999999))
