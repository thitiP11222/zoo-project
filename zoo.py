class Zoo:
    def get_ticket_price(self, age): 
        if 0 <= age <= 12: #s1 {0<=}
            return 50 #s2
        elif 13 <= age <= 20: #s3 {<=20}
            return 100 #s4
        elif 21 <= age <= 60: #s5 {21<=}
            return 150 #s6
        elif age > 60: #s7 {>60}
            return 100 #s8
        else: return "invalid age"  # handle invalid
        
zoo=Zoo()
print('test invalid: '+str(zoo.get_ticket_price(-1))) # 'invalid age'
print('test child: '+str(zoo.get_ticket_price(0))) # expected 50
print('test teen: '+str(zoo.get_ticket_price(13))) # expected 100
print('test adult: '+str(zoo.get_ticket_price(21))) # expected 150
print('test elderly: '+str(zoo.get_ticket_price(61))) # expected 100
