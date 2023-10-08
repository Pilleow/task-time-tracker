import os
from datetime import datetime

def main():

    timestamps = []

    os.system("cls")
    print("\nEnter a title, and press Enter to save.\n")
    i = input("I: ")
    timestamps.append(i.strip().upper() + "\n")

    start = datetime.now()
    filename = "timetable" + start.strftime("%d%m%y") + ".txt"
    timestamps.append(" 0 hours total.\n\n")
    
    while True:
        os.system("cls")
        print()
        for t in timestamps:
            print(t, end="")
        print("\nType a commit message, and press Enter to save with a timestamp.\n")
        i = input("I: ")

        now = datetime.now()
        ti = now.strftime("%H:%M") + " - " + i.strip() + "\n"
        timestamps.append(ti)
        timestamps[1] = (" " + getTimeDiffHours(start, now) + " hours total.\n\n")

        saveToFile(filename, timestamps)


def getTimeDiffHours(firstD : datetime, laterD : datetime):
    return str(round((laterD - firstD).seconds / 3600, 2))

def saveToFile(fname, lines):
    with open("C:/Users/Pilleow/Desktop/" + fname, "w+", encoding="utf-8") as f:
        f.writelines(lines)

if __name__ == "__main__":
    main()
