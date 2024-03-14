from flask import Flask
from json import dumps
from donnees import champions_list
import __future__

app = Flask(__name__)


@app.route('/champions', methods=['GET'])
def show_all_routes():
    '''
    
    Permet de Montrer toutes les routes pour les personnages
    '''
    route_list = {
        'route':[]
    }
    for c in champions_list['champion']:
        route_list['route'].append(f'/champions/{(c["id"])}')
    return dumps(route_list)


@app.route('/champions/<id>', methods=['GET'])
def show_champion_by_id(id:int):
    '''
    
    Permet d'afficher un champion par son id (Ordre Alphabetique)
    '''
    return dumps(champions_list['champion'][int(id)])


@app.route('/champions/all', methods=['GET'])
def show_all_champion():
    '''
    
    Permet d'afficher TOUS les champions de LOL avec certain attributs
    '''
    return dumps(champions_list)


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080)