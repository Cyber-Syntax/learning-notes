import file
import download

def main():
    filehandler = file.filehandler()
    filehandler.ask_inputs()
    filehandler.save_credentials()


if __name__ == "__main__":
    main()