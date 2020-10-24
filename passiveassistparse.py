import sys
import passiveassistlib

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} file")
        sys.exit(1)
    padata = passiveassistlib.loadAssist(sys.argv[1])
    print(f"Place Name: {padata.get('placeName')}")
    if padata.get("weather"):
        wt = padata.get("weather")
        print(f"Weather: {wt.get('status')}")
        if wt.get('currentTemprature'):
            print(f"Temprature: {wt.get('currentTemprature')}")

if __name__ == "__main__":
    main()