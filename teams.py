from flask import Blueprint, request, jsonify, render_template

teams = [{"id": 1, "role": "Developer", "count": 1}]

manage_teams_bp = Blueprint('manage_teams', __name__)

@manage_teams_bp.route("/team_ui")
def index():
    return render_template("team.html", teams=teams)


@manage_teams_bp.route("/teams/<int:team_id>", methods=['GET', 'PATCH', 'DELETE'])
def manage_team(team_id):
    team = next((t for t in teams if t['id'] == team_id), None)
    if not team:
        return "Team not found", 404
    
    if request.method == 'GET':
        return jsonify(team)
    elif request.method == 'PATCH':
        data = request.get_json()
        if 'role' in data:
            team['role'] = data['role']
        if 'count' in data:
            team['count'] = data['count']
        return jsonify(team)
    elif request.method == 'DELETE':
        teams.remove(team)
        return '', 204

@manage_teams_bp.route("/teams", methods=['GET', 'POST'])
def manage_all_teams():
    if request.method == 'GET':
        return jsonify(teams)
    elif request.method == 'POST':
        team = request.get_json()
        next_id = max(t['id'] for t in teams) + 1 if teams else 1
        team['id'] = next_id
        teams.append(team)
        return jsonify(team), 201
