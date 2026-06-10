import sqlite3

con = sqlite3.connect('youtube_video.db')

cursor = con.cursor()

cursor.execute(''' 
    CREATE TABLE IF  NOT EXISTS videos(
              id INTEGER PRIMARY KEY,
              name TEXT NOT NULL,
              TIME TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos ")
    for row in cursor.fetchall():
        print(row)

def add_time(name, time ):
    cursor.execute("INSERT INTO videos(name, time ) VALUES (?,?)",(name , time ))
    con.commit()

def update_video(video_id,newname,newtime):
    con.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(newname,newtime,video_id))
    con.commit()
    
def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?",(video_id,))
    con.commit()


def main():
    while True :
        print("\n youtube manager :")
        print("1. list all videos : ")
        print("2. upadate videos ")
        print("3. add vidoes ")
        print("4.delete vidoes ")
        print("5.exit app ")
        start = int(input("enter a number to start :"))
        print(start)

        if start == 1 :
            list_videos()

        elif start == 2 :
            name = input("enter the video name : ")
            time = input("enetr the video time : ")
            add_time(name, time)

        elif start == 3 :
            video_id = input("enter video id to update : ")
            name = input("enter the video name : ")
            time = input("enetr the video time : ")
            update_video(video_id,name,time)

        elif start == 4 :
            video_id = input("enter video id to delete : ")
            delete_video(video_id)

        elif start == 5 :
            break
        else :
            print("invalid choice ")

    con.close()



if __name__ == "__main__":
    main()
