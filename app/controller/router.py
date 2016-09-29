import sys
import os
sys.path.append(os.path.abspath("./../../"))

from flask import Blueprint
router = Blueprint('router', __name__)

@router.route('/')
def index():
    return "It worker..."