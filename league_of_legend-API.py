from flask import Flask
from json import dumps
from donnees import champions_list, SUPP,ADC,MID,TOP,JUNGLE
from league_of_legends import get_from_role, get_random_champion
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


@app.route('/champions/id=<id>', methods=['GET'])
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


@app.route('/champions/role=<roles>', methods=['GET'])
def show_champions_by_role(roles):
    match roles:
        case 'adc':
            return dumps(get_from_role('adc'))
        case 'support':
            return dumps(get_from_role('support'))
        case 'mid':
            return dumps(get_from_role('mid'))
        case 'jungle':
            return dumps(get_from_role('jungle'))
        case 'top':
            return dumps(get_from_role('top'))


@app.route('/champions/role=<roles>/random', methods=['GET'])
def give_random_champion(roles):
    match roles:
        case 'adc':
            return dumps(get_random_champion('adc'))
        case 'support':
            return dumps(get_random_champion('support'))
        case 'mid':
            return dumps(get_random_champion('mid'))
        case 'jungle':
            return dumps(get_random_champion('jungle'))
        case 'top':
            return dumps(get_random_champion('top'))
        case 'all':
            return dumps(get_random_champion('all'))


@app.route('/champions/get_team', methods=['GET'])
def give_me_team():
    team_base = ['top', 'jungle', 'mid', 'adc', 'support']
    side = ['red_side', 'blue_side']
    result = {
        'blue_side':[],
        'red_side':[]
    }
    for role in team_base:
        for s in side:
            champions = get_random_champion(role)
            print(champions)
            result[s].append(champions)
    return dumps(result)


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080)