import psycopg2

# All code written by Nicholas Colon

"""
Web Application
User tracks their pickleball match stats
    - Stats include wins, losses, match history
    - w/l ratio against specific dupr_ratings
"""

# Add a match and insert into my database

connection = psycopg2.connect(host="localhost", dbname="pickle_db", user="pickle_user",password="mypassword123", port=5432)
curr = connection.cursor()

try:
    while True:

        print("1 - Insert Match")
        print("2 - View User Stats")
        print("3 - Exit")

        menu_input = input()

        if menu_input == "1":
            # team_score = input("Friendly Team Score >>> ")
            # opponent_score = input("Opponents Team Score >>> ")
            # teammate = input("Teammate's Name >>> ")
            # opponent1_name = input("Opponent1 Name >>> ").lower()
            # opponent2_name = input("Opponent2 Name >>> ").lower()
            location_name = input("Location Name >>> ").lower()
            curr.execute("""INSERT INTO locations VALUES (%s);""", location_name,)
            curr.close()
            connection.close()
            # date = input("Today's Date >>>")
        elif menu_input == "2":
            print("Views Stats")
        elif menu_input == "3":
            break
        else:
            raise ValueError
except ValueError:
    print("Something went wrong")



