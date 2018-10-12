import random
randnum=random.randrange(0,9999,1)

#randnum=10

class wronganswerError(Exception):
    print(Exception)
class FIFTHwronganswerError(Exception):
    print(Exception)    
class SIXTHwronganswerError(Exception):
    print(Exception)
class SEVNTHwronganswerError(Exception):
    pass
class EIGTHwronganswerError(Exception):
    pass

print("let me tell the rules. You have to guess the number in my mind. I will give you only 9 attempts for this. ")
print("lets start the game")
print("Made by Python Pirates")
counter=0
while(counter<10):
    try:
        counter=counter+1
        a=int(input("Enter the number"))
        if(a==randnum):
            print("CONGRATULATIONS YOU WON")
            break;
        else:
            print("you have finished your chance number ",counter)
            if(counter<5):
                raise wronganswerError("Still wrong number")
            elif(counter==5):
               raise FIFTHwronganswerError("Still wrong number")
            elif(counter==6):
               raise SIXTHwronganswerError("Still wrong number")
            elif(counter==7):
               raise SEVNTHwronganswerError("Still wrong number")
            elif(counter==8):
               raise EIGTHwronganswerError("Still wrong number")   
            else:
                pass
    except wronganswerError:
        print("still wrong guess")
    except FIFTHwronganswerError:
        if(randnum-a>.1*randnum):
            print("sorry you are too far in 5th attempt and we need to end the game")
            break
        else:
            print("You have only got 4 more chances")
    except SIXTHwronganswerError:
        if(randnum-a>.05*randnum):
            print("sorry you are too far in 6th attempt and we need to end the game")
            break
        else:
            print("You have only got 3 more chances")
    except SEVNTHwronganswerError:
        if(randnum-a>.01*randnum):
            print("sorry you are too far in 7th attempt and we need to end the game")
            break
        else:
            print("You have only got 2 more chances")
    except EIGTHwronganswerError:
        if(randnum-a>.005*randnum):
            print("sorry you are too far in 8th attempt and we need to end the game")
            break
        else:
            print("You have only got 1 more chances")
            
            
    finally:
        pass
print("game over")
