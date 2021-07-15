# Prog Name : FinalProject.py
# Developer Name : ITCS 1950(Kevin Karawan)
# Date : 6/27/2021
# Description : This progtram contains the final version of my project. Some scenes such as scene 1 are guaranteed wins. Some scenes are supposed to result in a loss to stay in line witht the story such as scene Scene5.
# Loses are not logical errors, they are supposed to happen to stay true to the story.



import time
import sys
import random
from os import system

#class list, this is the players army.
playerarmy = []

#class list, this is the AI's army.
enemyarmy = []

#command list
commands = ["buy riflemen", "buy cavalry", "buy spy", "buy cannon", "treasury", "done"]
    
####### START OF CLASSES

class Riflemen:

    def __init__(self, atk, defense):
        self.atk = 3
        self.defense = 30

    #add riflemen units to army
    def AddRiflemen(self, units):
        
        x=0
        
        while x < units:
            y = Player_Riflemen
            playerarmy.append(y)
            x=x+1

    def AddEnemyRiflemen(self, units):
        
        x=0
        
        while x < units:
            y = Enemy_Riflemen
            enemyarmy.append(y)
            x=x+1

Player_Riflemen = Riflemen(3,30)
Enemy_Riflemen = Riflemen(3,30)

class Cavalry:

    def __init__(self, atk, defense):
        self.atk = 6
        self.defense = 100

    #add cavalry units to army
    def AddCavalry(self, units):
        
        x=0
        
        while x < units:
            y = Player_Cavalry
            playerarmy.append(y)
            x=x+1


    #add cavalry units to army
    def RemoveCavalry(self, units):
        
        x=0
        
        while x < units:
            y = Player_Cavalry
            playerarmy.remove(y)
            x=x+1

    #add enemy cavalry units to army
    def AddEnemyCavalry(self, units):
        
        x=0
        
        while x < units:
            y = Enemy_Cavalry
            enemyarmy.append(y)
            x=x+1

Player_Cavalry = Cavalry(5, 100)
Enemy_Cavalry = Cavalry(5, 100)

class Cannon:
    def __init__(self, atk, defense):
        self.atk = 12
        self.defense = 75

    #add cannon units to army
    def AddCannon(self,units):
        
        x=0
        while x < units:
            y = Player_Cannon
            playerarmy.append(y)
            x=x+1

    def AddEnemyCannon(self, units):
        x=0
        while x < units:
            y = Enemy_Cannon
            enemyarmy.append(y)
            x=x+1

Player_Cannon = Cannon(11,75)    
Enemy_Cannon = Cannon(11,75)


class Fort:
    def __init__(self, atk, defense):
        self.atk = 0
        self.defense = 3000

    #add cannon units to army
    def AddFort(self,units):
        
        x=0
        while x < units:
            y = Player_Fort
            playerarmy.append(y)
            x=x+1

    def AddEnemyFort(self, units):
        x=0
        while x < units:
            y = Enemy_Fort
            enemyarmy.append(y)
            x=x+1

Player_Fort = Fort(0,3000)    
Enemy_Fort = Fort(0,3000)

class Treasury:

    def __init__(self, amount):
        self.amount = amount

    def SetTreasury(self, amount):
        self.amount = amount

    def AddToTreasury(self, total):
        self.amount = total + Treasury.amount
        
    def GetTreasury(self):      
        return self.amount

    def PrintTreasury(self):
        print(self.amount)

Treasury = Treasury(2000)
    
######## END OF CLASSES
        
######## START OF FUNCTIONS

def PlayAgain(Scene):
    
    print('Do you want to play again? (yes or no)')
    playAgain = input()
    if playAgain == 'yes' or playAgain == "y":
        if Scene == Scene1:
            Scene1()
        elif Scene == Scene2:
            Scene2()
        elif Scene == Scene3:
            Scene3()
        elif Scene == Scene4:
            Scene4()
        elif Scene == Scene5:
            Scene5()
        elif Scene == Scene6:
            Scene6()
        elif Scene == Scene7:
            Scene7()
        elif Scene == Scene8:
            Scene8()
    else:
        sys.exit()

# Type Delay
def TypeDelay(string):
    for l in string:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(.00000001)

def SceneDateDelay(string):
        time.sleep(1)
        for l in string:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(.0000001)
        time.sleep(.0000001)
        
#sum the atk attribute of all objects in the army list
def GetArmyAtk():

    sum = 0
    for x in range(len(playerarmy)):
        sum = sum + getattr(playerarmy[x], 'atk')
    return sum

#sum the defense attribute of all objects in the army list
def GetArmyDefense():

    sum = 0
    for x in range(len(playerarmy)):
        sum = sum + getattr(playerarmy[x], 'defense')
    return sum


#sum the atk attribute of all objects in the enemy army list
def GetEnemyArmyAtk():

    sum = 0
    for x in range(len(enemyarmy)):
        sum = sum + getattr(enemyarmy[x], 'atk')
    return sum

#sum the defense attribute of all objects in the enemy army list
def GetEnemyArmyDefense():

    sum = 0
    for x in range(len(enemyarmy)):
        sum = sum + getattr(enemyarmy[x], 'defense')
    return sum

#sum the player's army size
def GetArmySize():

    sum = 0
    for x in range(len(playerarmy)):
        sum = sum + 1
    return sum

#sum the enemy's army size
def GetEnemyArmySize():

    sum = 0
    for x in range(len(enemyarmy)):
        sum = sum + 1
    return sum

#player Damage calculation, adds a chance to miss.
def PlayerDamage(playerAttack):
    return playerAttack*random.uniform(.90,.99)

#enemy Damage calculation, adds a slightly higher chance to miss.
def EnemyDamage(enemyAttack):
    return enemyAttack*random.uniform(.90,.96)

def GetMaxRiflemen():
    treasury = Treasury.GetTreasury()
    maxriflemen = treasury/25
    return int(maxriflemen)

def GetMaxCavalry():
    treasury = Treasury.GetTreasury()
    maxcavalry = treasury/50
    return int(maxcavalry)

def GetMaxCannon():
    treasury = Treasury.GetTreasury()
    maxcannon = treasury/100
    return int(maxcannon)

def BuyRiflemen(x):
    GetMaxRiflemen()
    
    if Treasury.GetTreasury() >= 25 and GetMaxRiflemen() > (x-1):
        Treasury.SetTreasury((Treasury.GetTreasury()-(x*25)))
        print("Treasury now = " + str(Treasury.GetTreasury()))
        GetMaxRiflemen()
        print("Max riflemen available now = " + str(GetMaxRiflemen()))
        Player_Riflemen.AddRiflemen(x)
    else:
        print("Insufficient funds, please try again")
            
    return Treasury.GetTreasury()

def BuyCavalry(x):
    GetMaxCavalry()
    
    if Treasury.GetTreasury() >= 50 and GetMaxCavalry() > (x-1):
        Treasury.SetTreasury((Treasury.GetTreasury()-(x*50)))
        print("Treasury now = " + str(Treasury.GetTreasury()))
        GetMaxCavalry()
        print("Max cavalry available now = " + str(GetMaxCavalry()))
        Player_Cavalry.AddCavalry(x)
    else:
        print("Insufficient funds, please try again")
            
    return Treasury.GetTreasury()

def BuyCannon(x):
    GetMaxCannon()
    
    if Treasury.GetTreasury() >= 100 and GetMaxCannon() > (x-1):
        Treasury.SetTreasury((Treasury.GetTreasury()-(x*100)))
        print("treasury now = " + str(Treasury.GetTreasury()))
        GetMaxCannon()
        print("max cannons available now = " + str(GetMaxCannon()))
        Player_Cannon.AddCannon(x)
    else:
        print("insufficient funds, please try again")
            
    return Treasury.GetTreasury()

## Start of Purchase units mechanic ##

# Battle Simulation
def Battle(enemyAttack, enemyDefense, playerAttack, playerDefense):
    
    enemyDamage = EnemyDamage(enemyAttack)
    playerDamage = PlayerDamage(playerAttack)
    d=('''
    Your defense :''' + str(playerDefense))
    e=('''
    Enemy Defense :''' + str(enemyDefense))
    print (d, end="\r" )
    print (e, end="\r \n")

    while enemyDefense > 0:
        
        enemyDamage = enemyAttack*random.uniform(.88,.96) + enemyDamage
        playerDamage = playerAttack*random.uniform(.90,.99) + playerDamage

        remainingPlayerDefense = playerDefense - enemyDamage
        remainingEnemyDefense = enemyDefense - playerDamage

        b = '''
    Army defense :''' + str(remainingPlayerDefense)
        c = '''
    Enemy defense :'''+str(remainingEnemyDefense)
        print (b, end="\r" )
        print (c, end="\r \n")
        time.sleep(.1)

        
        if playerDamage > enemyDefense:
        
            return "player"


        elif enemyDamage > playerDefense:
            return "enemy"
        
def BuyUnits():
    print('''
    Time to resupply. Use the follwing commands to purchase new troops:
    Show treasury: treasury
    Buy riflemen unit $25: buy riflemen
    Buy cavalry unit $50: buy cavalry 
    Buy cannon unit $100: buy cannon 
    when finished: done

''')

    lwrCommand = " "
        
    while lwrCommand != "done":
        command = input()
        lwrCommand = command.lower()
        
        #Start of the command check.
        if lwrCommand in commands:
            
            if lwrCommand == "buy riflemen":
                print("Max Riflemen available : = " + str(GetMaxRiflemen())) 
                print("How many would you like to recruit?")
                x = int(input())
                BuyRiflemen(x)
                command = input("Anything else?\n")
                lwrCommand = command.lower()
              
            elif lwrCommand == "buy cavalry":
                print("Max Cavalry available : = " + str(GetMaxCavalry())) 
                print("How many would you like to recruit?")
                x = int(input())
                BuyCavalry(x)
                command = input("Anything else?\n")
                lwrCommand = command.lower()
              
            elif lwrCommand == "buy cannon":
                print("Max Cannons available : = " + str(GetMaxCannon())) 
                print("How many would you like to recruit?")
                x = int(input())
                BuyCannon(x)
                command = input("Anything else?\n")
                lwrCommand = command.lower()

            elif lwrCommand =="treasury":
                print(Treasury.GetTreasury())
                command = input("Anything else?\n")
                lwrCommand = command.lower()

            elif lwrCommand == "done":
                break
                
        else:
            print('''Command is not supported, please choose a command or enter \"done\" if complete.\n''')
            print('''
    Time to resupply. Use the follwing commands to purchase new troops:
    Show treasury: treasury
    Buy riflemen unit $25: buy riflemen
    Buy cavalry unit $50: buy cavalry 
    Buy cannon unit $100: buy cannon 
    when finished: done

''')
            continue

            

        
######## END OF FUNCTIONS
                
def Intro():
    yearLine = '''
The year is 1755.'''
    SceneDateDelay(yearLine)
    print()
    introLine = '''
    The intensity of the French and Indian war grows daily.
    The Massachussetts Militia has been revived for the war effort.
    You have been named Major of the 3rd regiment int he Worcestor County Militia.
    Your name is Artemis Ward, and your story begins here.

'''
    TypeDelay(introLine)
    Scene1()

########Scene8
def Scene8():
    
    dateLine1  = '''
Charleston, South Carolina - September, 1783,
'''

    text1='''
    Following the Battle at Yorktown and Cornwallis’s surrender—and the British down one-third of its force—the British Parliament, in March 1782, passed a resolution calling for the nation to end the war.
    The British still had 30,000 men in North America, occupying the seaports of New York, Charles Town and Savannah,” according to Taylor.
    The demoralizing loss at Yorktown diminished the British will to continue to fight the rebels.
    On September 3, 1783, the Revolutionary War came to an official end with the signing of the Treaty of Paris.
    You served the continental army with dignith and grace.
    Despite all the challenges you faced, your whit, and braun stayed true.
    Without you, none of this were possible.

    Thank you for playing
    '''
    SceneDateDelay(dateLine1)
    TypeDelay(text1)
    
########Scene7
def Scene7():
    
    dateLine1  = '''
Yorktown, Virginia - June, 1781,
'''

    text1='''
    By mid-September 1781, Washington and French general Rochambeau arrived in Williamsburg, Virginia.
    13 miles from the tobacco port of Yorktown, where Cornwallis’s men had built a defense of 10 small forts with artillery batteries and connecting trenches.
    In response, Cornwallis asked Clinton for aid, and the general promised him a fleet of 5,000 British soldiers would set sail from New York to Yorktown.
    With a small force left in New York, gifted with a $120000 treasury you must resupply for the attack on Yorktown.

    '''

    text2='''Then began a nearly week-long artillery assault on the enemy on October 9.
    '''
    SceneDateDelay(dateLine1)
    TypeDelay(text1)
    del playerarmy[:]
    del enemyarmy[:]
    Treasury.SetTreasury(120000)
    Enemy_Riflemen.AddEnemyRiflemen(3000)
    Enemy_Cavalry.AddEnemyCavalry(500)
    Enemy_Cannon.AddEnemyCannon(200)
    BuyUnits()
    TypeDelay(text2)

    result = Battle(GetEnemyArmyAtk(), GetEnemyArmyDefense(), GetArmyAtk(), GetArmyDefense())
        
    if result == "player":
        winText1 = '''
    The heavy cannons pounded the British mercilessly, but the battle is not over.
    By October 11 had knocked out most of the British guns,” the Army Heritage Center Foundation states.
    Cornwallis received the unfortunate (for him) news that Clinton's departure from New York had been delayed.”
    Despite Washington\'s forces taking tremendous losses, he was resupplied by another division and Rochambeau came to his aid to secure a victory in this battle.
    A new parallel trench, 400 yards closer to the British lines, was ordered by Washington on October 11, but completing it would entail taking out the British redoubts No. 9 and No. 10.
    Washington orders the attack on the British redoubts No. 9 and 10.
'''
        TypeDelay(winText1)
        result = Battle(GetEnemyArmyAtk(), GetEnemyArmyDefense(), GetArmyAtk(), GetArmyDefense())
        
        if result == "player":
            winText2 = '''
    The attack on redoubt No. 9 would eventually be undertaken by French troops, while the No. 10 siege would be led by Colonel Alexander Hamilton.
    The Founding Father wasn\’t the top pick of Major General Marquis de Lafayette for the job, but Hamilton, who wanted to improve his reputation by proving himself on the battlefield, talked Washington into it.
    To speed up the siege of the two redoubts, French troops were to take redoubt No. 9, while Hamilton\’s men were assigned No. 10.
    Washington ordered the use of bayonets, rather than “pounding them slowly into submission with cannon fire.
    
'''
            TypeDelay(winText2)
            result = Battle(GetEnemyArmyAtk(), GetEnemyArmyDefense(), GetArmyAtk(), GetArmyDefense())
            
            if result == "player":
                winText3 = '''
    After nightfall on October 14, the allies fired several consecutive shells in the air that brilliantly illuminated the sky,.
    At that point, Hamilton and his men rallied from their trenches and sprinted across a quarter-mile of field with fixed bayonets.
    For the sake of silence, surprise, and soldierly pride, they had unloaded their guns to take the position with bayonets alone.
    Dodging heavy fire, they let out war whoops that startled their enemies. ... The whole operation had consumed fewer than ten minutes.
    Of his 400 infantrymen, Hamilton lost just nine in the attack, with some 30 wounded, while the 400 French-led troops lost 27 men, with 109 wounded. 
    Surrounded by enemy fire, and blocked from receiving aid by the French fleet that had arrived in Chesapeake Bay, Cornwallis was trapped.
    The successful siege allowed the allies to complete the second parallel trench and “snuffed out the last remains of resistance among the British.
    In a final effort on October 16, Cornwallis attempted a nighttime sea evacuation, but he was stopped by a storm.
    On the morning of October 17, the British sent forward a red-coated drummer boy, followed by an officer waving a white handkerchief to the parapet. All guns fell silent—Cornwallis had surrendered.
    
'''
                TypeDelay(winText3)
                Scene8()
        
            elif result == "enemy":
                loseText = '''
    Your men faught with courage and integrity, but your forces have been defeated.
    Would you like to continue?
    '''

                TypeDelay(loseText)
                PlayAgain(Scene7)

    elif result == "enemy":
        loseText = '''
    Your men faught with courage and integrity, but your forces have been defeated.
    Would you like to continue?
    '''

        TypeDelay(loseText)
        PlayAgain(Scene7)

########Scene6
def Scene6():

    dateLine1  = '''
Monmouth, New Jersey - June, 1778,
'''

    text1='''
    The British surrender at Saratoga brought the French into the war as American allies in February 1778.
    The new British commander, Lieutenant General Henry Clinton, received orders to follow a defensive strategy and consolidate forces in New York City.
    He abandoned Philadelphia and marched his army north. After a 40-hour halt at Monmouth Court House, the army moved out, leaving a small covering force.
    In order to strike a vigorous blow at the retreating enemy, general George Washington ordered Charles Lee, commanding the advance guard, to attack the British rear.
    When Lee attempted to surround the small force at the courthouse, he was surprised by the arrival of Lord Cornwallis’s rear guard, which Clinton had ordered back to resist the attackers.
    Rather than risk fighting a delaying action on difficult terrain, Lee ordered a retreat but was tardy giving Washington notice.

    '''
    text2='''
    It is your duty to ensure general washingtons army is fully equipped to meet Henry Clinton and Lord Cornwallis at Monmouth.
    congress has approved a treasury of $100000 for general Washington\'s army.
    
'''
    text3='''
    When Washington arrived, he was therefore surprised and indignant to find his Continental forces retreating in much disorder.
    Washington arrived about noon, ahead of his main army, in time to see Lee’s men fleeing the battlefield.
    Outraged, Washington rallied and re-formed the men to delay until his following units were in a battle line.
    There were attacks and counterattacks by both sides throughout the hot afternoon, with numerous casualties as American and British cannon swept the field in the largest artillery duel of the war.
    The American left held steady while the advanced right wing under Major General Nathanael Greene was pushed back. Greene re-formed his units as part of the main battle line and fought on.
    general Washington and Charles Lee engage the british forces.

'''

    SceneDateDelay(dateLine1)
    TypeDelay(text1)
    TypeDelay(text2)
    del playerarmy[:]
    del enemyarmy[:]
    Treasury.SetTreasury(100000)
    Enemy_Riflemen.AddEnemyRiflemen(2750)
    Enemy_Cavalry.AddEnemyCavalry(250)
    Enemy_Cannon.AddEnemyCannon(100)
    BuyUnits()
    TypeDelay(text3)

    result = Battle(GetEnemyArmyAtk(), GetEnemyArmyDefense(), GetArmyAtk(), GetArmyDefense())
        
    if result == "player":
        winText = '''
    Benefiting from their winter training at Valley Forge, the Continentals repulsed the British regulars and made bayonet counterattacks. By late afternoon both sides were exhausted and fighting stopped.
    Clinton rested his men until midnight, then he slipped them away to the coast and evacuation by the Royal Navy. Washington did not follow.
    The continentals are one step closer to indepenence.

'''
        TypeDelay(winText)
        Scene7()
        
            
    elif result == "enemy":
        loseText = '''
    Your men faught with courage and integrity, but your forces have been defeated.
    Would you like to continue?
    '''

        TypeDelay(loseText)
        PlayAgain(Scene6)
    
    
########Scene5
def Scene5():

    dateLine1  = '''
Saratoga, New York - October, 1777,
'''

    text1='''
    2 years have passed since Boston. The conflict grows constant and seemingly endless with the British.
    Battles have taken place all over the colonies and the war seems to be less favorable to us.
    The British have killed thousands of our soldiers and imprisoned thousands more.
    We have taken British lives as well, our hands are not clean anymore than theirs.
    2 years ago the continental congress called upon all the colonies to take arms agains the British tyrants.
    The colonies heard their call, and we created a powerful army, the continental army.
    They appointed George Washington as general of the continental army, and me his second in command.
    Congress is negotiating with the French to join the cause and ally against the British, but the French have made no committmentments.
    At time passes by and my bones grow older I cannot grace the fields of glory any longer.
    It is my duty to ensure the continental army has its supplies and maintains it's soldiers.
    
'''

    text2='''
    Our spies have learned that British strategy called for a three-pronged attack on New York, with three separate armies converging near Albany.
    For British General John Burgoyne, moving south from Canada with 7,500 men, the Hudson River Valley became the critical route for the invasion.
    By August, Burgoyne had captured Fort Ticonderoga, defeated fleeing American troops at Hubbardton (Vermont), and occupied Fort Edward, on the edge of the Hudson River.
    After a contingent of Burgoyne\’s troops was defeated in the Battle of Bennington, his reduced forces marched south toward Saratoga in early September.
    General Horatio Gates and his American soldiers had built formidable defenses on Bemis Heights, just south of Saratoga overlooking the Hudson.
    The two armies were set to battle at Freeman\'s farm in September.
    If we can defeat the British here, perhaps the French will agree to become our ally in this war.
    Before the battle, your job is to make sure General Gate\'s army has enough soldiers to take on general Burgoyne at Freeman\'s farm.

'''
    text3 = '''
    Before the battle, your job is to make sure General Gate\'s army has enough soldiers to take on general Burgoyne at Freeman\'s farm.
    Congress has gifted you with a $200,000 treasury for this battle, to ensure a patriot victory.
'''

    text4='''
'''
    SceneDateDelay(dateLine1)
    del playerarmy[:]
    del enemyarmy[:]
    Treasury.SetTreasury(200000)
    TypeDelay(text1)
    TypeDelay(text2)
    
    BuyUnits()
    Enemy_Fort.AddEnemyFort(1)
    Enemy_Riflemen.AddEnemyRiflemen(5500)
    Enemy_Cavalry.AddEnemyCavalry(1500)
    Enemy_Cannon.AddEnemyCannon(500)
    
    text5='''
    The time has come for battle.
'''

    TypeDelay(text5)
    result = Battle(GetEnemyArmyAtk(), GetEnemyArmyDefense(), GetArmyAtk(), GetArmyDefense())
        
    if result == "player":
            winText = '''
    God was truly with us on this day. General Burgoyne\'s put forth a spectacular defense but god smiled upon the patriots today.
    General burgoyne has surrendered.
    The French have taken notice of the victory today and they have agreed to an alliance with the colonies.

'''
            TypeDelay(winText)
            Scene6()
        
            
    elif result == "enemy":
        loseText1 = '''
    Your men faught with courage and integrity, but Gate\'s forces have been exhausted.
    Gate\'s has ordered a strategic withdraw.
    '''
     
        loseText2='''
    Gate\'s withdraws from battle but remains camped upon Freeman'\s farm hoping to trap the enemy or to receive reinforcements.
    His plan worked, and supplies are not received by the British nor do reinforcements come to their aid.
    General washington has also sent a force of 5000 men to reinforce gates.
    Several weeks later Gate\'s launches another attack.

'''

        TypeDelay(loseText1)
        TypeDelay(loseText2)
        Player_Riflemen.AddRiflemen(2500)
        Player_Cavalry.AddCavalry(1500)
        Player_Cannon.AddCannon(1000)

    result = Battle(GetEnemyArmyAtk(), GetEnemyArmyDefense(), GetArmyAtk(), GetArmyDefense())
        
    if result == "player":
        winText = '''
    God was truly with us on this day. General Burgoyne\'s put forth a spectacular defense but god smiled upon the patriots today.
    General burgoyne has surrendered.
    The French have taken notice of the victory today and they have agreed to an alliance with the colonies.
    '''
        print(winText)
        Scene6()
    else:
        loseText = '''
    Your men faught with courage and integrity, but your forces have been defeated.
    Would you like to continue?

    '''
        TypeDelay(loseText)
        PlayAgain(Scene5)
    
    
########Scene4
def Scene4():

    dateLine1  = '''
Boston, Massachusetts - June 10, 1775,
'''
    text1='''
    After the defense of Concord, your advisors are pushing for you to drive the British from Boston.
    You emerged victorious from the Battle on Concord, against greater numbers but your advisors are unsure if the British have resupplied since landing in Boston.
    Boston can be heavily fortified and it would be seemingly impossible to take Boston with such a small force.
    Despite sending the order for all troops to rally, you only have 400 troops. 350 riflemen and a small force of 50 cavalry men.
    You lobby the Safety Committee for funds to add to your treasury in order to recruit more troops.
    The Safety Committee agrees with your petition and has graciously committed $5000 to your trasury.
    The Safety Committee has restored your access to the war treasury. Grantying you access to the  treasury from the 3rd regiment.
    Before heading off to Boston, it is time to resupply your army.
    Your advisors have suggested the purchase of cannons since Boston is so heavily fortified.
    '''
    
    
    SceneDateDelay(dateLine1)
    TypeDelay(text1)
    del playerarmy[:]
    del enemyarmy[:]
    Player_Cavalry.AddCavalry(50)
    Player_Riflemen.AddRiflemen(500)
    Enemy_Fort.AddEnemyFort(1)
    Enemy_Riflemen.AddEnemyRiflemen(500)
    Enemy_Cannon.AddEnemyCannon(50)
    Treasury.AddToTreasury(5000)
    BuyUnits()
    
    text2 = '''
    After your resupply, you make way to Boston. you send a spy into the city to get an idea of the British numbers.
    Your spy reports that the british have a force of over 500 men garrisoned in boston, all riflemen.
    However, the port of Boston will allow for the British to easily resupply and garrison more troops.
    Your spy has identified a street to the west leading into Boston that is unmanned.
    The British believe you will attack from the north.
    You have three choices, will you attack from the north, attack from the west, or surround Boston and attack as needed?
    Reply with:
    Attack from the North
    Attack from the West
    Surround Boston
    
'''
    TypeDelay(text2)
    choice = input()
    choice = choice.lower()
    
    if choice == "surround boston":
        bostonText = '''
    You order your men to surround Boston.
    Your army blocks off the Boston neck and Charlestown neck, the thin strips of land connecting the Boston and Charlestown peninsulas to the mainland,
    This prevents the British from conducting anymore attacks on the surrounding countryside, raiding supplies.
    Supplies in the town quickly dwindled as the British awaited the arrival of supply ships.
    Your decision to cut surround Boston has prevented the British ships of docking and they cannot resupply.
    The British General Thomas Gage decided to fortify Boston’s hills and defensible positions to strengthen his hold over Boston.
    General Gage ordered a line of 10 twenty-pound guns at Roxbury neck and fortified four of the nearby hills.
    During the first few days of the 11-month long siege, any movement in or out of the city, whether it be military or civilian, was completely cut off.
    On April 22, British General Thomas Gage met with town officials to work out a deal that would allow civilians to leave or enter Boston, but the conflict remained.
    The battle has gone on for 11 months.
    Today will be the last battle in the Seige of Boston.
    
    '''
        TypeDelay(bostonText)
        result = Battle(GetEnemyArmyAtk(), GetEnemyArmyDefense(), GetArmyAtk(), GetArmyDefense())
        
        if result == "player":
            winText = '''
    The tactic to surround boston has paid off.
    The British were unable to deliver supplies or more troops because your army surrounds the city
    Your men faught valliantly for almost a year, and they have finally defeated the British.
    General Thomas Gage decided to surrender, and his troops are taken as prisoners of war.
    The seige is finally over.

'''
            TypeDelay(winText)
            Scene5()
        
            
        else:
            loseText = '''
    Your men faught with courage and integrity, but your forces have been defeated.
    Would you like to continue?

    '''
            TypeDelay(loseText)
            PlayAgain(Scene4)

    #head on choice tree         
    elif choice == "attack from the west":
        westtext = '''
    You ordered your army to concentrate on the western side of Boston.
    For 11 months the battle rages.
    The British received a resupply from the port of boston of 1000 soldiers, mostly riflemen and cavalry.
    '''
   
        Enemy_Riflemen.AddEnemyRiflemen(900)
        Enemy_Cavalry.AddEnemyCavalry(100)
        TypeDelay(westtext)
        result = Battle(GetEnemyArmyAtk(), GetEnemyArmyDefense(), GetArmyAtk(), GetArmyDefense())
        
        if result == "player":
            winText = ('''
    Your men faught valliantly for almost a year, and they have finally defeated the British.
    General Thomas Gage decided to surrender, and his troops are taken as prisoners of war.
    The seige is finally over.


''')
            TypeDelay(winText)
            Scene5()
            
        else:
            loseText = ('''
    Your men faught with courage and integrity, but concentrating on the west did not work.
    Would you like to continue?

    ''')
            TypeDelay(loseText)
            PlayAgain(Scene4)

    elif choice == "attack from the north":
        westtext = '''
    You ordered your army to concentrate on the northern side of Boston.
    For 11 months the battle rages.
    The British received a resupply from the port of boston of 1000 soldiers, mostly riflemen and cavalry.
    '''
   
        Enemy_Riflemen.AddEnemyRiflemen(900)
        Enemy_Cavalry.AddEnemyCavalry(100)
        TypeDelay(westtext)
        result = Battle(GetEnemyArmyAtk(), GetEnemyArmyDefense(), GetArmyAtk(), GetArmyDefense())
        
        if result == "player":
            winText = ('''
    Your men faught valliantly for almost a year, and they have finally defeated the British.
    General Thomas Gage decided to surrender, and his troops are taken as prisoners of war.
    The seige is finally over.


''')
            TypeDelay(winText)
            Scene5()
            
        else:
            loseText = ('''
    Your men faught with courage and integrity, but concentrating on the north did not work.
    Would you like to continue?

    ''')
            TypeDelay(loseText)
            PlayAgain(Scene4)
                
    else:
        elseText = '''
    You have been struck with an axe to the chest.
    Your story ends here.
    Would you like to try again?
    
    '''
         
        TypeDelay(elseText)
        PlayAgain(Scene4)
########SCENE 3

def Scene3():

    dateLine1  = '''
December 1755,
'''
    text1='''
    The word of your command of the 3rd regiment has made its way to the general court.
    the general court has offered you the opportunity to serve on the taxation committee to oversee taxation of the colonists.
    For years your dedication to the committee is absolute.
    '''
    
    dateLine2  = '''
December 1762,
'''
    text2='''
    For the past 7 years you sat on the committee along with John Hancock, and Samuel Adams.
    As time passes taxation of the colonists only increases, making life difficult in the colonies.
    Tension grows in committee hearings, time and time again.
    '''

    dateLine3  = '''
December 1770,
'''    
    text3='''
    You, Samuel, and John plead with the committee and the Royal Governor for fair taxation.
    Your pleads fall upon deaf ears.
    The crown and the Royal Governor have no intent to lower taxes on the colonists.
    As the unrest grows you speak out against the unfair taxation.
    As an outspoken patriot, you lash out against the king and the Royal Governor.
    The Royal Governor is infuriated by your words and has decided to strip your military comission and remove you from the committee.
    
    '''

    dateLine4  = '''
December 1772,
'''
    text4='''
    Despite your removal from the taxation committee, and loss of comission, you have refused to be silent for the last 2 years.
    Tensions with the king are at a tipping point. Militiamen are resigning from service to the king and are taking arms against him.
    Eventually the entire 3rd regiment of the Worcestor County militia has resigned from the British service, publicly declaring themselves in rebellion and elected you as their leader.
    Massachusetts’ politics are in upheaval, but they pulled together a Committee of Safety.
    To your surprise they have appointed YOU as general and commander-in-chief of their colony’s militia.

    '''

    dateLine5  = '''
Concord, Massachusetts - April 19, 1775,
'''
    text5=('''
    The night before, hundreds of British troops set off from Boston toward Concord, Massachusetts, in order to seize weapons and ammunition stockpiled there by colonists.
    Early the next morning, the British reached Lexington, where approximately 70 minutemen had gathered on the village green.
    Suddenly a shot rings out, but it’s uncertain which from side. Shortly after, a melee ensued.
    When the brief clash ended, eight Americans lay dead and at least an equal amount were injured, while one redcoat was wounded.
    British commanders ordered the redcoats to continue on to nearby Concord. Your job is to stop them.
    You send the order for your troops to rally at the north bridge of Concord.
    You set off for concord at a moments notice.
    By mid day, you and 200 troops mostly riflemen rally at the north bridge and you await the British arrival.
    Soon enough, you see a small force of what looks to be 2-300 british riflemen on the horizon.
    You are outnumbered, but you have a small force of 50 cavalry, and 100 riflemen units with you.
    ''')
    
    text5cont = '''
    As the British approach they draw a white flag. The British commander awaits you between forces.
    After a brief exchange, it is settled. The British will only enter concord after all of your troops have died.
    Shortly after the British launch an attack, the battle begins!
    You have to decide now, do you take on the british head on, or do you order your cavalry to break formation and flank the british?

    Will you order the cavalry to flank the british or charge them head on?
    
    '''

    
    
    SceneDateDelay(dateLine1)
    TypeDelay(text1)
    SceneDateDelay(dateLine2)
    TypeDelay(text2)
    SceneDateDelay(dateLine3)
    TypeDelay(text3)
    SceneDateDelay(dateLine4)
    TypeDelay(text4)
    SceneDateDelay(dateLine5)
    TypeDelay(text5)
    TypeDelay(text5cont)
    del playerarmy[:]
    del enemyarmy[:]
    Player_Cavalry.AddCavalry(50)
    Player_Riflemen.AddRiflemen(150)
    Enemy_Riflemen.AddEnemyRiflemen(150)
    
    choice = input()
    choice = choice.lower()
    
    if choice == "flank":
        flankText = '''
    You have ordered your cavalry to flank the enemy.
    British commanders see your cavalry break right and have ordered their troops to shift to the treeline.
    The counter by the british has cut off your cavalry from attacking.
    Only god may save us now.

    '''
        TypeDelay(flankText)
        Player_Cavalry.RemoveCavalry(50)
        result = Battle(GetEnemyArmyAtk(), GetEnemyArmyDefense(), GetArmyAtk(), GetArmyDefense())
        
        if result == "player":
            winText = '''
    Your men faught valliantly, and they have defeated the British.
    the British retreated back to Boston, skirmishing with colonial militiamen along the way.
    British forces suffer more casualties along the way; the Revolutionary War has begun.


'''
            TypeDelay(winText)
            Scene4()
            
        else:
            loseText = '''
    Your men faught with courage and integrity, but your forces have been defeated.
    Would you like to continue?

    '''
            TypeDelay(loseText)
            PlayAgain(Scene3)

    #head on choice tree         
    elif choice == "head on" or choice == "charge":
        head_ontext = '''
    You ordered the head on attack.
    Your riflemen volley muskets at the british and your cavalry breaks their defenses.
    The numbers are against you, but strength is on your side.
    '''
   
        
        TypeDelay(head_ontext)
        result = Battle(GetEnemyArmyAtk(), GetEnemyArmyDefense(), GetArmyAtk(), GetArmyDefense())
        
        if result == "player":
            winText = ('''
    Your men faught valliantly, and they have defeated the British.
    the British retreated back to Boston, skirmishing with colonial militiamen along the way.
    British forces suffer more casualties along the way; the Revolutionary War has begun.


''')
            TypeDelay(winText)
            Scene4()
            
        else:
            loseText = ('''
    Your men faught with courage and integrity, but the garrison has fallen.
    Would you like to continue?

    ''')
            TypeDelay(loseText)
            PlayAgain(Scene3)
                
    else:
        elseText = '''
    You have been struck with an axe to the chest.
    Your story ends here.
    Would you like to try again?
    
    '''
         
        TypeDelay(elseText)
        PlayAgain(Scene3)
                
    
########SCENE 2
    
def Scene2():
    
    del playerarmy[:]
    del enemyarmy[:]
    Player_Riflemen.AddRiflemen(60)
    Treasury.SetTreasury(3000)
    Enemy_Riflemen.AddEnemyRiflemen(150)

    dateLine  = '''
The next morning,
'''
    
    scene2part1='''
    You are fatigued from last nights defense of the garrison.
    First things first, you need coffee.
    You walk to the mess hall and are met along the way by your luitennant, Scrugg.
    Luitennant Scrugg reports that during last nights defense we lost over 400 troops and need to find more recruits.
    As you sit down for morning coffee Luitennant Scrugg says that Fortuna has a large population and that it would be a good place to start looking for recurits.
    You agree with Scrugg, and ask of our current situation.
    Scrugg advises that most of the regiment was destroyed last night and only 60 riflemen remain. Scrugg advises that another attack may be looming.
    Supplies are limited but are sufficient. He tells you that there is only $3000 dollars remaining in the war treasury.
    The Apache population is not pleased with the work the Militia has done to the lands and they are looking for blood.
    The coffee is good but it is time to go, you lace up and ride to Fortuna with a few body guards entail
    When you arrive the citizens whisper of your defense of the garrison the night before, word travels fast.
    You make your way to the army recruitment office and speak with the private.
    The private informs you that men are lining up in Fortuna and Spokane, the town nearby for an opportunity to join your regiment.
    You look over the list and ponder your choices.
    '''

    SceneDateDelay(dateLine)
    TypeDelay(scene2part1)
    BuyUnits()
    
    Scene2Text = '''
    You and the recruits travel back to camp, it is a 3 hour trip so many men ask of stories of the night before.
    Many of the recruits are no older than 17 years old.
    The trip back to the garrison is long but filled with song and stories.

    As you approach the garrison you hear yelling in the distance.
    You hurry the recruits to the garrison as fast as possible.
    The garrison is under attack once more by an Apache force.
    They attacked before dawn, Scruggs was wrong.
    You assess the situation and the Apache force is '''+ str(len(enemyarmy)) + ''' strong.
    There were only 60 riflemen left at the garrison this morning and '''+ str(len(playerarmy)) +''' now.
    They garrison troops cannot defend the garrison alone, the recruits need arms.
    The recruits can either head to the Armory to get outfitted or they can scavage the battlefield.

    Will you send the recruits to the armory or battlefield?
    
    '''
    TypeDelay(Scene2Text)
    
    choice = input()
    choice = choice.lower()
    
    #Start of choice evaluation
    if choice == "battlefield":
        battlefieldText = '''
    You sent the recruits to scavage the battlefield for arms.
    The inexperience shows, recruits are scared and begin fleeing the battlefield.
    Within an hour the garrison falls.

    '''
        
        TypeDelay(battlefieldText)
    
        loseText = ('''
    Your men faught like cowards and mostly fled and the garrison has fallen.
    Would you like to try again?

''')
        TypeDelay(loseText)
        PlayAgain(Scene2)
            
#Armory choice tree         
    elif choice == "armory":
        armoryText = '''
    You sent the recruits to the armory to get weapons.
    The Apache are strong but the garrison's defenses hold them off until the recruits are armed.
    You order the recruits to muster and break them into units.
    You will lead half and Scruggs will lead the other.
    You lead the men into battle.
    They are shaken, scared and ready to flee.
    You saw the fear in their eyes, the cold in their bones.
    You stop...'''
        armoryText2 = '''
    You tell of the fear in your heart the night before. The chill in your bones and the quiver in your heart.
    '"I am still here, before you"' you tell them.
    You yell, '"show me a man who does not fear, and I will show you a man that is already dead."'
    '"Follow me and I will lead you to glory!"'
    '''
   
        
        TypeDelay(armoryText)
        time.sleep(3)
        TypeDelay(armoryText2)
        result = Battle(GetEnemyArmyAtk(), GetEnemyArmyDefense(), GetArmyAtk(), GetArmyDefense())
        
        if result == "player":
            winText = ('''
    Your men faught valliantly, and they have defeated the Apache attackers.
    The men and recruits jeer.
    The men and recruits cannot believe the have defended the garrison.
    During the battle there were tremendous losses, but tremendous victories.
    Scruggs has been wounded but he will make it.
    Many recruits showed they will make fine soldiers.


''')
            TypeDelay(winText)
            Scene3()
            
        else:
            loseText = ('''
    Your men faught with courage and integrity, but the garrison has fallen.
    Would you like to continue?

    ''')
            TypeDelay(loseText)
            PlayAgain(Scene2)
                
    else:
        elseText = '''
    You have been struck with an axe to the chest.
    Your story ends here.
    Would you like to try again?
    
    '''
         
        TypeDelay(elseText)
        PlayAgain(Scene2)




##SCENE 1##            
def Scene1():
    
    dateLine = 'October, 1755.'
    Enemy_Riflemen.AddEnemyRiflemen(60)
    
    SceneDateDelay(dateLine)
    print()
    
    openingLine = '''
    You are suddenly awaken by your Luitenant.
    He informs you there has been an attack on the garrison by a force
    of ''' + str(len(enemyarmy)) +''' Apache warriors.
    Your regiment is in disarray.
    You must muster your men and repel the Apache attack on the garrison.
    You run out of the barracks and enter the camp.
    Troops are scattered and running towards the armory and the battlefield.
    
    Will you go to the armory or the battlefield?

    '''
    
    TypeDelay(openingLine)

    choice = input()
    choice = choice.lower()
#Battlefield choice tree
    
    if choice == "battlefield":
        Player_Riflemen.AddRiflemen(100)
        battlefieldText = '''
    You make your way to the battlefield and have mustered 100 riflemen
    You order the riflemen into 4 squads of 25, and order an attack.
    Your men fire at the enemy, firing line after firing line.
    You fearlessly lead the troops into battle.
    There battle rages for over hours.
    Time and time again, you manage to save your troops from certain death.

    '''
        
        TypeDelay(battlefieldText)

        result = Battle(GetEnemyArmyAtk(), GetEnemyArmyDefense(), GetArmyAtk(), GetArmyDefense())
            
        if result == "player":
            
            winText = ('''
    Your men faught valliantly, and they have defeated the Apache attackers
    The men gather around you.
    Men tell you how greatful they are for your courage.
    That night there is a celebration throughout the camp.
    You retire to your quarters for the evening in anticipation of tomorrow when you will head to the nearest town of fortuna

''')
            TypeDelay(winText)
            Scene2()
            
        else:
            loseText = ('''
    Your men faught with courage and integrity, but the garrison has fallen.
    Would you like to continue?

    ''')
            
            TypeDelay(loseText)
            PlayAgain(Scene1)
            
#Armory choice tree         
    elif choice == "armory":
        Player_Riflemen.AddRiflemen(150)
        armoryText = '''
    You make your way to the armory and found James the trumpeter.
    You have ordered James to muster the troops at the armory.
    150 riflemen have mustered at the armory.
    You fearlessly lead the troops into battle.
    There battle rages for over hours.
    Time and time again, you manage to save your troops from certain death.
    
    '''
        
        TypeDelay(armoryText)
        result = Battle(GetEnemyArmyAtk(), GetEnemyArmyDefense(), GetArmyAtk(), GetArmyDefense())
        
        if result == "player":
            winText = ('''
    Your men faught valliantly, and they have defeated the Apache attackers.
    The men gather around you.
    Men tell you how greatful they are for your courage.
    That night there is a celebration throughout the camp.

''')
            TypeDelay(winText)
            Scene2()
            
        else:
            loseText = ('''
    Your men faught with courage and integrity, but the garrison has fallen.
    Would you like to continue?

    ''')
            TypeDelay(loseText)
            PlayAgain(Scene1)
    else:
        elseText = '''
    You have been struck with a musketball.
    Your story ends here.
    Would you like to try again?
    
    '''
         
        TypeDelay(elseText)
        PlayAgain(Scene1)

########

def Main():
   title =  ('''We the people
Developed by Kevin Karawan

    ''')
   TypeDelay(title)
   Intro()

########

Main()

