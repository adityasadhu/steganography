from Tkinter import *
from PIL import Image,ImageTk
import binascii
import optparse
a=""

def rgb2hex(r, g, b):
	return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def hex2rgb(hexcode):
	return tuple(map(ord, hexcode[1:].decode('hex')))

def str2bin(message):
	binary = bin(int(binascii.hexlify(message), 16))
	return binary[2:]

def bin2str(binary):
	message = binascii.unhexlify('%x' % (int('0b'+binary,2)))
	return message

def encode(hexcode, digit):
	if hexcode[-1] in ('0','1', '2', '3', '4', '5'):
		hexcode = hexcode[:-1] + digit
		return hexcode
	else:
		return None

def decode(hexcode):
	if hexcode[-1] in ('0', '1'):
		return hexcode[-1]
	else:
		return None

def hide():
    filename=e1.get()
    message=e2.get()
    img = Image.open(filename)
    binary = str2bin(message) + '1111111111111110'
    if img.mode in ('RGBA'):
	    img = img.convert('RGBA')
	    datas = img.getdata()
		
	    newData = []
	    digit = 0
	    temp = ''
	    for item in datas:
		    if (digit < len(binary)):
			    newpix = encode(rgb2hex(item[0],item[1],item[2]),binary[digit])
			    if newpix == None:
				    newData.append(item)
			    else:
				    r, g, b = hex2rgb(newpix)
				    newData.append((r,g,b,255))
				    digit += 1
		    else:
			    newData.append(item)	
	    img.putdata(newData)
	    img.save(filename, "PNG")
	    print "Completed!"
	    c1()
    return "Incorrect Image Mode, Couldn't Hide"
def c1():
        a144=Tk()
        ax=Label(a144,text="completed")
        ax.pack()
        ax.mainloop()
        
						


    

def retr():
    global a 
    filename=e1.get()
    img = Image.open(filename)
    binary = ''
	
    if img.mode in ('RGBA'): 
	    img = img.convert('RGBA')
	    datas = img.getdata()
		
	    for item in datas:
		    digit = decode(rgb2hex(item[0],item[1],item[2]))
		    if digit == None:
			    pass
		    else:
			    binary = binary + digit
			    if (binary[-16:] == '1111111111111110'):
				    print "Success"
				    print bin2str(binary[:-16])
				    a=bin2str(binary[:-16])
				    print a
				    d()
				    exit(0)
				    

	    print bin2str(binary)
    return "Incorrect Image Mode, Couldn't Retrieve"
    
def d():
        aditya1=Tk()
        global a
        print a
        label2=Label(aditya1,text="decoded message is")
        label2.pack()
        labell=Label(aditya1,text=a)
        labell.pack()
        labell.mainloop()
        
def x():
    aditya=Tk()
    aditya.title("about stegenography")
    a1=Label(aditya,text="segenography, The art and science of")
    a1.grid(row=0)
    a2=Label(aditya,text="hiding information byembedding messages within other, seemingly")
    a2.grid(row=1)
    a3=Label(aditya,text="harmless messages. Steganography works by replacing bits of useless")
    a3.grid(row=2)
    a4=Label(aditya,text="or unused data in regular computer files")
    a4.grid(row=3)
    a5=Label(aditya,text="such as graphics, sound, text, HTML, or even floppy disks  with bits")
    a5.grid(row=4)
    a6=Label(aditya,text="of different, invisible information. This hidden information can be plain text")
    a6.grid(row=5)
    a7=Label(aditya,text="cipher text, or even images.")
    a7.grid(row=6)
    a8=Label(aditya,text="Steganography sometimes is used when encryption is not permitted.")
    a8.grid(row=7)
    a9=Label(aditya,text="Or, more commonly, steganography is used to supplement encryption. An encrypted")
    a9.grid(row=8)
    a11=Label(aditya,text="file may still hide information using steganography, so even if the encrypted")
    a11.grid(row=9)
    a12=Label(aditya,text="file is deciphered, the hidden message is not seen.")
    a12.grid(row=10)
    aditya.mainloop()
    
        
root=Tk()
menu=Menu(root)
root.config(menu=menu)

subMenu= Menu(menu)
menu.add_cascade(label="About", menu=subMenu)
subMenu.add_command(label="About", command=x)

root.title('stegenography')
root.geometry("500x500")
temp=Image.open("stege.png")
temp = temp.save("stege.ppm","ppm")
photo = PhotoImage(file = "stege.ppm")
imagepanel=Label(root,image = photo)
imagepanel.grid(row=0)

a=Label(root,text="enter the file path(only use .png images)")
a.grid(row=1)
e1= Entry(root,width=30)
e1.grid(row=2)

a1=Label(root,text="enter the message")
a1.grid(row=3) 


e2=Entry(root)
e2.grid(row=4)
button=Button(root,text='encrypt',command=hide)
button.grid(row=5)
button1=Button(root,text='decrypt',command=retr)
button1.grid(row=6)

root.mainloop()
