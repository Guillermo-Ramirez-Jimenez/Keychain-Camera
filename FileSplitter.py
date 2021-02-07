#File splitter v1.1
#By Guillermo Ramírez Jiménez

file_name = input('Enter input file name:')         #Input file name
offsets_name = input('Enter offsets file name:')    #Offsets file name
previous = 0                                        #Previous address
i = 0                                               #File counter

with open(file_name, 'rb') as f:
    with open(offsets_name, 'r') as offsets:
        for line in offsets:
            data = f.read(int(line, 16)-previous)
            previous = int(line, 16)
            with open(str(i)+'.bin', 'wb') as out:
                i = i+1
                out.write(data)
                out.close()
        with open(str(i)+'.bin', 'wb') as out:
            out.write(f.read())
            out.close()
            print('Finished!')
