import sys
import struct
import binascii
import re

def binprint(string, length):
	return ' '.join(string[i:i+length] for i in xrange(0,len(string),length))

def swapEndian(input):
    count = 0
    output = ""
    tmp = ""
    for characters in input:
        tmp += str(characters)
        if count == 3:
            output += tmp[::-1]
            tmp = ""
            count = 0
        else:
            count +=1

    return output

binaryConv = lambda x: " ".join(reversed( [i+j for i,j in zip( *[ ["{0:04b}".format(int(c,16)) for c in reversed("0"+x)][n::2] for n in [1,0] ] ) ] ))

input = sys.argv[1]

print("input is " + str(input))

print("hex is " + str(input))
print("len of hex input: " + str(len(input)))


#binary = bin(int(input, 16))[2:]
binary = binaryConv(input)
binary.replace(" ", "")
binary.replace(' ', '').replace("\t", "")
re.sub(r'\s+', '', binary)
binary = ''.join(binary.split())
print("type is " + str(type(binary)))
#swpBin = swapEndian(binary)
swpBin = binary

print(" test " + "test"[:2] + str(len("test")))


print("decimal is " + str(binary))
print("decimal len " + str(len(binary)))
#print("swap is " + str(swpBin))
#print("swap len " + str(len(swpBin)))

res = []
ind = 8
manufacturer_code = str(swpBin[:ind])
print("manufacturer code is " + manufacturer_code + " len " + str(len(manufacturer_code)))
print("hex " + hex(int(manufacturer_code,2)))
res.append(manufacturer_code)

reserved = str(swpBin[ind:ind+6])
print("reserved " + reserved + " len " + str(len(reserved)))
print("hex " + hex(int(reserved,2)))
ind += 6
res.append(reserved)

cardBGA = str(swpBin[ind:ind+2])
print("card/bga " + cardBGA + " len " + str(len(cardBGA)))
print("hex " + hex(int(cardBGA,2)))
ind += 2
res.append(cardBGA)

OEMID = str(swpBin[ind:ind+8])
print("OEM application ID " + OEMID + " len " + str(len(OEMID)))
print("hex " + hex(int(OEMID,2)))
ind += 8
res.append(OEMID)

productName = str(swpBin[ind:ind+48])
print("Product name " + productName + " len " + str(len(productName)))
print("hex " + hex(int(productName,2)))
ind += 48
res.append(productName)

prodRevision = str(swpBin[ind:ind+8])
print("product revision " + prodRevision + " len " + str(len(prodRevision)))
print("hex " + hex(int(prodRevision,2)))
ind += 8
res.append(prodRevision)

prodSerial = str(swpBin[ind:ind+32])
print("product serial number " + prodSerial + " len " + str(len(prodSerial)))
print("hex " + hex(int(prodSerial,2)))
ind += 32
res.append(prodSerial)

manufacture_date = str(swpBin[ind:ind+8])
print("manufacturing date " + manufacture_date + " len " + str(len(manufacture_date)))
print("hex " + hex(int(manufacture_date,2)))
ind += 8
res.append(manufacture_date)

crc_checksum = str(swpBin[ind:ind+7])
print("CRC7 Checksum " +  crc_checksum + " len " + str(len(crc_checksum)))
print("hex " + hex(int(crc_checksum,2)))
ind += 7
res.append(crc_checksum)

endb = str(swpBin[ind:])
print("END should be 1 " + endb + " len " + str(len(endb)))
print("hex " + hex(int(endb,2)))
res.append(endb)


# difference between two
if(len(sys.argv) == 3):
    input2 = sys.argv[2]
    bin2 = binaryConv(input2)
    bin2.replace(" ", "")
    bin2.replace(' ', '').replace("\t", "")
    re.sub(r'\s+', '', bin2)
    bin2 = ''.join(bin2.split())

    print(" a " + sys.argv[1])
    print(" b " + sys.argv[2])
    print(" bin : " + binary)
    print(" bi2 : " + bin2 )
    print(" bhex : "  + hex(int(binary,2)))
    print(" b2ex : " + hex(int(bin2, 2)))

    # swpBin = swapEndian(binary)
    swpBin = bin2

    #print(" test " + "test"[:2] + str(len("test")))

    #print("decimal is " + str(s2))
    #print("decimal len " + str(len(s2)))
    # print("swap is " + str(swpBin))
    # print("swap len " + str(len(swpBin)))
    rind = 0

    ind = 8
    manufacturer_code = str(swpBin[:ind])
    #print("manufacturer code is " + manufacturer_code + " len " + str(len(manufacturer_code)))
    #print("hex " + hex(int(manufacturer_code, 2)))
    if(res[rind] != manufacturer_code):
        print("difference \n" + str(res[rind]) + "\n" + manufacturer_code)
    rind += 1

    reserved = str(swpBin[ind:ind + 6])
    #print("reserved " + reserved + " len " + str(len(reserved)))
    #print("hex " + hex(int(reserved, 2)))
    ind += 6
    if (res[rind] != reserved):
        print("difference \n" + str(res[rind]) + "\n" + reserved)
    rind += 1


    cardBGA = str(swpBin[ind:ind + 2])
    #print("card/bga " + cardBGA + " len " + str(len(cardBGA)))
    #print("hex " + hex(int(cardBGA, 2)))
    ind += 2
    if (res[rind] != cardBGA):
        print("difference \n" + str(res[rind]) + "\n" + cardBGA)
    rind += 1

    OEMID = str(swpBin[ind:ind + 8])
    #print("OEM application ID " + OEMID + " len " + str(len(OEMID)))
    #print("hex " + hex(int(OEMID, 2)))
    ind += 8
    if (res[rind] != OEMID):
        print("difference \n" + str(res[rind]) + "\n" + OEMID)
    rind += 1

    productName = str(swpBin[ind:ind + 48])
    #print("Product name " + productName + " len " + str(len(productName)))
    #print("hex " + hex(int(productName, 2)))
    ind += 48
    if (res[rind] != productName):
        print("difference productname \n" + str(res[rind]) + "\n" + productName)
        print(hex(int(res[rind], 2)))
        print(hex(int(productName, 2)))
    rind += 1


    prodRevision = str(swpBin[ind:ind + 8])
    #print("product revision " + prodRevision + " len " + str(len(prodRevision)))
    #print("hex " + hex(int(prodRevision, 2)))
    ind += 8
    if (res[rind] != prodRevision):
        print("difference prodrevision \n" + str(res[rind]) + "\n" + prodRevision)
        print(hex(int(res[rind], 2)))
        print(hex(int(prodRevision, 2)))
    rind += 1

    prodSerial = str(swpBin[ind:ind + 32])
    #print("product serial number " + prodSerial + " len " + str(len(prodSerial)))
    #print("hex " + hex(int(prodSerial, 2)))
    ind += 32
    if (res[rind] != prodSerial):
        print("difference prodserial \n" + str(res[rind]) + "\n" + prodSerial)
	r1 = binprint(res[rind],4)
	r2 = binprint(prodSerial, 4)
        print(hex(int(res[rind], 2)))
        print(hex(int(prodSerial, 2)))
	print(r1)
	print(r2)

	# change bits of original cid
	
    rind += 1

    manufacture_date = str(swpBin[ind:ind + 8])
    #print("manufacturing date " + manufacture_date + " len " + str(len(manufacture_date)))
    #print("hex " + hex(int(manufacture_date, 2)))
    ind += 8
    if (res[rind] != manufacture_date):
        print("difference manufacture date \n" + str(res[rind]) + "\n" + manufacture_date)
        print(hex(int(res[rind], 2)))
        print(hex(int(manufacture_date, 2)))
    rind += 1

    crc_checksum = str(swpBin[ind:ind + 7])
    #print("CRC7 Checksum " + crc_checksum + " len " + str(len(crc_checksum)))
    #print("hex " + hex(int(crc_checksum, 2)))
    ind += 7
    if (res[rind] != crc_checksum):
        print("difference crc \n" + str(res[rind]) + "\n" + crc_checksum)
    rind += 1

    endb = str(swpBin[ind:])
    #print("END should be 1 " + endb + " len " + str(len(endb)))
    #print("hex " + hex(int(endb, 2)))
    if (res[rind] != endb):
	r1 = binprint(res[rind],4)
	r2 = binprint(endb, 4)
        print("difference \n" + str(res[rind]) + "\n" + endb)
        print(hex(int(res[rind],2)))
        print(hex(int(endb, 2)))
	print(r1)
	print(r2)
    rind += 1
