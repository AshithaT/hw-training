import json
import re
error_log = []
# url=''
# file = input('Enter the input file :')
with open("firstweber_2022_01_03.json", 'r') as myfile:
    file_data = myfile.read()

    if 'null' in file_data:
        lines = file_data.split('\n')
        for line_number, line in enumerate(lines):
            error = ''
            try:
                d = json.loads(line)
            except Exception as e:
                error = str(e)

            if not error:

                if "None" in d.values():
                    key = list(d.keys())[list(d.values()).index("None")]
                    error_log.append(
                        {'error': 'None', 'line_number': line_number+1, 'key': key})
                    print("key=", key)
                    print("line no=", line_number+1)

                elif "null" in d.values():
                    key = list(d.keys())[list(d.values()).index("null")]
                                      
                    error_log.append({'error':'null', 'line_number': line_number+1, 'key': key})
                    
                    res = [str(i or '') for i  in error_log]
                    
                    print("key=", key)
                    print("line no=", line_number+1)


                elif "\t" in d.values():
                    key = list(d.keys())[list(d.values()).index("\t")]
                    # print("exists")
                    error_log.append({'error': '\t', 'line_number': line_number+1,'key': key})
                    print("key=", key)
                    print("line no=", line_number+1)

                elif "\r" in d.values():
                    key = list(d.keys())[list(d.values()).index("\r")]
                   
                    error_log.append({'error': '\r', 'line_number': line_number+1,'key': key})
                    print("key=", key)
                    print("line no=", line_number+1)

                elif(str(d["first_name"]).find('\n') != -1):
                    
                    error_log.append({'error': '\n', 'line_number': line_number+1,'key': d["first_name"]})

                elif(str(d["last_name"]).find('\n')!=-1):
                  
                    error_log.append({'error': '\n', 'line_number': line_number+1,'key': d["last_name"]})

                elif(str(d["description"]).find('\n')!=-1):
                    
                    error_log.append({'error': '\n', 'line_number': line_number+1,'key': d["description"]})

                elif(str(d["address"]).find('\n')!=-1):
                   
                    error_log.append({'error': '\n', 'line_number': line_number+1,'key': d["address"]})

                elif(str(d["office_name"]).find('\n')!=-1):
                    
                    error_log.append({'error': '\n', 'line_number': line_number+1,'key': d["office_name"]})

                elif(str(d["city"]).find('\n')!=-1):
                    
                    error_log.append({'error': '\n', 'line_number': line_number+1,'key': d["city"]})


                elif(str(d["zipcode"]).find('\n')!=-1):
                    
                    error_log.append({'error': '\n', 'line_number': line_number+1,'key': d["zipcode"]})

                elif(str(d["languages"]).find('\n')!=-1):
                    
                    error_log.append({'error': '\n', 'line_number': line_number+1,'key': d["languages"]})

                elif(str(d["country"]).find('\n')!=-1):
                    
                    error_log.append({'error': '\n', 'line_number': line_number+1,'key': d["country"]})

            else:
                if line_number+1 != len(lines):
                    
                    error_log.append(
                        {'error': error, 'line_number': line_number+1,'key': key})
                    print("error=", error)
                    print("line no=", line_number+1 )
                    print ("not matched")
                else:
                    print("number of lines matched")

            
print(error_log)

val=input("wheather to check total number of lines :(yes/No)?")
if val=="yes":
    print(line_number+1)

# #for line matched or unmatched

lower=int(input("enter the lower and upperlimit :"))
upper=int(input())
if lower<=line_number+1<=upper:
    print("line number matched")
else:
    print("count unmatched")