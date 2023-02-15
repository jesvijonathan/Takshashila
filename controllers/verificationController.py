
from utils.email_system import generate_hash 

from database.models.verificationModel import *


def create_verification(data):
    if (Verification.findExistingUser(data["email"])): 
        pass
    
    alt_hash = generate_hash()
    data['alt_hash'] = alt_hash
    user = Verification(data)
    db.session.add(user)
    db.session.commit()

    return alt_hash