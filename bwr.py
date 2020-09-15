# Bitcoin wallet recovery

import requests, hashlib, random, os, binascii, ecdsa, base58, PySimpleGUI as sg, pyperclip

        

menu_def = [
            ['&Menu', ['&Recover wallet', '&Copy', '&Paste', 'E&xit']],
            ['&Help', '&About...'], ]



        
sg.ChangeLookAndFeel('LightBlue')
layout =  [
            [sg.Menu(menu_def, tearoff=True)],
            [sg.Image('bit.png', size=(199, 122))],
            [sg.Text('Enter seed phrase:', font=('Helvetica', 12), size=(15,1)), sg.InputText(size=(70,1), font=('Helvetica', 12), text_color='white', key = 'recovery')],
            [sg.Text('Address:', font=('Helvetica', 12),size=(15,1)), sg.Text('', size=(70,1), font=('Helvetica', 12),  key='generator')],
            [sg.Text('Privatekey:',font=('Helvetica', 12), size=(15,1)), sg.Text('', size=(70,1), font=('Helvetica', 12), key='privatekey')],
            [sg.Text('WIF:', font=('Helvetica', 12), size=(15,1)), sg.Text('', size=(70,1), font=('Helvetica', 12), key='wif')],
            [sg.Button('Recover wallet', font=('Helvetica', 12))]]


window = sg.Window('Bitcoin wallet recovery',
                  layout=layout,
                   default_element_size=(12,1),
                   font='Helvetica 18',
                   )





while True:
    event, values = window.Read()
    if event == 'Recover wallet':
        f = values['recovery']
        secret_exponent = hashlib.sha256(f.encode("utf-8")).hexdigest()
        key = binascii.unhexlify(secret_exponent)
        s = ecdsa.SigningKey.from_string(key, curve = ecdsa.SECP256k1)
        public_key = '04' + binascii.hexlify(s.verifying_key.to_string()).decode('utf-8')
        output = []; alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
        var = hashlib.new('ripemd160')
        var.update(hashlib.sha256(binascii.unhexlify(public_key.encode())).digest())
        var = '00' + var.hexdigest() + hashlib.sha256(hashlib.sha256(binascii.unhexlify(('00' + var.hexdigest()).encode())).digest()).hexdigest()[0:8]
        count = [char != '0' for char in var].index(True) // 2
        n = int(var, 16)
        while n > 0:
            n, remainder = divmod(n, 58)
            output.append(alphabet[remainder])
        for i in range(count): output.append(alphabet[0])
        address = ''.join(output[::-1])
        var80 = "80"+secret_exponent
        var = hashlib.sha256(binascii.unhexlify(hashlib.sha256(binascii.unhexlify(var80)).hexdigest())).hexdigest()
        WIF = str(base58.b58encode(binascii.unhexlify(str(var80) + str(var[0:8]))))
        data = open("Wallet.txt","a")
        data.write("Wallet: "+"\n\n" +"\n"+"seed phrase:   "+ str(f) +"\n"+"Address:    "+str(address)+"\n"+ "Privatekey: " +str(secret_exponent)+"\n"+"Publickey:  " + str(public_key)+"\n"+"WIF:        " +str(WIF)+"\n\n"+'-------------------------------------------------------------------------------------------------------------------------------'+"\n\n")
        data.close()
        window.Element('generator').Update(str(address))
        window.Element('privatekey').Update(str(secret_exponent))
        window.Element('wif').Update(str(WIF))

    elif event == 'Copy':
        cypher_message = cypher(f)
        pyperclip.copy(str(cypher_message))
        pyperclip.paste()


    elif event == 'Paste':
        text = pyperclip.paste()
        window.Element('recovery').Update(str(text))
    

    elif event == 'About...':      
        sg.popup('About:', 'Created by Adrijan Petek', 'Bitcoin wallet recovery', 'Version 1.0',)

        

        
    elif event in (None, 'Exit'):
        break


window.Close()    


