from sqlalchemy import select
from model import Training

class TrainingService:
    def __init__(self, database):
        self.database = database
    
    def add_training(self, name, coach_name, capacity_max, price):
        name = name.strip()
        coach_name = coach_name.strip().lower()
        
        if name == "":
            return (False, "Le nom est invalide")
        if coach_name == "":
            return (False, "Le nom est invalide")
        if capacity_max <= 0:
            return (False, 'La capacité doit être positif')
        if price <= 0:
            return (False, 'Le prix doit être positif')
        
        with self.database.create_session()as session:
            training = Training(
                name=name,
                coach = coach_name,
                capacity = capacity_max, 
                price=price
            )
         
            session.add(training)
            session.commit()
            
        return True, "Cours ajouté"
    
    def get_all_training(self):
        with self.database.create_session() as session:
            statement = select(Training)
            training = session.scalars(statement).all()
            return training
        
    def get_full_training(self):
        with self.database.create_session() as session:
            statement = select(Training).where(Training.registered_count == Training.capacity)
            training = session.scalars(statement).all()
            return training
        
    def register_someone(self, training_id):
        with self.database.create_session() as session:
            statement = select(Training).where(Training.id == training_id)
            training = session.scalars(statement).first()

            if training is None:
                return False, "Formation introuvable"

            if training.registered_count >= training.capacity:
                return False, "Le cours est complet"

            training.registered_count += 1
            session.commit()
            return True, "Inscription réussie"