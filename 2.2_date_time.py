# Here do not use NO2_date, use sth like "df_date", so the focus is on the syntax itself
# use small quick sample data to enable the example

# convert YYYYMMDD to YYYY-MM-DD
test = pd.to_datetime(20201220,format = '%Y%m%d')


# convert "DD/MM/YYYY HH:mm" to "YYYY-MM-DD HH:mm"

# convert 

# generate "YYYY-MM-DD" using "year,month,day"

# but this is a string, not a real date time object
df = pd.DataFrame()
df['year'] = [2019,2020,2021]
df['month'] = [1,2,3]
df['day'] = [28,29,30]
df = df.astype(str)
df['date'] = df['year'] +'-'+ df['month'] + '-' + df['day']
print(df)

#
