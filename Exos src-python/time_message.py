# version finalisée avec le module datetime :
from datetime import datetime

# Exo - la valeur booléenne vrai si nous sommes le matin, sinon la valeur booléenne faux à une variable

# première version avec input :
################
# is_morning, day = 0, 0
# day_time = input("Sommes-nous le matin ou l'après-midi ? (matin/après-midi): ")

# if day_time == "matin":
#     is_morning = True
#     print(f"donc est : {is_morning}, car nous sommes le matin.")
# elif (day_time == "apres midi" or day_time == "apres-midi" or day_time == "après-midi"):
#     is_morning = False
#     print(f"donc est : {is_morning}, car nous sommes l'après-midi.")
# else:
#     day_time = input("Veuillez recommencer et taper le choix correct (matin ou après-midi): ")

# précision sur les périodes de la journée :
    # matin: 00:00:00 jusqu'à 11:59:59
    # apres midi: 12:00:00 jusqu'à 18:59:59
    # soir: 19:00:00 jusqu'à 20:59:59
    # nuit: 21:00:00 jusqu'à 23:59:59

def time_message():
    is_morning = 0
    # datetime.now() renvoie la date et l'heure locale actuelle
    now = datetime.now()

    # now.hour renvoit l'heure, now.minute les minutes et now.second les secondes en cours
    if ((now.hour >= 00 and now.hour <= 11 ) and (now.minute >= 00 and now.minute <= 59 ) and (now.second >= 00 and now.second <= 59)):
        is_morning = True
        print("C'est le matin car il est %02d:%02d:%02d" %(now.hour, now.minute, now.second)\
        + f" et donc is_morning = {is_morning}.")
    elif ((now.hour >= 12 and now.hour <= 18 ) and (now.minute >= 00 and now.minute <= 59 ) and (now.second >= 00 and now.second <= 59)):
        is_morning = False
        print("C'est l'après-midi car il est %02d:%02d:%02d" %(now.hour, now.minute, now.second)\
        + f" et donc is_morning = {is_morning}.")
    elif ((now.hour >= 19 and now.hour <= 20 ) and (now.minute >= 00 and now.minute <= 59 ) and (now.second >= 00 and now.second <= 59)):
        is_morning = False
        print("C'est le soir, car il est %02d:%02d:%02d" %(now.hour, now.minute, now.second)\
        + f" et donc is_morning = {is_morning}.")
    else:
        is_morning = False
        print("C'est la nuit, car il est %02d:%02d:%02d" %(now.hour, now.minute, now.second)\
        + f" et donc is_morning = {is_morning}.")

    # fichier utilisable comme script aussi bien que comme module importable
    if __name__ == "__main__":
        import sys
        time_message(int(sys.argv[1]))
