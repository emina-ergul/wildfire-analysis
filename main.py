from src.load_data import load_csv_data


def run():
    fire_events = load_csv_data()
    print("!!!!!!!!!!!", fire_events)


if __name__ == "__main__":
    run()
