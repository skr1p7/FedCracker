import hashlib
import sys
import time

def encode(hash_type,word):
    if hash_type=="1":
        md5=hashlib.md5()
        md5.update(word.encode())
        return md5.hexdigest()
    elif hash_type=="2":
        sha1=hashlib.sha1()
        sha1.update(word.encode())
        return sha1.hexdigest()
    elif hash_type=="3":
        sha224=hashlib.sha224()
        sha224.update(word.encode())
        return sha224.hexdigest()
    elif hash_type=="4":
        sha256=hashlib.sha256()
        sha256.update(word.encode())
        return sha256.hexdigest()
    elif hash_type=="5":
        sha384=hashlib.sha3_384()
        sha384.update(word.encode())
        return sha384.hexdigest()
    elif hash_type=="6":
        sha512=hashlib.sha512()
        sha512.update(word.encode())
        return sha512.hexdigest()
    
def decode(hash,wordlist):
    table={32:1,40:2,56:3,64:4,96:5,128:6}
    hash_type=table[len(hash)]
    wordlist=wordlist.split('\n')
    for x in wordlist: 
        if str(encode(str(hash_type),x))==hash:
            print("\033[91m"+ hash + "\033[0m" + "-->" + "\033[92m"+x+"\033[0m")
            return
    print("Hash " + "\033[91m"+ hash + "\033[0m"+ " not found")
    return

if __name__=="__main__":
    while True:
        print ("(1)"+ "\033[92m" + " Hashing"+"\033[0m")
        print ("(2)"+ "\033[92m" + " Cracking" + "\033[0m")
        print ("(q)"+ "\033[91m" +" Quit" + "\033[0m")
        option=str(input("Enter your choice> "))
        if option=="1":
            print ("(1) md5 ")
            print ("(2) sha1 ")
            print ("(3) sha224 ")
            print ("(4) sha256 ")
            print ("(5) sha 384")
            print ("(6) sha512 ")
            question="Enter the hash type (number)> "
            hash_option=str(input(question))
            plain_string=str(input("Enter the string to be encoded> "))
            print(plain_string+" = "+encode(hash_option,plain_string))
        elif option=="2":
            hashed_string=str(input("Enter the hash> "))
            word_list_path=str(input("Enter name of password list> "))
            try:            
                word_list=open("./"+word_list_path,"r")
            except FileNotFoundError:
                print("Wrong wordlist path")
                continue
            decode(hashed_string,word_list.read())
        elif option == "q":
            print ("Exiting program... ")
            time.sleep(1)
            sys.exit()
        else:
            print("unknown command")