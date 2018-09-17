import os
import mysql.connector

#calculate the number of lines in each file. fname = file name
def file_len(fname):
    with open(fname) as f:
        for k, l in enumerate(f):
            pass
    return k + 1

#read the text file, seperate it into attributes and upload to the mysql server
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
        line_num = file_len(file_path)
        print(line_num)
        temp = [line[:-1] for line in file]

        for i in range(0, line_num - 4, 4):
            #create a single line for each record
            single_line = temp[i] + temp[i + 1] + temp[i + 2] + temp[i + 3] + "\n"

            fs_region = single_line[0:2]
            fs_unit = single_line[2:4]
            fire_number = single_line[4:7]
            destrict_number = single_line[7:9]
            stat_cause = single_line[9]
            gen_cause = single_line[10]
            spesific_cause = single_line[11:13]
            class_of_people = single_line[13]
            fire_size_class = single_line[14]
            total_area_burned = single_line[15:24]
            fs_area_burned = single_line[24:33]
            nonfs_ufs_parea_burned = single_line[33:42]
            nonfs_area_burned = single_line[42:51]
            vegetation_cover_type = single_line[51:53]
            nfmas_aspect = single_line[53]
            topography_code = single_line[54]
            fmz_code = single_line[55:59]
            blank = single_line[59]
            rep_weather_station_number = single_line[60:66]
            nfdrs_fuel_model = single_line[66]
            fire_intensity_level = single_line[67]
            fire_intensity_source = single_line[68:70]
            latitude = single_line[70:76]
            longitude = single_line[76:83]
            township = single_line[83:88]
            range2 = single_line[88:93]
            section = single_line[93:95]
            sub_section = single_line[95:99]
            principal_meridan = single_line[99:101]
            slope_percent = single_line[101:104]
            aspect_class = single_line[104]
            elevation = single_line[105:110]
            state_code = single_line[110:112]
            county_code = single_line[112:115]
            protection_agency = single_line[115:118]
            ownership_at_origin = single_line[118]
            prescribed_fire = single_line[119]
            escaped_fire = single_line[120]
            init_suppression_strategy = single_line[121]
            fff_cost_in_dollars = single_line[122:131]
            fire_ignition_date = single_line[131:139]
            fire_ignition_time = single_line[139:143]
            fire_discovery_date = single_line[143:151]
            fire_discovery_time = single_line[151:155]
            first_action_date = single_line[155:163]
            first_action_time = single_line[163:167]
            second_action_date = single_line[167:175]
            second_action_time = single_line[175:179]
            declared_wildfire_date = single_line[179:187]
            declared_wildfire_time = single_line[187:191]
            fire_contained_date = single_line[191:199]
            fire_contained_time = single_line[199:203]
            fire_controled_date = single_line[203:211]
            fire_controled_time = single_line[211:215]
            fire_out_date = single_line[215:223]
            fire_out_time = single_line[223:227]
            fire_name = single_line[227:247]
            fire_id = single_line[247:254]
            pcode = single_line[254:259]
            wilderness = single_line[259:262]

            mycursor = mydb.cursor()

            sql = "INSERT INTO `WildfireData`(`RepFSRegion`, `RepFSUnit`, `FireNum`, `DistNum`, " \
                  "`StatCause`, `GeneralCause`, `SpecificCause`, `ClassOfPeople`, `FireSizeClass`, `TotalAreaBurned`, " \
                  "`FSAreaBurned`, `NonFSUFSAreaBurned`, `NonFSAreaBurned`, `VegCoverType`, `NFMASAspect`, `TopoCode`, `FMZCode`," \
                  " `Blank`, `WeatherStation`, `NFDRSFualModel`, `FireIntensityLevel`, `FireIntensitySource`, `Latitude`, `Longitude`, " \
                  "`Township`, `Range`, `Section`, `SubSection`, `PrinMeridian`, `Slope`, `Aspect`, `Elevation`, `State`, `CountyCode`, " \
                  "`ProtAgency`, `OwnershipAtOrigin`, `PrescribedFire`, `EscapedFire`, `InitSuppressionStat`, `FFFCost`, `IgniDate`, " \
                  "`IgniTime`, `DiscoDate`, `DiscoTime`, `FristActionDate`, `FristActionTime`, `SecondActionDate`, `SecondActionTime`, " \
                  "`DecWildfireDate`, `DecWildfireTime`, `ContDate`, `ContTime`, `ControledDate`, `ControledTime`, `FireOutDate`, " \
                  "`FireOutTime`, `FireName`, `FireId`, `Pcode`, `Wilderness`) " \
                  "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" \
                  ", %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" \
                  ", %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" \
                  ", %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" \
                  ", %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" \
                  ", %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            val = (fs_region, fs_unit, fire_number, destrict_number, stat_cause, gen_cause, spesific_cause,
                   class_of_people, fire_size_class, total_area_burned, fs_area_burned, nonfs_ufs_parea_burned,
                   nonfs_area_burned, vegetation_cover_type, nfmas_aspect, topography_code, fmz_code, blank,
                   rep_weather_station_number, nfdrs_fuel_model, fire_intensity_level, fire_intensity_source, latitude,
                   longitude, township, range2, section, sub_section, principal_meridan, slope_percent, aspect_class,
                   elevation,
                   state_code, county_code, protection_agency, ownership_at_origin, prescribed_fire, escaped_fire,
                   init_suppression_strategy,
                   fff_cost_in_dollars, fire_ignition_date, fire_ignition_time, fire_discovery_date,
                   fire_discovery_time, first_action_date,
                   first_action_time, second_action_date, second_action_time, declared_wildfire_date,
                   declared_wildfire_time, fire_contained_date,
                   fire_contained_time, fire_controled_date, fire_controled_time, fire_out_date, fire_out_time,
                   fire_name,
                   fire_id, pcode, wilderness)
            mycursor.execute(sql, val)

            mydb.commit()

def loop_through_files_in_directory(dir):
    for filename in os.listdir(dir):
        upload(os.path.join(dir, filename))


loop_through_files_in_directory('data/az')
