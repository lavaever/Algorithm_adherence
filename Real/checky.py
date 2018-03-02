a_list = [1,2,3,4,60,]
aa_list = [10,20,30,40,50]

beu = abs(sum(a_list)-sum(aa_list))/5

print(beu)

actual_sales = [223,208,234,104,233,212,196,206,195,200,]
human_forecast = [200,200,200,200,200,200,200,200,200,200]
sum =0
for i in range(10):
    ae = abs(actual_sales[i]-human_forecast[i])
    sum += ae

print(sum)