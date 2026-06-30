from db import Database
from training_service import TrainingService
from training_app import TrainingApp

def main():
    database = Database()
    database.create_tables()

    services = TrainingService(database)
    app = TrainingApp(services)
    app.start()

if __name__ == "__main__":
    main()