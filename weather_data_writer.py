import xlwt


with open('devore_data.txt') as f:
    file = f.readlines()
#for i in lines:
    temp = [line[:-1] for line in file]
    #print (temp)
    n=0
    wb = xlwt.Workbook()

    ws = wb.add_sheet("Weather Data")


    for i in temp:
        n=temp.index(i)
        record_type = i[0:3]
        station_number = i[3:9]
        observation_year = i[9:13]
        observation_month = i[13:15]
        observation_day = i[15:17]
        observation_date = i[9:17]
        observation_time = i[17:21]
        observation_type = i[21]
        state_weather_code = i[22]
        dry_bulb_temperature = i[23:26]
        atmospheric_moisture = i[26:29]
        wind_direction = i[29:32]
        avg_windspeed = i[32:35]
        lag_fuel_moisture = i[35:37]
        max_temp = i[37:40]
        min_temp = i[40:43]
        max_rel_humidity = i[43:46]
        min_rel_humidity = i[46:49]
        precipitation_dur = i[49:51]
        precipitation_amount = i[51:56]
        wet_flag = i[56]
        hgf = i[57:59]
        sgf = i[59:61]
        moisture_type_code = i[61]
        measurement_type_code = i[62]
        season_code = i[63]
        solar_radiation = i[64:68]
        peak_gust_wind_direction = i[68:71]
        peak_gust_wind_speed = i[71:74]
        snow_flag = i[-1]

        ws.write(n, 0, record_type)
        ws.write(n, 1, station_number)
        ws.write(n, 2, observation_date)
        ws.write(n, 3, observation_time)
        ws.write(n, 4, observation_type)
        ws.write(n, 5, state_weather_code)
        ws.write(n, 6, dry_bulb_temperature)
        ws.write(n, 7, atmospheric_moisture)
        ws.write(n, 8, wind_direction)
        ws.write(n, 9, avg_windspeed)
        ws.write(n, 10, lag_fuel_moisture)
        ws.write(n, 11, max_temp)
        ws.write(n, 12, min_temp)
        ws.write(n, 13, max_rel_humidity)
        ws.write(n, 14, min_rel_humidity)
        ws.write(n, 15, precipitation_dur)
        ws.write(n, 16, precipitation_amount)
        ws.write(n, 17, wet_flag )
        ws.write(n, 18,  hgf)
        ws.write(n, 19,  sgf )
        ws.write(n, 20, moisture_type_code)
        ws.write(n, 21, measurement_type_code)
        ws.write(n, 22, season_code)
        ws.write(n, 23, solar_radiation)
        ws.write(n, 24, peak_gust_wind_direction)
        ws.write(n, 25, peak_gust_wind_speed)
        ws.write(n, 26, snow_flag)







wb.save("formated_data3.xls")