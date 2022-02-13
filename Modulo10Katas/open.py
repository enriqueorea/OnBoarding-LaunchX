# def main():
#     open("/path/to/mars.jpg")

def main():
    try:
        open("trip_config.config")
    except FileNotFoundError:
        print("Couldn't find the config file for the trip")

if __name__ == '__main__':
    main()