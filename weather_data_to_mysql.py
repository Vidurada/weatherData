import os
import mysql.connector

#calculate the number of lines in each file. fname = file name
def file_len(fname):
    with open(fname) as f:
        for k, l in enumerate(f):
            pass
    return k + 1


def upload(file_path):
    mydb = mysql.connector.connect(
        host="localhost", #your mysql host
        user="vidura",   #your user name
        passwd="denta", #your mysql password
        database="Research" #table name
    )

    with open(file_path) as f:
        file = f.readlines()
        # for i in lines:
        temp = [line[:-1] for line in file]

        for i in temp:

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

            mycursor = mydb.cursor()

            sql = "INSERT INTO `WeatherData`(`Record type`, `StationNumber`, `ObservationDate`, `" \
                  "ObservationTime`, `ObservationType`, `StateOfWeatherCode`, `DBTemp`, " \
                  "`AMoisture`, `WindDir`, `AvgWinSpeed`, `10hr`, " \
                  "`MaxTemp`, `MinTemp`, `MaxRelHum`, `MinRelHum`, `PreDur`, " \
                  "`PreAmount`, `WetFlag`, `HGreenFact`, " \
                  "`SGreenFact`, `MoistureType`, `MesuType`, `SeasonCode`, `SolarRed`, " \
                  "`WindDirAtPeak`, `SpeedAtPeak`, `SnowFlag`) " \
                  "VALUES(%s,%s,%s,%s,%s, %s,%s,%s,%s, " \
                  "%s,%s,%s,%s,%s, %s,%s,%s,%s," \
                  "%s,%s,%s,%s,%s, %s,%s,%s,%s)"

            val = (record_type, station_number, observation_date,
                   observation_time, observation_type, state_weather_code, dry_bulb_temperature,
                   atmospheric_moisture, wind_direction, avg_windspeed, lag_fuel_moisture, max_temp, min_temp,
                   max_rel_humidity, min_rel_humidity, precipitation_dur, precipitation_amount, wet_flag, hgf,
                   sgf, moisture_type_code, measurement_type_code,season_code, solar_radiation, peak_gust_wind_direction,
                   peak_gust_wind_speed,snow_flag)

            mycursor.execute(sql, val)

            mydb.commit()


def loop_through_files_in_directory(dir):
    for filename in os.listdir(dir):
        if filename.endswith('.fw13'):
            print (os.path.join(dir, filename))
            upload(os.path.join(dir, filename))



loop_through_files_in_directory('weather/data/al')