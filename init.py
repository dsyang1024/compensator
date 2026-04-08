import readfiles as rf
import graphy

obsdir = 'observation'
barometric_name = ['Level_Baro', 'Baro_csv']
mode = 'Compensated' # subfolder name in station folder

dir = rf.get_dir(obsdir)


stationlist = rf.get_stationlist(dir)
stationlist.remove(barometric_name[0])

print ('\nStation list :', stationlist)


barolist = rf.get_f_from_baro(dir, barometric_name, barometric_name[1])
print ('\nBarometric :', len(barolist))
# rf.connect_files(barometric_name[0], dir, barometric_name[1], barolist)

# stationlist = stationlist[:1]
for station in stationlist:
    filelist = rf.get_f_from_station (stationlist, station, dir, mode)
    print (station, ':', len(filelist))
    # filelist = filelist[10:15]
    rf.connect_files(station, dir, mode, filelist)


graphy.read_connected(stationlist, dir, mode)
graphy.read_connected([barometric_name[0]], dir, barometric_name[1])