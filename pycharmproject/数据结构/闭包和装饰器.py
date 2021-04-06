


def make_av():
    series=[]
    a=1
    def av(new_value):
        nonlocal a
        series.append(new_value)
        total=sum(series)
        a+=1
        return total/len(series)
    return av

xx=make_av()
print(xx(4))