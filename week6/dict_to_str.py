server_data={
  'palm.cpu': [
    (1150864247, 0.5),
    (1150864248, 0.5)
  ],
  'eardrum.cpu': [
    (1150864250, 3.0),
    (1150864251, 4.0)
  ],
  'eardrum.memory': [
    (1503320872, 4200000.0)
  ]
}



def get(data):
    msg=''
    text=data.split(' ')
    
    if text[0]=='get':
        if text[1][:-1] in server_data:
            msg='ok\n'
            for values in server_data[text[1][:-1]]:
                val1=str(values[0])
                #print(val1)
                val2=str(values[1])
                msg=msg+text[1][:-1]+' '+val1+' '+val2+'\n'
        elif text[1][:-1]=='*':
            msg=server_data
        msg=msg+'\n'
        print(msg.encode()) 
    
    return (msg)

    
a=get('get eardrum.cpu\n')


#print(server_data['eardrum.cpu'][0][0])

for key, values in server_data:
    print(values)
