data_file = open('shampoo_study.txt','r')
i = 1
sparkle_avg_price = 0
pantene_avg_price = 0
tresemmee_avg_price = 0
sparkle_avg_rate = 0
pantene_avg_rate = 0
tresemmee_avg_rate = 0
for line in data_file.readlines():
    line_data = line.split(',')
    if i == 1:
        sparkle_avg_price += float(line_data[1].replace(' ',''))
        sparkle_avg_rate += float(line_data[2].replace(' ',''))
    elif i == 2:
        pantene_avg_price += float(line_data[1].replace(' ',''))
        pantene_avg_rate += float(line_data[2].replace(' ',''))
    else:
        tresemmee_avg_price += float(line_data[1].replace(' ',''))
        tresemmee_avg_rate += float(line_data[2].replace(' ',''))
    i += 1
    if i == 4:
        i = 1
sparkle_avg_price *=1/5
pantene_avg_price *=1/5
tresemmee_avg_price *=1/5
sparkle_avg_rate *=1/5
pantene_avg_rate *=1/5
tresemmee_avg_rate *=1/5
data_file.close()
output_file = open('my_study_and_some_of_my_friends.txt', 'w')
output_file.write(f'sparkle,{sparkle_avg_price},{sparkle_avg_rate}\n')
output_file.write(f'pantene,{pantene_avg_price},{pantene_avg_rate}\n')
output_file.write(f'tresemmee,{tresemmee_avg_price},{tresemmee_avg_rate}\n')

arr = ['sparkle','pantene','tresemmee']
comp = [sparkle_avg_price,pantene_avg_price,tresemmee_avg_price]
comp1 = [sparkle_avg_rate,pantene_avg_rate,tresemmee_avg_rate]
max_price = 0
for i in range(len(comp)):
    if comp[i] > comp[max_price]:
        max_price = i
max_rank = 0
for i in range(len(comp1)):
    if comp1[i] > comp1[max_rank]:
        max_rank = i
output_file.write(f'The best brand based on rank: {arr[max_rank]}\n')
output_file.write(f'The best brand based on price: {arr[max_price]}\n')
if max_price == max_rank:
    output_file.write('High price equals high quality, very materialistic world : D\n')
else:
    output_file.write('We live in heaven, lot of loves\n')
output_file.close()
